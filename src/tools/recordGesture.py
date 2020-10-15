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

import time

# Records the detected gesture, zoom factor, and
# time in the form of an empty file with a coded name
def recordGesture(gesture, zoomFactor):
    fileName = "info/" + str(int(time.time()))
    fileName += "_" + gesture[0] + "_" + str(zoomFactor)
    open(fileName, "w").close()
