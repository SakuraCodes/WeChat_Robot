# -*- coding: utf-8 -*-
import os
import time
import random
import datetime

import schedule
from wxauto import WeChat

from select_category import rand_shop

BREAKFAST_TITLE = [
    "🍂秋高气爽，来碗热气腾腾的🍚吧！",
    "吃完早餐，又是元气满满的一天。",
    "好好吃个早餐‹🍞🥨🥖🍳›",
    "又是热爱生活的一天🌞",
    "🥛今天是早餐𝑝𝑙𝑜𝑔🥚",
    "🍞 𓏼🥛早餐时间到了，请选择你喜欢的食物",
    "在每一个早上和自己说加油ᵎᵎᵎ🌞",
    "早餐带来的幸福感✌︎",
    "    🥯˃ꌂ˂ 🥯    ",
    "◡̈ 🔆 𝙈𝙤𝙧𝙣𝙞𝙣𝙜 💐",
    "🌿开启幸运的一天☻",
    "𖠚ᐝ早起的鸟儿𓅯ˎˊ˗",
    "🍞🥯面包脑袋૮ ´• •` ა",
    "早八人ᜊ ᶻᶻᶻ困",
    "早起的意义是为了吃早餐🥨🥖",
]

DINNER_TITLE = [
    "*𝑭𝒐𝒐𝒅𝒊𝒆 𝒍𝒊𝒔𝒕🧾🫕🌮",
    "日子不紧不慢 每天好好吃饭",
    "𓌉◯𓇋 ʜᴀ͟ᴘ͟ᴘ͟ʏ ᴇᴠᴇʀʏᴅᴀʏ̆̈",
    "常言道：“食食物者为俊杰”🍔🍟🍗🍕",
    "ʔ•̫͡•ʕ ·𝙃𝙤𝙩𝙥𝙤𝙩·🥘“快乐的标配,火锅和姐妹",
    "𝙄𝙣𝙩𝙚𝙧𝙚𝙨𝙩𝙞𝙣𝙜🍤🍣“吃得饱想的少 天天开心没烦恼”",
    "ʔ•̫͡•ʕᶠᵃᵗ ᶠᵃᵗ ᶠᵃᵗ🥩",
    "一年四季：春肥 夏胖 秋膘 冬圆",
    ": / 𝙁𝙤𝙤𝙙𝙞𝙚𝙚𝙚𝙚 𓀠𓀤𓀥𓀫",
    "‘‘ 叮🔔！双下巴续费成功 ’’🥢",
    "𝑩𝒂𝒓𝒃𝒆𝒄𝒖𝒆 / 🥓🥘",
    "把眼睛留给风景 把体重留给美食",
    "☾˚‧º气氛都到这了 发个朋友圈吧 ⍥⃝",
    "˗ˋˏ 🍻 ˎˊ˗𝐞𝐚𝐭𝐭𝐭𝐭…肚子喂饱•可爱到老⌇",
    "˗ˋˏ 𝗙𝗼𝗼𝗱𝗶𝗲🥯🥢ˎˊ˗",
    "别和体重斤斤计较 吃得开心就好",
    "🍨🍯不要急 好吃慢喝来日方长🥛",
    "🥢𝑻𝒐𝒈𝒆𝒕𝒉𝒆𝒓👫",
    "爱吃的女孩子运气不会差·因为食来运转🥘",
    "✏️今天依然是碌碌无为的知食分子",
    "ॱଳ做一枚快乐的吃货🥧",
    ".✐  Føøđ  ᵕ̈ 吃喝小日常",
    "“小肚 小肚” “ 我在🙋🏻‍♂”",
    "*ʚ◡̈⃝ɞ晚胖不如早胖",
    ": / 𝙁𝙤𝙤𝙙𝙞𝙚𝙚𝙚𝙚 𓀠𓀤𓀥𓀫",
    "‘‘ 叮🔔！双下巴续费成功 ’’🥢",
    "人生幸事, 八九不离食 🍱",
    "闺蜜👭就是：一起吃饭一起胖 ♡̷🍹🧀️🍮🍣🍕",
    "嘴巴一张 下吧变双~`oˊ~走进漫画风的一天",
    "𓌉◯𓇋 ︎ 今日菜单📝",
    "🥘∙咕噜咕噜⑉",
    "𝐅 🍔🍔 𝐝𝐝𝐝𝐝𝐝𝐝𝐝𝐝𝐝𝐝𝐝",
    "恰飯◍˃ᵕ˂◍",
]

