import cv2
import os

def load_image(file_name):
    caminho = os.path.join("Photos", file_name)
    img = cv2.imread(caminho)
    return img

def gray_scale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
