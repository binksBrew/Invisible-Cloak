### 📄 `README.md`

```markdown
# Invisible Cloak using OpenCV

A fun computer vision project that simulates an "invisibility cloak" using OpenCV. It detects a specific cloak color (red, blue, or green) and replaces it with the background in real-time—creating the illusion of invisibility.

## 🚀 Features

- Real-time video processing via webcam  
- Background capture and cloak detection using HSV masking  
- Simple GUI for color selection and configuration  
- Outputs processed video to file  
- Written in Python 3.7.4 with OpenCV

## 🧰 Requirements

- Python 3.7.4  
- `opencv-python==4.11.0.86`  
- `numpy`  
- `tkinter` *(usually comes pre-installed with Python)*

> 💡 Recommended: Use a virtual environment (`venv`) to manage dependencies.

## 📦 Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone <your-repo-url>
cd Invisible-Cloak-using-OpenCV
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install opencv-python==4.11.0.86 numpy
```

### 4. Run the Program

```bash
python main.py
```

## 🖥️ Usage

1. Select the cloak color from the dropdown (red, blue, or green).  
2. Adjust the number of frames to capture for the background (default is 60).  
3. Enter the desired output filename.  
4. Click **Start Cloak** and step out of frame during background capture.  
5. Press `q` to stop recording.

## 📂 Output

The output video is saved in `.avi` format with the name you specify (default: `output.avi`).

## ⚠️ Notes

- Good lighting and solid-colored cloaks work best.  
- Avoid overlapping colors between the cloak and surroundings.  
- Webcam access is required.

## 📸 Example

Imagine wrapping yourself in a red blanket and vanishing in front of the camera!

## 🧪 Tested On

- Windows 11  
- Python 3.7.4  
- OpenCV 4.11.0.86

## 📜 License

This project is for educational purposes.  
Feel free to modify and experiment with it.
