import cv2
import os

# Load an image from the 'photos' folder
def load_image(filename):
    # Build the full path: photos/filename
    path = os.path.join("photos", filename)
    # Read the image using OpenCV
    return cv2.imread(path)
