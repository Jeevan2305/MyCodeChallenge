# Create a class for a simple car with methods like start and stop.
class Car:
    def __init__(self, model, color = "Black"):
        self.model = model
        self.color = color
        self.is_running = False

    def start(self):
        if self.is_running == False:
            self.is_running = True
            print(f"{self.color} {self.model} is started now")
        else:
            print(f"{self.color} {self.model} is already running")
    
    def stop(self):
        if self.is_running == True:
            self.is_running = False
            print(f"{self.color} {self.model} is stopped now")
        else:
            print(f"{self.color} {self.model} is already stopped")
    
bmw = Car("BMW", "Red")
audi = Car("Audi")

bmw.start()
bmw.start()
bmw.stop()
bmw.stop()

audi.start()
audi.start()
audi.stop()
audi.stop()
