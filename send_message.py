from wxauto import WeChat
import schedule
import time
import random

delim = [
    "————՞•・•՞————",
    "—— ฅ՞••՞ฅ♥ ——",
    "———๑ᵔ⤙ᵔ๑ ⸝⸝———",
    "——ᐢ⸝⸝ › ~ ‹⸝⸝ᐢ——",
    "———ʕ·͡ˑ·ཻʔ ———",
    "———🥯˶╹ꇴ╹˶🥯———",
    "———❛˓◞˂̵✧———",
]

activity = "🔥国庆团长赛火热进行中！🔥\n🧧邀新赢12-70元现金红包🧧\n💎点餐下单送30天会员💎\n👉活动入口：https://s.c1ns.cn/9XnXV"

# 发送对象列表
listen_atall_list = [
    # '测试群'
    # '宁波歪麦霸王餐福利群002',
    # '宁波歪麦霸王餐福利群003',
    # '宁波歪麦霸王餐福利群004',
    # '在宁波0-5元吃霸王餐-A8'
]
listen_list = [
    # '测试群'
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
    # 消息列表
    msg_list = [
        # '这是个测试消息'
        "🏆 【霸王餐来袭】 🏆\n🥪 一日之计在于晨，一顿霸王餐让你全天精神百倍！\n\n真味豆浆\n🈵20返14\n懂包帝·包子豆浆\n🈵20返10\n咬不得高祖生煎\n🈵30返15\n绍兴小笼\n🈵20返10\n三米粥铺\n🈵20返11\n------------------\n⬇快来点链接选店啵~👇\ns.c1ns.cn/i14hj\n\n—————՞•・•՞—————\n🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n👉活动入口：打开APP-点击赚钱-点击活动二海报"
    ]
    # 文件列表
    filepath = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\breakfast.jpg'
        r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\breakfast.jpg"
    ]
    PushMsg(msg_list, filepath)


def PushLunch():
    msg_list = [
        # '肯德基星期四，疯狂不止一点点！\n\n🍗 2桶20翅，疯狂美味不停歇！\n💰 61.8元，超值优惠等你来！\n🛵 配送费半价，歪麦平台让你轻松享美食！\n------------------\n⬇快来点链接选店啵~👇\ns.c1ns.cn/i14hj\n\n—————՞•・•՞—————\n🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n👉活动入口：打开APP-点击赚钱-点击活动二海报'
        "🌈 【午餐不设防】 🌈\n🍔 歪麦霸王餐，让你的午餐时光，美味又自由！\n\n西北阁(炒饭·炒面·炒菜)\n🈵20返14\n兴宁桥烤鸡(邱隘店)\n🈵20返15\n食光解馋坊\n🈵20返15\n尝态·健康创意简餐\n🈵25返15\n来一餐木桶饭第一档口\n🈵20返15\n------------------\n⬇快来点链接选店啵~👇\ns.c1ns.cn/i14hj\n\n—————՞•・•՞—————\n🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n👉活动入口：打开APP-点击赚钱-点击活动二海报"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg"]
    PushMsg(msg_list, filepath)


def PushTea():
    msg_list = [
        "𝖬𝖾𝖾𝗍𝗂𝗇𝗀▸ ʚ🍰ɞ꙳⋆🍜\n🍹ɞ ⋆慵懒下午茶️时光♡゛ 🍹\n\n蜜雪冰城(宁波通用)\n🈵20返10\n榴小可榴莲饮品\n🈵20返12\n喜茶(宁波海曙龙湖天街店)\n🈵20返10\nF·CAFE\n🈵25返12\n273C(带梦陶然店)\n🈵30返15\n------------------\n⬇快来点链接选店啵~👇\ns.c1ns.cn/i14hj\n\n—————՞•・•՞—————\n🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n👉活动入口：打开APP-点击赚钱-点击活动二海报"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\tea.jpg"]
    PushMsg(msg_list, filepath)


def PushSupper():
    msg_list = [
        "千万别点，真的一言难尽...\n一句两句说不清这些店有多好吃😋\n\n\n久久丫·鸭脖(古林店)\n🈵15返12\n食光解馋坊\n🈵20返15\n尝态·健康创意简餐\n🈵25返15\nbigbear韩国炸鸡(海曙店)\n🈵20返13\n毅动轻食·沙拉(镇海新城店)\n🈵25返18\n------------------\n⬇快来点链接选店啵~👇\ns.c1ns.cn/i14hj\n\n—————՞•・•՞—————\n🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n👉活动入口：打开APP-点击赚钱-点击活动二海报"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg"]
    PushMsg(msg_list, filepath)


def PushSnack():
    msg_list = [
        "🍖 【深夜食堂，美食不打烊】 🍲\n夜宵时间到，啤酒🍺烧烤🍗不能少！\n\n盱眙兄弟龙虾·活龙虾(宁波汽车东站店)\n🈵50返27\n8+1小酒馆\n🈵40返37\n思念酒馆·现调鸡尾酒\n🈵55返18\n永钰烤串·必出精品满\n🈵30返16\n------------------\n⬇快来点链接选店啵~👇\ns.c1ns.cn/i14hj\n\n—————՞•・•՞—————\n🔔宵夜订单记得要提交哦~~\n🔔别顾着吃忘记啦~"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\snack.png"]
    PushMsg(msg_list, filepath)


def PushActivity():
    msg_list = [
        # "🧧外卖通用神券红包\n美团👉s.c1ns.cn/Vx9J5\n饿了么👉s.c1ns.cn/c25G3\ntips：神券红包和霸王餐可以同时减免呦~\n\n🔗霸王餐链接：s.c1ns.cn/i14hj\n------------------\n🎉【活动挑战赛】🎁\n• 🔥迎国庆限时团长赛，7天邀新7人赢70元红包🧧\n• 🔥参与吃货挑战赛，30天累计10单赢10元红包🧧\n• 🔥点餐返会员挑战赛，30天累计10单赢30天会员💎\n\n👉活动入口：点击霸王餐链接-点击赚钱-点击活动二海报，即可参与挑战赛"
    ]
    filepath = [r"C:\Users\MM\PycharmProjects\WeChat-Robot\pic\enter.jpg"]
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
    schedule.every().day.at("10:00:00").do(PushActivity)
    schedule.every().day.at("10:30:00").do(PushLunch)
    schedule.every().day.at("14:00:00").do(PushTea)
    schedule.every().day.at("16:30:00").do(PushActivity)
    schedule.every().day.at("17:00:00").do(PushSupper)
    schedule.every().day.at("21:00:00").do(PushSnack)

    while True:
        schedule.run_pending()
        time.sleep(1)
