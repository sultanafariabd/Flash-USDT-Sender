#!/bin/bash

# This script obfuscates main.py using pyarmor.
# The output will be placed in the dist/ directory.

pyarmor gen main.py
