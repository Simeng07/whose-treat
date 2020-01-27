#!/usr/bin/env python
#-*- encoding:UTF-8 -*-
"""
Background: 
JJ and MM want to have a fine dinner, celebrating their annual bonuses. They make this rule: 
This dinner is on the person who gets more annual bonus. And the cost of the dinner is the diff of money they make mod 300, per capita.

Requirement:
Decide the money amount and the money provider, without letting one know how much the other's annual bonus is.

Method:
Hide the input.
Use the method "Best two out of three" in case of any typo, since the input strings are hidden.
"""
import getpass

def cal():
	"""
	Decide the money amount and the money provider.
	"""
	incomejj = validInput("JJ: ")
	incomemm = validInput("MM: ")
	diff = incomejj - incomemm
	onWhom = "JJ"
	if diff < 0:
		onWhom = "MM"
	result = int(round(abs(diff) % 300))
	return result, onWhom

def validInput(prompt):
	"""
	Get a valid input and convert it to a float number.
	"""
	while 1:
		inputStr = getpass.getpass(prompt)
		try:
			inputFloat = float(inputStr)
			return inputFloat
		except ValueError:
			print("Invalid input. Try again.")
			pass

if __name__ == "__main__":
	"""
	Use the method "Best two out of three" in case of any typo, since the input strings are hidden.
	"""
	(result1, onWhom1) = cal()
	print("Let's double check.")
	(result2, onWhom2) = cal()
	if result1 == result2 and onWhom1 == onWhom2:
		if result1 == 0:
			print("No dinner at all. But go to buy some lottery~")
		else :
			print("OK. Let's have dinner. " + str(result1) + " yuan per person on " + onWhom1 + ".")
	else :
		print("Something's wrong. Let's triple check.")
		(result3, onWhom3) = cal()
		if (result1 == result3 and onWhom1 == onWhom3) or (result2 == result3 and onWhom2 == onWhom3):
			if result3 == 0:
				print("No dinner at all. But go to buy some lottery~")
			else :
				print("OK. " + str(result3) + " it is. It's on " + onWhom3 + ".")
		else:
			print("Are you kidding me? I quit!")
