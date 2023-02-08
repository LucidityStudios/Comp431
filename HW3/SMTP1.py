#Lucy Amaranto
#On my honor, I have not given nor received unauthorized aid on this assignment

import os
import sys
print(sys.argv)
currentIndex = 0
result = "250 OK"
state = 0
RCPTList = []
EmailTextList = []
inData = False

def inBounds():
	global input
	global currentIndex
	return len(input) > currentIndex
def resetLoop():
	global currentIndex
	global result
	currentIndex = 0
	result = "250 OK"
	return True
def fullReset():
	global currentIndex
	global result
	global RCPTList
	global EmailTextList
	global inData
	inData = False
	currentIndex = 0
	result = "250 OK"
	RCPTList = []
	EmailTextList = []

def mailFromCmdParser():
	global currentIndex
	global input
	global result

	if inBounds() and input[currentIndex] == "M":
		currentIndex+=1
		if inBounds() and input[currentIndex] == "A":
			currentIndex+=1
			if inBounds() and input[currentIndex] == "I":
				currentIndex+=1
				if inBounds() and input[currentIndex] == "L":
					currentIndex+=1
					if not whitespaceParser():
						result = "ERROR -- whitespace"
						return False
					if inBounds() and input[currentIndex] == "F":
						currentIndex+=1
						if inBounds() and input[currentIndex] == "R":
							currentIndex+=1
							if inBounds() and input[currentIndex] == "O":
								currentIndex+=1
								if inBounds() and input[currentIndex] == "M":
									currentIndex+=1
									if inBounds() and input[currentIndex] == ":":
										currentIndex+=1
										nullspaceParser()
										if not reversePathParser():
											return False
										nullspaceParser()
										if not CRLFParser() and result == "250 OK":
											result = "ERROR -- CRLF"
											return False
										return True
									else:
										return False
								else:
									return False
							else:
								return False
						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
def MAILFROMParser():
	global currentIndex
	global input
	global result

	if inBounds() and input[currentIndex] == "M":
		currentIndex+=1
		if inBounds() and input[currentIndex] == "A":
			currentIndex+=1
			if inBounds() and input[currentIndex] == "I":
				currentIndex+=1
				if inBounds() and input[currentIndex] == "L":
					currentIndex+=1
					if not whitespaceParser():
						result = "ERROR -- whitespace"
						return False
					if inBounds() and input[currentIndex] == "F":
						currentIndex+=1
						if inBounds() and input[currentIndex] == "R":
							currentIndex+=1
							if inBounds() and input[currentIndex] == "O":
								currentIndex+=1
								if inBounds() and input[currentIndex] == "M":
									currentIndex+=1
									if inBounds() and input[currentIndex] == ":":
										return True
									else:
										return False
								else:
									return False
							else:
								return False
						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
def rcptToCmdParser():
	global currentIndex
	global input
	global result

	if inBounds() and input[currentIndex] == "R":
		currentIndex+=1
		if inBounds() and input[currentIndex] == "C":
			currentIndex+=1
			if inBounds() and input[currentIndex] == "P":
				currentIndex+=1
				if inBounds() and input[currentIndex] == "T":
					currentIndex+=1
					if not whitespaceParser():
						result = "ERROR -- whitespace"
						return False
					if inBounds() and input[currentIndex] == "T":
						currentIndex+=1
						if inBounds() and input[currentIndex] == "O":
							currentIndex+=1
							if inBounds() and input[currentIndex] == ":":
								currentIndex+=1
								nullspaceParser()
								if not forwardPathParser():
									return False
								nullspaceParser()
								if not CRLFParser() and result == "250 OK":
									result = "ERROR -- CRLF"
									return False
								return True
							else:
								return False
						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
def RCPTTOParser():
	global currentIndex
	global input
	global result

	if inBounds() and input[currentIndex] == "R":
		currentIndex+=1
		if inBounds() and input[currentIndex] == "C":
			currentIndex+=1
			if inBounds() and input[currentIndex] == "P":
				currentIndex+=1
				if inBounds() and input[currentIndex] == "T":
					currentIndex+=1
					if not whitespaceParser():
						result = "ERROR -- whitespace"
						return False
					if inBounds() and input[currentIndex] == "T":
						currentIndex+=1
						if inBounds() and input[currentIndex] == "O":
							currentIndex+=1
							if inBounds() and input[currentIndex] == ":":
								return True
							else:
								return False
						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
