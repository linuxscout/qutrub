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
import pyarabic.araby as araby
import sys
sys.path.append("../")
import core.qutrub_api

DATAFILE = "../data/verbsarfiabase.csv"
class converter():
    """ a class to convert basic data into specific data table"""
    def __init__(self, datafile=DATAFILE):
        """
        """
        self.datafile = datafile
        self.conjugator = core.qutrub_api.QutrubApi()
        
    def load(self, datafile=False):
        """
        load verb file
        """
        if not datafile:
            # if not datafile given load the defaul one, or previous datafile
            datafile = self.datafile
        else:
            self.datafile = datafile
        self.df = pd.read_csv(datafile,comment='#', encoding="utf8", delimiter="\t")
        print(self.df.head())
    def convert(self,):
        """
        Convert loaded file
        """
        # create unvocalized column
        self.df["unvocalized"] = self.df["verb"].apply(lambda x: araby.strip_tashkeel(x))
        self.df["unmarked"] = self.df["verb"].apply(lambda x: araby.strip_harakat(x))
        self.df["normalized"] = self.df["unvocalized"].apply(lambda x: araby.normalize_hamza(x))
        self.df["stamp"] = self.df["unvocalized"].apply(lambda x: self.conjugator.verb_stamp(x))
        # the length is made with counting Shadda and normializing hamza"
        self.df["length"] = self.df["unmarked"].apply(lambda x: len(araby.normalize_hamza(x)))
        
        #verb features
        
        self.df["salim"] = self.df["verb"].apply(lambda x: self.get_info(x).get("سالم"))
        self.df["weak"] = self.df["verb"].apply(lambda x: self.get_info(x).get("علة"))
        self.df["url"] = self.df["unmarked"].apply(lambda x: "http://qutrub.arabeyes.org/verb/%s"%x)
        
        
    def get_info(self, verb):
        """
        extract fearures from verb
        """
        features = self.conjugator.get_verb_info(verb, future_type="فتحة", transitive=True)
        # ~ print(verb)
        # ~ return repr(features)
        return features
        
        
    def dump(self, outfile):
        """
        
        """
        self.df.to_csv(outfile, encoding="utf8", sep="\t")
        

     
        
def main(args):
    conv = converter()
    conv.load()
    print("***********loading-----------------")
    print(conv.df.head())
    conv.convert()
    print(">>>>>>>> Output -------------------")    
    print(conv.df.head())
    conv.dump("temp.csv")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
