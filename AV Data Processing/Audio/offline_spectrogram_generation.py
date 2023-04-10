import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os 
from moviepy.editor import *
import numpy as np
import time
from skimage import io
from skimage.transform import resize

source_folder = 'audio_files/'
target_folder = 'spectrograms/'

for i in os.listdir(source_folder):

    y, sr = librosa.load(source_folder + i,sr=16000)
    mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=512, hop_length=1024)
    mel_spect = librosa.power_to_db(mel_spect, ref=np.max)

    file_name = i.split('.')[0] + '.png'
    print(file_name)

    librosa.display.specshow(mel_spect, fmax=sr)

    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)

    plt.savefig(target_folder + file_name,bbox_inches = 'tight',pad_inches=0)
    time.sleep(0.1)

    im = io.imread(target_folder + file_name)
    # (Optional) use first three channels only and resize to 480x640
    im = resize(im[:,:,0:3],(480,640))
    io.imsave(target_folder + file_name, im)