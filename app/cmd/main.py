import cv2
from utils import load_image, gray_scale
import process

def main():
    path = input("Type the image name (ex: dog.jpg): ")

    img = load_image(path)

    if img is None:
        print("Erro: image not found in app/photos.")
        return

    # Processamentos
    gray = gray_scale(img)
    shine = process.shine(img, 40)
    blur = process.blur(img, 5)
    sharpness = process.sharpness(img)

    # Mostrar
    cv2.imshow("Original", img)
    cv2.imshow("Gray", gray)
    cv2.imshow("Shine", shine)
    cv2.imshow("Blur", blur)
    cv2.imshow("sharpness", sharpness)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
