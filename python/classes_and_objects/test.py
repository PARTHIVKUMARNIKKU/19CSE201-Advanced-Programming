class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class car(Vehicle):
    def __init__(self,make, model, year, name ):
        Vehicle.__init__(self,make,model,year):
        self.year=year