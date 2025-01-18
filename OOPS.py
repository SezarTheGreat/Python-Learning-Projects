#object = A bundle of related attributes (variables) and methods(functions). Ex- Phone, Cup,Book.
#         You need a class to create many objects.
# Classes are (blueprint) to design the structures and layout of an object.

#Class Variable = Shared among all instances of a class.All the instances share one variable.
#                 Defined outside the constructor. Allows you to share data among all objects created from    that class

class Car:                                                              #Class
    wheels =4                                                           #Class Variable
    num_cars = 0
    def __init__(self,model,year,colour,for_sale):                      #Constructor
        self.model = model                                              
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
        Car.num_cars += 1 
    
    def drive(self):                                                    #class methods
        print(f"You drive the car {self.colour} {self.model}")
    
    def stop(self):
        print(f"You stop the car {self.colour} {self.model}")
    
    def describe(self):
        print(f"{self.year} {self.model} {self.colour} {self.for_sale}")

car1 = Car("Porsche 911","2024","Red",False)#Instantiate object car
car2 = Car("Mustang","2024","Black",True) 
print(Car.wheels)
print(Car.num_cars)                              
car1.drive()                                #calling ths class method
car1.stop()                                 #dot is the attribute access operator
car2.drive()
car2.stop()
print(car1.wheels)
