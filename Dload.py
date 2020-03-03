#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Feb.,2020

@Author:Zhengyi Wang@BNU
'''
import itchat
import os
from pydub import AudioSegment
import numpy as np
import cv2
import csv

@itchat.msg_register([itchat.content.RECORDING, itchat.content.PICTURE,itchat.content.TEXT], isGroupChat=True)
def download(msg):
    global count, GID, UID, SelfID, FolderName
    #download audio, photo and text informations
    if msg['FromUserName'] == GID and msg['ActualUserName'] in UID and msg['Type']=='Recording':
        print("获取音频:#{} 来自 {}".format(count, msg['ActualNickName']))
        msg['Text']('{}/audio/{}.mp3'.format(FolderName,count))
        count += 1
    if msg['FromUserName'] == GID and msg['ActualUserName'] in UID and msg['Type']=='Picture':
        print("下载图片:#{} 来自 {}".format(count, msg['ActualNickName']))
        msg['Text']('{}/Picture/{}.png'.format(FolderName,count))
        count += 1
    if  msg['FromUserName'] == SelfID and msg['ToUserName'] in GID and msg['Type']=='Text' and msg['Text'].startswith('老师，您辛苦了！'):
        # print("合并音频中.....")
        # AudioConcat(count, FolderName)
        print("下载完成，感谢使用，有问题请在GitHub或Bilibili下评论，GitHub请关注:http://github.com/Wang-ZhengYi，Biliili：氢离子宇宙，祝身体健康，我们下次再会！")
        itchat.logout()
        exit(0)




def AudioConcat(count, FolderName):
    if not count:
        return
    result = AudioSegment.from_mp3('{}/audio/0.mp3'.format(FolderName))
    for i in range(1, count):
        result += AudioSegment.from_mp3('{}/audio/{}.mp3'.format(FolderName, i))
    result.export('{}/audio/{}.mp3'.format(FolderName, 'result'), format='mp3')

def course_Info():
    print('**--------武-汉-加-油--------**')
    while True:
        FolderName = input("课程文件夹（请命名与上一次不同）")
        if os.path.exists(FolderName):
            print("文件夹已存在，请重试！")
        else:
            os.mkdir(FolderName)
            os.mkdir(FolderName+"/audio")
            os.mkdir(FolderName+"/Picture")
            os.mkdir(FolderName+"/video")
            # os.mknod(''FolderName.csv'')
            break

    print('**--------武-汉-加-油--------**')
    itchat.get_chatrooms(update=True)
    while True:
        GName = input('微信群名称')
        G = itchat.search_chatrooms(name=GName)
        if G:
            break
    GID = G[0]['UserName']

    print('**--------武-汉-加-油--------**')
    G = itchat.update_chatroom(userName=GID, detailedMember=True)
    MList = G['MemberList']
    UID = []
    Unum = 1 #int(input("请输入老师的总人数："))
    print("请输入主讲人的用户名：")
    while len(UID)< Unum:
        UName = input('用户名：')
        aUID = 0
        for m in MList:
            # print(m['NickName'], m['RemarkName'])
            if UName in [m['NickName'], m['RemarkName']]:
                aUID = m['UserName']
        if aUID:
            UID.append(aUID)
            print('已加入名单:{}'.format(UName))
        else:
            print('无法查找:{}| 请检查后重新输入!'.format(UName))
    print('正在收录： @{}@{}'.format(GName, UName))
    SelfID = itchat.get_friends()[0]['UserName']
    return GID, UID, FolderName, SelfID


if __name__ == '__main__':
    itchat.auto_login(hotReload=False)
    count = 0
    GID, UID, FolderName, SelfID = course_Info()
    data = []
    data = ['{}'.format(FolderName)]
    with open('FolderName.csv', 'w', newline='') as t_file:
        csv_writer = csv.writer(t_file)
        for l in data:
            csv_writer.writerow(l)
    itchat.run()