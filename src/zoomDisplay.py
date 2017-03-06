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
from transfunction import transfunction
from screenres import screenres
import time
import cv2
import sys
import os

w = screenres.width
h = screenres.height

xc = 0.3
yc = 0.8

numberOfStages = 2

stageNumber = 0

lastTime = ""

rawImg = cv2.imread("image.jpg")

img = cv2.resize(rawImg, (w, h))

roiList = [img]

def zoomOut(stageNumber):

  if stageNumber == 0:

    roi = roiList[stageNumber]

    return roi, stageNumber

  roi = roiList[stageNumber - 1]

  return roi, stageNumber

def zoomIn(img, stageNumber, factor):
  
  if len(roiList) <= stageNumber:

    height, width = img.shape[:2]

    rawRoi = img[int(round(height * factor)):int(round(height * (1 - factor))), int(round(width * factor)):int(round(width * (1 - factor)))]

    roi = cv2.resize(rawRoi, (w, h))

    roiList.append(roi)

    return roi, stageNumber

  else:

    roi = roiList[stageNumber]

    return roi, stageNumber
  
def getCommand(lastTime):

  fileList = os.listdir("info")

  if len(fileList) == 0:

    return "none", "none", "none"

  for file in fileList:

    os.remove("info/" + file)

  fileList.sort()

  file = fileList[-1]

  fileName = file.split("_")

  time = fileName[0]

  if time == lastTime:
        
      return "none", "none", time

  gesture = fileName[1]

  zoomFactor = float(fileName[2])

  if gesture == None:

    gesture = "none"

  if zoomFactor == None:

    zoomFactor = "none"

  return gesture, zoomFactor, time

def zoom(img, status, zoomFactor, currentStage, numberOfStages):

  stageFactor = zoomFactor/numberOfStages

  if status == "f":

    for i in range(currentStage + 1, currentStage + numberOfStages + 1):

      newImg, stageNumber = zoomIn(img, i, stageFactor)

      img = newImg

      loadImg = transfunction.transform(img, w, h, xc, yc)

      cv2.imshow("window", loadImg)

      cv2.waitKey(1)

    return img, stageNumber

  else:

    for i in range(currentStage - 1, currentStage - numberOfStages - 1, -1):

      newImg, stageNumber = zoomOut(i)

      loadImg = transfunction.transform(newImg, w, h, xc, yc)

      cv2.imshow("window", loadImg)

      cv2.waitKey(1)

    return newImg, stageNumber
      
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

loadImg = transfunction.transform(img, w, h, xc, yc)

cv2.imshow("window", loadImg)

cv2.waitKey(1000)

time.sleep(0.01)

"""gesture = "c"
zoomFactor = 0.4
img, stageNumber = zoom(img, gesture, zoomFactor, 0, numberOfStages)
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)

time.sleep(1)
gesture = "f"
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)

time.sleep(1)
gesture = "c"
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)

time.sleep(1)
gesture = "f"
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)
img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)

time.sleep(1)"""
while True:

  key = cv2.waitKey(1) & 0xFF

  if key == 27:

    break

  gesture, zoomFactor, lastTime = getCommand(lastTime)

  if gesture == "none" or zoomFactor == "none" or lastTime == "none":

    continue
  
  img, stageNumber = zoom(img, gesture, zoomFactor, stageNumber, numberOfStages)
