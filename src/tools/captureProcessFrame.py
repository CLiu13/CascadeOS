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

import cv2

# Captures a frame via PiCamera and processes
# frame to eliminate unnecessary noise
def captureProcessFrame(camera, rgbFrame, blurRegion):
    camera.capture(rgbFrame, format="bgr", use_video_port=True)
    rawFrame = rgbFrame.array

    grayFrame = cv2.cvtColor(rawFrame, cv2.COLOR_BGR2GRAY)
    blurFrame = cv2.GaussianBlur(grayFrame, (blurRegion, blurRegion), 0)

    rgbFrame.truncate(0)

    return blurFrame
