import re
import pandas as pd

df = pd.read_excel("./data/result.xlsx")


# \d+匹配任意数字，\.转义小数点
# 应用正则表达式去除.00
def remove_dot_zero(text):
    pattern_replace = r"(\d+)\.00"
    # 返回使用替换模式在原始文本中去除.00
    return re.sub(pattern_replace, r"\1", text)


# 取第一个匹配结果
def take_the_first_match(text):
    # 匹配规则
    pattern = "满\d+返\d+"
    matches = re.findall(pattern, text)
    # 排除无匹配结果
    if matches:
        return matches[0]
    else:
        return None


df["满返"] = df["满返"].apply(remove_dot_zero)
df["满返"] = df["满返"].apply(take_the_first_match)
df = df.dropna(subset=["满返"])
df = df.dropna(subset=["经营品类"])

# 将处理数据写入Excel文件
df.to_excel("./data/result.xlsx", index=False)
