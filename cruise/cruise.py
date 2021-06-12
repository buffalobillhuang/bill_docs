#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import YB_Pcb_Car    #导入Yahboom专门库文件

car = YB_Pcb_Car.YB_Pcb_Car()

Tracking_Right1 = 11   #X1A  右边第一个传感器
Tracking_Right2 = 7  #X2A  右边第二个传感器
Tracking_Left1 = 13   #X1B 左边第一个传感器
Tracking_Left2 = 15   #X2B 左边第二个传感器

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(Tracking_Left1,GPIO.IN)
GPIO.setup(Tracking_Left2,GPIO.IN)
GPIO.setup(Tracking_Right1,GPIO.IN)
GPIO.setup(Tracking_Right2,GPIO.IN)


def tracking_function():
    Tracking_Left1Value = GPIO.input(Tracking_Left1);
    Tracking_Left2Value = GPIO.input(Tracking_Left2);
    Tracking_Right1Value = GPIO.input(Tracking_Right1);
    Tracking_Right2Value = GPIO.input(Tracking_Right2);
    
        #四路循迹引脚电平状态
        # 0 0 X 0
        # 1 0 X 0
        # 0 1 X 0
        #以上6种电平状态时小车原地右转
        #处理右锐角和右直角的转动
    if (Tracking_Left1Value == False or Tracking_Left2Value == False) and  Tracking_Right2Value == False:
        car.Car_Spin_Right(70, 30)
        time.sleep(0.2)
 
        #四路循迹引脚电平状态
        # 0 X 0 0       
        # 0 X 0 1 
        # 0 X 1 0       
        #处理左锐角和左直角的转动
    elif Tracking_Left1Value == False and (Tracking_Right1Value == False or  Tracking_Right2Value == False):
        car.Car_Spin_Left(30, 70) 
        time.sleep(0.2)
  
        # 0 X X X
        #最左边检测到
    elif Tracking_Left1Value == False:
        car.Car_Spin_Left(70, 70) 
        time.sleep(0.05)
        # X X X 0
        #最右边检测到
    elif Tracking_Right2Value == False:
        car.Car_Spin_Right(70, 70)
        time.sleep(0.05)
        #四路循迹引脚电平状态
        # X 0 1 X
        #处理左小弯
    elif Tracking_Left2Value == False and Tracking_Right1Value == True:
        car.Car_Spin_Left(60, 60) 
        time.sleep(0.02)
        #四路循迹引脚电平状态
        # X 1 0 X  
        #处理右小弯
    elif Tracking_Left2Value == True and Tracking_Right1Value == False:
        car.Car_Spin_Right(60, 60)
        time.sleep(0.02)
   
        #四路循迹引脚电平状态
        # X 0 0 X
        #处理直线
    elif Tracking_Left2Value == False and Tracking_Right1Value == False:
	    car.Car_Run(70, 70) 
   
        #当为1 1 1 1时小车保持上一个小车运行状态


try:
    while True:
        #car.Car_Run(70) 
        tracking_function()
except KeyboardInterrupt:
    pass
car.Car_Stop() 
del car
print("Ending")
GPIO.cleanup()