def dataCmdParser():
	global currentIndex
	global input
	global result

	if inBounds() and input[currentIndex] == "D":
		currentIndex+=1
		if inBounds() and input[currentIndex] == "A":
			currentIndex+=1
			if inBounds() and input[currentIndex] == "T":
				currentIndex+=1
				if inBounds() and input[currentIndex] == "A":
					currentIndex+=1
					nullspaceParser()
					if not CRLFParser() and result == "250 OK":
						result = "ERROR -- CRLF"
						return False
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
def DATAParser():
	global currentIndex
	global input
	global result

	if inBounds() and input[currentIndex] == "D":
		currentIndex+=1
		if inBounds() and input[currentIndex] == "A":
			currentIndex+=1
			if inBounds() and input[currentIndex] == "T":
				currentIndex+=1
				if inBounds() and input[currentIndex] == "A":
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
def endEmailTextParser():
	global currentIndex
	global input
	global result
	
	if inBounds() and input[currentIndex] == ".":
		currentIndex += 1
		if inBounds() and CRLFParser():
			return True
		currentIndex -= 1
		return False
	else:
		return False
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
def nullspaceParser():
	whitespaceParser()
	return True
def reversePathParser():
	global currentIndex
	global input
	global result

	if not pathParser() and result == "250 OK":
		result = "ERROR -- path"
		return False
	else: return True
def forwardPathParser():
	global currentIndex
	global input
	global result

	if not pathParser() and result == "250 OK":
		result = "ERROR -- path"
		return False
	else: return True
def pathParser():
	global currentIndex
	global input
	global result
	if inBounds() and input[currentIndex] == "<":
		currentIndex+=1
		if mailboxParser():
			if inBounds() and input[currentIndex] == ">":
				currentIndex+=1
				return True
			else:
				return False
		elif result == "250 OK":
			result = "ERROR -- mailbox"
		return False
	else:
		return False
def mailboxParser():
	global currentIndex
	global input
	global result
	localPartParser()
	if inBounds() and input[currentIndex] == "@":
		currentIndex+=1
		domainParser()
		return True
	else:
		return False
def localPartParser():
	global currentIndex
	global input
	global result
	if not stringParser() and result == "250 OK":
		result = "ERROR -- string"
		return False
	return True
def stringParser():
	global currentIndex
	global input
	global result
	if inBounds():
		if charParser():
			stringParser()
			return True
		else:
			return False
	else:
		return False
def charParser():
	global currentIndex
	global input
	global result
	if inBounds():
		x = input[currentIndex]
		if x == "<" or x == ">" or x == "(" or x == ")" or x == "[" or x == "]" or x == "\\" or x == "." or x == "," or x == ";" or x == ":" or x == "@" or x == "\"" or x == " " or x == "\t":
			return False
		else:
			currentIndex+=1
			return True
	else:
		return False
def domainParser():
	global currentIndex
	global input
	global result
	if inBounds() and elementParser():
		if inBounds() and input[currentIndex] == ".":
			currentIndex+=1
			domainParser()
		return True
	else:
		if result == "250 OK":
			result = "ERROR -- element"
		return False
def elementParser():
	global currentIndex
	if inBounds():
		if letterParser():
			currentIndex-=1
			if nameParser():
				return True
			else:
				letterParser()
			return True
		else:
			return False
	else:
		return False
def nameParser():
	global currentIndex
	global input
	global result

	currentIndex+=1
	#checks if there are at least 2 characters remaining
	if inBounds():
		currentIndex-=1
		if letterParser():
			if letDigStrParser():
				return True
			else:
				return False
		else:
			return False
	else:
		currentIndex-=1
		return False
def letterParser():
	global currentIndex
	global input
	global result
	if inBounds():
		x = input[currentIndex]
		if x == "a" or x == "b" or x == "c" or x == "d" or x == "e" or x == "f" or x == "g" or x == "h" or x == "i" or x == "j" or x == "k" or x == "l" or x == "m" or x == "n" or x == "o" or x == "p" or x == "q" or x == "r" or x == "s" or x == "t" or x == "u" or x == "v" or x == "w" or x == "x" or x == "y" or x == "z" or x == "A" or x == "B" or x == "C" or x == "D" or x == "E" or x == "F" or x == "G" or x == "H" or x == "I" or x == "J" or x == "K" or x == "L" or x == "M" or x == "N" or x == "O" or x == "P" or x == "Q" or x == "R" or x == "S" or x == "T" or x == "U" or x == "V" or x == "W" or x == "X" or x == "Y" or x == "Z":
			currentIndex+=1
			return True
		else:
			return False
	else:
		return False
