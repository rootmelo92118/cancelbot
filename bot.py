from Linephu.linepy import *
from Linephu.akad.ttypes import *
from time import sleep
import time, os



client = LINE()

oepoll = OEPoll(client)

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.acceptGroupInvitation(op.param1)
        client.sendMessage(op.param1, client.getContact(op.param2).displayName + " 我受傷了 不能陪你玩了")
        client.sendMessage(op.param1, "但是.... 我還可以為你再做一件事")
        client.sendMessage(op.param1, "✿千本桜❀帝國...降臨✘\nhttps://fb.com/star.nightcrazy")
        group = client.getGroup(op.param1)
        if group.invitee is None:
            client.sendMessage(op.param1, "欸欸....沒有邀請欸 " + client.getContact(op.param2).displayName + " 掰掰")
            client.kickoutFromGroup(op.param1, [op.param2])
            client.leaveGroup(op.param1)
        else:
            group = client.getGroup(op.param1)
            groupinvitingmembersmid = [contact.mid for contact in group.invitee]
            for _mid in groupinvitingmembersmid:
                client.cancelGroupInvitation(op.param1, [_mid])
                time.sleep(0.5)
            client.leaveGroup(op.param1)
    except Exception as e:
        print(e)
        print("發生錯誤 正在自動重新登入 如果你是用網址登入的 請自己手動重新登入")
        restart()
        return


oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

while True:
    oepoll.trace()
    
