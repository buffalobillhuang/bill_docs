import RPi.GPIO as GPIO
import time

PIN = 36;   #定义红外遥控器的引脚 

#设置GPIO口为BIARD编码方式
GPIO.setmode(GPIO.BOARD)

#忽略警告信息
GPIO.setwarnings(False)
ir_repeat_cnt = 0
#红外接收头的引脚需要设置成输入上拉
GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)
print("IR test start...")  #初始化打印“IR test start".


try:
    print("start")
    while True:
        if GPIO.input(PIN) == 0:   #检测到红外遥控器发射过来的信号
            ir_repeat_cnt = 0;
            count = 0
            while GPIO.input(PIN) == 0 and count < 200:   #判断9ms高电平脉冲的引导码
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(PIN) == 1 and count < 80:   #判断4.5ms低电平脉冲的引导码
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]   #定义data用于存放红外信号的地址码、地址反码、信号码、信号反码
            for i in range(0,32):   #data[0],data[1],data[2],data[3]一共是8bit*4=32
                count = 0
                while GPIO.input(PIN) == 0 and count < 10:   #解码开始 用于过滤逻辑0和逻辑1最前面的560us的脉冲
                    count += 1
                    time.sleep(0.00006)

                count = 0
                while GPIO.input(PIN) == 1 and count < 40:   #用于判断560us高电平脉冲之后，剩下的低电平脉冲时间长度，以此来判断是逻辑0还是逻辑1
                    '''
                    说明：
                    根据红外NCE协议可知：
                    逻辑1的周期是2.25ms，脉冲时间是0.56ms. 总的周期-脉冲时间即可得到我们这里所设定的值，设定值要比实际的值略大一些。
                    同理：
                    逻辑0周期是1.12，时间是0.56ms. 总的周期-脉冲时间即可得到我们这里所设定的值，设定值要比实际的值略大一些。
                    '''
                    count += 1
                    time.sleep(0.00006)

                if count > 9:    
                    #用于判断当前接收到的信号是逻辑1还是逻辑0.如果count>9的话，证明当前低电平信号的时长大于560(9*60=540us)，也就是逻辑1.
                    #比如：当count=10时，低电平信号是10*60=600us(大于560us）为逻辑1。
                    data[idx] |= 1<<cnt   #1左移cnt位，并与data[idx]为了获取data[idx]的cnt位
                if cnt == 7:   #当cnt=7时，满一个字节，开始准备存储下一个字节。
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1  #当cnt不等于7时，继续按顺序存储当前字节。
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #data[0]与datap[1]互为反码，dta[2]datap[3互为反码，反码相加为0XFF. 这里用于判断收到的是正确的红外遥控器码值。
                print("Get the key: 0x%02x" %data[2])   #打印获取到的命令码
        else:
            if ir_repeat_cnt > 110*0.001: #判断红外遥控器按键是否被松开，因为重复周期的时间是110ms,所以这里要设置成110*0.001.
                ir_repeat_cnt = 0
            else:
                time.sleep(0.001)
                ir_repeat_cnt += 1
except KeyboardInterrupt:
    pass
print("Ending")
GPIO.cleanup()