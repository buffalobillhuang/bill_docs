import YB_Pcb_Car  #导入亚博智能专用的底层库文件
import time

car = YB_Pcb_Car.YB_Pcb_Car()

car.Ctrl_Servo(1, 90) #连接在扩展板上S1接口的舵机，转动到90度
time.sleep(0.5)
    
car.Ctrl_Servo(2, 90) #连接在扩展板上S2接口的舵机，转动到90度
time.sleep(0.5)

car.Ctrl_Servo(1, 0) #连接在扩展板上S1接口的舵机，转动到180度
time.sleep(0.5)

car.Ctrl_Servo(2, 0) #连接在扩展板上S2接口的舵机，转动到0度
time.sleep(0.5)

car.Ctrl_Servo(1, 180) #连接在扩展板上S2接口的舵机，转动到180度
time.sleep(0.5)
    
car.Ctrl_Servo(2, 180)
time.sleep(0.5)

car.Ctrl_Servo(1, 90) #连接在扩展板上S1接口的舵机，转动到90度
car.Ctrl_Servo(2, 90) #连接在扩展板上S1接口的舵机，转动到90度
time.sleep(0.5)

del car

