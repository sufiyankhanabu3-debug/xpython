import math
print(20*"=", "WELCOME", 20*"=")
print(" Choose one option")
print(" ")
print(" 1). celsius to Fahrenheit")
print(" 2). Fahrenheit to Celsius")
op= input(" Enter your option: ")
print(" ")
tem=int(input(" Enter Temperature: "))
if op== "1" :
	result=(tem*9/5)+32
	print("Fahrenheit is ", result)
elif op=="2":
	result=5/9*(tem-32)
	print("Celsius is ", result)
else:
	print ("invalid")