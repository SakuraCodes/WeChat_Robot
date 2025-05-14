# -*- coding: utf-8 -*-
import re

import pandas as pd

# 读取Excel文件
df = pd.read_excel("./data/门店发布统计.xlsx")

# 筛选宁波市的店铺
df = df[df["市"] == "宁波市"]
# 提取需要的列
selected_df = df.loc[:, ["店铺名称", "经营品类", "返利信息", "满返差额", "创建时间"]]
# 确保"创建时间"列是日期格式
selected_df["创建时间"] = pd.to_datetime(selected_df["创建时间"])


def cleaned_shopname(value: str) -> str:
    """
    使用正则表达式去除特殊字符
    :param value: 待处理的文本
    :return: 去除特殊字符的文本
    """
    pattern_replace = r"[\n\r\t]"
    # 返回使用替换模式在原始文本中去除特殊字符
    return re.sub(pattern_replace, r"", value)


def remove_dot_zero(value: str) -> str:
    """
    使用正则表达式去除.00 (\d+匹配任意数字，\.转义小数点)
    :param value: 待处理的文本
    :return: 去除.00的文本
    """
    pattern_replace = r"(\d+)\.00"
    # 返回使用替换模式在原始文本中去除.00
    return re.sub(pattern_replace, r"\1", value)


def rebateinfo_first_match(value: str) -> str | None:
    """
    使用正则表达式匹配第一个结果
    :param value: 待匹配的文本
    :return: 匹配到的结果
    """
    # 匹配规则
    pattern = "满\d+返\d+|每单返利\d+"
    matches = re.findall(pattern, value)
    # 排除无匹配结果
    if matches:
        return matches[0]
        # return matches[-1]
    else:
        return None


# 去除"店铺名称"列中的特殊字符
selected_df["店铺名称"] = selected_df["店铺名称"].apply(cleaned_shopname)

# 去除"返利信息"列中的.00
selected_df["返利信息"] = selected_df["返利信息"].apply(remove_dot_zero)
# 提取"返利信息"列中的第一个匹配结果
selected_df["返利信息"] = selected_df["返利信息"].apply(rebateinfo_first_match)


# 处理"满返差额"列：先转换为字符串，再分割并取第一个元素，最后转换为数值
selected_df["满返差额"] = selected_df["满返差额"].astype(str).str.split(";").str[0]
selected_df["满返差额"] = pd.to_numeric(
    selected_df["满返差额"], errors="coerce"
)  # errors="coerce" 会将无法转换的值设置为NaN

# 删除"返利信息"列有缺失值的行
cleaned_df = selected_df.dropna(subset=["返利信息"])

# 将处理数据写入Excel文件
cleaned_df.to_excel("./data/result.xlsx", index=False)
