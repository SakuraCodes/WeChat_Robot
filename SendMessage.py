from wxauto import WeChat
import schedule
import time

# 发送对象列表
listen_list = [
    # '测试群'
    '宁波歪麦霸王餐福利群002',
    '宁波歪麦霸王餐福利群003',
    '宁波歪麦霸王餐福利群004',
    '在宁波0-5元吃霸王餐-A8',
    '在宁波0-5元吃霸王餐-A9',
    '宁波福利群-100',
    '宁波福利群-101'
]

# At人员列表
at_list = [
    '桜'
]


def PushBreakfast():
    # 获取微信窗口对象
    wx = WeChat()
    # 发送消息列表
    message_list = [
        # '这是个早餐测试消息'
        '早上好！新的一天，从一顿美味的霸王餐开始吧！🌞\n店铺已选好，就等你啦！\n🥛真味豆浆\n🈵20返14\n🥚懂包帝·包子豆浆\n🈵20返10\n🥟咬不得高祖生煎\n🈵30返15\n🥙绍兴小笼\n🈵20返10\n🍚三米粥铺\n🈵20返11\n霸王餐链接：👇\n6url.cn/C8XKHh \n————՞•・•՞————\n[庆祝]上线参与有机会把iPad、拍立得等开学礼包带回家！\n活动：sourl.cn/PGDZa2'
    ]
    # 发送文件
    files = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\breakfast.jpg',  # 图片
        r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\breakfast.jpg',  # 图片
        # r'C:\Users\user\Desktop\2.txt',  # 文件
        # r'C:\Users\user\Desktop\3.mp4'  # 视频
    ]
    for l in listen_list:
        for m in message_list:
            wx.SendMsg(msg=m, who=l)
            # wx.AtAll(msg=m, who=l)
            # wx.SendFiles(filepath=files, who=l)


def PushLunch():
    # 获取微信窗口对象
    wx = WeChat()
    # 发送消息列表
    message_list = [
        # '【🔔歪麦资讯】\n①、\n②、'
        # '中午好！是时候用一顿丰盛的霸王餐来犒劳自己了！🍽️\n店铺已选好，就等你啦！\n🍛鮨·渔知精致料理\n🈵20返12\n🥘食光解馋坊\n🈵20返15\n🍲会飞不二(创新128广场店)\n🈵25返15\n🥙尝态·健康创意简餐\n🈵25返15\n🍳来一餐木桶饭第一档口\n🈵20返15\n霸王餐链接：👇\n6url.cn/C8XKHh\n————՞•・•՞————\n[庆祝]上线参与有机会把iPad、拍立得等开学礼包带回家！\n活动：sourl.cn/PGDZa2'
        '今日午餐任务🥘🍲🍱🥙🍔\n你想好吃什么了吗？\n\n西北阁(炒饭·炒面·炒菜)\n🈵20返14\n\n🐥兴宁桥烤鸡(邱隘店)\n🈵20返15\n\n🥘食光解馋坊\n🈵20返15\n\n🥙尝态·健康创意简餐\n🈵25返15\n\n🍳来一餐木桶饭第一档口\n🈵20返15\n带你0-5元点一顿豪华外卖\n-----------------\n⬇快来点链接选店~👇\n6url.cn/C8XKHh\n————՞•・•՞————\n[庆祝]上线参与有机会把iPad、拍立得等开学礼包带回家！\n活动：sourl.cn/PGDZa2'
    ]
    # 发送文件
    files = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\dinner.jpg',  # 图片
        r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg',  # 图片
        # r'C:\Users\user\Desktop\2.txt',  # 文件
        # r'C:\Users\user\Desktop\3.mp4'  # 视频
    ]
    for l in listen_list:
        for m in message_list:
            wx.SendMsg(msg=m, who=l)
            # wx.AtAll(msg=m, who=l)
            # wx.SendFiles(filepath=files, who=l)


