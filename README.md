# Real-Time Hand Tracking

A computer-vision project that detects and tracks hand landmarks from a live webcam feed using MediaPipe and OpenCV, then derives simple finger states and gesture labels.

## Features

- **Real-Time Webcam Capture:** Live video stream processing with OpenCV.
- **Hand Landmark Detection:** 21 3D hand keypoints extracted using MediaPipe Hands.
- **Handedness Classification:** Distinguishes between Left and Right hands.
- **Finger-State Estimation:** Evaluates open/closed states for thumb and fingers via landmark geometry.
- **Simple Gesture Recognition:** Recognizes basic gestures:
  - Fist
  - Open palm
  - Point
  - Peace
- **FPS Display:** Real-time frames-per-second monitoring overlay.
- **Multi-Hand Support:** Concurrently tracks up to two hands.

## Tech Stack

- **Language:** Python
- **Computer Vision:** OpenCV (`opencv-python`)
- **ML Framework:** MediaPipe (`mediapipe`)

## How It Works

1. **Webcam Frame Capture:** Reads live video frames sequentially using OpenCV `VideoCapture`.
2. **RGB Conversion:** Converts BGR frames to RGB for MediaPipe processing.
3. **MediaPipe Inference:** Runs MediaPipe Hands pipeline to detect 21 landmarks per hand.
4. **Landmark Drawing:** Renders skeletal joints and connections using MediaPipe drawing utilities.
5. **Finger-State Inference:** Evaluates landmark coordinate relationships (tips relative to PIP joints).
6. **Gesture Labeling:** Maps finger states to recognized gesture names (`Fist`, `Open palm`, `Point`, `Peace`).
7. **FPS Overlay:** Computes frame deltas and draws the current FPS on screen.

## Demo

> TODO: Record a short GIF/video of the real webcam demo.

## Installation & Run

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tracking script:
   ```bash
   python main.py
   ```

Press `q` to exit the application.

> **Note:** Webcam permissions are required. MediaPipe availability can vary by Python version; Python 3.10 or 3.11 is recommended.
