import unittest
from mock import patch
import filecmp

from intergalactic_converter import *
from metal import *

class TestIntergalacticConverter(unittest.TestCase):
    path = "YYY.txt"
    test_input_path = "test_input.txt"
    test_output_path = "test_output.txt"

    def setUp(self):
        self.intergalactic_converter = IntergalacticConverter()

    def tearDown(self):
        Metal.remove_all_metals()
        self.intergalactic_converter = None

    def test_default_intergalactic_converter_creation_no_path(self):
        self.assertEqual(self.intergalactic_converter.file_path, IntergalacticConverter.default_file_path)

    def test_default_intergalactic_converter_creation_custom_path(self):
        intergalactic_converter = IntergalacticConverter(self.path)
        self.assertEqual(intergalactic_converter.file_path, self.path)

    def test_intergalactic_converter_run_no_path(self):
        with patch.object(self.intergalactic_converter, 'parse_input_line') as parse_input_line_mock:
            with patch.object(self.intergalactic_converter, 'write_to_file') as write_to_file_mock:
                try:
                    self.intergalactic_converter.run()
                except IOError:
                    self.fail("run() for default intergalactic_converter raised IOError unexpectedly.")
        # check that parse_input_line() and write_to_file() were called inside run
        self.assertTrue(parse_input_line_mock.called)
        self.assertTrue(write_to_file_mock.called)

    def test_intergalactic_converter_run_no_path_test_output(self):
        # use test_input.txt as input and test_putput.txt should match the output file
        intergalactic_converter = IntergalacticConverter(self.test_input_path)
        try:
            intergalactic_converter.run()
        except IOError:
            self.fail("run() for default intergalactic_converter raised IOError unexpectedly.")

        # compare output file to test_output.txt
        self.assertTrue(filecmp.cmp(self.test_output_path, intergalactic_converter.output_file_path))

    def test_intergalactic_converter_run_custom_path(self):
        intergalactic_converter = IntergalacticConverter(self.path)
        with patch.object(intergalactic_converter, 'parse_input_line') as parse_input_line_mock:
            with patch.object(intergalactic_converter, 'write_to_file') as write_to_file_mock:
                with self.assertRaises(IOError):
                    intergalactic_converter.run()
        # check that parse_input_line() and write_to_file() were NOT called inside run
        self.assertFalse(parse_input_line_mock.called)
        self.assertFalse(write_to_file_mock.called)

    def test_intergalactic_converter_parse_question(self):
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        resp = self.intergalactic_converter.parse_question("how much is glob glob ?".split(' '))
        # check answer is what we expect
        self.assertEqual(resp, "glob glob is 2")

    def test_intergalactic_converter_parse_question_no_question_mark(self):
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        resp = self.intergalactic_converter.parse_question("how much is glob glob".split(' '))
        # check answer is what we expect
        self.assertEqual(resp, "glob glob is 2")

    def test_intergalactic_converter_parse_question_no_answer(self):
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        resp = self.intergalactic_converter.parse_question("how much is bla bla ?".split(' '))
        # check answer is what we expect
        self.assertEqual(resp, "I have no idea what you are talking about")

    def test_intergalactic_converter_parse_question_part_answer(self):
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        resp = self.intergalactic_converter.parse_question("how much is glob bla ?".split(' '))
        # check answer is what we expect
        self.assertEqual(resp, "glob is 1")

    def test_intergalactic_converter_store_metal(self):
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        self.intergalactic_converter.store_metal_price("glob glob Silver is 34 Credits".split(' '))
        # check Metal was created
        self.assertEqual(Metal.get_num_metals(), 1)
        # check price per 1 item is 34/2
        self.assertEqual(Metal.get_price("Silver"), 17)

    def test_intergalactic_converter_store_metal_part_good_question(self):
        # use one correct intergalactic numeral and one wrong one
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        self.intergalactic_converter.store_metal_price("bla glob Silver is 34 Credits".split(' '))
        # check Metal was created
        self.assertEqual(Metal.get_num_metals(), 1)
        # check price per 1 item is 34/2
        self.assertEqual(Metal.get_price("Silver"), 34)

    def test_intergalactic_converter_store_metal_part_bad_question(self):
        # use one correct intergalactic numeral and one wrong one
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        self.intergalactic_converter.store_metal_price("glob bla Silver is 34 Credits".split(' '))
        # check Metal was NOT created
        self.assertEqual(Metal.get_num_metals(), 0)

    def test_intergalactic_converter_store_metal_multiple_metal_question(self):
        # use one correct intergalactic numeral and one wrong one
        self.intergalactic_converter.intergalactics_to_romans["glob"] = "I"
        self.intergalactic_converter.store_metal_price("glob glob Silver is 34 Credits and glob Gold is 10 Credits".split(' '))
        # check Metal was created
        self.assertEqual(Metal.get_num_metals(), 1)
        # check price per 1 item is 34/2
        self.assertEqual(Metal.get_price("Silver"), 17)

    def test_intergalactic_converter_get_arabic_from_roman(self):
        self.assertEqual(self.intergalactic_converter.get_arabic_from_roman("MCMIII"), 1903)

    def test_intergalactic_converter_get_arabic_from_roman_no_input(self):
        with self.assertRaises(TypeError):
            self.intergalactic_converter.get_arabic_from_roman()

    def test_intergalactic_converter_get_arabic_from_roman_empty_input(self):
        self.assertEqual(self.intergalactic_converter.get_arabic_from_roman(""), 0)

    def test_intergalactic_converter_get_arabic_from_roman_bad_input(self):
        self.assertEqual(self.intergalactic_converter.get_arabic_from_roman("ZZZ"), 0)

if __name__ == '__main__':
    unittest.main()