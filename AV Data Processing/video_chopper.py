# pip install moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import pandas as pd
import numpy as np
import os

with open('timestamps.txt') as f:
    lines = f.readlines()

target_folder = 'chopped_videos/'
os.makedirs(target_folder, exist_ok=True)

def process_time(t):
    minutes, seconds = t.split(':')
    # Remove leading '0', for example in the timestamp 03:32 to 3 min and 32 seconds 
    if minutes[0] == '0' : minutes = minutes[1]
    if seconds[0] == '0' : seconds = seconds[1]
    # print(minutes, seconds)
    return round(float(minutes) * 60 + float(seconds),3)

for i in lines:

    start, end, name = i.split(',')
    start_time = process_time(start)
    end_time = process_time(end)
    name = name.rstrip('\n')
    file_name = target_folder + name + '.mp4' # or .mov
    # print(start_time, end_time, file_name)

    # extracting short video clips
    # original large video in .mp4 or .mov format
    ffmpeg_extract_subclip("long_duration_video.mp4", start_time, end_time, targetname=file_name)
    

""" 
Example of timestamps.txt

03:32,04:22,vid1
05:30,06:08,vid2
09:59,10:43,vid3

"""