def PushTea():
    # 获取微信窗口对象
    wx = WeChat()
    # 发送消息列表
    message_list = [
        # '🧁'
        # '限时限量！下午茶霸王餐，手慢无！🍮\n店铺已选好，就等你啦！\n🧋蜜雪冰城(宁波通用)\n🈵20返10\n🍹榴小可榴莲饮品\n🈵20返12\n🍸️喜茶(宁波海曙龙湖天街店)\n🈵20返10\n🥃F·CAFE\n🈵25返12\n🥤273C(带梦陶然店)\n🈵30返15\n霸王餐链接：👇\n6url.cn/C8XKHh\n————՞•・•՞————\n[庆祝]上线参与有机会把iPad、拍立得等开学礼包带回家！\n活动：sourl.cn/PGDZa2'
        '犯困可真是个喝奶茶的好理由呀[嘿哈]\n🧋蜜雪冰城(宁波通用)\n🈵20返10\n\n🍸️喜茶(宁波海曙龙湖天街店)\n🈵20返10\n\n🍹榴小可榴莲饮品\n🈵20返12\n\n🥃F·CAFE\n🈵25返12\n\n🍮山奈(咖啡·甜点)\n🈵20返13\n霸王餐链接：👇\n6url.cn/C8XKHh\n————՞•・•՞————\n[庆祝]上线参与有机会把iPad、拍立得等开学礼包带回家！\n活动：sourl.cn/PGDZa2'
    ]
    # 发送文件
    files = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\tea.jpg',  # 图片
        r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\tea.jpg',  # 图片
        # r'C:\Users\user\Desktop\2.txt',  # 文件
        # r'C:\Users\user\Desktop\3.mp4'  # 视频
    ]
    for l in listen_list:
        for m in message_list:
            wx.SendMsg(msg=m, who=l)
            # wx.AtAll(msg=m, who=l)
            # wx.SendFiles(filepath=files, who=l)


def PushSupper():
    # 获取微信窗口对象
    wx = WeChat()
    # 发送消息列表
    message_list = [
        # '这是个早餐测试消息'
        # '晚上好！一天的忙碌过后，是时候用一顿丰盛的晚餐来放松自己了！🌙\n店铺已选好，就等你啦！\n🍛鮨·渔知精致料理\n🈵20返12\n🥘食光解馋坊\n🈵20返15\n🍲会飞不二(创新128广场店)\n🈵25返15\n🥙尝态·健康创意简餐\n🈵25返15\n🍳来一餐木桶饭第一档口\n🈵20返15\n霸王餐链接：👇\nhttps://6url.cn/C8XKHh\n————՞•・•՞————\n邀请好友吃霸王餐 领20R奖励'
        # '下班干饭，让我用美食驱赶一天的疲惫！\n\n🥘久久丫·鸭脖(古林店)\n🈵15返12\n\n兴宁桥烤鸡(邱隘店)\n🈵20返15\n\n食光解馋坊\n🈵20返15\n\n西北阁(炒饭·炒面·炒菜)\n🈵20返14\n\n高大乐桂林米粉(128广场店)\n🈵30返15\n\n[红包]『歪麦』成本价点外卖\n👉https://6url.cn/fEGtuw\n————՞•・•՞————\n [庆祝]上线参与0元许愿，点餐就把iPad、拍立得等开学礼包带回家！今天参与明天14：30开奖哦~详情入口：https://sourl.cn/PGDZa2'
        # '📣【吃晚餐啦】超值新品上线\n🥰麻辣烫🥘，猪脚饭🍱，轻食🥙，面食🍜...应有尽有\n\n🥓久久丫·鸭脖(古林店)\n🈵15返12\n—— —— —— —— ——\n🍲西北阁(炒饭·炒面·炒菜)\n🈵20返14\n—— —— —— —— ——\n🍗兴宁桥烤鸡(邱隘店)\n🈵20返15\n—— —— —— —— ——\n🍱食光解馋坊\n🈵20返15\n😍超低限时补贴，手慢无！👉6url.cn/fEGtuw\n🔥吃霸王餐0元许愿，赢取iPad、拍立得👉：sourl.cn/PGDZa2'
        '回头客飙升的店铺，必须拿捏👇\n\n🥓久久丫·鸭脖(古林店)\n🈵15返12\n—— —— —— —— ——\n🍲西北阁(炒饭·炒面·炒菜)\n🈵20返14\n—— —— —— —— ——\n🍗兴宁桥烤鸡(邱隘店)\n🈵20返15\n—— —— —— —— ——\n🍱食光解馋坊\n🈵20返15\n😍超低限时补贴，手慢无！👉6url.cn/fEGtuw\n🔥吃霸王餐0元许愿，赢取iPad、拍立得👉：sourl.cn/PGDZa2'
    ]
    # 发送文件
    files = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\快乐干饭.png',  # 图片
        r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\快乐干饭.png',  # 图片
        # r'C:\Users\user\Desktop\2.txt',  # 文件
        # r'C:\Users\user\Desktop\3.mp4'  # 视频
    ]
    for l in listen_list:
        for m in message_list:
            wx.SendMsg(msg=m, who=l)
            # wx.AtAll(msg=m, who=l)
            # wx.SendFiles(filepath=files, who=l)


