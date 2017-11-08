# intergalactic-currency

# PROBLEM
# Merchant's Guide to the Galaxy

# DESIGN
# the metal class is used for storing the different metals we get prices for
#   it stores a list of all metals we've created so we can easily query and get price per metal name
# the FileParser class is a generic file parser which reads & writes to file and has the possibility of parsing input lines or questions
#   these functions can be overriden in the classes inheriting from FileParser class so they're fit for purpose
# the IntergalacticConverter class inherits from the FileParser class since it needs the generic file handling capabilities
#   it overrides the parse_input_line() and parse_question() methods since we require custom handling for our intergalactic currency input
#   it also adds more methods specific to it's purpose such as converting from roman_numerals to arabic_numerals and storing new Metals when seen in input
#   contains some attributes which define the requirements for our problem like the arabic value of every roman numeral
# I chose to use inheritance becuse the FileParser class could be easily used in other cases with some common functionality

# TESTING
# used the unittest library
# unit tests used here since it's a simple framework and there's not many working parts to actually implement more complex integration or end-to-end tests
# unit tests are also cheapest to use and can provide great benefits
# more complex testcases will be beneficial in projects with complex functionality
# also used filecmp library in test_intergalactic_converter.py to compare the resulting output_file to the expected one

# ASSUMPTIONS (most of these comments will be found along the code)
# assume we could have a dif currency mentioned in file so we want to keep track of it in self.currency
# assume that there's only a set of intergalactic numerals in a question
#   alternatively we would want to check that the prev word was a numeral
#   and treat it as a separate number group if there's a non-numeral word inbetween
# assume a metal comes right after the intergalactic numerals
#   and also that the metal is the last word we care to parse in an input line (appart from the intergalactic valuation ones)
# assume the output should include the currency name if input does
# we assume the next word after intergalactic currency (starting with caps) is the metal name
# assume currency comes right after the number representing the value
#   and that there's only one value per input line
# assume metals are unique by name
# assume last price in list is the one considered for answering Qs
# assume only one currency is used (Credits in example input)

# INSTRUCTIONS
# to run do:
#   python main.py
# (I used python 2.7)
# running results in an output.txt file in the same directory
# the output.txt file gets emptied on every run and filled with only the last output
# to change input file do:
#   IntergalacticConverter.default_file_path = "XXX.txt"
# to run all tests:
#   python -m unittest discover -v
# to run one test suite:
#   python test_metal.py
# test test_intergalactic_converter_run_no_path_test_output (inside test_intergalactic_converter) will run the intergalactic_converter with the provided test_input
#   and compares the resulting output file with one containing the provided test_output