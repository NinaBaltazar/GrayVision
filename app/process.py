import cv2
import numpy as np

def shine(img, valor):
    return cv2.convertScaleAbs(img, alpha=1, beta=valor)

def blur(img, tamanho):
    if tamanho % 2 == 0:
        tamanho += 1
    return cv2.GaussianBlur(img, (tamanho, tamanho), 0)

def sharpness(img):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    return cv2.filter2D(img, -1, kernel)
