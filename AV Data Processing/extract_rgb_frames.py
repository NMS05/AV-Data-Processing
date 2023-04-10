import cv2
import os

root_dir = "videos/"
save_dir = "rgb_frames/"
os.makedirs(save_dir,exist_ok=True)


total_vids = len(os.listdir(root_dir))
vid_num = 1

for file_name in os.listdir(root_dir):

    num_frames = 0
    save_name = file_name.split('.mp4')[0]
    os.makedirs(save_dir + save_name, exist_ok=True)
    save_path = save_dir + save_name

    print("Processing....",file_name,"\tProgress",round(vid_num/total_vids,2))
    vid_num += 1

    cap = cv2.VideoCapture(root_dir + file_name)

    # while (True):
    for i in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
        ret, frame = cap.read()
        if ret == False: break

        # asssuming 30fps for original video save frames at 10 fps
        if i%3 != 0: continue
        # comment above line to save frames at 30fps
        # i%10 != 0 for 3fps
        
        frame = cv2.resize(frame,(224,224), interpolation=cv2.INTER_CUBIC)
        num_frames += 1

        s = "%04d" % num_frames
        save_image = save_path + '/frame_' + s + '.jpg'
        cv2.imwrite(save_image, frame)

    # break