TEA_TITLE = [
    "🍮🌈𝖬𝖾𝖾𝗍𝗂𝗇𝗀▸ʚ🍰ɞ꙳⋆🍜\n🍹ɞ⋆慵懒下午茶时光♡゛🍹",
    "你有一份甜甜日常请查收~🍰",
    "下午茶𝘁𝗶𝗺𝗲₍˄·͈༝·͈˄*₎◞ ̑̑☕",
    "☕️ ᴍᴏᴍᴇɴᴛ静谧的下午茶时光",
    "没有文案,只想续杯🥤",
    "甜茶记🍓➕🍰🟰☕️",
    "偷得浮生半日闲,轻煮岁月慢煮茶☕",
    "📷相机里午茶的小碎片☕",
    "「☕」▸COFFEE TIME",
    "咖啡一杯精神百倍( ･⊝･∞)☕️",
    "•͈ᴗ•͈⸝⸝⸝甜品治愈一切 ˁ῁̬ˀ",
    "ᵕ̈下午茶時間🍸🧈☕️",
    "🍮·热量𝚋𝚘𝚘𝚖 𝚍𝚊𝚢💥.ᐟ",
    "瑞了个幸⋆⁺☕️♪🔖ᯤ🤎",
    "🌈我的快乐多巴胺🍹🥧𓌉𓇋",
    "🍰•ᴗ•🥄从吃小蛋糕开始幸福‧₊˚",
    "🍮°₊ 焦糖布丁⟢🥚₊⋆🥛˚⁺ 🍯 ഒ",
    "🐰‧˖⁺🧁⁺˚ 播放幸福正片🧈𓈒꙳⋆ 🍧",
    "🧁 🥂 🇭 🇦 🇵 🇵 🇾 下午茶️时光🙋‍♀️",
    "🍨甜食配方：50%快乐+50%脂肪 𓂂 𓋜",
]

SNACK_TITLE = [
    "“尝尝酒酒，瓶瓶安安”",
    "ᵕ̈ ɴɪᴄᴇ 🍻 ᵕ̈\n“不负时光，与友相聚”\n🍺(ˊᗜˋ*)",
    "🌃夜生活才刚刚开始~🥠\n啤酒🍺烧烤🍗不能少！",
    "🍖· 今日☑",
    "📷｜烧烤篇",
    "夜宵｜自由🅱️🅱️𝐐",
    "“搞点夜宵𝟳𝟳𝟴🍺🦞”",
    "❀͈ “开心就要咔̾滋̾咔̾滋̾”",
    "🥓 % 今·日·热·量：9̺͆9̺͆%̺͆",
    "好胖友 ˃̶͈🐽˂̶͈",
    "Barbecue.🍻🍢🍗🍺",
    "嗝～烤肉滋滋上线🔥",
    "串串不贵，但很对胃",
    "🦪🍤🥓烧烤就是0.5慢放的快乐𝗶𝗻𝗴",
    "🥓 :𝙙𝙖𝙮 ²⁰²⁴‽",
    "开心有好多种，燒烤是第一种🍗🍖🌯🍢🍡🍆",
    "“滋̾滋̾滋̾，冒香͂味͂的夜间快͝乐͝”",
    "ʜᵃᵖᵖᵞ •多烤两串🍡🍢⚘",
    "🍖𓂂𓈒𓏸 “香迷糊了”😛💭",
    "🍺🍗烧烤配啤酒✿.",
    "烧烤🍱🍢🍻",
    "ᶠᵃᵗ🍯总要留下长肉的证据˙Ꙫ˙",
]

