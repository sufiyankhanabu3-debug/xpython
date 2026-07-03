import math

# Information 

print(20*"=", "WELCOME",20*"=")
print(" ")
print(" Which You Want To Find ?")
print("  (H)Hypotenuse")
print("  (P)perpendicular")
print("  (B)Base")
opp=input("Choose Which You Want To Find [H/P/B] ")
opp=opp.upper()

#For Hypotenuse 

if opp=="H":
	print(" ")
	per=float(input("Enter Perpendicular: "))
	bas=float(input("Enter Base: "))
	result=math.sqrt(per**2+bas**2)
	print("Hypotenuse is ",result)
	
# perpendicular	

elif opp=="P":
	print(" ")
	hyp=float(input("Enter Hypotenuse: "))
	bas=float(input("Enter Base: "))
	if hyp <= bas:
		print("Error: Hypotenuse must be greater than Base.")
	else:
		result=math.sqrt(hyp**2-bas**2)
		print("Perpendicular is ",result)	

# Base	
	
elif opp=="B":
	print(" ")
	hyp=float(input("Enter Hypotenuse: "))
	per=float(input("Enter Perpendicular: "))
	result=math.sqrt(hyp**2-per**2)
	print("Base  is ",result)
	
# For Error	
	
else:
	print("")
	print(" Please Enter H OR P OR B Not ",opp,)
	print(" because", opp, "is Invalid")