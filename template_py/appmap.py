'''
   Copyright 2024 Matthew Ralston

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

'''
import sys
import os

import yaml
from collections import OrderedDict

import jsonschema


from template_py import config, util



yaml.add_representer(OrderedDict, util.represent_yaml_from_collections_dot_OrderedDict)

default_logline_choices = (20, 50, 100, 200)
PINNED_ISSUES = (140, 141, 143, 149, 150, 153,)

PROGRAM_BANNER = """


     |||
     |||             [|[          template_py           ]|]
     |||
     |||        version :     v{0}
     |||
     |||        GitHub  : https://github.com/MatthewRalston/template_py/issues
     |||         PyPI   : https://pypi.org/project/template_py/
     |||      Website   : https://matthewralston.github.io/template_py
     |||









# |||||||||||||||||||||||||||||||||||||||
#      [ Usage ] :        |||||||||||||||
# |||||||||||||||||||||||||||||||||||||||




""".format(config.VERSION)
INTERPRETER = "                                                                       lang :         python\n"
# hardcoded

# print_program_header
#        sys.stderr.write(PROGRAM_BANNER)
#        sys.stderr.write(INTERPRETER)
#        sys.stderr.write(self.VERSION_HARDCODED)
#        sys.stderr.write(self.PACKAGE_MANAGER)



GITHUB_LOGO = """
 .--------------------------------------------------.
 |                 .mmMMMMMMMMMMMMMmm.              |
 |             .mMMMMMMMMMMMMMMMMMMMMMMMm.          |
 |          .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.       |
 |        .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.     |
 |      .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.   |
 |     MMMMMMMM'  `"MMMMM"""""""MMMM""`  'MMMMMMMM  |
 |    MMMMMMMMM                           MMMMMMMMM |
 |   MMMMMMMMMM:                         :MMMMMMMMMM|
 |  .MMMMMMMMMM                           MMMMMMMMMM.
 |  MMMMMMMMM"                             "MMMMMMMMM
 |  MMMMMMMMM                               MMMMMMMMM
 |  MMMMMMMMM                               MMMMMMMMM
 |  MMMMMMMMMM                             MMMMMMMMMM
 |  `MMMMMMMMMM                           MMMMMMMMMMM
 |   MMMMMMMMMMMM.                     .MMMMMMMMMMMMM
 |    MMMMMM  MMMMMMMMMM         MMMMMMMMMMMMMMMMMMM|
 |     MMMMMM  'MMMMMMM           MMMMMMMMMMMMMMMM` |
 |      `MMMMMM  "MMMMM           MMMMMMMMMMMMMM`   |
 |        `MMMMMm                 MMMMMMMMMMMM`     |
 |          `"MMMMMMMMM           MMMMMMMMM"`       |
 |             `"MMMMMM           MMMMMM"`          |
 |                 `""M           M""`              |
 '--------------------------------------------------'


"""

THREE_LINES = """



"""


DNA_SPACER_1 = """
=================================
=================================


O       o O       o O       o O
| O   o | | O   o | | O   o | | O
| | O | | | | O | | | | O | | | |
| o   O | | o   O | | o   O | | o
o       O o       O o       O O


=================================
"""

DNA_SPACER_lol = """
=================================
=================================
Carbon rules everything around me

O       o O       o O       o O
| O   o | | O   o | | O   o | | O
| | O | | | | O | | | | O | | | |
| o   O | | o   O | | o   O | | o
o       O o       O o       O O


=================================
"""



DNA_COLUMN_1 = """
O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O
"""

GITHUB_PROJECT_BANNER = """
==============================================================
                  ||      G i t H u b     ||
==============================================================
                         Repo: template_py
               Feature branch: main

Issue Tracker: https://github.com/MatthewRalston/template_py/issues
-------------------------------------------------------
"""



PINNED_ISSUE = """
                 Pinned issue: {0}
""".format(", ".join(list(map(str, PINNED_ISSUES))))





"""
===============================
COMMAND INFO
===============================
"""





command_1_name, command_2_name = config.subcommands

COMMANDS = [
    command_1_name, #"first_command",
    command_2_name, #"second_command",
]




        
command_1_description = None
command_1_description_long = None


command_1_parameters = None
command_1_inputs = None
command_1_usage = None
COMMAND_1_BANNER = None

COMMAND_1_PARAMS = None

COMMAND_1_INPUTS = None