DELIM = [
    "————՞•・•՞————",
    "—— ฅ՞••՞ฅ♥ ——",
    "———๑ᵔ⤙ᵔ๑ ⸝⸝———",
    "——ᐢ⸝⸝ › ~ ‹⸝⸝ᐢ——",
    "———ʕ·͡ˑ·ཻʔ ———",
    "———🥯˶╹ꇴ╹˶🥯———",
    "———❛˓◞˂̵✧———",
]

LINK = "\n------------------\n点击链接选店啵👉s.mrw.so/9K4AN\n"

ACTIVITY = [
    "\n🔥参与吃货挑战赛，赢取10元现金🧧和30天会员！\n👉打开歪麦APP，首页-活动挑战赛，报名参与！",
    "\n🔥挑战味蕾，赢取大奖！10元现金🧧和30天会员等你拿！\n👉打开歪麦APP，首页-活动挑战赛，报名参与！",
    "\n🔥吃货必看！挑战成功，10元现金🧧和30天会员轻松到手！\n👉打开歪麦APP，首页-活动挑战赛，报名参与！",
    "\n🔥敢挑战吗？10元现金🧧和30天会员就是你的啦！\n👉打开歪麦APP，首页-活动挑战赛，报名参与！",
    "\n🔥你是真正的吃货吗？来挑战吧！10元现金🧧和30天会员等你来拿！\n👉打开歪麦APP，首页-活动挑战赛，报名参与！",
]


def is_wednesday() -> str:
    """
    判断今日为周三,则对activity重新赋值
    :return: 活动文案
    """
    if datetime.datetime.today().weekday() == 2:
        act = (
            random.choice(ACTIVITY)
            + "\n\n🌟歪麦周三狂欢！送你3天会员！输入口令“歪麦周三霸王日”\n👉打开歪麦APP，我的-兑换专区，立即兑换！"
        )
        return act
    else:
        return random.choice(ACTIVITY)


# 获取pic文件夹绝对路径
current_file_dir = os.path.dirname(os.path.abspath(__file__))
pic_files = os.path.join(current_file_dir, "pic")


# 发送对象列表
LISTEN_ATALL_LIST = [
    # "传输助手"
]
LISTEN_LIST = [
    # "传输助手"
    "在宁波0-5元吃霸王餐-A3",
    "【歪麦】宁波0-5元吃外卖-A1",
    "【歪麦】宁波0-5元吃外卖-A2",
    "【歪麦】宁波0-5元吃外卖-A3",
    "【歪麦】宁波0-5元吃外卖-A4",
    "宁波歪麦霸王餐福利群002",
    "宁波歪麦霸王餐福利群003",
    "宁波歪麦霸王餐福利群004",
]


def random_image_path(folder_path: str) -> str | None:
    """
    随机返回指定文件夹中的图片路径
    :param folder_path: 指定文件夹路径
    :return: 指定文件夹路径中的图片路径
    """
    # 获取文件夹中的所有文件
    all_files = os.listdir(folder_path)
    # 筛选出图片文件(根据需要调整图片格式)
    image_files = [
        f for f in all_files if f.endswith((".jpg", ".jpeg", ".png", ".bmp"))
    ]
    # 如果没有找到图片文件,返回None
    if not image_files:
        return None
    # 随机选择一张图片
    random_image = random.choice(image_files)
    # 拼接完整路径
    return os.path.join(folder_path, random_image)


def push_msg(msg_list: list, filepath: list[str | None]) -> None:
    """
    遍历发送消息
    :param msg_list: 发送消息列表
    :param filepath: 发送文件路径列表
    :return:
    """
    # 获取微信窗口对象
    wx = WeChat()
    # 切换到聊天页面
    wx.SwitchToChat()
    for la in LISTEN_ATALL_LIST:
        for m in msg_list:
            wx.AtAll(msg=m, who=la)
            wx.SendFiles(filepath=filepath, who=la)
    for l in LISTEN_LIST:
        for m in msg_list:
            wx.SendMsg(msg=m, who=l)
            wx.SendFiles(filepath=filepath, who=l)


