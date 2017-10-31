import os

from intergalactic_converter import *

# Roman numerals to value
roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
# REQUIREMENTS:
# can repeat max 3 times
repeat = ['I', 'X', 'C', 'M']
# only subtract from 2 higher levels
subtract_levels = 2
# cannot subtract the following:
not_subtract = ['V', 'L', 'D']
# subtract only one small from one large
# Arabic to Roman (1903 -> MCMIII)
# ASSUMPTIONS:
# metals are unique by name
# last price in list is the one considered for answering Qs
# assume only one currency is used (Credits in example input)

# to change input file do:
# IntergalacticConverter.default_file_path = "XXX.txt"
converter = IntergalacticConverter()
converter.run()



class Metal:
	'''A class for storing different types of metal'''

	def __init__(self, name, price):
		self.name = name
		self.price = price
