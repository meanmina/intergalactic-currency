from metal import *
from file_parser import FileParser

class IntergalacticConverter(FileParser):
    '''Represents the converter class'''
    '''Inherits from FileParser & overrides some of the functionality to match our requirements'''

    # map intergalactic numerals to roman numerals
    intergalactics_to_romans = {}
    # keep track of the currency used ('Credits' in test_input)
    # assume we could have a dif currency mentioned in file so we want to keep trakc of it
    currency = ""

    # Roman numerals to value
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M': 1000}

    def parse_input_line(self, line):
        line_elems = line.rstrip().split(' ')

        if line_elems[1] == 'is' and line_elems[2] in self.roman_numerals:
            self.intergalactics_to_romans[line_elems[0]] = line_elems[2]
        elif line_elems[0] in self.intergalactics_to_romans:
            self.store_metal_price(line_elems)
        elif line_elems[-1] == '?':
            return self.parse_question(line_elems)
        else:
            print "Couldn't parse line >>" + line
        return None

    def parse_question(self, elems):
        # mention currency in output if mentioned in input
        include_currency = False
        if self.currency is not None and self.currency in elems:
            include_currency = True

        found_numerals = False
        roman_numeral = ''
        intergalactic_numeral = ''
        # assuming price will never be less than 0 so -1 used as default
        price = -1
        name = None
        for el in elems:
            # naively assume that there's only a set of intergalactic numerals in a question
            # alternatively we would want to check that the prev word was a numeral
            # and treat it as a separate number group if there's a non-numeral word inbetween
            if el in self.intergalactics_to_romans:
                roman_numeral += self.intergalactics_to_romans[el]
                if len(intergalactic_numeral) == 0:
                    intergalactic_numeral+= el
                else:
                    intergalactic_numeral += ' ' + el
                found_numerals = True
            price = Metal.get_price(el)
            # naively assume a metal comes right after the intergalactic numerals
            # and also that the metal is the last word we care to parse
            if price is not None:
                # if we found a price then this was a metal so we can return the value
                # also keep track of the metal name
                name = el
                break
            # alternatively we would check if we find more numerals and continue to parse
            # (instead of break) and keep track of all numerals and metals mentioned
            # and return a total
            # eg: 'how many Credits is XXX Silver and YYY Gold?'
        amount = self.get_arabic_from_roman(roman_numeral)

        if found_numerals:
            # value to be based on priceonly if metal included in input
            if price > -1:
                value = amount * price
            else:
                value = amount
            # output to include currency if input did
            currency = (' ' + self.currency) if include_currency else ''
            # output to file
            return intergalactic_numeral + (' ' + name if name is not None else '') + \
                    " is " + str(value).rstrip('0').rstrip('.') + currency
        else:
            # output to file
            return "I have no idea what you are talking about"

    def store_metal_price(self, elems):
        roman_value = ''
        last_was_digit = False
        last_intergalactic = -2
        name = ''

        for idx, el in enumerate(elems):
            get_currency = False
            if last_was_digit:
                get_currency = True
                last_was_digit = False
            if el in self.intergalactics_to_romans:
                roman_value += self.intergalactics_to_romans[el]
                last_intergalactic = idx
            elif idx == (last_intergalactic + 1) and el[0].isupper():
                # we expect the next word after intergalactic currency (starting with caps) to be metal name
                name = el
            elif el.isdigit():
                last_was_digit = True
                # assuming this is a simple case and not unicode
                try:
                    value = int(el)
                    continue
                except ValueError:
                    value = int(float(el))
            elif get_currency:
                # naively assume currency comes right after the number representing the value
                # and that there's only one value per input line 
                self.currency = el
                break
        arabic_value = self.get_arabic_from_roman(roman_value)
        if arabic_value > 0:
            price = value/float(arabic_value)
        else:
            price = 0
        if len(name) > 0 and price > 0:
            Metal(name, price)
        else:
            print "Can't save metal with name/price = " + name + "/" + str(price)

    # REQUIREMENTS:
    # can repeat max 3 times
    repeat = ['I', 'X', 'C', 'M']
    # only subtract from 2 higher levels
    subtract_levels = 2
    # cannot subtract the following:
    not_subtract = ['V', 'L', 'D']
    # subtract only one small from one large
    # ASSUMPTIONS:
    # metals are unique by name
    # last price in list is the one considered for answering Qs
    # assume only one currency is used (Credits in example input)

    def get_arabic_from_roman(self, roman):
        if len(roman) == 0:
            return 0

        repeats = {}
        total = 0
        # make a list to help in counting subtraction levels
        roman_numerals_list = list(sorted(self.roman_numerals, key=self.roman_numerals.__getitem__))
        for idx, char in enumerate(roman):
            # handle repeating of romans
            if char in repeats:
                repeats[char] += 1
            else:
                repeats[char] = 1
            if repeats[char] > 1 and char not in self.repeat:
                print char + " can't be repeated. Return 0."
                return 0
            if repeats[char] > 3:
                print char + " can't be repeated more than 3 times. Return 0."
                return 0
            # handle total of romans
            prev = roman[idx-1] if (idx-1 >= 0) else None
            nxt = roman[idx+1] if (idx+1 < len(roman)) else None
            if (char in self.roman_numerals and (True if prev is None else self.roman_numerals[char] <= self.roman_numerals[prev])
                    and (True if nxt is None
                            else self.roman_numerals[char] >= self.roman_numerals[nxt])):
                # only count towards total if smaller than previous and bigger than next
                # if bigger than previous then we need subtraction
                # if smaller than next then we will need subtraction on next one
                total += self.roman_numerals[char]
            elif prev is not None and self.roman_numerals[char] > self.roman_numerals[prev]:
                # handle subtraction
                if prev in self.not_subtract:
                    print char + " can't be subtracted. Return 0."
                    return 0
                # check if roman[idx-1] can be subtracted from roman[idx]
                diff_in_level = roman_numerals_list.index(char) - roman_numerals_list.index(prev)
                if diff_in_level > self.subtract_levels:
                    print char + " can't be subtracted from " + prev + ". Return 0."
                    return 0
                # do the subtraction
                total += self.roman_numerals[char] - self.roman_numerals[prev]
        return total