#!/bin/bash

# This script is required to create .tar.gz files that can be included in the site installation
# of the configurator module: $PATH_TO_VENV/lib/python3.12/site-packages/configurator
# These tar files are decompressed by the configurator and used to instantiate the templates.

# FastAPI template: removes node_modules and other junk
#rm -rf fastapi_template/{fastapi_template.egg-info,build,node_modules}
tar -zcvf configurator/fastapi_template.tar.gz fastapi_template

# template_py
tar -zcvf configurator/template_py.tar.gz template_py


