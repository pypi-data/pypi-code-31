import os
import pyansys
from pyansys import ansys_functions

VALID_COMMANDS = dir(ansys_functions._InternalANSYS)

NON_INTERACTIVE_COMMANDS = ['*CRE', '*VWR']


def IsFloat(string):
    """ Returns true when a string can be converted to a float """
    try:
        float(string)
        return True
    except:
        return False


def ConvertFile(filename_in, filename_out, loglevel='INFO', auto_exit=True,
                line_ending=None, exec_file=None, macros_as_functions=True):
    """
    Converts an ANSYS input file to a python pyansys script.

    Parameters
    ----------
    filename_in : str
        Filename of the ansys input file to read in.

    filename_out : str
        Filename of the python script to write a translation to.

    loglevel : str, optional
        Log level of the ansys object within the script.

    auto_exit : bool, optional
        Adds a line to the end of the script to exit ANSYS.  Default True.

    line_ending : str, optional
        When None, automatically determined by OS being used.  
        Acceptable inputs are:

        - \n
        - \r\n

    Returns
    -------
    clines : list
        List of lines translated

    """
    # use_function_names : bool, optional
    #     When enabled, will translate "MP,EX,1,30E6" to "ansys.Mp('EX', 1, 30E6)"
    #     When disabled, will translate "MP,EX,1,30E6" to ansys.Run("MP,EX,1,30E6")
    #     Enabled by default.

    translator = FileTranslator(loglevel, line_ending, exec_file=exec_file,
                                macros_as_functions=macros_as_functions)
    with open(filename_in) as file_in:
        for line in file_in.readlines():
            translator.TranslateLine(line)

    if auto_exit:
        translator.WriteExit()
    translator.Save(filename_out)
    return translator.lines


