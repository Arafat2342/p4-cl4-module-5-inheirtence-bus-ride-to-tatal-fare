# Create a Bus child class inherited from the Vehicle class to calculate the total fare.

# make a child class for the Bus that inherits form the Vehicle class. Any vehicle's default fare price is seating capacity * 100. For exxample, we must add a maintenance charge of 10% to the full fare. As a result, the final fare for a bus ride will be equal to the toral fare plus 10% of the total fare.

# The bus has a seating capacity of 50 people. as a result, the total fare should be INR 5500. in the Bus class, you must override the fare() method of the vehicle class.

# parent class
class Vehicle():

    # constructor
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    #method

    def fare(self):
        total_fare = self.seating_capacity * 100
        return total_fare

#child class
class Bus(Vehicle):

    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
    
    # overwriting parent class method
    def fare(self):
        total_fare = self.seating_capacity * 100
        maintenance_char = total_fare * (10/100)
        return round(total_fare + maintenance_char)

    
# object creation

BusObj = Bus(50)

print(BusObj.fare())