def PushSnack():
    # 获取微信窗口对象
    wx = WeChat()
    # 发送消息列表
    message_list = [
        # '夜宵时间到，啤酒🍺烧烤🍗不能少。\n\n🍤盱眙兄弟龙虾·活龙虾(宁波汽车东站店)\n🈵50返27\n\n🍺8+1小酒馆\n🈵40返37\n\n🍻思念酒馆·现调鸡尾酒\n🈵55返18\n\n🍢永钰烤串·必出精品满\n🈵30返16\n\n歪麦霸王餐链接👇\n6url.cn/C8XKHh\n美团红包链接👇\n6url.cn/yzc5b8\n————՞•・•՞————\n[庆祝]上线参与有机会把iPad、拍立得等开学礼包带回家！\n活动：sourl.cn/PGDZa2'
        '女孩子千万不要夜跑🏃‍♀️太危险了，\n😱万一遇到烧烤摊就完了\n\n🍤盱眙兄弟龙虾·活龙虾(宁波汽车东站店)\n🈵50返27\n—— —— —— —— ——\n🍺8+1小酒馆\n🈵40返37\n—— —— —— —— ——\n🍻思念酒馆·现调鸡尾酒\n🈵55返18\n—— —— —— —— ——\n🍢永钰烤串·必出精品满\n🈵30返16\n『歪麦』成本价点外卖\n👉6url.cn/fEGtuw\n————՞•・•՞————\n宵夜订单记得要提交哦~~\n别顾着吃忘记啦'
    ]
    # 发送文件
    files = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\Snack.png',  # 图片
        r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\Snack.png',  # 图片
        # r'C:\Users\user\Desktop\2.txt',  # 文件
        # r'C:\Users\user\Desktop\3.mp4'  # 视频
    ]
    for l in listen_list:
        for m in message_list:
            wx.SendMsg(msg=m, who=l)
            # wx.AtAll(msg=m, who=l)
            wx.SendFiles(filepath=files, who=l)


def PushActivity():
    # 获取微信窗口对象
    wx = WeChat()
    # 发送消息列表
    message_list = [
        # '这是个早餐测试消息'
        # '🚀【活动置顶】开学季狂欢，会员福利享不停！🎉\n\n🎁【开学季点霸王餐返会员】开学季福利大放送！ \n30天内完成10单即享30天会员，霸王餐等你拿！\n\n🎁【开学季限时团长赛】开学季就是要拼团！ 邀请好友，赢取70麦粒，快来挑战吧！\n\n⏰【活动时间】：9月2日-9月16日，限时狂欢，抓紧机会！\n\n👥【呼朋唤友】\n快告诉你的小伙伴们，一起组队参与，让这份开学惊喜传递给更多人！🌈\n\n活动详情戳：6url.cn/C8XKHh'
        # '[庆祝]周三霸王日活动一览表，[礼物]福利快速浏览\n\n1⃣【吃霸王餐抽取iPad】🔥\n越吃越幸运，奖品有iPad、拍立得、年会员、万元红包等开学礼包，连续14天每日送一台；\n参与的宝子都能领取1天会员，人人有份\n\n2⃣【独家口令】\n7天会员免费领，在app兑换专区-输入口令：上歪麦抽ipad\n\n3⃣【好友助力】\na.每邀请一位好友吃霸王餐，额外获得❺张许愿卷！\nb.邀请好友吃霸王餐 领7天会员和13元现金[红包]\nc.参与开学季限时团长赛可获得70元现金[红包]\nd.参与开学季点霸王餐活动可获得30天会员奖励\n\n👉 还没领取的宝子快速领取，开学季活动这里看：https://sourl.cn/PGDZa2'
        '[庆祝]活动一览表，[礼物]福利快速浏览\n\n1⃣【吃霸王餐抽取iPad】🔥\n越吃越幸运，奖品有iPad、拍立得、年会员、万元红包等开学礼包，连续14天每日送一台；\n参与的宝子都能领取1天会员，人人有份\n\n2⃣【好友助力】\na.每邀请一位好友吃霸王餐，额外获得❺张许愿卷！\nb.邀请好友吃霸王餐 领7天会员和13元现金[红包]\nc.参与开学季限时团长赛可获得70元现金[红包]\nd.参与开学季点霸王餐活动可获得30天会员奖励\n\n👉 还没领取的宝子快速领取，开学季活动这里看：https://sourl.cn/PGDZa2\n👉 领7天会员：6url.cn/DquG8s'
    ]
    # 发送文件
    files = [
        # r'F:\!Code\Code_Python\WeChat-Robot\pic\activity.jpg',  # 图片
        r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\activity.jpg'
        # r'C:\Users\user\Desktop\2.txt',  # 文件
        # r'C:\Users\user\Desktop\3.mp4'  # 视频
    ]
    for l in listen_list:
        for m in message_list:
            wx.SendMsg(msg=m, who=l)
            # wx.AtAll(msg=m, who=l)
            wx.SendFiles(filepath=files, who=l)


# PushBreakfast()
# PushLunch()
# PushTea()
# PushSupper()
# PushActivity()
# PushSnack()

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
