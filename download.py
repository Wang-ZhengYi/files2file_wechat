#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Feb.,2020

@Author:Zhengyi Wang@BNU
'''

import itchat



@itchat.msg_register([itchat.content.RECORDING, itchat.content.PICTURE])

def download_files(msg):
    msg.download(msg.fileName)
#the function will download audio files and pictures automaticlly

itchat.auto_login(hotReload = True)
itchat.run()


