# Eye Movement Detection using OpenCV

## Overview

This project utilizes OpenCV, a popular computer vision library, to detect eye movements in real-time video captured from a webcam. It tracks the position of the eyes within detected faces and provides visual feedback on the screen.

## Installation

To run this project, you need to have Python installed on your system along with the following libraries:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- Time (`time`)

You can install the required libraries using pip:

```bash
pip install opencv-python numpy

How it Works
------------
- **Face and Eye Detection:** The program uses pre-trained Haar cascade classifiers provided by OpenCV to detect faces and eyes in the webcam feed.
  
- **Eye Tracking:** After detecting a face, the program focuses on the region of interest (ROI) containing the eyes. It tracks the movement of the eyes by drawing lines between consecutive positions of the detected eye centers.
  
- **Eyes Closed Detection:** If the program detects that the eyes are closed or not looking at the screen, it displays a message in red indicating this condition.
  
- **Countdown Timer:** A countdown timer is displayed on the screen, starting from 5 seconds. If the eyes remain closed or not looking at the screen for the duration of the countdown, the program captures a picture from the webcam.
  
- **Snapshot Capture:** Upon reaching zero, the program captures and saves a picture with a timestamp. It continues to capture pictures every 2 seconds until the eyes are detected back.

Usage
-----
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/hiluxfnh/Proctoshield.git
    ```

2. Navigate to the project directory:

    ```bash
    cd eye-movement-detection
    ```

3. Run the Python script:

    ```bash
    python vision.py
    ```

4. Follow the on-screen instructions. Press 'q' to quit the program.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README according to your specific project details and preferences!
