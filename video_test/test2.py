import itchat
import os
from pydub import AudioSegment
import numpy as np
import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
from moviepy.editor import *
from moviepy.audio.fx import all
from PIL import Image

def blank_video():
    img = np.zeros((1080,1920,3), np.uint8)
    img[:,:,0].fill(0)
    img[:,:,1].fill(255)
    img[:,:,2].fill(0)
    # cv2.imshow('image', img)
    cv2.imwrite('bg4.png',img)


# input_music_2 = AudioSegment.from_mp3("E:/input2.mp3") 
# input_music_1_db = input_music_1.dBFS
# input_music_2_db = input_music_2.dBFS


fps = 1
save_path = './video_test/saveVideo.mp4'
input_music = AudioSegment.from_mp3("./file/result.mp3") 
input_music_time = len(input_music)
img_path='./video_test/'
frames = int(fps*input_music_time/1000+0.5)
coding = 'mp4v'





def Vmker(img_path,coding,save_path,fps,frames):
	img_list=os.listdir(img_path)
	img_list.sort()
	# img_list.sort(key = lambda x: int(x[2:-4]))
	fourcc = cv2.VideoWriter_fourcc(*coding)
	image = Image.open(img_path + img_list[0])
	videoWriter = cv2.VideoWriter(save_path,fourcc,fps,image.size)
	audio_clip = AudioFileClip('./file/result.mp3')
	background_clip = VideoFileClip(save_path,target_resolution=image.size)
	# print(image.size)
	for i in range(frames):
	    img_name=img_path+'bg1.png'
	    frame = cv2.imread(img_name)
	    videoWriter.write(frame)
	for j in range(len(os.listdir(img_path))):

	videoWriter.release()


Vmker(img_path,coding,save_path,fps,frames)

for i in range(len(os.listdir(img_path))):
	img_list=os.listdir(img_path)
	img_list.sort()
	audio_clip = AudioFileClip('./file/result.mp3')
	background_clip = VideoFileClip(save_path,target_resolution=(1080,1920))
	text_clip = TextClip('test')
	text_clip = text_clip.set_position('center')
	text_clip = text_clip.set_duration(0.2*input_music_time)
	image_clip = ImageClip(img_path + img_list[i])
	image_clip = image_clip.set_duration(0.2*input_music_time).set_audio(audio_clip)


CompositeVideoClip([background_clip,text_clip]).write_videofile('./file/saveVideo.mp4',codec = 'libx264', fps = fps)





exit()