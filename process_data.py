import re
import pandas as pd

# 读取Excel文件
df = pd.read_excel("./data/门店发布统计.xlsx")

# 提取需要的列
selected_df = df.loc[:, ["店铺名称", "经营品类", "返利信息"]]


# \d+匹配任意数字，\.转义小数点
# 应用正则表达式去除.00
def remove_dot_zero(text):
    pattern_replace = r"(\d+)\.00"
    # 返回使用替换模式在原始文本中去除.00
    return re.sub(pattern_replace, r"\1", text)


# 取最后一个匹配结果
def take_the_last_match(text):
    # 匹配规则
    pattern = "满\d+返\d+"
    matches = re.findall(pattern, text)
    # 排除无匹配结果
    if matches:
        return matches[-1]
    else:
        return None


selected_df["返利信息"] = selected_df["返利信息"].apply(remove_dot_zero)
selected_df["返利信息"] = selected_df["返利信息"].apply(take_the_last_match)
cleaned_df = selected_df.dropna(subset=["返利信息"])

# 将处理数据写入Excel文件
cleaned_df.to_excel("./data/result.xlsx", index=False)
