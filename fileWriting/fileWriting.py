def readFile():
	try:
		fileName = input("Which file you want to see:")
		file = open(f"{fileName}.py",'r')
		for detail in file:
			print(detail)
		file.close()
	except FileNotFoundError as fe:
		print("File Not Found, bro!")

def fileWrite():
	fileName = input("File name:")
	mode = input("Overwrite(w) / Adding (a):")
	file = open(f"{fileName}.py",mode)
	file.write("What you want to write:")
	file.close()
print("""-- PY WRITE --
	1. Read File
	2. Write to File
	3. """)

while True: 
	choice = input("Choose:")	
	if choice == '1':
		readFile()
	elif(choice == '2'):
		fileWrite()
	else:
		print("Program successfully finished!")
		break	
