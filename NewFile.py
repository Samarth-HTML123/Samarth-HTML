Temperature = int(input("Enter todays teperarurein celsius:"))

if Temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today")
    print("Wear a", outfit)
     
is_raining = input("is it raining today? (yes/no): ")
     
if is_raining == "yes":
    print("Bring an umbrella")
         
wind_speed = int(input("Enter the wind speed in km/h"))
         
if wind_speed > 30:
    need_windbreaker = "yes"
    print("it is windy today")
    print("wear a windbraker needed over youre", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today")
    print("No windbreaker needed over you", outfit)
             
has_puddles = input("Are there puddles on the ground (yes/no): ")
             
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")    
print("")
print("Weather check complete!")
    
    
print("===== Weather outfit picker =====")
print("Temperature:", Temperature)
print("Outfit chosen:", outfit)
print("")
    
         