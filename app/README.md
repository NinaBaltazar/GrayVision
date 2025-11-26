# GrayVision

This project allows you to edit an image using sliders in real time.
You can control:

- Brightness
- Blur
- Sharpness
- Grayscale toggle

All edits are applied using **OpenCV**.


## Project Structure
```
project/
├── photos/
├── main.py
├── process.py
├── README.md
├── requirements.txt
└── utils.py
```

## How to Run

### Running Locally

If you have Python installed on your machine:

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Run the program:
```
python main.py
```

And the program opens with all sliders working.

# How the Application Works

1. The program asks for the image filename (inside `photos/`).
2. Opens the main window with sliders.
3. You control:
   - **Brightness** (lighter/darker)
   - **Blur** (more/less blur)
   - **Sharpness** (crisper edges)
   - **Grayscale** (color or B&W)
4. All changes update in real time.
5. Press **ESC** to close.
