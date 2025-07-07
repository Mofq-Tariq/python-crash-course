def make_car(manufacture,model_name,**car) :
    car["manufacture"]=manufacture
    car["model_name"]=model_name
    return car
car=make_car("Jordan","Toyota",color="blue",doors=4)
for info in car.keys() :
    print(info, car[info])
