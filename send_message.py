# -*- coding: utf-8 -*-
import time
import random
from pathlib import Path
from datetime import datetime, timedelta

import schedule
from wxauto import WeChat
from chinese_calendar import is_workday

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
    "💮-—🏮•̀֊•́🏮—-💮",
]

LINK = "\n  点击链接选店啵\n👉s.mrw.so/9K4AN"

MSG_HOLIDAY = "\n\n『美团🧧』链接\n👉dpurl.cn/AvSbR2Fz\n『饿了么🧧』链接\n👉u.ele.me/lZfkgmHt\n『歪麦』店铺入口\n👉s.mrw.so/9K4AN\n"


def is_within_date(start_date: str, end_date: str) -> bool:
    """
    判断当前日期是否在日期范围内
    :param start_date: 开始日期(1.22)
    :param end_date: 结束日期(2.5)
    :return: 是与否
    """
    today = datetime.today()
    start_date = datetime.strptime(f"{today.year}.{start_date}", "%Y.%m.%d")
    end_date = datetime.strptime(f"{today.year}.{end_date}", "%Y.%m.%d")
    end_date += timedelta(days=1)

    return start_date <= today <= end_date


def redeem_code() -> str:
    """
    输出今日兑换码
    :return: 兑换码文案
    """
    # 口令:[2025新年快乐][歪麦宁波][歪麦周三霸王日][2025蛇年大吉]
    code = "\n-------兑换专区-------"
    base_code = code  # 记录初始内容，防止无意义返回

    # 判断今日是否在日期范围内
    if is_within_date("1.22", "2.5"):
        code += "\n🏮欢度春节赢好礼🏮\n👉新年口令：打开歪麦APP📱-我的-兑换专区输入-“2025蛇年大吉”领取14天会员\n（有效期：1.22-2.5）抓紧时间兑换哦！"

    # 判断今日是否为周三 (wed)
    if datetime.today().weekday() == 2:
        code += "\n🌟歪麦周三狂欢送3天会员🌟\n👉打开歪麦APP，进入“我的-兑换专区”，输入口令“歪麦周三霸王日”兑换！"

    return code if code != base_code else ""


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
    "【歪麦】宁波0-5元吃外卖-A5",
    "【歪麦】宁波0-5元吃外卖VIP群",
    "宁波歪麦霸王餐福利群002",
    "宁波歪麦霸王餐福利群003",
    "宁波歪麦霸王餐福利群004",
]

# 获取pic文件夹绝对路径
current_file_dir = Path(__file__).resolve().parent
pic_files = current_file_dir / "pic"


def is_file() -> bool:
    """
    判断result.xlsx文件是否存在
    :return: 是与否
    """
    try:
        data_files = Path(current_file_dir) / "data" / "result.xlsx"
        return data_files.is_file()
    except OSError:
        return False


def random_image_path(folder_path: str) -> str | None:
    """
    随机返回指定文件夹中的图片路径
    :param folder_path: 指定文件夹路径
    :return: 指定文件夹路径中的图片路径
    """
    # 获取文件夹路径对象
    folder = Path(folder_path)

    # 获取文件夹中的所有图片文件(指定格式)
    image_files = [
        f for f in folder.glob("*") if f.suffix in {".jpg", ".jpeg", ".png", ".bmp"}
    ]

    # 如果没有找到图片文件,返回None
    if not image_files:
        return None

    # 随机选择一张图片并返回绝对路径
    return str(random.choice(image_files))


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
    today = datetime.now()
    if is_workday(today) & is_file():
        category = ["⾯粉粥包"]
        # 消息列表
        msg_list = [
            random.choice(BREAKFAST_TITLE)
            + "\n"
            + rand_shop(category)
            + "\n"
            + random.choice(DELIM)
            + LINK
            + redeem_code()
        ]
    else:
        msg_list = [
            random.choice(BREAKFAST_TITLE)
            + MSG_HOLIDAY
            + random.choice(DELIM)
            # + "\n📢放假期间，群内无值班人员哦~有事🉑app在线联系客服或致电：6url.cn/u7DXRx【4008275517】"
            + "\n记得及时去提交订单哦！"
            + redeem_code()
        ]
    # 文件列表
    filepath = [random_image_path(pic_files / "breakfast")]
    push_msg(msg_list, filepath)