def push_breakfast() -> None:
    """
    推送早餐消息
    :return:
    """
    category = ["⾯粉粥包"]
    # 消息列表
    msg_list = [
        random.choice(BREAKFAST_TITLE)
        + "\n"
        + rand_shop(category)
        + LINK
        + random.choice(DELIM)
        + is_wednesday()
    ]
    # 文件列表
    filepath = [random_image_path(os.path.join(pic_files, "breakfast"))]
    push_msg(msg_list, filepath)


def push_dinner() -> None:
    """
    推送正餐消息
    :return:
    """
    category = ["特色小吃", "中餐便餐", "⽕锅冒菜", "异国料理"]
    msg_list = [
        # "肯德基星期四，疯狂不止一点点！\n\n🍗 2桶20翅，疯狂美味不停歇！\n💰 61.8元，超值优惠等你来！\n🛵 配送费半价，歪麦平台让你轻松享美食！\n"
        random.choice(DINNER_TITLE)
        + "\n"
        + rand_shop(category)
        + LINK
        + random.choice(DELIM)
        + is_wednesday()
    ]
    filepath = [random_image_path(os.path.join(pic_files, "dinner"))]
    push_msg(msg_list, filepath)


def push_tea() -> None:
    """
    推送下午茶消息
    :return:
    """
    category = ["水果果切", "奶茶甜点", "咖啡"]
    msg_list = [
        random.choice(TEA_TITLE)
        + "\n"
        + rand_shop(category)
        + LINK
        + random.choice(DELIM)
        + is_wednesday()
    ]
    filepath = [random_image_path(os.path.join(pic_files, "afternoontea"))]
    push_msg(msg_list, filepath)


def push_snack() -> None:
    """
    推送宵夜消息
    :return:
    """
    category = ["特色小吃", "其他", "烧烤夜宵", "异国料理"]
    msg_list = [
        random.choice(SNACK_TITLE)
        + "\n"
        + rand_shop(category)
        + LINK
        + random.choice(DELIM)
        + is_wednesday()
        + "\n🔔宵夜订单记得要提交哦~~"
    ]
    filepath = [random_image_path(os.path.join(pic_files, "snack"))]
    push_msg(msg_list, filepath)


def push_activity() -> None:
    """
    推送活动消息
    :return:
    """
    msg_list = [
        # "🧧外卖通用神券红包\n美团👉s.c1ns.cn/Vx9J5\n饿了么👉s.c1ns.cn/c25G3\ntips：神券红包和霸王餐可以同时减免呦~\n\n🔗霸王餐链接：s.c1ns.cn/i14hj\n------------------\n🎉【活动挑战赛】🎁\n• 🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n• 🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n• 🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n\n👉活动入口：点击霸王餐链接-点击赚钱-点击活动二海报，即可参与挑战赛"
    ]
    filepath = [os.path.join(pic_files, "activity.jpg")]
    push_msg(msg_list, filepath)


if __name__ == "__main__":

    # push_breakfast()
    # push_dinner()
    # push_tea()
    # push_snack()
    # push_activity()

    # 定时执行任务
    schedule.every().day.at("08:30:00").do(push_breakfast)
    # schedule.every().day.at("10:00:00").do(push_activity)
    schedule.every().day.at("10:30:00").do(push_dinner)
    schedule.every().day.at("14:00:00").do(push_tea)
    # schedule.every().day.at("15:30:00").do(push_activity)
    schedule.every().day.at("16:45:00").do(push_dinner)
    schedule.every().day.at("21:00:00").do(push_snack)

    while True:
        schedule.run_pending()
        time.sleep(1)
