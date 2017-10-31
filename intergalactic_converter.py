import os

# Roman numerals to value
roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M': 1000}

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

	def run(self):
		read_from = os.path.dirname(os.path.realpath(__file__)) + self.file_path
		file = open(read_from)

		for line in file:
			self.parse_input_line(line)

	def parse_input_line(self, line):
		print line
		line_elems = line.split(' ')
		if line_elems[1] == 'is' and line_elems[2] in roman_numerals:
			self.intergalactics_to_romans[line_elems[0]] = line_elems[2]
			print self.intergalactics_to_romans
		elif line_elems[0] in self.intergalactics_to_romans:
			self.store_metal_price(line_elems)
		elif line_elems[-1] == '?'
			self.parse_question(line_elems)
		else:
			print "Couldn't parse line |" + line + "|"

	def store_metal_price(self, elems):
		pass
		# map intergalactic->Roman->Arabic
		# self.currency = Credits?
		# price = Credits/Arabic
		# self.metals.append(Metal(name, price))

	def parse_question(self, elems):
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
			print None
			# if find metal:
				# print roman->arabic * metal.price
			# else:
				# print roman->arabic
		else:
			print "I have no idea what you are talking about"

		# check if we find more numerals and continue to parse?
		# eg: how many Credits is XXX Silver and YYY Gold?