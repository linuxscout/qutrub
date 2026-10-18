#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qutrub_config.py
#  

import os

# Base directory of the project (parent of this config/ directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Database config directory
DB_BASE_PATH = BASE_DIR + os.sep
# Logging file
LOGGING_CFG_FILE = os.path.join(BASE_DIR, "config", "logging.cfg")
LOGGING_FILE = os.path.join(BASE_DIR, "demo.log")
# in developement True in production False
MODE_DEBUG = True
# ~ MODE_DEBUG = False
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
