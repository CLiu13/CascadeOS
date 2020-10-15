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

import numpy
import cv2

m = None

# Creates a matrix for perspective transformation
def matrix(width, height, xcompressfactor, ycompressfactor):
    x1 = (xcompressfactor / 2) * width
    x2 = width - x1
    newheight = height * ycompressfactor
    oldpoints = numpy.float32([[0, 0], [width, 0],
                              [0, height], [width, height]])
    newpoints = numpy.float32([[x1, 0], [x2, 0],
                              [0, newheight], [width, newheight]])
    matrix = cv2.getPerspectiveTransform(oldpoints, newpoints)
    return matrix


# Performs perspective transformation on an image using the given factors
def transform(img, width, height, xcompressfactor, ycompressfactor):
    global m
    if m is None:
        m = matrix(width, height, xcompressfactor, ycompressfactor)

    newimg = cv2.warpPerspective(img, m, (width, height))
    return newimg
