import cv2 as cv
import os 
import numpy as np
import sys

#load the cascade untuk pengenalan wajah


DATA_PATH = 'dataset'
MODEL_OUTPUT = 'model_wajah.yml'
LABEL_MAP_OUTPUT = 'label_map.txt'
FACE_SIZE = (200, 200)

def load_face_cascade():
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    #handle error jika file haarcascade tidak ditemukan
    if face_cascade.empty():
        print("Error: Haar cascade file not found.")
        sys.exit(1)
    return face_cascade

def load_dataset():

def save_label_map():

def train_model():

if __name__ == '__main__':
    train_model()