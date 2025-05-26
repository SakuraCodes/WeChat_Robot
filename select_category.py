# -*- coding: utf-8 -*-
import random

import pandas as pd


def rand_shop(categories: list) -> str:
    """
    根据给定品类输出推荐店铺
    :param categories: 品类列表
    :return: 推荐店铺信息
    """
    # 读取Excel文件并去重(保留满返差额较小的行)
    df = pd.read_excel("./data/result.xlsx")
    # 保留"满返差额"小的同名店铺数据
    df = df.sort_values("满返差额").drop_duplicates("店铺名称", keep="first")
    # 确保categories是列表类型，以便可以处理单个或多个品类的情况
    if not isinstance(categories, list):
        categories = [categories]
    # 筛选“经营品类”，使用isin函数筛选经营品类
    filtered_df = df[df["经营品类"].isin(categories)]
    # # 按创建时间(降序)和满返差额(升序)排序后取前10行
    # filtered_df = filtered_df.sort_values(
    #     by=["创建时间", "满返差额"], ascending=[False, True]
    # )[:10]
    # 按满返差额(升序)排序后取前10行
    # filtered_df = filtered_df.sort_values(by="满返差额", ascending=True)[:10]
    # print(filtered_df)
    # 随机选择5个商家(如果行数不足则返回原值)
    num_selected = 5
    # num_selected = random.randint(3, 5)
    if num_selected <= len(filtered_df):
        selected_df = filtered_df.sample(n=num_selected)
    else:
        selected_df = filtered_df
    # 替换“满返”列中所有“满”字为“🈵”
    selected_df["返利信息"] = selected_df["返利信息"].str.replace("满", "🈵")
    # 替换“满返”列中所有“返”字为“🉐”
    selected_df["返利信息"] = selected_df["返利信息"].str.replace("返", "🉐")
    # 遍历选择的商家，并将商家名称和满返信息拼接到输出字符串中
    shop_info = ""
    for index, row in selected_df.iterrows():
        name = row["店铺名称"].strip()
        cashback = row["返利信息"]
        shop_info += f"\n{name}\n✨会员{cashback}"
    return shop_info


# print(rand_shop(["中餐便餐"]))
