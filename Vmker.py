#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Feb.,2020

@Author:Zhengyi Wang@BNU
'''

import numpy as np
import os
import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
from moviepy.editor import *
from moviepy.audio.fx import all
from PIL import Image
from pydub import AudioSegment
import time



# f = open('FolderName.csv', 'r')
# csvreader = csv.reader(f)
# FNs = list(csvreader)
# FolderName = FNs[0]

FolderName = 'course'

numP = len(os.listdir('{}/picture/'.format(FolderName)))
numA = len(os.listdir('{}/audio/'.format(FolderName)))
# global numP,numA

def AudioConcat():
	if not numA:
		return '0'
	result = AudioSegment.from_mp3('{}/audio/0.mp3'.format(FolderName))
	for k in range(1, numA):
		result += AudioSegment.from_mp3('{}/audio/{}.mp3'.format(FolderName,k))
	result.export('{}/video/result.mp3'.format(FolderName), format='mp3')

def vframe():
	img_list=os.listdir('{}/picture/'.format(FolderName))
	img_list.sort()
	img_list.sort(key = lambda x: int(x[0:-4]))
	cc = cv2.VideoWriter_fourcc(*'mp4v')
	image = Image.open('{}/picture/'.format(FolderName) + img_list[0])
	videoWriter = cv2.VideoWriter('{}/video/course_video.mp4'.format(FolderName),cc,1,image.size)
	audio_t = np.zeros(numA,dtype='float')
	audio_t[0]=int(len(AudioSegment.from_mp3('{}/audio/{}.mp3'.format(FolderName,0)))/1000)
	for i in range(1,numA):
		audio_t[i] = audio_t[i-1] + int(len(AudioSegment.from_mp3('{}/audio/{}.mp3'.format(FolderName,i)))/1000)
	for m in range(int(audio_t[int(img_list[0][0:-4])])):
		img_name = '{}/picture/'.format(FolderName)+img_list[0]
		frame = cv2.imread(img_name)
		videoWriter.write(frame)
	for i in range(numP):
		for k in range(int(audio_t[int(img_list[int(i+1)*(i<numP-1)][0:-4])]*(i<numP-1)+audio_t[-1]*(i==numP-1) - audio_t[int(img_list[i][0:-4])])):
			img_name = '{}/picture/'.format(FolderName)+img_list[i]
			frame = cv2.imread(img_name)
			videoWriter.write(frame)

	videoWriter.release()
	audio_clip = AudioFileClip('{}/video/{}.mp3'.format(FolderName,'result'))
	text_clip0 = TextClip('', fontsize = 13, color = 'black')
	text_clip0 = text_clip0.set_position('bottom')
	text_clip0 = text_clip0.set_duration(1).set_audio(audio_clip)
	CompositeVideoClip(text_clip0).write_videofile('{}/video/{}.mp4'.format(FolderName,'course_video'),codec = 'mp4v', fps = 1)


if __name__ == '__main__':
	Time_start=time.time()
	# AudioConcat()
	vframe()
	Time_end=time.time()
	print('running time:',Time_end-Time_start,'s')
