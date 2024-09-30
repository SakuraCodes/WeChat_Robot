from wxauto import WeChat
import schedule
import time
import random
from select_category import rand_shop

delim = [
    "————՞•・•՞————",
    "—— ฅ՞••՞ฅ♥ ——",
    "———๑ᵔ⤙ᵔ๑ ⸝⸝———",
    "——ᐢ⸝⸝ › ~ ‹⸝⸝ᐢ——",
    "———ʕ·͡ˑ·ཻʔ ———",
    "———🥯˶╹ꇴ╹˶🥯———",
    "———❛˓◞˂̵✧———",
]

link = "\n------------------\n点击链接选店啵👉s.c1ns.cn/i14hj\n"

activity = "\n🔥国庆团长赛火热进行中！🔥\n🧧邀新赢12-70元现金红包🧧\n💎点餐下单送30天会员💎\n👉活动入口：https://s.c1ns.cn/9XnXV"


# 发送对象列表
listen_atall_list = [
    # '测试群'
    # '宁波歪麦霸王餐福利群002',
    # '宁波歪麦霸王餐福利群003',
    # '宁波歪麦霸王餐福利群004',
    # '在宁波0-5元吃霸王餐-A8'
]
listen_list = [
    # "测试群"
    "【歪麦】宁波外卖聚集地-A9",
    "宁波福利群-100",
    "宁波福利群-101",
    "宁波歪麦霸王餐福利群002",
    "宁波歪麦霸王餐福利群003",
    "宁波歪麦霸王餐福利群004",
    "在宁波0-5元吃霸王餐-A8",
]


def PushMsg(msg_list, filepath):
    # 获取微信窗口对象
    wx = WeChat()
    # 切换到聊天页面
    wx.SwitchToChat()
    for la in listen_atall_list:
        for m in msg_list:
            wx.AtAll(msg=m, who=la)
            wx.SendFiles(filepath=filepath, who=la)
    for l in listen_list:
        for m in msg_list:
            wx.SendMsg(msg=m, who=l)
            wx.SendFiles(filepath=filepath, who=l)


def PushBreakfast():
    category = ["⾯粉粥包"]
    # 消息列表
    msg_list = [
        "🍂秋高气爽，来碗热气腾腾的🍚吧！\n"
        + rand_shop(category)
        + link
        + random.choice(delim)
        + activity
    ]
    # 文件列表
    filepath = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\breakfast.jpg'
        r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\breakfast.jpg"
    ]
    PushMsg(msg_list, filepath)


def PushLunch():
    category = ["特色小吃", "中餐便餐", "⽕锅冒菜", "异国料理"]
    msg_list = [
        # "肯德基星期四，疯狂不止一点点！\n\n🍗 2桶20翅，疯狂美味不停歇！\n💰 61.8元，超值优惠等你来！\n🛵 配送费半价，歪麦平台让你轻松享美食！\n"
        "肚子里的馋🐛在抗议啦，快去投喂它吧！\n"
        + rand_shop(category)
        + link
        + random.choice(delim)
        + activity
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg"]
    PushMsg(msg_list, filepath)


def PushTea():
    category = ["水果果切", "奶茶甜点", "咖啡"]
    msg_list = [
        "🍮🌈𝖬𝖾𝖾𝗍𝗂𝗇𝗀▸ʚ🍰ɞ꙳⋆🍜\n🍹ɞ⋆慵懒下午茶时光♡゛🍹\n"
        + rand_shop(category)
        + link
        + random.choice(delim)
        + activity
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\tea.jpg"]
    PushMsg(msg_list, filepath)


def PushSupper():
    category = ["特色小吃", "中餐便餐", "⽕锅冒菜", "异国料理"]
    msg_list = [
        # "肯德基星期四，疯狂不止一点点！\n\n🍗 2桶20翅，疯狂美味不停歇！\n💰 61.8元，超值优惠等你来！\n🛵 配送费半价，歪麦平台让你轻松享美食！\n"
        "🍱晚餐想吃点什么特别的呢？\n🍤🍛🍗🥘🍲🥙🍢🍔\n"
        + rand_shop(category)
        + link
        + random.choice(delim)
        + activity
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg"]
    PushMsg(msg_list, filepath)


def PushSnack():
    category = ["特色小吃", "其他", "烧烤夜宵", "异国料理"]
    msg_list = [
        "🌃夜生活才刚刚开始~🥠\n啤酒🍺烧烤🍗不能少！\n"
        + rand_shop(category)
        + link
        + random.choice(delim)
        + activity
        + "\n🔔宵夜订单记得要提交哦~~"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\snack.jpg"]
    PushMsg(msg_list, filepath)


def PushActivity():
    msg_list = [
        # "🧧外卖通用神券红包\n美团👉s.c1ns.cn/Vx9J5\n饿了么👉s.c1ns.cn/c25G3\ntips：神券红包和霸王餐可以同时减免呦~\n\n🔗霸王餐链接：s.c1ns.cn/i14hj\n------------------\n🎉【活动挑战赛】🎁\n• 🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n• 🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n• 🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n\n👉活动入口：点击霸王餐链接-点击赚钱-点击活动二海报，即可参与挑战赛"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\acti.jpg"]
    PushMsg(msg_list, filepath)


if __name__ == "__main__":

    # PushBreakfast()
    # PushLunch()
    # PushTea()
    # PushSupper()
    # PushSnack()
    # PushActivity()

    # 定时执行任务
    schedule.every().day.at("08:30:00").do(PushBreakfast)
    # schedule.every().day.at("10:00:00").do(PushActivity)
    schedule.every().day.at("10:30:00").do(PushLunch)
    schedule.every().day.at("14:00:00").do(PushTea)
    # schedule.every().day.at("16:30:00").do(PushActivity)
    schedule.every().day.at("17:00:00").do(PushSupper)
    schedule.every().day.at("21:00:00").do(PushSnack)

    while True:
        schedule.run_pending()
        time.sleep(1)
