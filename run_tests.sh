#!/usr/bin/env bash
PYTHONPATH=./src:PYTHONPATH python -m unittest discover -s test -p '*.py'
