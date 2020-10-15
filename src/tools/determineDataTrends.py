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

# Apply a linear regression to the x-data and find the range of the y-data to
# compare those values against pre-determined values for determining a gesture
def determineDataTrends(xData, yData, xDataThreshold, yDataThreshold):
    xAxis = []

    for i in range(1, len(xData) + 1):
        xAxis.append(i)

    if len(xData) > 0:
        xSlope = numpy.polyfit(xAxis, xData, 1)[0]

    yRange = max(yData) - min(yData)

    if xSlope < -xDataThreshold:
        gestureDetected = "closer"

    elif xSlope > xDataThreshold:
        gestureDetected = "farther"

    elif yRange > yDataThreshold:
        gestureDetected = "reset"

    else:
        gestureDetected = None

    return gestureDetected
