import os

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

class IntergalacticConverter:
	'''Represents the converter class'''

	default_file_path = "test_input.txt"

	def __init__(self, file_path=None):
		if file_path is None:
			self.file_path = default_file_path
		else:
        	self.file_path = file_path
        # could have used {metal_name:price} map for faster retrieval
        # self.metals = []
        # self.intergalactic_units = []

	def run(self):
		read_from = os.path.dirname(os.path.realpath(__file__)) + self.file_path
		file = open(read_from)

		for line in file:
			self.parse_input_line(line)

	def parse_input_line(self, line):
		print line
		# if intergalactic to Roman: (XXX is III)
			unit = XXX
			if next_word in roman_numerals:
				# map intergalactic unit to Roman
				self.intergalactic_units[unit] = next_word
		# elif intergalactic x Metal to Credits:
			# map intergalactic->Roman->Arabic
			# self.currency = Credits?
			# price = Credits/Arabic
			# self.metals.append(Metal(name, price))
		# elif question
			# parse_question()
		# else print warning msg

	def parse_question(self, question):
		include_currency = False
		# mention currency in output if mentioned in input
		if self.currency is not None and self.currency in question:
			include_currency = True

		found_roman_nums = False
		roman_numeral = ''
		# while next_is_roman:
			# found_roman = True
			# find intergalactic
			# map to Roman & roman_numeral += mapped_roman
		if found_roman_nums:
			# if find metal:
				# print roman->arabic * metal.price
			# else:
				# print roman->arabic
		else print "I have no idea what you are talking about"

		# check if we find more numerals and continue to parse?
		# eg: how many Credits is XXX Silver and YYY Gold?

class Metal:
	'''A class for storing different types of metal'''

	def __init__(self, name, price):
		self.name = name
		self.price = price
