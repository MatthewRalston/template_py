#!/bin/bash

rm -rf fastapi_template/{fastapi_template.egg-info,build,node_modules}
tar -zcvf configurator/fastapi_template.tar.gz fastapi_template
