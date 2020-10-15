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

# Records all the collected data from gestureDetected.py
# into .csv files located in ../info
def recordData(xData, xDataFiltered, yData, yDataFiltered):
    xDataFile = open("data-x-raw.csv", "w")
    xDataFilteredFile = open("data-x-filtered.csv", "w")

    yDataFile = open("data-y-raw.csv", "w")
    yDataFilteredFile = open("data-y-filtered.csv", "w")

    # Write the raw x data file with data from xData
    xAxis = []

    for i in range(0, len(xData)):
        xAxis.append(i)

    for i in range(0, len(xData)):
        xDataFile.write(str(xAxis[i]) + ", " + str(xData[i]) + "\n")

    # Write the filtered x data file with data from xFilteredData
    xAxis = []

    for i in range(0, len(xDataFiltered)):
        xAxis.append(i)

    for i in range(0, len(xDataFiltered)):
        xDataFilteredFile.write(str(xAxis[i]) + ", " +
                                str(xDataFiltered[i]) + "\n")

    # Write the y data file with data from yData
    xAxis = []

    for i in range(0, len(yData)):
        xAxis.append(i)

    for i in range(0, len(yData)):
        yDataFile.write(str(xAxis[i]) + ", " + str(yData[i]) + "\n")

    # Write the filtered y data file from yFilteredData
    xAxis = []

    for i in range(0, len(yDataFiltered)):
        xAxis.append(i)

    for i in range(0, len(yDataFiltered)):
        yDataFilteredFile.write(str(xAxis[i]) + ", " +
                                str(yDataFiltered[i]) + "\n")
