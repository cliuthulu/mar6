from arithmetic import *

input = 0

while input != "q":
	input = raw_input(">")
	token = input.split(" ")
	num1 = int(token[1])
	num2 = int(token[2])
	
	if token[0] == "+":
		print add(num1, num2)

	elif token[0] == "-":
		print subtract(num1, num2)
	elif token[0] == "*":
		print multiply(num1, num2)
	elif token[0] == "/":
		print divide(num1, num2)
	elif token[0] == "square":
		print square(num1)
	elif token[0] == "cube":
		print cube(num1)
	elif token[0] == "pow":
		print power(num1, num2)
	elif token[0] == "mod":
		print mod(num1, num2)
	


	#when done