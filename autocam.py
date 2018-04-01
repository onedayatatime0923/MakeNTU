import time
import RPi.GPIO as GPIO
import os


thresholdDist = 25
detect = False

def distance():
  dist = []

  # Use BCM GPIO references
  # instead of physical pin numbers
  GPIO.setmode(GPIO.BCM)

  # Define GPIO to use on Pi
  GPIO_TRIGGER = 23
  GPIO_ECHO = 24

  # Set pins as output and input
  GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
  GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

  # Allow module to settle
  time.sleep(0.2)

  for i in range(3):
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
      start = time.time()
  
    while GPIO.input(GPIO_ECHO)==1:
      stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000/2
    dist.append(distance)

    time.sleep(0.1)

  print(dist)

  GPIO.cleanup()  
  return sum(dist)/len(dist)

def takePhoto(filename):
  action = "fswebcam -p YUYV data/test/" + filename + ".jpg"
  os.system(action)


def checkClothes():
  latestDist = []
  for i in range(5):
    latestDist.append(distance())

  print(latestDist)
  nearNum = sum(i < thresholdDist for i in latestDist)
  return nearNum >= 4
