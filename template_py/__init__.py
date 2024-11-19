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



import logging
import argparse
import os
import sys
import yaml
import json
import time
import signal

#from multiprocessing import cpu_count

#from collections import OrderedDict



global logger
logger = None


global step
step = 0

global feature
feature = 0

global exit_code
exit_code = -1


global exit_summary
exit_summary = None


def version(arguments):
    from template_py import config

    print(config.VERSION)


def print_argv():
    argv = sys.argv
    sys.stderr.write(" ".join(argv[0:4]) + " ...\n")

def citation(arguments):

    MODULE_ROOT = os.path.dirname(__file__)
    citation_file = os.path.join(MODULE_ROOT,  'CITATION.txt')
    if os.access(citation_file, os.R_OK):

        sys.stderr.write("Removing '{0}'\n".format(citation_file))
        os.remove(citation_file)

    sys.stderr.write("On the real, gotta eat.\n")
    sys.stderr.write("Consider a +1 on Github to keep it real...\n\n")

    if function_name in ["usage", "help", "citation"]:
        subcommand_name = function_name
    else:
        subcommand_name = config.subcommands[config.subcommand_functions.index(function_name)]



def expanded_help(arguments):

    import sys
    
    argv = sys.argv
    
    from template_py import config, appmap

    template_py_appmap = appmap.template_py_appmap( argv )

    match arguments.method:
        case "subcommand1":
            template_py_appmap.print_subcommand1_header()
        case "subcommand2":
            template_py_appmap.print_subcommand2_header()
        
    if arguments.method not in config.subcommands:
        raise ValueError("unsupported method")
    elif arguments.method == "subcommand1":
        template_py_appmap.print_subcommand1_header()

    sys.stderr.write("\n\nUse --help for expanded usage\n")

        


def subcommand(args):
    print("Full argparse argument object:")
    print(args)

    print("Hello, world!")
    print("I'm running 'template_py subcommand' with these arguments")


def new(args):
    print("Hello world")

def cli():

    import sys

    from configurator import config, appmap

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help="Use -h|--help with the individual subcommands, OR the 'usage' and 'help' subcommands to describe inputs, parameters, features, steps, etc.")


    new_parser = subparsers.add_parser("new", help="Run a subcommand of template_py")
    new_parser.add_argument("-p", "--project-name", type=str, required=True, help="The project-name to use throughout the Python template")
    new_parser.add_argument("-v", "--verbose", help="Prints warnings to the console by default", default=0, action="count")
    new_parser.add_argument("--debug", action="store_true", default=False, help="Debug mode. Do not format errors and condense log")
    new_parser.add_argument("-nl", "--num-log-lines", type=int, choices=config.default_logline_choices, default=50, help=argparse.SUPPRESS)
    new_parser.add_argument("-l", "--log-file", type=str, default="template_py.log", help=argparse.SUPPRESS)
    new_parser.set_defaults(func=new)






    """
    Final argument parsing and error handling
    """
    args=parser.parse_args()
    
    global logger
    global exit_code

    
    global step
    global feature

    
    global logs



    sys.stderr.write("Constructed a logger for the program...\n")
    #logger.debug(sys.path)

    # Print program header
    sys.stderr.write("Starting the program run-time timer...\n\n\n")
    start = time.time()

        
    logger = template_py_Logger.Loggah(logfile=args.log_file or None, level=args.verbose)
        

    template_py_appmap = appmap.template_py_appmap( argv , logger )


    
    template_py_appmap.print_program_header()
    sys.stderr.write("Beginning program...\n")
    kmerdb_appmap.print_verbosity_header()
    
    if args.debug is True:
        args.func(args)
    else:
        logger.log_it("Running with error summary feature enabled, bypass with --debug for vague/invalid exceptions", "DEBUG")
        
        try:
            args.func(args)
            
            exit_code = 0

        except TypeError as e:
            
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 1
        
            raise e
        except ValueError as e:
        
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 2
        
            raise e
        except KeyError as e:
        
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 3
        
            raise e
        except RuntimeError as e:
        
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 4
        
            raise e
        except OSError as e:

            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 5
        
            raise e
        except IOError as e:
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 6
            raise e
        
        except ArgumentError as e:

            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 7
        
            raise e
        except AssertionError as e:

            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = 8
        
            raise e
        except FileNotFoundError as e:
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            
            exit_code = 9
            raise e
        except Exception as e:
            exit_summary = template_py_appmap.exit_gracefully(e , subcommand=subcommand_name, step=step, feature=feature, logs=logger.logs, n_logs=args.num_log_lines or None)
            exit_code = -1
        
            raise e
        finally:
            sys.stderr.write("Program ran for {0} seconds...\n\n\n".format(time.time() - start))
            sys.stderr.write(config.thanks)
            sys.stderr.write(config.DONE)
            sys.exit(exit_code)



    
