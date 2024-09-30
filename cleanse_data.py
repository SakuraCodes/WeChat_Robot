import pandas as pd

# 读取Excel文件
df1 = pd.read_excel("./data/发布计划.xlsx")
df2 = pd.read_excel("./data/商家发布.xlsx")

# 提取需要的列
selected_df1 = df1.loc[:, ["商家名称", "满返"]]
selected_df2 = df2.loc[:, ["店铺名称", "经营品类"]]

# 对匹配列进行首尾去空白字符
selected_df1["商家名称"] = selected_df1["商家名称"].str.strip()
selected_df2["店铺名称"] = selected_df2["店铺名称"].str.strip()

# 去除重复行
selected_df1 = selected_df1.drop_duplicates(subset=["商家名称", "满返"], keep="first")
selected_df2 = selected_df2.drop_duplicates(
    subset=["店铺名称", "经营品类"], keep="first"
)

# 合并数据(根据相同列进行匹配)
merged_df = pd.merge(
    selected_df1, selected_df2, left_on="商家名称", right_on="店铺名称", how="left"
)

# 去除匹配列(axis=0表示删除行，axis=1表示删除列)
merged_df = merged_df.drop(["店铺名称"], axis=1)

# 将合并数据写入Excel文件
merged_df.to_excel("./data/result.xlsx", index=False)