def push_dinner() -> None:
    """
    推送正餐消息
    :return:
    """
    today = datetime.now()
    if is_workday(today) & is_file():
        category = ["特色小吃", "中餐便餐", "⽕锅冒菜", "异国料理"]
        msg_list = [
            random.choice(DINNER_TITLE)
            + "\n"
            + rand_shop(category)
            + "\n"
            + random.choice(DELIM)
            + LINK
            + redeem_code()
        ]
    else:
        msg_list = [
            random.choice(DINNER_TITLE)
            + MSG_HOLIDAY
            + random.choice(DELIM)
            # + "\n📢放假期间，群内无值班人员哦~有事🉑app在线联系客服或致电：6url.cn/u7DXRx【4008275517】"
            + "\n记得及时去提交订单哦！"
            + redeem_code()
        ]
    filepath = [random_image_path(pic_files / "dinner")]
    push_msg(msg_list, filepath)


def push_tea() -> None:
    """
    推送下午茶消息
    :return:
    """
    today = datetime.now()
    if is_workday(today) & is_file():
        category = ["水果果切", "奶茶甜点", "咖啡"]
        msg_list = [
            random.choice(TEA_TITLE)
            + "\n"
            + rand_shop(category)
            + "\n"
            + random.choice(DELIM)
            + LINK
            + redeem_code()
        ]
    else:
        msg_list = [
            random.choice(TEA_TITLE)
            + MSG_HOLIDAY
            + random.choice(DELIM)
            # + "\n📢放假期间，群内无值班人员哦~有事🉑app在线联系客服或致电：6url.cn/u7DXRx【4008275517】"
            + "\n记得及时去提交订单哦！"
            + redeem_code()
        ]
    filepath = [random_image_path(pic_files / "afternoontea")]
    push_msg(msg_list, filepath)


def push_snack() -> None:
    """
    推送宵夜消息
    :return:
    """
    today = datetime.now()
    if is_workday(today) & is_file():
        category = ["特色小吃", "其他", "烧烤夜宵", "异国料理"]
        msg_list = [
            random.choice(SNACK_TITLE)
            + "\n"
            + rand_shop(category)
            + "\n"
            + random.choice(DELIM)
            + LINK
            + "\n🔔宵夜订单记得要提交哦~~"
            + redeem_code()
        ]
    else:
        msg_list = [
            random.choice(SNACK_TITLE)
            + MSG_HOLIDAY
            + random.choice(DELIM)
            # + "\n📢放假期间，群内无值班人员哦~有事🉑app在线联系客服或致电：6url.cn/u7DXRx【4008275517】"
            + "\n记得及时去提交订单哦！"
            + redeem_code()
        ]
    filepath = [random_image_path(pic_files / "snack")]
    push_msg(msg_list, filepath)


def push_activity() -> None:
    """
    推送活动消息
    :return:
    """
    msg_list = [
        "🎉蛇年开门红，邀好友赚不停！🐍\n\n1️⃣ 邀3人首单，奖励15元！\n2️⃣ 邀7人首单，奖励40元！\n3️⃣ 邀10人首单，奖励60元！\n\n🎉蛇年狂欢，邀请越多，奖励越高，快来赚红包！🧧\n"
        + random.choice(DELIM)
        + "\n👉活动入口：s.mrw.so/9K4AN"
    ]
    filepath = [
        pic_files / "activity.jpg",
        pic_files / "guide.png",
    ]
    push_msg(msg_list, filepath)


if __name__ == "__main__":

    # push_breakfast()
    # push_dinner()
    # push_tea()
    # push_snack()
    # push_activity()

    # 定时执行任务
    schedule.every().day.at("08:00:00").do(push_breakfast)
    schedule.every().day.at("10:15:00").do(push_dinner)
    # schedule.every().day.at("10:30:00").do(push_activity)
    schedule.every().day.at("14:00:00").do(push_tea)
    schedule.every().day.at("16:30:00").do(push_dinner)
    # schedule.every().day.at("17:00:00").do(push_activity)
    schedule.every().day.at("20:00:00").do(push_snack)

    while True:
        schedule.run_pending()
        time.sleep(1)
