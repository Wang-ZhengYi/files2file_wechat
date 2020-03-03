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

@itchat.msg_register([itchat.content.RECORDING,itchat.content.PICTURE,itchat.content.TEXT], isGroupChat=True)
def download(msg):
    global count, GID, SelfID, FolderName
    #download audio, photo and text informations
    if msg['FromUserName'] == GID and msg['Type']=='Recording':
        msg['Text']('{}/audio/{}.mp3'.format(FolderName,count))
        count += 1
    if msg['FromUserName'] == GID and msg['Type']=='Picture':
        msg['Text']('{}/Picture/{}.png'.format(FolderName,count0))
    if msg['FromUserName'] == SelfID and msg['ToUserName'] in GID and msg['Type']=='Text' and msg['Text'].startswith('Class_over'):
        # print("Concating.....")
        # AudioConcat(count, FolderName)
        print("Downloading over，thanks for using，please comment on Github or Bilibili if have questions，GitHub:http://github.com/Wang-ZhengYi，Biliili：氢离子宇宙，祝身体健康，我们下次再会！")
        itchat.logout()
        exit(0)


def courseG(FolderName,GName):
    os.mkdir(FolderName)
    os.mknod(''FolderName.csv'')
    os.mkdir(FolderName+"/audio")
    os.mkdir(FolderName+"/Picture")
    os.mkdir(FolderName+"/video")
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
    print('##-------武--汉--加--油-------##')
    print('input “Class_over” on WeChat to stop')
    GID, SelfID, FolderName = courseG(wecourse,wecourse_test)

    data = []
    data = ['{}'.format(FolderName)]
    with open('FolderName.csv', 'w', newline='') as t_file:
        csv_writer = csv.writer(t_file)
        for l in data:
            csv_writer.writerow(l)
    itchat.run()