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
import shutil


#from multiprocessing import cpu_count

#from collections import OrderedDict


from configurator import logger as template_py_Logger
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

    
    if arguments.method not in config.subcommands:
        raise ValueError("unsupported method")
    elif arguments.method == "subcommand":
        template_py_appmap.subcommand_profile_header()

    sys.stderr.write("\n\nUse --help for expanded usage\n")

        


def subcommand(args):
    print("Full argparse argument object:")
    print(args)

    print("Hello, world!")
    print("I'm running 'template_py subcommand' with these arguments")


def cli_app(args):
    import tempfile
    import tarfile
    import shutil
    from configurator import util
    """
    Create source directory and destination directory references
    """

    template = os.path.join(os.path.dirname(__file__), "template_py.tar.gz")
    tempdir = tempfile.mkdtemp()
    with tarfile.open(template, 'r:gz') as tfile:
        tfile.extractall(tempdir)
    logger.log_it("Extracted tar contents to '{0}'".format(tempdir), "INFO")

    source_dir = os.path.join(tempdir, "template_py")
    
    if os.path.exists(args.project) and os.access(args.project, os.R_OK):
        raise ValueError("argument 'project' cannot point to an existing directory")

    dest_dir = args.project
    #dest_dir = os.path.join(".", args.project)
    
    try:
        
        util.copy_tree_with_replace(source_dir, args.project, "template_py", args.project)
    except FileExistsError as e:
        logger.log_it("An exception occurred while creating the CLI app at the destination directory '{0}'...".format(dest_dir), "ERROR")
        raise e
    except Exception as e:
        logger.log_it("An exception occurred while creating the CLI app at the destination directory '{0}'...".format(dest_dir), "ERROR")
        raise e

def fastapi_app(args):
    import tempfile
    import tarfile
    import shutil
    from configurator import util
    """
    Create source directory and destination directory references
    """

    template = os.path.join(os.path.dirname(__file__), "fastapi_template.tar.gz")
    tempdir = tempfile.mkdtemp()
    with tarfile.open(template, 'r:gz') as tfile:
        tfile.extractall(tempdir)
    logger.log_it("Extracted tar contents to '{0}'".format(tempdir), "INFO")

    source_dir = os.path.join(tempdir, "fastapi_template")
    
    if os.path.exists(args.project) and os.access(args.project, os.R_OK):
        raise ValueError("argument 'project' cannot point to an existing directory")

    dest_dir = args.project
    #dest_dir = os.path.join(".", args.project)
    
    try:
        
        util.copy_tree_with_replace(source_dir, args.project, "fastapi_template", args.project)
    except FileExistsError as e:
        logger.log_it("An exception occurred while creating the FastAPI app at the destination directory '{0}'...".format(dest_dir), "ERROR")
        raise e
    except Exception as e:
        logger.log_it("An exception occurred while creating the FastAPI app at the destination directory '{0}'...".format(dest_dir), "ERROR")
        raise e


def django_app(args):
    print("this will make a django app")

    
def cli():

    import sys

    from configurator import config, appmap


    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help="Use -h|--help with the individual subcommands, OR the 'usage' and 'help' subcommands to describe inputs, parameters, features, steps, etc.")


    cli_parser = subparsers.add_parser("cli", help="Create a new CLI")

    cli_parser.add_argument("-v", "--verbose", help="Prints warnings to the console by default", default=0, action="count")
    cli_parser.add_argument("--debug", action="store_true", default=False, help="Debug mode. Do not format errors and condense log")
    cli_parser.add_argument("-nl", "--num-log-lines", type=int, choices=config.default_logline_choices, default=50, help=argparse.SUPPRESS)
    cli_parser.add_argument("-l", "--log-file", type=str, default="configurator.log", help=argparse.SUPPRESS)
    cli_parser.add_argument("project", type=str,  help="The project-name for your new Python cli")
    cli_parser.set_defaults(func=cli_app)

    fastapi_parser = subparsers.add_parser("fastapi", help="Create a new Fastapi app")
    fastapi_parser.add_argument("-v", "--verbose", help="Prints warnings to the console by default", default=0, action="count")
    fastapi_parser.add_argument("--debug", action="store_true", default=False, help="Debug mode. Do not format errors and condense log")
    fastapi_parser.add_argument("-nl", "--num-log-lines", type=int, choices=config.default_logline_choices, default=50, help=argparse.SUPPRESS)
    fastapi_parser.add_argument("-l", "--log-file", type=str, default="configurator.log", help=argparse.SUPPRESS)
    fastapi_parser.add_argument("project", type=str, help="The project-name for your FastAPI app")
    fastapi_parser.set_defaults(func=fastapi_app)
    
    django_parser = subparsers.add_parser("django", help="Create a new Django app")
    django_parser.add_argument("-v", "--verbose", help="Prints warnings to the console by default", default=0, action="count")
    django_parser.add_argument("--debug", action="store_true", default=False, help="Debug mode. Do not format errors and condense log")
    django_parser.add_argument("-nl", "--num-log-lines", type=int, choices=config.default_logline_choices, default=50, help=argparse.SUPPRESS)
    django_parser.add_argument("-l", "--log-file", type=str, default="configurator.log", help=argparse.SUPPRESS)
    django_parser.add_argument("project", type=str,  help="The project-name for your new Django application")

    django_parser.set_defaults(func=django_app)



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

        
    logger = template_py_Logger.AppLogger(logfile=args.log_file or None, level=args.verbose)
        

    template_py_appmap = appmap.template_py_appmap( args , logger )


    
    template_py_appmap.print_program_header()
    sys.stderr.write("Beginning program...\n")
    template_py_appmap.print_verbosity_header()
    
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



    
