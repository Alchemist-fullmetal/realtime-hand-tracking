# Real-Time Hand Tracking

A small computer-vision project that tracks hand landmarks from a webcam using MediaPipe and OpenCV.

## Features
- Live webcam capture
- Hand landmark detection
- Finger-state estimation
- Simple gesture label
- FPS overlay

## Run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

Press `q` to quit.

> Note: webcam permission is required. MediaPipe availability can vary by Python version; Python 3.10 or 3.11 is usually the safest choice.
