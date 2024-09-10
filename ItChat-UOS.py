import itchat
import schedule
import time

# 登录微信
itchat.auto_login()


# 获取群聊名称（根据实际情况修改）
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['Text'] == '获取群聊名称':
        return msg['User']['NickName']


# 定时发送消息
def send_message():
    # 获取群聊唯一标识（通过上述方法获取）
    chatroom_id = '你的群聊唯一标识'
    itchat.send('这是定时发送的消息', toUserName=chatroom_id)


# 每小时发送一次
schedule.every().hour.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
