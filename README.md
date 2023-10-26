# Smart Tech Final Project

Welcome to the Smart Tech Final Project repository! This project is designed to [detect and classify box by text(large, small) by dobot].

## Key Features

### 1. Real-time Object Recognition
The project captures video frames from a camera in real-time, isolates specific regions of interest, and processes them for object recognition.

### 2. Text Recognition with OCR
Utilizing Tesseract OCR, the application extracts text from the captured frames. It identifies specific keywords such as "large" and "small."

### 3. Robotic Automation
Based on the detected keywords, the integrated Dobot robotic arm performs automated tasks. When "large" is recognized, the robotic arm moves to acquire a box, distinguishes between "a" and "b" positions, and returns to the home position. Similarly, for "small" objects, the arm follows a different set of instructions.

### 4. User Interaction
The application provides user interaction through the terminal, displaying debug information using the IceCream library. Users can monitor the detection process and see the application's decisions in real-time.

## Use Cases

- **Automated Sorting:** The project can be employed in environments where objects need to be sorted based on their size. For instance, in manufacturing industries, it can automate the sorting process based on the text recognition results.

- **Interactive Robotics:** By integrating computer vision and robotics, the application can be utilized for interactive robotics demonstrations, showcasing the capabilities of robotic automation in real-time.

- **Educational Purposes:** The Smart Tech Final Project serves as an educational tool, demonstrating the integration of various technologies, making it a valuable resource for students and enthusiasts interested in computer vision, OCR, and robotics.

## Prerequisites

- Python 3.x installed on the system.
- Access to a compatible camera for real-time video input.
- Properly configured serial ports for communicating with the Dobot robotic arm.
- Dependencies listed in the `requirements.txt` file installed to ensure the correct functioning of the application.

**Note:** This overview provides a high-level understanding of the project's functionality. For detailed information on installation, usage, and specific interactions, please refer to the project's documentation and code comments in the `main.py` file.


## Installation

To get started, install the project dependencies by running the following command:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Stopping the Application

To stop the application, simply press `q` in the terminal where the application is running. This will close the video feed and terminate the program.

