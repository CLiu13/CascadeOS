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

# Filters corresponding data lists by eliminating outliers
# (determined by preset values) and the remaining maximum and minimum values
def filterData(dataWindowSize, xData, yData,
               lowerOutlierCutoff, upperOutlierCutoff):
    xDataWindow = xData[len(xData) - dataWindowSize:len(xData)]
    yDataWindow = yData[len(yData) - dataWindowSize:len(yData)]

    xWindowFiltered = []
    yWindowFiltered = []

    for i in range(0, len(xDataWindow)):
        if xDataWindow[i] > lowerOutlierCutoff and \
                xDataWindow[i] < upperOutlierCutoff:
            xWindowFiltered.append(xDataWindow[i])
            yWindowFiltered.append(yDataWindow[i])

    if len(xWindowFiltered) >= 2:
        maxIndex = xWindowFiltered.index(max(xWindowFiltered))

        if maxIndex == 0:
            minIndex = 0

        else:
            minIndex = xWindowFiltered.index(min(xWindowFiltered)) - 1

        xWindowFiltered.remove(max(xWindowFiltered))
        xWindowFiltered.remove(min(xWindowFiltered))

        del yWindowFiltered[maxIndex]
        del yWindowFiltered[minIndex]

        if len(xWindowFiltered) > 1:
            return (xWindowFiltered, yWindowFiltered)

        return None

    return None
