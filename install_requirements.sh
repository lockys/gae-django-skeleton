#!/bin/bash

# install requirements separately to /libs
pip install -r requirements/local.txt -t ./libs

./project_name/lib.sh