class FileTranslator():
    obj_name = 'ansys'
    indent = ''
    non_interactive = False

    def __init__(self, loglevel='INFO', line_ending=None, exec_file=None,
                 macros_as_functions=True):
        self._non_interactive_level = 0
        self.lines = []
        self._functions = []
        if line_ending:
            self.line_ending = line_ending
        else:
            self.line_ending = os.linesep
        self.macros_as_functions = macros_as_functions
        self._infunction = False

        self.WriteHeader()
        self.InitializeANSYSObject(loglevel, exec_file)

    def WriteHeader(self):
        header = '""" Script generated by pyansys version %s"""%s' % (pyansys.__version__,
                                                                      self.line_ending)
        self.lines.append(header)

    def WriteExit(self):
        self.lines.append('%s.Exit()%s' % (self.obj_name, self.line_ending))

    def Save(self, filename):
        """ Saves lines to file """
        if os.path.isfile(filename):
            os.remove(filename)
        with open(filename, 'w') as f:
            for line in self.lines:
                f.write(line)

    def InitializeANSYSObject(self, loglevel, exec_file):
        """ Initializes ansys object as lines """
        self.lines.append('import pyansys%s' % self.line_ending)
        if exec_file:
            exec_file_parameter = '"%s", ' % exec_file
        else:
            exec_file_parameter=''
        line = 'ansys = pyansys.ANSYS(%sloglevel="%s")%s' % (exec_file_parameter,
                                                             loglevel,
                                                             self.line_ending)
        self.lines.append(line)

    @property
    def line_ending(self):
        return self._line_ending

    @line_ending.setter
    def line_ending(self, line_ending):
        if line_ending not in ['\n', '\r\n']:
            raise Exception('Line ending must be either "\\n", "\\r\\n"')
        self._line_ending = line_ending

    def TranslateLine(self, line):
        """ Converts a single line from an ANSYS APDL script """
        self.comment = ''
        line = line.strip()
        line = line.replace('"', "'")

        # check if line contains a comment
        if '!' in line:
            if line[0] == '!':  # entire line is a comment
                self.comment = line.replace('!', '').strip()
                self.StoreComment()
                return
            else: # command and in-line comment
                split_line = line.split('!')
                line = split_line[0]
                self.comment = ' '.join(split_line[1:])
                self.comment = self.comment.lstrip()

        if not line:
            return

        if '*END' in line:
            if self.macros_as_functions:
                self.StoreEmptyLine()
                self.StoreEmptyLine()
                self.indent = self.indent[4:]
                self._infunction = False
                self.EndNonInteractive()
                return
            else:
                self.StoreRunCommand(line)
                self.EndNonInteractive()
                return

        # check for if statement
        if line[:3].upper() == '*IF' or '*IF' in line.upper():
            self.StartNonInteractive()
            self.StoreRunCommand(line)
            return

        # check if line ends non-interactive
        if line[0] == '(':
            if not self.non_interactive:
                print('Possible invalid line:\n%s\n' % line +
                      'This line requires a *VWRITE beforehand')
            self.StoreRunCommand(line)
            self.EndNonInteractive()
            return
            # else:
        elif line[:4] == '*USE' and self.macros_as_functions:
            items = line.split(',')
            func_name = items[1]
            if func_name in self._functions:
                args = ', '.join(items[2:])
                call_line = '%s(%s)%s' % (func_name, args, self.line_ending)
                self.lines.append(call_line)
                return

        # check if a line is setting a variable
        items = line.split(',')
        if '=' in items[0]:  # line sets a variable:
            self.StoreRunCommand(line)
            return

        command = items[0].capitalize().strip()
        parameters = items[1:]
        if not command:
            self.StoreEmptyLine()
            return

        # check valid command
        if command not in VALID_COMMANDS:
            if line[:4] == '*CRE':
                if self.macros_as_functions:
                    self.StartFunction(items[1])
                    return
                else:
                    self.StartNonInteractive()
            elif line[:4] in NON_INTERACTIVE_COMMANDS:
                self.StartNonInteractive()
            self.StoreRunCommand(line)
        else:
            self.StoreCommand(command, parameters)

    def StartFunction(self, func_name):
        self._functions.append(func_name)
        self.StoreEmptyLine()
        self.StoreEmptyLine()
        self._infunction = True
        spacing = ' '*(len(func_name) + 5)
        line = 'def %s(%s,%s' % (func_name, ', '.join(["ARG%d=''" % i for i in range(1, 7)]),
                                 self.line_ending)
        line += '%s%s,%s' % (spacing, ', '.join(["ARG%d=''" % i for i in range(7, 13)]),
                             self.line_ending)
        line += '%s%s):%s' % (spacing, ', '.join(["ARG%d=''" % i for i in range(13, 19)]),
                              self.line_ending)
        self.lines.append(line)
        self.indent = self.indent + '    '

    def StoreRunCommand(self, command):
        """
        Stores pyansys.ANSYS command that cannot be broken down into a
        function and parameters.
        """
        if self._infunction and 'ARG' in command:
            args = []
            for i in range(1, 19):
                arg = 'ARG%d' % i
                c = 0
                if arg in command:
                    command = command.replace(arg, '{%d:s}' % c)
                    args.append(arg)
                    c += 1

            line = '%s%s.Run("%s".format(%s))%s' % (self.indent, self.obj_name, command,
                                                    ', '.join(args), self.line_ending)

        elif self.comment:
            line = '%s%s.Run("%s")  # %s%s' % (self.indent, self.obj_name, command,
                                            self.comment, self.line_ending)
        else:
            line = '%s%s.Run("%s")%s' % (self.indent, self.obj_name, command,
                                         self.line_ending)

        self.lines.append(line)

    def StoreComment(self):
        """ Stores a line containing only a comment """
        line = '%s# %s%s' % (self.indent, self.comment, self.line_ending)
        self.lines.append(line)

    def StoreEmptyLine(self):
        """ Stores an empty line """
        self.lines.append(self.line_ending)

    def StoreCommand(self, function, parameters):
        """ Stores a valid pyansys function with parameters """
        parsed_parameters = []
        for parameter in parameters:
            parameter = parameter.strip()
            if IsFloat(parameter):
                parsed_parameters.append(parameter)
            elif 'ARG' in parameter and self._infunction:
                parsed_parameters.append('%s' % parameter)
            else:
                parsed_parameters.append('"%s"' % parameter)

        parameter_str = ', '.join(parsed_parameters)
        if self.comment:
            line = '%s%s.%s(%s)  #%s%s' % (self.indent, self.obj_name, function,
                                           parameter_str, self.comment, self.line_ending)
        else:
            line = '%s%s.%s(%s)%s' % (self.indent, self.obj_name, function,
                                      parameter_str, self.line_ending)

        self.lines.append(line)

    def StartNonInteractive(self):
        self._non_interactive_level += 1
        if self.non_interactive:
            return
        self.lines.append('%swith %s.non_interactive:%s' % (self.indent, self.obj_name,
                                                            self.line_ending))
        self.non_interactive = True
        self.indent = self.indent + '    '

    def EndNonInteractive(self):
        self._non_interactive_level -= 1
        if self._non_interactive_level == 0:
            self.non_interactive = False
            self.indent = self.indent[4:]
