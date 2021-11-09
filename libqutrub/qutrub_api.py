#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qutrub_api.py
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
import libqutrub.conjugator
class QutrubApi:
    """
    a class as conjugator 
    """
    def __init__(self,):
        """
        init qutrub api
        """
        self.db_path = "."
        self.display_format = "HTML"
    
    def set_db_path(self, db_path):
        """
        set the db path
        """
        self.db_path = db_path
    def set_display_format(self, display_format):
        """
        set the db path
        """
        self.db_path = db_path
        
    def conjugate(word, future_type, alltense = True, past = False, future = False, 
passive = False, imperative = False, future_moode = False, confirmed = False,
 transitive = False):
        """
        conjugate verb
        """
        return conjugator.conjugate(word, future_type, 
            alltense, past, future, passive, imperative, future_moode, confirmed,
            transitive, 
            self.display_format,
            )
    
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
