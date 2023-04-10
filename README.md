# AV-Data-Processing

This repo provides a compilation of the PyTorch scripts for processing video data. This is helpful for folks working on Audio Visual Multimodal learning. A brief description of these scripts are provided below.

## Video

- ***YT_video_downloader.py*** - Most AV datasets (like VGG Sound, AudioSet, VoxCeleb etc.) are released as csv files, which contains the YouTube video ID and timestamps. This script automatically downloads the videos from YouTube.

- ***video_chopper.py*** - It takes a long duration video and a timestamps (.txt) file as input and chops the videos into smaller segments.

 
## Visual Modality

- ***extract_rgb_frames.py*** - Extract individual frames from a video and save them as RGB images.

- ***Face/extract_face_frames.py*** - Extract individual frames from a video, perform face detection using MTCNN detector and save the face images.


## Audio Modality

- ***Audio/video_to_audio.py*** - Extract .wav audio files from .mp4 videos

- ***Audio/offline_spectrogram_generation.py*** - Preprocess audio by generating spectrograms using Librosa and save them as .png images. This operation need to be performed everytime a spectrogram parameter needs to be changes.

- ***Audio/online_spectrogram_generation.ipynb*** - Generate spectrogram online with torchaudio and calculate the normalization (mean/std) stats. Suitable if the spectrogram parameters need to be adjusted on the fly.
