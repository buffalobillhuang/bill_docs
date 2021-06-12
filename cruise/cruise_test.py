#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

Tracking_Left1 = 13   #X1B 左边第一个传感器
Tracking_Left2 = 15   #X2B 左边第二个传感器
Tracking_Right1 = 11   #X1A  右边第一个传感器
Tracking_Right2 = 7  #X2A  右边第二个传感器

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(Tracking_Left1,GPIO.IN)
GPIO.setup(Tracking_Left2,GPIO.IN)
GPIO.setup(Tracking_Right1,GPIO.IN)
GPIO.setup(Tracking_Right2,GPIO.IN)

print ('start')

try:
    while True:
        Tracking_Left1Value = GPIO.input(Tracking_Left1);
        Tracking_Left2Value = GPIO.input(Tracking_Left2);
        Tracking_Right1Value = GPIO.input(Tracking_Right1);
        Tracking_Right2Value = GPIO.input(Tracking_Right2);
        print (Tracking_Left1Value)
        print (Tracking_Left2Value)
        print (Tracking_Right1Value)
        print (Tracking_Right2Value)
        print ('---')
        time.sleep(1)
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()