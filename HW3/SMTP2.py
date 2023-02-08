#Lucy Amaranto
#On my honor, I have not given nor received unauthorized aid on this assignment

import os
import sys
currentIndex = 0
state = 0
fileInput = ""

def inBounds():
	global input
	global currentIndex
	return len(input) > currentIndex
def resetLoop():
	global currentIndex
	currentIndex = 0
	return True
def whitespaceParser():
	global currentIndex
	global input
	global result
	if inBounds() and (input[currentIndex] == "\t" or input[currentIndex] == " "):
		currentIndex+=1
		whitespaceParser()
		return True
	else:
		return False
def responseCodeParser(currentCmd):
	global currentIndex
	global input
	currentIndex = 0
	if len(currentCmd) > currentIndex and inBounds() and (currentCmd[currentIndex] == input[currentIndex]):
		currentIndex += 1
		if len(currentCmd) > currentIndex and inBounds() and (currentCmd[currentIndex] == input[currentIndex]):
			currentIndex += 1
			if len(currentCmd) > currentIndex and inBounds() and (currentCmd[currentIndex] == input[currentIndex]):
				currentIndex += 1
				if not whitespaceParser():
					return False
				while inBounds() and input[currentIndex] != "\n":
					currentIndex += 1
				if inBounds() and input[currentIndex] == "\n":
					return True
		else:
			return False
	else:
		return False

moreThanOne = False
if len(sys.argv) <= 1 or not os.path.isfile(str(sys.argv[1])):
	exit()
file = open(str(sys.argv[1]), "r")

for fileInput in file.readlines():
	if fileInput[0:5] == "From:":
		if state == 2:
			#end of email, need to place .
			sys.stdout.write(".\n")
			moreThanOne = True
			input = sys.stdin.readline()
			sys.stderr.write(input)
			if not responseCodeParser("250"):
				sys.stdout.write("QUIT\n")
				exit()
			resetLoop()
			state = 0
		elif state == 1:
			sys.stdout.write("DATA\n")
			input = sys.stdin.readline()
			sys.stderr.write(input)
			if not responseCodeParser("354"):
				sys.stdout.write("QUIT\n")
				exit()
			resetLoop()
		sys.stdout.write("MAIL FROM:" + fileInput[5:])
		input = sys.stdin.readline()
		sys.stderr.write(input)
		if not responseCodeParser("250"):
			sys.stdout.write("QUIT\n")
			exit()
		resetLoop()
	elif fileInput[0:3] == "To:":
		sys.stdout.write("RCPT TO:" + fileInput[3:])
		input = sys.stdin.readline()
		sys.stderr.write(input)
		if not responseCodeParser("250"):
			sys.stdout.write("QUIT\n")
			exit()
		state = 1
		resetLoop()
	#text body has begun
	elif state == 1:
		sys.stdout.write("DATA\n")
		input = sys.stdin.readline()
		sys.stderr.write(input)
		if not responseCodeParser("354"):
			sys.stdout.write("QUIT\n")
			exit()
		state = 2
		sys.stdout.write(fileInput)
		resetLoop()
	elif state == 2:
		sys.stdout.write(fileInput)
if state == 1:
	sys.stdout.write("DATA\n")
	input = sys.stdin.readline()
	sys.stderr.write(input)
	resetLoop()
	if not responseCodeParser("354"):
		sys.stdout.write("QUIT\n")
		exit()
	sys.stdout.write(".\n")
if state == 2:
	if moreThanOne:
		sys.stdout.write("\n")
	sys.stdout.write(".\n")

input = sys.stdin.readline()
sys.stderr.write(input)
resetLoop()
sys.stdout.write("QUIT\n")
exit()