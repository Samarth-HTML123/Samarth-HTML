class vehicle:
    
    def __init__(self, max_speed, milage):
        
        self.max_speed = max_speed
        self.milage = milage
        
        
model1x = vehicle(240, 10)
model2x = vehicle(300, 15)

print("Model Max speed:", model1x.max_speed)
print("Model Milage:", model1x.milage)

print("Model Max speed:", model2x.max_speed)
print("Model Milage:", model2x.milage)
