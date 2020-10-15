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

import subprocess

# Finds and stores the screen resolution of a display
command = subprocess.Popen(["fbset", "-s"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

rawOutput, error = command.communicate()

output = rawOutput.decode("utf-8")

lines = output.split("\n")
info = lines[2].strip().split(" ")
width = int(info[1])
height = int(info[2])
