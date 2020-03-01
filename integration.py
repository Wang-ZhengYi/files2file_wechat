#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Feb.,2020

@Author:Zhengyi Wang@BNU
'''

import itchat

from pydub import AudioSegment

files_path = "/home/hii-univers/GitHub/files2file_wechat/audio"
save_path = "/home/hii-univers/GitHub/files2file_wechat/file/result.mp3"


# 加载需要合并的两个mp3音频
input_music_1 = AudioSegment.from_mp3(files_path + "/Finale.mp3") 
input_music_2 = AudioSegment.from_mp3(files_path + "/your_answer.mp3") 
#获取两个音频的响度（音量）
input_music_1_db = input_music_1.dBFS
input_music_2_db = input_music_2.dBFS
# 获取两个音频的时长，单位为毫秒
input_music_1_time = len(input_music_1)
input_music_2_time = len(input_music_2)
# 调整两个音频的响度一致
db = input_music_1_db - input_music_2_db
if db > 0:
    input_music_1 += abs(db)
elif db < 0:
    input_music_2 += abs(db)
# 合并音频
output_music = input_music_1 + input_music_2
# 简单输入合并之后的音频
# output_music.export("E:/output_music.mp3", format="mp3")# 前面是保存路径，后面是保存格式
#复杂输入合并之后的音频
# bitrate：比特率，album：专辑名称，artist：歌手，cover：封面图片
output_music.export(save_path, format="mp3", bitrate="192k", tags={"album": "专辑", "artist": "歌手"},
	# cover="E:/封面.jpg"
	) 
print(len(output_music), output_music.channels)# 合并音频的时长，音频的声道，1是单声道，2是立体声

def Audio_merge(files_folder,save_path)
	input_music_1 = AudioSegment.from_mp3(files_path + "/Finale.mp3")