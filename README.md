# Volume Control 🎵

Control your computer's volume using hand gestures! This project uses computer vision to detect your hand and lets you adjust volume by pinching your thumb and index finger together.

## How It Works

The app uses your webcam to:
1. **Detect your hand** in real-time using AI technology
2. **Track your thumb and index finger** positions
3. **Measure the distance** between them
4. **Adjust volume** based on that distance — closer fingers = lower volume, further apart = higher volume

## Features

✨ **Hand Gesture Recognition** - Detects hands and finger positions  
🎚️ **Real-time Volume Control** - Instantly adjust volume with your hand  
📊 **Live Feedback** - See current volume percentage on screen  
⚡ **Performance Tracking** - FPS counter for smooth operation  
👋 **Multi-hand Support** - Can detect up to 2 hands

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- NumPy
- PyCAW (for Windows volume control)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AmrEladawey/volume-control.git
cd volume-control
```

2. Install dependencies:
```bash
pip install opencv-python mediapipe numpy pycaw
```

## Usage

Run the main script:
```bash
python VolumeControl.py
```

Then:
- Show your hand to the camera
- Bring your thumb and index finger together to lower volume
- Move them apart to increase volume
- Watch the volume percentage display on screen

Press `q` to quit the application.

## Files

- **VolumeControl.py** - Main application script
- **HandTrackingModule.py** - Hand detection and tracking module

## Technologies Used

- **OpenCV** - Video capture and image processing
- **MediaPipe** - Hand detection and landmark tracking
- **PyCAW** - Windows audio device control

## How to Improve This Project

- Add support for other gestures
- Fine-tune detection sensitivity
- Add mute/unmute functionality
- Support for macOS and Linux
- Add hand gesture UI overlay

---

**Made with ❤️ using Computer Vision**
