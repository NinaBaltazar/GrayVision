import cv2
import numpy as np

# Adjust image brightness
# value: amount to add/subtract (-50 to +50)
def adjust_brightness(img, value):
    return cv2.convertScaleAbs(img, alpha=1, beta=value)

# Apply Gaussian blur
# strength: blur intensity (must be odd)
def apply_blur(img, strength):
    if strength <= 1:
        return img
    if strength % 2 == 0:  # Blur requires odd number
        strength += 1
    return cv2.GaussianBlur(img, (strength, strength), 0)

# Apply sharpness filter (sharpen kernel)
def apply_sharpness(img, amount):
    if amount == 0:
        return img

    # Sharpening kernel — higher center value gives stronger sharpening
    kernel = np.array([
        [0, -1, 0],
        [-1, 5 + amount, -1],
        [0, -1, 0]
    ])
    return cv2.filter2D(img, -1, kernel)

# Convert image to grayscale
def to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
