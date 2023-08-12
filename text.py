from tabnanny import verbose
import cv2
import os
import numpy as np
# import openpyxl
#import matplotlib.pyplot as plt
import torch
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# from tensorflow.keras import load_model
from glob import glob
import time
import random
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
tmp = 'winter'


input_path = '/media/hdd08/dungdt/datasets/RoadCond/demo/Night/train/medium'
# output_path = '/media/hdd08/dungdt/outputs/2023-08-8/ModeltrainNew_Night_Transformer/val/no'


# name1 = output_path.split(os.path.sep)[-1].split('_')[1:]


# image_size = (256, 256)
image_size = (512, 512)
class_names = ['heavy', 'medium', 'no']

image_paths = sorted(glob(os.path.join(input_path, '*.*')))
preprocess_input = tf.keras.applications.efficientnet.preprocess_input

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference
def find_max(a, b, c):
    return max(a, b, c)
def create_label_text(result):
    heavy_score = np.round(result[0], 2) * 100
    light_score = np.round(result[1], 2) * 100
    no_score = np.round(result[2], 2) * 100
    max1= find_max(heavy_score, light_score, no_score)
    if heavy_score==max1:
        label_text = f"Heavy"
    if no_score==max1:
        label_text = f"No"
    if light_score==max1:
        label_text = f"Medium"
    return label_text



# checkpoint = torch.load('/media/hdd04/hiennt/Dsnow_Transformer_Day/model_best.pth.tar')
checkpoint = '/media/hdd04/hiennt/checkpointSnowfall_Night_20231008'
# checkpoint = '/media/hdd0/bunbu/dungdt/snowfall_detection/checkpoint_snowfall3_20230808_Day'

# ...

print('Loading checkpoint...')

model = tf.keras.models.load_model(checkpoint)
print('xong ==================================')
# model.summary()
output_file = 'test.txt'
with open(output_file, 'a') as f:
    for i, path in enumerate(image_paths[:10000]):
        print(f'[{i}] Process this image: {path}')
        frame = cv2.imread(path)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, image_size)
        img = tf.expand_dims(img, axis=0)
        img = preprocess_input(img)
        start = time.time()
        result = model.predict(img, verbose=0)
        res = result[0]
        print('Processing time: ', time.time() - start)
        name = os.path.basename(path)
        label_text = create_label_text(res)
        f.write(f"{name},")
        f.write("Medium,")
        f.write(label_text + "\n")

print('Please check the output in', output_file)

