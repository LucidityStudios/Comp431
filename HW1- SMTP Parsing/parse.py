#Lucy Amaranto
#On my honor, I have not given nor received unauthorized aid on this assignment

import sys
#input = sys.stdin.readline()
#sys.stdout.write(input)
currentIndex = 0
result = "Sender ok"

def inBounds():
	global input
	global currentIndex
	return len(input) > currentIndex

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
						return
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
										if not CRLFParser() and result == "Sender ok":
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

	if not pathParser() and result == "Sender ok":
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
		elif result == "Sender ok":
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
	if not stringParser() and result == "Sender ok":
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
		if result == "Sender ok":
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

for input in sys.stdin:
	sys.stdout.write(input)
	if not mailFromCmdParser() and result == "Sender ok":
		result = "ERROR -- mail-from-cmd"
	sys.stdout.write(result +"\n")
	#RESET FOR NEXT LOOP
	currentIndex = 0
	result = "Sender ok"
