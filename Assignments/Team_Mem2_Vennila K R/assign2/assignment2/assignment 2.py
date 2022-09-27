import random

temp=random.randint(1,50)
humidity=random.randint(1,50)
print("temperature:",temp)
if temp > 10 and temp <25:
    print("temperature is normal")
elif temp <10:
    print ("temperature is low")
else:
    print("temperature is high")
    
print("Humidity:",humidity)
if humidity>35 and humidity<45:
    print ("humidity is normal")
elif humidity <35:
    print ("humidity is low")
else:
    print("humidity is high")
