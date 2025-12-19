# Hand Controlled Fluid Box

A real-time **hand-controlled fluid simulation** using Python, OpenCV, and MediaPipe. Move your hand in front of the webcam to interact with fluid particles inside a box!

## Features
- Tracks your hand using MediaPipe.
- Fluid particles respond to hand movements.
- Interactive and real-time simulation.

## Requirements
- Python 3.10+
- Libraries:
  - `opencv-python`
  - `mediapipe`
  - `numpy`
  - `pygame` (if using for particles)
  - `tensorflow` (optional if using ML features)

Install dependencies using:
```bash
pip install opencv-python mediapipe numpy pygame tensorflow
Usage
Clone or download the repository.

Make sure your webcam is connected.

Run the main Python file:

bash
Copy code
python hand_fluid_simulation.py
Move your hand in front of the webcam to control the fluid particles.

Project Structure
bash
Copy code
📁 hand_fluid_box
        main.py
 ├── fluid.py # Main script
 ├── hand_tracking.py                  
 ├── README.md                  # Project documentation
 └── .gitignore                 # Git ignore file
Notes
Works best in good lighting conditions.

Tested on Windows 10/11, should work on Acer Aspire 3 and other laptops with webcam.

For best performance, close other heavy apps