def letDigStrParser():
	global currentIndex
	global input
	global result
	if inBounds() and letDigParser():
		letDigStrParser()
		return True
	else:
		return False
def letDigParser():
	global currentIndex
	global input
	global result
	if inBounds():
		if letterParser():
			return True
		elif digitParser():
			return True
		else:
			return False
	else:
		return False
def digitParser():
	global currentIndex
	global input
	global result
	if inBounds():
		x = input[currentIndex]
		if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
			currentIndex+=1
			return True
		else:
			return False
	else:
		return False
def CRLFParser():
	global currentIndex
	global input
	global result
	if inBounds() and input[currentIndex] == "\n":
		currentIndex+=1
		return True
	else:
		return False
def spliceString(string: input):
	startIndex = 0
	endIndex = 0
	for x in range(len(input)):
		if input[x] == "<":
			startIndex = x+1
		elif input[x] == ">":
			endIndex = x
			break
	return input[startIndex:endIndex]
def error500():
	if not MAILFROMParser():
		resetLoop()
		if not RCPTTOParser():
			resetLoop()
			if not DATAParser():
				sys.stdout.write("500 Syntax error: command unrecognized\n")
				resetLoop()
				return True
	resetLoop()
	return False
def error503(currentCmd):
	if currentCmd == "mailFromCmd":
		if not RCPTTOParser():
			resetLoop()
			if not DATAParser():
				resetLoop()
				return False
		resetLoop()
		sys.stdout.write("503 Bad sequence of commands\n")
		return True
	elif currentCmd == "rcptToCmd":
		if not MAILFROMParser():
			resetLoop()
			if not DATAParser():
				resetLoop()
				return False
		resetLoop()
		sys.stdout.write("503 Bad sequence of commands\n")
		return True
	else:
		if not MAILFROMParser():
			resetLoop()
			if not RCPTTOParser():
				resetLoop()
				return False
		resetLoop()
		sys.stdout.write("503 Bad sequence of commands\n")
		return True
	
for input in sys.stdin:
	sys.stdout.write(input)
	if state == 0:
		if mailFromCmdParser() and result == "250 OK":
			state = 1
			sys.stdout.write(result + "\n")
			EmailTextList.append("From: <" + spliceString(input) + ">\n")
		else:
			resetLoop()
			if not error500():
				resetLoop()
				if not error503("mailFromCmd"):
					sys.stdout.write("501 Syntax error in parameters or arguments\n")
			fullReset()
			state = 0
	elif state == 1:
		if rcptToCmdParser() and result == "250 OK":
			state = 2
			sys.stdout.write(result + "\n")
			EmailTextList.append("To: <" + spliceString(input) + ">\n")
			RCPTList.append(spliceString(input))
		else:
			resetLoop()
			if not error500():
				resetLoop()
				if not error503("rcptToCmd"):
					sys.stdout.write("501 Syntax error in parameters or arguments\n")
			fullReset()
			state = 0
	elif state == 2:
		if dataCmdParser():
			sys.stdout.write("354 Start mail input; end with <CRLF>.CRLF>\n")
			inData = True
			state = 3
		elif resetLoop() and rcptToCmdParser() and result == "250 OK":
			sys.stdout.write(result + "\n")
			EmailTextList.append("To: <" + spliceString(input) + ">\n")
			RCPTList.append(spliceString(input))
		else:
			resetLoop()
			if not error500():
				resetLoop()
				if MAILFROMParser():
					sys.stdout.write("503 Bad sequence of commands\n")
				else:
					sys.stdout.write("501 Syntax error in parameters or arguments\n")
			fullReset()
			state = 0
	elif state == 3:
		if not endEmailTextParser():
			EmailTextList.append(input)
		else:
			for x in range(len(RCPTList)):
				#open up file to append to
#				print("opened " + "forward/" + RCPTList[x])
				home_dir = os.path.dirname(os.path.abspath(__file__))
				home_dir = os.path.join(home_dir, "forward/")
				file = open(home_dir + RCPTList[x], "a")
				#write to file
				for y in range(len(EmailTextList)):
#					print(EmailTextList[y])
					file.write(EmailTextList[y])
				file.close()
			fullReset()
			state = 0
			sys.stdout.write("250 OK\n")
				#close file
	resetLoop()
if inData:
	sys.stdout.write("501 Syntax error in parameters or arguments\n")