COMMAND_1_FEATURES = OrderedDict({
    "name": "features",
    "type": "array",
    "items": [
        OrderedDict({
            "name": "k-mer count array produced as sequences are read by sliding window approach. (Un)compressed support for .fa/.fq.",
            "shortname": "parallel OOP sliding window k-mer shredding",
            "description": "N = 4^k count-vector from one or more sequence files. (index, k-mer id, count, and frequency [as float64])"
        }),
        OrderedDict({
            "name": "k-mers are tallied, and metadata merged from the input files",
            "shortname": "merge counts, metadata from across inputs",
            "description": "a final metadata structure and output metrics are collected for display to the user."
        })

            ]
})


COMMAND_2_STEPS = None

command_2_description = None
command_2_description_long = None


command_2_parameters = None
command_2_inputs = None
command_2_usage = None
COMMAND_2_BANNER = None

COMMAND_2_PARAMS = None

COMMAND_2_INPUTS = None



COMMAND_2_FEATURES = OrderedDict({
    "name": "features",
    "type": "array",
    "items": [
        OrderedDict({
            "name": "k-mer count array produced as sequences are read by sliding window approach. (Un)compressed support for .fa/.fq.",
            "shortname": "parallel OOP sliding window k-mer shredding",
            "description": "N = 4^k count-vector from one or more sequence files. (index, k-mer id, count, and frequency [as float64])"
        }),
        OrderedDict({
            "name": "k-mers are tallied, and metadata merged from the input files",
            "shortname": "merge counts, metadata from across inputs",
            "description": "a final metadata structure and output metrics are collected for display to the user."
        })

            ]
})


COMMAND_2_STEPS = None

###################################################

#            F i n a l     c o m m a n d    a g g r e g a t e

###################################################


ALL_PARAMS = {
    "command_1_name": COMMAND_1_PARAMS["items"],
    "command_2_name": COMMAND_2_PARAMS["items"],
}

ALL_INPUTS = {
    "command_1_name": COMMAND_1_INPUTS["items"],
    "command_2_name": COMMAND_2_INPUTS["items"],
}

ALL_FEATURES = {
    "command_1_name": COMMAND_1_FEATURES["items"],
    "command_2_name": COMMAND_2_FEATURES["items"],
}


