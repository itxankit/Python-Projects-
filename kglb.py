import time

# user name
while True:
	user = input("Enter your Good name:")
	if len(user) >= 12:
		print("name cannot be longer than 12 char")
	elif not user.isalpha():
		print("name cannot contain numbers or other symbols")
	else: break 
print(" ")

#weight input
while True:
	weight = input("Enter your body weight:") #Floating point number problem
	if not weight.isdigit(): # isdigit only checks integers not even float because of the decimal point
		print("weight cannot contain letters or other symbols")
	else: 
		weight = float(weight)
		break


#choose unit 
while True:
	upperunit = input("Enter Unit of Your weight kilogram Or pounds ('K' OR 'P') ").upper()
	if not upperunit.isalpha():
		print("please enter unit only in letters")
	elif upperunit not in ('K', 'P'):
		print("please choose ('K' OR 'P')")
	else : break

#basic input and display symbols for fstring 
otherunit = ""

if upperunit == "K":
	finalunit = "Kg"
	otherunit = "lb"
else:
	finalunit = "lb"
	otherunit = "kg"
print(" ")

#display current weight
print(f"Your weight is {weight}{finalunit}")
print(" ")

#validation for conversion
while True:
	upperconvertor = input(f"Corrently your unit is {finalunit} do you want to convert your weight into {otherunit}? (Y/N):").upper()
	if not upperconvertor.isalpha():
		print("please enter only in letters")
	elif upperconvertor not in ('Y', 'N'):
		print(f"{user} You entered wrong input... pls choose (Y OR N)")
	else:
		break
print(" ")

while True:
	if upperconvertor == "Y":
		if upperunit == "K" :
			weight1 = weight * 2.20462 # kg to lb
			print(f"{user} Your weight in Pounds is {weight1} {otherunit}")
			print(" ")
			break
		else:
			weight1 = weight / 2.20462 # lb to kg
			print(f"{user} Your weight in Kilograms is {weight1} {otherunit}")
			print(" ")
			break
	else :
		print(f"Closing....")
		time.sleep(1)
		break

print(f"Thanks {user} for using my tool")