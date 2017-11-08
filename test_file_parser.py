import unittest
# need to install mock |pip install mock|
from mock import patch

from file_parser import *

class TestFileParser(unittest.TestCase):
    path = "XXX.txt"

    def setUp(self):
        self.file_parser = FileParser()

    def tearDown(self):
        self.file_parser = None

    def test_default_file_parser_creation_no_path(self):
    	self.assertEqual(self.file_parser.file_path, FileParser.default_file_path)

    def test_default_file_parser_creation_custom_path(self):
    	file_parser = FileParser(self.path)
    	self.assertEqual(file_parser.file_path, self.path)

    def test_file_parser_run_no_path(self):
    	try:
    		with patch.object(self.file_parser, 'parse_input_line') as mock:
    			self.file_parser.run()
    		# check that parse_input_line() was called inside run
    		self.assertTrue(mock.called)
    	except IOError:
    		self.fail("run() for default file_parser raised IOError unexpectedly.")

    def test_file_parser_run_custom_path(self):
    	file_parser = FileParser(self.path)
    	with self.assertRaises(IOError):
    		file_parser.run()

    def test_file_parser_parse_question(self):
    	try:
    		self.file_parser.parse_question([])
    	except Exception, e:
    		self.fail("file_parser perse_question() failed with %s" % e)

    def test_file_parser_write_to_file(self):
        lines = ["test", "test1"]
        self.file_parser.write_to_file(lines)
        file = open(self.file_parser.output_file_path)
        for idx, line in enumerate(file):
            self.assertEqual(line.rstrip(), lines[idx])

    def test_file_parser_write_to_file_no_lines(self):
        lines = []
        with self.assertRaises(ValueError):
            self.file_parser.write_to_file(lines)

if __name__ == '__main__':
    unittest.main()