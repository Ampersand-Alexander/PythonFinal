from train import *

t1 = Metro(axel_load = 9000, motor_type = "Electric", color = "Red")

t2 = Amtrak(axel_load = 10000, motor_type = "Diesel", color = "Black")

t3 = Box(axel_load = 200000, motor_type = "Diesel", color = "Gray")
t3.max_cars = 100

t4 = Container(axel_load = 160000, motor_type = "Diesel", color = "White")
t4.max_cars = 75

mylist = [t1, t2, t3, t4]

for x in mylist:
    print("-------------------------------------------------------")
    print("train_classification:", x.train_classification)
    print("train_type          :", x.train_type)
    print("track_gauge         :", x.track_gauge)
    print("motor_type          :", x.motor_type)
    print("color               :", x.color)
    print("chassis_length      :", x.chassis_length)
    print("axel_load           :", x.axel_load)
    print("max_cars            :", x.max_cars)
