row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")
print("")

for r in range(row):
	print(symbol, end = " ")
print("")
for c in range(column-2):
	print(symbol + (((row + row)-4) * " ") +" " + symbol )
for r in range(row):
	print(symbol, end = " ")
print("")