import os

class FileParser:
    '''Represents the file parser class'''
    '''Used to parse an input file'''

    default_file_path = "test_input.txt"
    output_file_path = "output.txt"

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = self.default_file_path
        else:
            self.file_path = file_path

    def run(self):
        read_from = os.path.dirname(os.path.realpath(__file__)) + '/' + self.file_path
        file = open(read_from)

        lines_to_write = []
        for line in file:
            resp = self.parse_input_line(line)
            if resp is not None:
                lines_to_write.append(resp)

        # output to file
        if len(lines_to_write) > 0:
            self.write_to_file(lines_to_write)

    def parse_input_line(self, line):
        pass

    def parse_question(self, elems):
        pass

    def write_to_file(self, lines):
        if len(lines) == 0:
            print "Trying to write 0 lines"
            return None

        try:
            file = open(self.output_file_path)
            # empty file if existent
            file.truncate()
        except IOError:
            # doesn't exist so make it
            file = open(self.output_file_path, "w+")

        for line in lines:
            # add '\n' if not last line in array
            endl = "" if (line == lines[-1]) else "\n"
            file.write(str(line) + endl)

        file.close()