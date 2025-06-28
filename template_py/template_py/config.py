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



VERSION="0.0.2"
REQUIRES_PYTHON="3.7.4"


requirements_count = 4
requirements_dev_count = 8


subcommands = ["your_subcommand", "unimplemented"] # The name of each subcommand as a string
subcommand_functions = ["your_subcommand", "unimplemented"] # The name of each associated method called by args.func(yourmethodname)

default_logline_choices = (20, 50, 100, 200)



thanks = "\n\n\n" + "="*40 + """\n

  template_py v{0}    -     view -h|--help (or usage subcommand) for detailed information.


  please report any issues to https://github.com/yourusername/template_py/issues and thanks.
""".format(VERSION)


#DONE = + usage + issue_tracker
# Accept the citation notice with 'template_py citation'
DONE = """
DONE\n
"""


