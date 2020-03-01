import itchat
import os
from pydub import AudioSegment
import numpy as np
import cv2

@itchat.msg_register([itchat.content.RECORDING, itchat.content.PICTURE,itchat.content.TEXT], isGroupChat=True)
def download(msg):
    global count, GID, UID, SelfID, FolderName
    #download audio, photo and text informations
    if msg['FromUserName'] == GID and msg['ActualUserName'] in UID and msg['Type']=='Recording':
        print("Recording:#{} from {}".format(count, msg['ActualNickName']))
        msg['Text']('{}/{}.mp3'.format(FolderName,count))
        count += 1
    # if msg['FromUserName'] == GID and msg['ActualUserName'] in UID and msg['Type']=='Picture':
    #     print("Pictures downloading:#{} From {}".format(count, msg['ActualNickName']))
    #     msg['Text']('{}/{}.png'.format(FolderName,count))
    #     count += 1
    if  msg['FromUserName'] == SelfID and msg['ToUserName'] in GID and msg['Type']=='Text' and msg['Text'].startswith('老师，您辛苦了！'):
        print("Concating.....")
        AudioConcat(count, FolderName)
        print("Everything is done，Thx for using，comment blow my github if workout，GitHub:http://github.com/Wang-ZhengYi，Biliili：氢离子宇宙，祝身体健康，我们下次再会！")
        itchat.logout()
        exit(0)

# def blank_video():
#     img = np.zeros((1920,1080,3), np.uint8)
#     img.fill(255)
#     cv2.imshow('image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


def AudioConcat(count, FolderName):
    if not count:
        return
    result = AudioSegment.from_mp3('{}/0.mp3'.format(FolderName))
    for i in range(1, count):
        result += AudioSegment.from_mp3('{}/{}.mp3'.format(FolderName, i))
    result.export('{}/{}.mp3'.format(FolderName, 'result'), format='mp3')

def course_Info():
    print('**--------武-汉-加-油--------**')
    while True:
        FolderName = input("Coure FolderName")
        if os.path.exists(FolderName):
            print("Folder Exits, Plz try again！")
        else:
            os.mkdir(FolderName)
            break

    print('**--------武-汉-加-油--------**')
    itchat.get_chatrooms(update=True)
    while True:
        GName = input('Wechat Group Name:')
        G = itchat.search_chatrooms(name=GName)
        if G:
            break
    GID = G[0]['UserName']

    print('**--------武-汉-加-油--------**')
    G = itchat.update_chatroom(userName=GID, detailedMember=True)
    MList = G['MemberList']
    UID = []
    Unum = 1 #int(input("请输入老师与助教的总人数："))
    print("Teacher's UserName：")
    while len(UsrID)< Unum:
        UName = input('UserName：')
        aUsrID = 0
        for m in MList:
            # print(m['NickName'], m['RemarkName'])
            if UName in [m['NickName'], m['RemarkName']]:
                aUsrID = m['UserName']
        if aUsrID:
            UID.append(aUsrID)
            print('Added:{}'.format(UName))
        else:
            print('Cannot find:{}| plz reinput after checking!'.format(UName))
    print('Recording ： @{}@{}'.format(GName, UName))
    SelfID = itchat.get_friends()[0]['UserName']
    return GID, UID, FolderName, SelfID


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    count = 0
    GID, UID, FolderName, SelfID = course_Info()
    itchat.run()