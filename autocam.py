import time
import RPi.GPIO as GPIO
import cv2


thresholdDist = 30

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

  for i in range(4):
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
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

  GPIO.cleanup()  
  return sum(dist)/len(dist)

def takePhoto(filename):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(filename+".jpeg", frame)
    cap.release()
    cv2.destroyAllWindows()


detect = False
latestDist = [100, 100, 100, 100, 100]

while True:
  del(latestDist[0])
  latestDist.append(distance())
  print(latestDist)
  
  nearNum = sum(latestDist < thresholdDist for i in latestDist)
 
  if not detect and nearNum <= 1:
    detect = True
    #takePhoto("clothes")
    print("takephone")
    continue

  if detect and nearNum == 5:
    detect = False

