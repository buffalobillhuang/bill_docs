import YB_Pcb_Car  #导入亚博智能专用的底层库文件
import time

car = YB_Pcb_Car.YB_Pcb_Car()


car.Car_Run(50, 50)
time.sleep(0.5)
car.Car_Stop()

car.Car_Back(50, 50)
time.sleep(0.5)
car.Car_Stop()

car.Car_Left(0, 50)
time.sleep(0.5)
car.Car_Stop()


car.Car_Right(50, 0)
time.sleep(0.5)
car.Car_Stop()


car.Car_Spin_Left(50, 50)
time.sleep(0.5)
car.Car_Stop()


car.Car_Spin_Right(50, 50)
time.sleep(0.5)
car.Car_Stop()

car.Car_Stop()

del car

