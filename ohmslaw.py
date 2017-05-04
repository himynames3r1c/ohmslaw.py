import sys

def volts(i, r):
	return i * r

def resistance(v, i):
	return v / i

def current(v, r):
	return v / r

def wattage(a, v):
	return a * v

while True:
	decision = raw_input("what do you want to find type help for commands  :")

	
	if (decision == "exit" or decision == "Exit"):
		sys.exit(0)

	if (decision == "help"):
		print("""Type "v" to find voltage""")
		print("""Type "i" to find current""")
		print("""Type "r" to find resistance""")
		print("""Type "w" to find wattage""")
		print("""Type "m" to find all possible outcomes""")

	if (decision == "v" or decision == "V"):
		current = float(raw_input("What is the current  :"))
		resistance = float(raw_input("What is the resistance  :"))
		outputvolts = volts(current,resistance)
		outputvolts = str(outputvolts)
		print("#######################")
		print (outputvolts + "volts")
		print("#######################")

	if (decision == "r" or decision == "R"):
		volts = float(raw_input("What is the voltage  :"))
		current = float(raw_input("What is the current  :"))
		outputresistance = resistance(volts, current)
		outputresistance = str(outputresistance)
		print("###########################")
		print (outputresistance + "ohms")
		print("###########################")

	if (decision == "i" or decision == "I"):
		volts = float(raw_input("What is the voltage  :"))
		resistance = float(raw_input("What is the resistance :"))
		outputcurrent = current(volts, resistance)
		outputcurrent = str(outputcurrent)
		print("#######################")
		print(outputcurrent + "amps")
		print("#######################")

	if (decision == "w" or decision == "W"):
		current = float(raw_input("What is the current  :"))
		volts = float(raw_input("Waht is the voltage  :"))
		outputwattage = wattage(current, volts)
		print("#######################")
		print(outputwattage + "watts")
		print("#######################")


	if (decision == "m" or decision == "M"):
		try:
			voltsin = float(raw_input("What is the volts if you dont have it just press enter  :"))
		except ValueError:
			voltsin = ''
		try:
			currentin = float(raw_input("What is the current if you dont have it just press enter  :"))
		except ValueError:
			currentin = ''
		try:
			resistancein = float(raw_input("What is the resistance if you dont have it just press enter :"))
		except ValueError:
			resistancein = ''
		try:
			wattagein = float(raw_input("What is the wattage  :"))
		except ValueError:
			wattagein = ''

		if (voltsin == '' and currentin == '' and resistancein == ''):
			print("Please type an amount for 2 fields")

		if (type(voltsin) == float and type(resistancein) == float and type(currentin) == str):
			currentin = current(voltsin, resistancein)
			float(currentin)
		if (type(voltsin) == float and type(currentin) == float and type(resistancein) == str):
			resistancein = resistance(voltsin, currentin)
			float(resistancein)
		if (type(currentin) == float and type(resistancein) == float and type(voltsin) == str):
			voltsin = volts(resistancein, currentin)
			float(voltsin)
		if (type(voltsin) == float and type(currentin) == float and type(wattagein) == str):
			wattagein = wattage(voltsin, currentin)
			float(wattagein)



		voltsin = str(voltsin)
		currentin = str(currentin)
		resistancein = str(resistancein)
		wattagein = str(wattagein)
		print("############################################")
		print("The voltage is " + voltsin + " volts")
		print("Current is " + currentin + " amps")
		print("The resistance is " + resistancein + " ohms")
		print("The wattage is " + wattagein + " watts")
		print("############################################")

