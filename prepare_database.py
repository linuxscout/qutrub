#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prepare_database.py
#  
#  Copyright 2021 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pandas as pd

DATAFILE = "../data/verbsarfiabase.csv"
class converter():
    """ a class to convert basic data into specific data table"""
    def __init__(self, datafile=DATAFILE):
        """
        """
        self.datafile = datafile
        
    def load(self, datafile=False):
        """
        load verb file
        """
        if not datafile:
            # if not datafile given load the defaul one, or previous datafile
            datafile = self.datafile
        else:
            self.datafile = datafile
        self.dataframe = pd.read_csv(datafile, encoding="utf8")
        self.datafram.head()
        
        
        
def main(args):
    conv = converter()
    conv.load()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
