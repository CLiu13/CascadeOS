"""
    Copyright 2017 Charlie Liu and Bryan Zhou

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from tools.captureProcessFrame import *
from tools.determineDataTrends import *
from tools.processWhitePoints import *
from tools.recordGesture import *
from tools.filterData import *
from tools.recordData import *
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# Image resolution of captured frames
IMG_SIZE = 256

# Size of the surrounding region utilized
# when appying a Gaussian blur on frames
BLUR_REGION = 5

# Cutoff for gray intensity value of pixels when thresholding frames
PIXEL_INTENSITY_THRESHOLD = 10

# Number of elements to analyze when calculating
# trends in x-axis and y-axis movement
DATA_WINDOW_SIZE = 10

# Cutoff values for data points when being filtered
LOWER_OUTLIER_CUTOFF = 25
UPPER_OUTLIER_CUTOFF = 150

# Cutoff values for calculated trends to compare with when detecting gestures
X_DATA_THRESHOLD = 0.5
Y_DATA_THRESHOLD = int(0.25 * IMG_SIZE)

# Value at which the gesture detection will
# terminate and record all data in files
FRAME_COUNT_LIMIT = int(input("Enter a frame count limit: "))

# Zoom scale factor value to pass through the pipe for zoomDisplay.py
ZOOM_FACTOR = 0.4

# Initialize data lists
xData = []
xDataSample = []
xDataFiltered = []

yData = []
yDataSample = []
yDataFiltered = []

# Define camera settings and specify variable to store frame
camera = PiCamera()
camera.resolution = (IMG_SIZE, IMG_SIZE)
rgbFrame = PiRGBArray(camera, size=camera.resolution)

time.sleep(0.1)

frameCount = 0
frame1 = captureProcessFrame(camera, rgbFrame, BLUR_REGION)

while frameCount <= FRAME_COUNT_LIMIT:
    # Increment the frame count each iteration
    frameCount += 1
    frame2 = captureProcessFrame(camera, rgbFrame, BLUR_REGION)

    # Create an image based on the differences between
    # the two frames and then enhance the result
    diffImg = cv2.absdiff(frame1, frame2)
    threshImg = cv2.threshold(diffImg, PIXEL_INTENSITY_THRESHOLD,
                              255, cv2.THRESH_BINARY)[1]

    # Assign frame 1 to frame 2 for the next iteration of comparison
    frame1 = frame2

    whitePixelsData = processWhitePoints(threshImg)
    xData.append(whitePixelsData[0])
    yData.append(whitePixelsData[1])

    # Analyze for trends when a full window of data points has been gathered
    if len(xData) % DATA_WINDOW_SIZE == 0:
        filteredDataWindows = filterData(DATA_WINDOW_SIZE, xData, yData,
                                         LOWER_OUTLIER_CUTOFF,
                                         UPPER_OUTLIER_CUTOFF)

        # If no data points survived the filtering,
        # continue to the next iteration
        if filteredDataWindows is None:
            continue

        xWindowFiltered = filteredDataWindows[0]
        yWindowFiltered = filteredDataWindows[1]

        # Save all filtered data so they can be logged later
        xDataFiltered += xWindowFiltered
        yDataFiltered += yWindowFiltered

        gestureDetected = determineDataTrends(xWindowFiltered, yWindowFiltered,
                                              X_DATA_THRESHOLD,
                                              Y_DATA_THRESHOLD)

        if gestureDetected is not None:
            recordGesture(gestureDetected, ZOOM_FACTOR)
            print("[INFO] Gesture detected: " + gestureDetected)

recordData(xData, xDataFiltered, yData, yDataFiltered)
print("[INFO] Data recorded!")
