import RPi.GPIO as GPIO
import time

#设置引脚编码方式为BOARD编码方式
GPIO.setmode(GPIO.BOARD)

#忽略警告
GPIO.setwarnings(False)

LED1 = 40   #定义LED1(红色)的引脚
LED2 = 38   #定义LED2(蓝色)的引脚

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)

GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)

GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)

