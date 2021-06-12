#!/usr/bin/python3
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import YB_Pcb_Car    #导入Yahboom专门库文件

car = YB_Pcb_Car.YB_Pcb_Car()

PIN = 36; #红外接收头引脚定义
buzzer = 32; #蜂鸣器引脚定义

#设置GPIO口为BIARD编码方式
GPIO.setmode(GPIO.BOARD)

#忽略警告信息
GPIO.setwarnings(False)

ir_repeat_cnt = 0



def init():
    GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)  #红外接收头的引脚需要设置成输入上拉
    GPIO.setup(buzzer,GPIO.OUT)         #蜂鸣器的引脚需要设置成输出模式
    
    print("IR control start...")

#小车鸣笛
def whistle():
    p = GPIO.PWM(buzzer, 440)
    p.start(50)
    time.sleep(0.5)
    p.stop() 

def exec_cmd(key_val):
    if key_val==0x45:  #红外遥控器上面的电源按键
        car.Ctrl_Servo(1, 90)
        car.Ctrl_Servo(2, 90)
        car.Car_Stop()
    elif key_val==0x40:   #+按键
        car.Car_Run(100, 100)   #小车前进
    elif key_val==0x15:   #暂停按键
        car.Car_Stop()
    elif key_val==0x07:   #左按键
        car.Car_Left(100, 100)
    elif key_val==0x47:   #MENU按键
        whistle()         #蜂鸣器鸣笛
    elif key_val==0x09:   #右按键
        car.Car_Right(100, 100)
    elif key_val==0x16:   #0按键
        car.Car_Spin_Left(100, 100)
    elif key_val==0x19:   #-按键
        car.Car_Back(100, 100)  
    elif key_val==0x0d:   #C按键
        car.Car_Spin_Right(100, 100)
    elif key_val==0x0c:   #数字1按键
        car.Ctrl_Servo(1, 0)
    elif key_val==0x18:   #数字2按键
        car.Ctrl_Servo(1, 90)
    elif key_val==0x5e:   #数字3按键
        car.Ctrl_Servo(1, 180)
    elif key_val==0x08:   #数字4按键
        car.Ctrl_Servo(2, 0)
    elif key_val==0x1c:   #数字5按键
        car.Ctrl_Servo(2, 90)
    elif key_val==0x5a:   #数字6按键
        car.Ctrl_Servo(2, 180)
    else:
        print(key_val)
        print("no cmd")
        
try:
    init()
    while True:
        if GPIO.input(PIN) == 0:
            ir_repeat_cnt = 0;
            count = 0
            while GPIO.input(PIN) == 0 and count < 200:
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(PIN) == 1 and count < 80:
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
                count = 0
                while GPIO.input(PIN) == 0 and count < 15:
                    count += 1
                    time.sleep(0.00006)

                count = 0
                while GPIO.input(PIN) == 1 and count < 40:
                    count += 1
                    time.sleep(0.00006)

                if count > 9:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:
                print("Get the key: 0x%02x" %data[2])
                exec_cmd(data[2])
        else:
            if ir_repeat_cnt > 110: #判断红外遥控器按键是否被松开，因为重复周期的时间是110ms,所以这里要设置成110*0.001.
                ir_repeat_cnt = 0
                car.Car_Stop()
            else:
                time.sleep(0.001)
                ir_repeat_cnt += 1
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()



