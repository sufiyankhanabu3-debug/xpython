# For Information And Welcome 

print(20*"=", "✨WELCOME✨", 20*"=")
print(" 🎉Please Enter two Numbers To Generate Table Between them🎉 ")

# For Input Numbers

num1=int(input("Entet First Number: "))
num2=int(input("Entet Second Number: "))

# Functions 

for num in range(num1,num2):
	for I in range(1,11):
		print (" " ,num, "×" ,I ,"=" ,  I * num)
	print(" ")