# SDVs
Explore the world of Self-Driving Vehicles (SDVs) with this beginner-friendly repository, offering essential resources into autonomous driving and documenting my progress.

This Python repository provides an implementation of lane detection in road images and videos using the Hough Transform and Canny Edge Detection techniques. It also includes a Region of Interest (ROI) feature for more precise lane detection within a defined region.

## Modules

### 1. Hough

The `Hough.py` module contains functions to detect and draw lanes in road images or videos using the Hough Transform.

### 2. Canny Edge Detector

The `Canny_edge_detector.py` module implements the Canny Edge Detection algorithm, which is used to identify edges in the input images, making lane detection more accurate.

### 3. ROI (Region of Interest)

The `roi.py` module defines a region of interest within the input images or videos. This region isolates the lanes and reduces noise, improving the overall lane detection process.

### 4. Real-Time Road Lane Detection

The `Real_Time_Road_lanedetection.py` script demonstrates real-time lane detection using your computer's camera. It combines the Hough and Canny Edge Detection techniques to identify and visualize lanes while driving.

### 5. Sample Video Files

- `lanetest2.mp4`: A sample video demonstrating lane detection on a real road.
- `lanetest3.mp4`: Another sample video showcasing the lane detection algorithm's performance.

### 6. Test Image

The `test_image.jpg` file is a sample road image for testing and validating the lane detection code.

## Getting Started

To get started with this lane detection code, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed (e.g., OpenCV).
3. Run the `Real_Time_Road_lanedetection.py` script to see real-time lane detection in action.

## Usage

You can use this code to implement lane detection in your projects, whether it's for self-driving cars or other computer vision applications.

