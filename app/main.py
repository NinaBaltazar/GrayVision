import cv2
from utils import load_image
import process

# Main application with sliders
def main():
    name = input("Enter the image filename (e.g., dog.jpg): ")

    # Load image from photos/
    original = load_image(name)

    if original is None:
        print("Error: image not found in 'photos' folder.")
        return

    # Create main window
    cv2.namedWindow("Image Editor")

    # Trackbars (sliders)
    cv2.createTrackbar("Brightness", "Image Editor", 50, 100, lambda x: None)
    cv2.createTrackbar("Blur", "Image Editor", 1, 25, lambda x: None)
    cv2.createTrackbar("Sharpness", "Image Editor", 0, 5, lambda x: None)
    cv2.createTrackbar("Grayscale (0/1)", "Image Editor", 0, 1, lambda x: None)

    # Main loop
    while True:
        img = original.copy()  # Always start with the original image

        # Read slider values
        brightness = cv2.getTrackbarPos("Brightness", "Image Editor") - 50
        blur = cv2.getTrackbarPos("Blur", "Image Editor")
        sharpness = cv2.getTrackbarPos("Sharpness", "Image Editor")
        grayscale = cv2.getTrackbarPos("Grayscale (0/1)", "Image Editor")

        # Apply effects
        img = process.adjust_brightness(img, brightness)
        img = process.apply_blur(img, blur)
        img = process.apply_sharpness(img, sharpness)

        # Apply grayscale if enabled
        if grayscale == 1:
            img = process.to_grayscale(img)

        # Show final image
        cv2.imshow("Image Editor", img)

        # ESC key exits the program
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
