#Wolf Encryption Method - Encrypt anything using a password
#Program written by Zach Hofmeister
#READ THE README BEFORE USING ANY OF MY CODE!!!


#TO DO: encrypt user original password as well and add it to the end of the encrypted data, then when decrypting remove it, decrypt the password, and make sure that the password used to decrypt matches. Otherwise, cancel decryption.


#Variables go below.

mode = 0	#Mode is weather the program encrypts (True) or decrypts (False), 0 is null.

passMode = 0	#PassMode is weather the program uses password procedures (True) or does not (False), 0 is null.

userDataOriginal = ""	#The original data that the user enters to either be encrypted or decrypted.

userPasswordOriginal = ""	#The original password that the user enters, will be converted to a number later.

userDataConverted = ""

userPasswordConverted = ""

possibleChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
'X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ',',','.','?','!','/','\\','[',']','{','}',
'|','<','>',';',':','+','=','-','_','(',')','@','#','$','%','^','&','*','~','`']  #0-92 The characters that the message/password can contain, only letters and numbers.

defaultWolfEncryption = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
'X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ',',','.','?','!','/','\\','[',']','{','}',
'|','<','>',';',':','+','=','-','_','(',')','@','#','$','%','^','&','*','~','`']  #0-92 The default order of encryption characters

changedWolfEncryption = []  #0-92 The cyphered order of encryption characters

possibleCharsToDigit = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',
'24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48',
'49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73',
'74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92'] #0-92 The same number of characters as in possible chars, but converted to digits. Used to change all chars to digits.



#Functions go below.

def selectMode(): #The starting function that defines the modes to use
	global mode
	global passMode
	global userPasswordOriginal
	global userDataOriginal

	userDataOriginal = raw_input("Enter the data that you want to encrypt/decrypt. All letters/numbers/special characters are supported (No alt-characters though). > ")

	passMode = raw_input("Password protect(ed)? (Y/N) > ").upper()
	if passMode == "Y":
		passMode = True
		userPasswordOriginal = raw_input("Enter the password that you want to use to encrypt/decrypt the data. All letters/numbers/special characters are supported (No alt-characters though). > ")
	elif passMode == "N":
		passMode = False
	else:
		print "Incorrect input. Please try again."
		selectMode()

	mode = raw_input("Encrypt or decrypt? (E/D) > ").upper()
	if mode == "E":
		mode = True
		encrypt()
	elif mode == "D":
		mode = False
		decrypt()
	else:
		print "Incorrect input. Please try again."
		selectMode()

def encrypt():
	if passMode == True:
		global userPasswordConverted
		global changedWolfEncryption
		convertToDigit(userPasswordOriginal)
		shuffleDefault(int(userPasswordConverted) % 92)
		convertData()
		print "Encrypted data: (" + str(userDataConverted) +")"

	else:
		changedWolfEncryption = defaultWolfEncryption
		convertData()
		print "Encrypted data: (" + str(userDataConverted) + ")"

def decrypt():
	if passMode == True:
		global userPasswordConverted
		global changedWolfEncryption
		convertToDigit(userPasswordOriginal)
		shuffleDefault(int(userPasswordConverted) % 92)
		convertData()
		print "Decrypted data: (" + str(userDataConverted) + ")"
	else:
		changedWolfEncryption = defaultWolfEncryption
		convertData()
		print "Decrypted data: (" + str(userDataConverted) + ")"

def convertToDigit(inputToConvert):
	global stringLen
	replaceChars = []
	stringLen = len(inputToConvert) #puts the length of the password in a variable
	i = 0 #i is the selected character in the password
	j = 0 #j is the selected possible char, i.e. '0' is 'A' in possibleChars or '1' in possibleCharsToDigit
	while i < stringLen:
		if inputToConvert[i] == possibleChars[j]:
			replaceChars.append(possibleCharsToDigit[j])
			i += 1
			j = 0
		else:
			if j < 92:
				j += 1
			else:
				print "Incorrect character present in password."
	global userPasswordConverted
	userPasswordConverted = ''.join(replaceChars)

def shuffleDefault(intFactor):
	global defaultWolfEncryption
	global changedWolfEncryption
	i = 0
	j = intFactor
	while i <= 92:
		if j <= 92:
			changedWolfEncryption.append(defaultWolfEncryption[j])
			j += 1
			i += 1
		else:
			j = 0

def convertData():
	global userDataOriginal
	global userPasswordOriginal
	global userDataConverted
	global changedWolfEncryption
	global possibleChars
	global mode
	global passMode

	dataLen = len(userDataOriginal)
	replaceChars = []
	i = 0
	j = 0

	if mode == True: #If encrypting
		while i < dataLen:
			if userDataOriginal[i] == possibleChars[j]:
				replaceChars.append(changedWolfEncryption[j])
				i += 1
				j = 0
			else:
				if j < 92:
					j += 1
				else:
					print "Incorrect character present in data to convert."
		userDataConverted = ''.join(replaceChars)
		if passMode == True:
			userDataConverted += str(userPasswordConverted)
	else: #If decrypting
		while i < dataLen:
			if userDataOriginal[i] == changedWolfEncryption[j]:
				replaceChars.append(possibleChars[j])
				i += 1
				j = 0
			else:
				if j < 92:
					j += 1
				else:
					print "Incorrect character present in data to convert."
		userDataConverted = ''.join(replaceChars)
		if passMode == True:
			if userPasswordConverted == userDataOriginal[len(userDataOriginal) - len(userPasswordConverted):]:
				print "Password match. Decryping..."
				userDataConverted = userDataConverted[:len(userDataOriginal) - len(userPasswordConverted)]
			else:
				userDataConverted = "Incorrect password. Could not decrypt."



#Starting command goes below.

selectMode()
