#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qutrub_config.py
#  

#Database config directory
DB_BASE_PATH = "/var/www/html/qutrub/"
# Logging file
LOGGING_CFG_FILE = "/var/www/html/qutrub/config/logging.cfg"
LOGGING_FILE = "/var/www/html/qutrub/demo.log"
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
