from CAR import Car

car_1 = Car("KA20MC0303",5)
car_2 = Car("KA20MC0302",4)
car_3 = Car("KA20MC0301",3)
car_4 = Car("KA02mb0908",4)
car_5 = Car("KA20CC0099",2)

car_1.start()
car_2.start()
car_3.start()
car_1.change_gear()
car_2.change_gear()
car_1.change_gear()
car_2.change_gear()
car_1.change_gear()



lst = [car_1,car_2,car_3,car_4,car_5]

for CAR in lst:
    CAR.showInfo()
c=len(list(filter(lambda x:x.is_started and x.c_gear ==0,lst)))
print(c)