import random
temperature = random.randint(20,35)
light = random.randint(10,100)
noise = random.randint(30,90)
sitting = random.randint(10,120)
print("SMART DESK GUARDIAN")
print("-------------------")
print("Temperature:",temperature,"C")
print("Light:",light,"%")
print("Noise:",noise,"dB")
print("Sitting:",sitting,"minutes")
if temperature > 30:
	print("WARNING:Temperature is high")
else:
	print("Temperature: NORMAL")
if light < 30:
	print("WARNING : Low light")
else:
	print("Light:NORMAL")
if noise > 70:
	print("WARNING : High noise")
else:
	print("Noise: NORMAL")
if sitting > 60:
	print("WARNING: Take a break")
else:
	print("Sitting time:NORMAL")
score = 100
if temperature > 30:
	score = score-25

if light < 30:
	score = score-25

if noise > 70:
	score = score - 25

if sitting > 60:
	score = score - 25
print ("Desk Safety Score:",score,"/100")
 
if score == 100:
	print("STATUS: EXCELLENT")
elif score >= 75:
	print("STATUS : ACCEPTABLE")
else:
	print("STATUS: POOR - ACTION NEEDED")

