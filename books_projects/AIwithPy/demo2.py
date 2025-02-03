class Car:
    def __init__(self, brand, weight, power):
        self.brand = brand
        self.weight = weight
        self.power = power
    
    def drive(self):
        print("driving straight")
        
    def right(self):
        print('turning right')
    
    def left(self):
        print('turning left')

    def brake(self):
        print('braking')
    
    def signal(self):
        print('beeeep')
        
    def __str__(self):
        return f'Brand: {self.brand:20} Weight: {self.weight:10} Power: {self.power:10}'

        
my_car = Car(brand="Nissan GT-R R35", weight="1 785", power="565 hp")
my_car2 = Car(brand="Tayota Supra MK4", weight="1 460", power="over 1 000")

# print(f'Brand: {my_car.brand:20} Weight: {my_car.weight:10} Power: {my_car.power:10}')
# print(f'Brand: {my_car2.brand:20} Weight: {my_car2.weight:10} Power: {my_car2.power:10}')
print(my_car)
print(my_car2)
my_car2.drive()   #oh it can do smth!
print("saw the danger!")
my_car2.brake()   #oh it can do smth!
my_car2.signal()   #oh it can do smth!
my_car2.right()   #oh it can do smth!
my_car2.left()   #oh it can do smth!