ALL_STEPS = {

    "command_1_name": COMMAND_1_STEPS["items"],
    "command_2_name": COMMAND_2_STEPS["items"],
}




        
class template_py_appmap:



    
    def __init__(self, argv, logger=None):


        if logger is not None:
            self.logger = logger
            self.logfile = logger.logfile
        else:
            self.logger = None
            self.logfile = None
        self._loggable = logger is not None
        
        
        self.MODULE_ROOT = os.path.join("..", os.path.dirname(__file__))
        self.COMMAND_FILE = os.path.join(self.MODULE_ROOT, "__init__.py")
        self.PACKAGE_MANAGER = """
                      package manger : pip
                        version      : >= 24.0
        package root : {0}
        exe file     : {1}

                      required packages : {2}
                   development packages : {3}

           ARGV : {4}
        """.format(self.MODULE_ROOT, self.COMMAND_FILE, config.requirements_count, config.requirements_dev_count, argv)
        self.REQUIRES_PYTHON = config.REQUIRES_PYTHON
        self.VERSION_HARDCODED = "                                                                          v :      >= v{0}\n".format(config.REQUIRES_PYTHON)


        
        #
        # loaded_modules
        #

        #
        # dependencies
        #
        #      required:
        #      optional:

        # usage_notes.txt





        


        
        # KMEANS_BANNER = """
        #                   name : kmeans
        #            description : 
        # """

        # HIERARCHICAL_BANNER = """

        # """


        # config.py features
        #SUPPORTED_FEATURES = {}

        # ASCII + RICH.py checklist
        
    def print_verbosity_header(self):
        """
        This prints the verbosity warnings and default logging behavior for the user.
        """

        sys.stderr.write("="*40 + "\n")
        sys.stderr.write("[ DEBUG ] : Default is warning-only logging. [-v,-vv, --debug, --quiet]\n")
        sys.stderr.write("[ INFO  ] : Default is warning-only logging. [-v,-vv, --debug, --quiet]\n")
        sys.stderr.write("="*40 + "\n")
        sys.stderr.write("WARNING. Some features are experimental. Note: you are tracking template_py/main. Visit the README.md header, usage section, or quickstart page for additl.\n")
        sys.stderr.write("-"*40 + "\n")

        #print("x..xx")
        #print("xd up ya brakes")

        #
        #
        #...


        #' ...#x'"' ''"'?"    # ... #xdupyabrakexsz '#xdupyabreakesz' '"'"''"""""""...'"'. #XduPyabrakx. '"' ....

        return




    def print_program_header(self):
        """
        Only used in 'usage' method. Spacer at bottom is permissible because this may be used externally to usage.
        """
        
        sys.stderr.write(PROGRAM_BANNER)
        sys.stderr.write(INTERPRETER)
        sys.stderr.write(self.VERSION_HARDCODED)
        sys.stderr.write(self.PACKAGE_MANAGER)

        # Spacer
        sys.stderr.write(DNA_COLUMN_1)

        sys.stderr.write(THREE_LINES)

    def print_graph_header(self):
        """
        'kmerdb usage graph'

        Writes input files, parameters, steps, and features as verbose --help on the parameters effects on the runtime.

        """
        
        sys.stderr.write(COMMAND_2_BANNER)

        sys.stderr.write(THREE_LINES)
        
        sys.stderr.write(yaml.dump(COMMAND_2_PARAMS))
        
        sys.stderr.write(THREE_LINES)
        
        sys.stderr.write(yaml.dump(COMMAND_2_INPUTS))

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(yaml.dump(COMMAND_2_FEATURES))

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(yaml.dump(COMMAND_2_STEPS))



    def print_profile_header(self):
        """
        'kmerdb usage profile'

        Writes input files, parameters, steps, and features as verbose --help on the parameters effects on the runtime.

        """
        sys.stderr.write(COMMAND_1_BANNER)

        sys.stderr.write(THREE_LINES)
            
        sys.stderr.write(yaml.dump(COMMAND_1_PARAMS))

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(yaml.dump(COMMAND_1_INPUTS))

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(yaml.dump(COMMAND_1_FEATURES))

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(yaml.dump(COMMAND_1_STEPS))




        
        
    def print_github_block(self):
        """
        Github repo block. May be useful to some users when browsing logilfe.
        """


        sys.stderr.write(THREE_LINES)
        
        sys.stderr.write(DNA_SPACER_lol)

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(GITHUB_LOGO)

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(GITHUB_PROJECT_BANNER)

        sys.stderr.write(PINNED_ISSUE)

        sys.stderr.write(THREE_LINES)

        sys.stderr.write(DNA_SPACER_1)

        sys.stderr.write(THREE_LINES)

        
        

    def exit_gracefully(self, e:Exception, subcommand:str=None, step:int=None, feature:int=None, logs:list=None, n_logs:int=None):
        """
        We need to handle exit gracefully. The 'step' and 'feature' categories/flags/ints are passed from __init__ or down its callstack to 
        """
        import traceback


        # if e is None:
        #     raise ValueError("Need an error to exit")
        # elif not isinstance(e, Exception):
        #     raise ValueError("Need an error to exit")

        
        # if n_logs is None or type(n_logs) is not int:
        #     raise TypeError("kmerdb.appmap.exit_gracefully expects the keyword argument n_logs to be a int")
        # elif logs is None or type(logs) is not list:
        #     raise TypeError("kmerdb.appmap.exit_gracefully expects the keyword argument logs to be a list")
        # elif feature is not None and type(feature) is not int:
        #     raise TypeError("kmerdb.appmap.exit_gracefully expects the keyword argument feature to be a int")
        # elif step is not None and type(step) is not int:
        #     raise TypeError("kmerdb.appmap.exit_gracefully expects the keyword argument step to be a int")
        # elif subcommand is not None and type(subcommand) is not str:
        #     raise TypeError("kmerdb.appmap.exit_gracefully expects the keyword argument subcommand to be a str")



        
        N = min(len(logs), n_logs)

        tb = traceback.extract_tb(e.__traceback__)
        last_traceback_FrameSummary = tb[-1]
        error_file_name = last_traceback_FrameSummary.filename
        error_line_number = last_traceback_FrameSummary.lineno

        
        #assert subcommand in config.subcommand_functions, "Unknown subcommand"

        if self._loggable:
            self.logger.log_it("Program error! Collecting error metadata and formatting...", "ERROR")
        # This is the "Error blocks" metadata


        sys.stderr.write("Aggregating program metadata, if this fails without error without the --debug flag, please report to the GitHub issue tracker with the title 'Error summary convenience function'.")
        sys.stderr(subcommand)
        sys.stderr(config.VERSION)
        sys.stderr(config.REQUIRES_PYTHON)
        sys.stderr(feature)
        sys.stderr(ALL_FEATURES[subcommand][feature]["name"])
        sys.stderr(ALL_FEATURES[subcommand][feature]["shortname"])
        sys.stderr(ALL_FEATURES[subcommand][feature]["description"])
        sys.stderr(step)
        sys.stderr(ALL_STEPS[subcommand][step]["name"])
        sys.stderr(ALL_STEPS[subcommand][step]["shortname"])
        sys.stderr(ALL_STEPS[subcommand][step]["description"])
            # The *total* number of logged lines produced by the program and returned to the global 'logs' var in __init__.py
        sys.stderr(self.logfile)
        sys.stderr(str(tb))
        sys.stderr(error_file_name)
        sys.stderr(error_line_number)
        sys.stderr(e.__str__())

        
        e_sum = {
            "subcommand": subcommand,
            "template-py-version": config.VERSION,
            "python-version": config.REQUIRES_PYTHON,
            "feature": feature,
            "feature_name": ALL_FEATURES[subcommand][feature]["name"],
            "feature_shortname": ALL_FEATURES[subcommand][feature]["shortname"],
            "feature_description": ALL_FEATURES[subcommand][feature]["description"],
            "step" : step,
            "step_name": ALL_STEPS[subcommand][step]["name"],
            "step_shortname": ALL_STEPS[subcommand][step]["shortname"],
            "step_description": ALL_STEPS[subcommand][step]["description"],
            # The *total* number of logged lines produced by the program and returned to the global 'logs' var in __init__.py
            "log_file": self.logfile,
            "traceback": str(tb),
            "error_file_name": error_file_name,
            "error_line_number": error_line_number,
            "error": e.__str__(),
        }

        
        exit_summary = OrderedDict(e_sum)

        
        yaml.add_representer(OrderedDict, util.represent_yaml_from_collections_dot_OrderedDict)
        

        try:
            jsonschema.validate(instance=exit_summary, schema=config.exit_summary_schema)
        except jsonschema.ValidationError as e:
            sys.stderr.write("Failed to validate the exit summary. Internal Error.\n")
            raise e
                
        self.print_github_block()

        """
        Print last n lines of log
        """



        
        for i in range(N):

            try:
                if self._loggable:
                    sys.stderr.write("{0} - last line of log\n".format(n_logs - i))
                    self.logger.log_it(logs[i], "ERROR")
                else:
                    sys.stderr.write("{0} - last line of log\n".format(n_logs - i))
                    sys.stderr.write(logs[i])
            except Exception as e:
                raise e
                
        sys.stderr.write("-" * 80 + "\n")
        if self._loggable:
            
            self.logger.log_it("...displaying last {0} lines of the log. Please see '{1}' for more details...".format(n_logs, self.logfile), "ERROR")
            self.logger.log_it(e.__str__())

            sys.stderr.write(THREE_LINES)

            sys.stderr.write(DNA_SPACER_1)

            sys.stderr.write(THREE_LINES)

            self.logger.log_it("="*40 + "\n", "ERROR")

            self.logger.log_it(" "*20 + "ERROR: Program exit summary:\n", "ERROR")
            
            self.logger.log_it("="*40 + "\n", "ERROR")
            
            self.logger.log_it("\n" + yaml.dump(exit_summary), "ERROR")

            self.logger.log_it("="*40 + "\n")

            sys.stderr.write(THREE_LINES)
            
            
        else:
            sys.stderr.write("...displaying last {0} lines of the log. Please see '{1}' for more details...\n".format(n_logs, self.logfile))
            sys.stderr.write(e.__str__())

            sys.stderr.write(THREE_LINES)

            sys.stderr.write(DNA_SPACER_1)

            sys.stderr.write(THREE_LINES)

            sys.stderr.write("="*40 + "\n\n")

            sys.stderr.write(" "*20 + "ERROR: Program exit summary:\n\n")
            
            sys.stderr.write("="*40 + "\n")
            
            sys.stderr.write("\n" + yaml.dump(exit_summary) + "\n")

            sys.stderr.write("="*40 + "\n")

            sys.stderr.write(THREE_LINES)



            
        return exit_summary


    








