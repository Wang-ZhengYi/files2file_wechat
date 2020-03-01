import itchat
import os
from pydub import AudioSegment
import numpy as np
import cv2

@itchat.msg_register([itchat.content.RECORDING,itchat.content.TEXT], isGroupChat=True)
def download(msg):
    global count, GID, SelfID, FolderName
    #download audio, photo and text informations
    if msg['FromUserName'] == GID and msg['Type']=='Recording':
        msg['Text']('{}/{}.mp3'.format(FolderName,count))
        count += 1
    if  msg['FromUserName'] == SelfID and msg['ToUserName'] in GID and msg['Type']=='Text' and msg['Text'].startswith('*END*'):
        print("Concating.....")
        AudioConcat(count, FolderName)
        print("Concated，thx for using，comment on Github or Bilibili if have questions，GitHub:http://github.com/Wang-ZhengYi，Biliili：氢离子宇宙，祝身体健康，我们下次再会！")
        itchat.logout()
        exit(0)


def AudioConcat(count, FolderName):
    if not count:
        return
    result = AudioSegment.from_mp3('{}/0.mp3'.format(FolderName))
    for i in range(1, count):
        result += AudioSegment.from_mp3('{}/{}.mp3'.format(FolderName, i))
    result.export('{}/{}.mp3'.format(FolderName, 'result'), format='mp3')

def course_Info(FolderName,GName):
    os.mkdir(FolderName)
    itchat.get_chatrooms(update=True)
    while True:
        G = itchat.search_chatrooms(name=GName)
        if G:
            break
    GID = G[0]['UserName']
    G = itchat.update_chatroom(userName=GID, detailedMember=True)
    SelfID = itchat.get_friends()[0]['UserName']
    return GID, SelfID,FolderName


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    count = 0
    GID, SelfID, FolderName = course_Info(Audio,HII)
    itchat.run()