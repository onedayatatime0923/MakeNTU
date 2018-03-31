
import sys
import os
with os.popen('python3 2.py') as pse:
    for line in pse:
        print(line)
