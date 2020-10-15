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

# Searches for white pixels in an image and returns the ranges of the
# x-coordinates data set and y-coordinates data set;
# if there are nowhite pixels, 0s are returned
def processWhitePoints(img):
    whitePixels = cv2.findNonZero(img)

    if whitePixels is not None:
        whitePixelsList = cv2.findNonZero(img).tolist()

        whitePixelsXValues = []
        whitePixelsYValues = []

        for nestedLists in whitePixelsList:
            for singleList in nestedLists:
                whitePixelsXValues.append(singleList[0])
                whitePixelsYValues.append(singleList[1])

        xMinimum = min(whitePixelsXValues)
        xMaximum = max(whitePixelsXValues)
        xDifference = xMaximum - xMinimum

        yMinimum = min(whitePixelsYValues)
        yMaximum = max(whitePixelsYValues)
        yDifference = yMaximum - yMinimum

        return (xDifference, yDifference)

    return (0, 0)
