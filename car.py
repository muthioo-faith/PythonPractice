class Vihicle:
    color="White"
    def __init__(self,name,max_speed,mileage,capacity) :
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
        


        
    def greet(self):
        return f"Congratulation  Faith Mutua for buying thise car {self.name} and its color is {self.color} and its max_speed is{self.max_speed} and it mileage is {self.mileage}"    


    def capacity(self):
        return f"its name is {self.name} and its capacity is {self.capacity}"
