import random
import numpy
i=1
while i>0:
 temp=random.randint(0,100)
 humid=random.randint(1,100)
 print("Temperature : ",temp)
 if temp>21 and temp<50 :
     print("Temperature is normal")
 elif temp<21:
     print("Temperature is low")
 else:
     print("Warning! Temperature is high")
 print("Humidity: ",humid)
 if humid>31 and humid<60 :
     print("Humidity is normal")
 elif humid<31:
     print("Humidity is low")
 else:
     print("Warning! Humidityis high")











     

 
