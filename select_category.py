import pandas as pd
import random

# 读取Excel文件
df = pd.read_excel("./data/result.xlsx")


def rand_shop(categories):
    # 确保categories是列表类型，以便可以处理单个或多个品类的情况
    if not isinstance(categories, list):
        categories = [categories]
    # 筛选“经营品类”，使用isin函数筛选经营品类
    filtered_df = df[df["经营品类"].isin(categories)]
    # 随机选择3到5个商家
    num_selected = random.randint(3, 5)
    selected_df = filtered_df.sample(n=num_selected)
    # 替换“满返”列中所有“满”字为“🈵”
    selected_df["返利信息"] = selected_df["返利信息"].str.replace("满", "🈵")
    # 遍历选择的商家，并将商家名称和满返信息拼接到输出字符串中
    shop_info = ""
    for index, row in selected_df.iterrows():
        name = row["店铺名称"].strip()
        cashback = row["返利信息"]
        shop_info += f"\n{name}\n{cashback}"
    return shop_info


# print(rand_shop(["中餐便餐"]))
