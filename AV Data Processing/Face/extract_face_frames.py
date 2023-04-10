import cv2
from tools import FaceAlignmentTools
import os
import numpy as np

root_dir = "videos/"
save_dir = "face_frames/"

tool = FaceAlignmentTools()

total_vids = len(os.listdir(root_dir))
vid_num = 1

for file_name in os.listdir(root_dir):

    num_frames = 0
    save_name = file_name.split('.mp4')[0]
    os.mkdir(save_dir + save_name)
    save_path = save_dir + save_name

    print("Processing....",file_name,"\tProgress",round(vid_num/total_vids,2))
    vid_num += 1

    cap = cv2.VideoCapture(root_dir + file_name)

    while (True):
        ret, frame = cap.read()
        if ret == False: break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        aligned_img = tool.align(frame)

        if aligned_img is None:
            continue  # if no face detected, do not increase the num-frames

        aligned_img = cv2.cvtColor(aligned_img, cv2.COLOR_RGB2BGR)
        aligned_img = cv2.resize(aligned_img,(224,224))
        num_frames += 1

        s = "%04d" % num_frames
        save_image = save_path + '/frame_' + s + '.jpg'

        cv2.imwrite(save_image, aligned_img)

    # break