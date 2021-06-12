
import RPi.GPIO as GPIO
import time

Buzzer = 32 #定义蜂鸣器的引脚

BL1 = 248
BL2 = 278
BL3 = 294
BL4 = 330
BL5 = 371
BL6 = 416
BL7 = 467

B1 = 495
B2 = 556
B3 = 624
B4 = 661
B5 = 742
B6 = 833
B7 = 935

BH1 = 990
BH2 = 1112
BH3 = 1178
BH4 = 1322
BH5 = 1484
BH6 = 1665
BH7 = 1869

NTC1 = 262
NTC2 = 294
NTC3 = 330
NTC4 = 350
NTC5 = 393
NTC6 = 441
NTC7 = 495

NTCL1 = 131
NTCL2 = 147
NTCL3 = 165
NTCL4 = 175
NTCL5 = 196
NTCL6 = 221
NTCL7 = 248

NTCH1 = 525
NTCH2 = 589
NTCH3 = 661
NTCH4 = 700
NTCH5 = 786
NTCH6 = 882
NTCH7 = 990

NTD0 = -1
NTD1 = 294
NTD2 = 330
NTD3 = 350
NTD4 = 393
NTD5 = 441
NTD6 = 495
NTD7 = 556

NTDL1 = 147
NTDL2 = 165
NTDL3 = 175
NTDL4 = 196
NTDL5 = 221
NTDL6 = 248
NTDL7 = 278

NTDH1 = 589
NTDH2 = 661
NTDH3 = 700
NTDH4 = 786
NTDH5 = 882
NTDH6 = 990
NTDH7 = 1112

NTE1 = 330
NTE2 = 350
NTE3 = 393
NTE4 = 441
NTE5 = 495
NTE6 = 556
NTE7 = 624

NTEL1 = 165
NTEL2 = 175
NTEL3 = 196
NTEL4 = 221
NTEL5 = 248
NTEL6 = 278
NTEL7 = 312

NTEH1 = 661
NTEH2 = 700
NTEH3 = 786
NTEH4 = 882
NTEH5 = 990
NTEH6 = 1112
NTEH7 = 1248


tune =  [
NTC3, NTC5, NTC5, NTC3, NTC6, NTC6, NTC7, NTC6, NTC6, NTC6, NTC5, NTCH1, NTCH1, NTCH1, NTCH1, NTC6,
 NTCH1, NTC6, NTC5, 

NTC3, NTC5, NTC5, NTC5, NTC3, NTC6, NTC6, NTC7, NTC6, NTC6, NTC6, NTC5, NTCH1, NTCH1, NTCH1,
 NTCH1, NTC6, NTC6, NTCH1,NTCH2, 

NTCH5, NTCH5, NTCH5, NTCH5,NTCH5, NTCH3, NTCH2, NTCH1, NTCH1, NTC6, NTCH1, NTC6, NTCH1, NTCH2,
  NTCH2, NTCH2, NTCH2,NTCH2, NTCH1, NTCH3, NTCH2, NTCH2, 

NTCH3, NTCH3, NTCH3, NTCH3, NTCH2, NTCH2, NTCH1, NTCH1, NTCH1, NTCH2, NTCH1, NTC6, NTC5, NTC5, 
 NTC5, NTC5, NTC6, NTC5,NTCH2, NTCH3,NTCH1,
]

durt = [
0.5, 0.5, 1.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2,
0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 
2,0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 0.5, 0.5, 0.5, 1, 0.25,0.5, 0.5, 0.5, 0.5, 
1, 0.25, 2, 0.5, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 
0.5, 0.5, 0.5, 2,
]


def setup():
        GPIO.setmode(GPIO.BOARD)      #设置GPIO口为BIARD编码方式         
        GPIO.setup(Buzzer, GPIO.OUT)  #蜂鸣器的引脚设置成输出模式
        global Buzz                                            
        Buzz = GPIO.PWM(Buzzer, 440)   
        Buzz.start(50) 


def loop():
	while True:
		print('\n Playing song star...')
		for i in range(1, len(tune)):		
			Buzz.ChangeFrequency(tune[i])	
			time.sleep(durt[i] * 0.5)		
			
if __name__ == '__main__':		
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:  	
        GPIO.cleanup()
        print("Ending")