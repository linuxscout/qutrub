# -*- coding: utf-8 -*-

import sys
import os
PWD = os.path.join(os.path.dirname(sys.argv[0]))
sys.path.append(os.path.join(PWD, '../support/'))
sys.path.append(os.path.join(PWD, '../'))

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui 

import gui.appgui as qutrubgui 
#from gui.qutrubgui import *
import libqutrub.verb_db as verb_db
verb_db.create_index_triverbtable()
import sys

app = QtGui.QApplication(sys.argv)

widget = QtGui.QMainWindow()
##widget.resize(250, 150)
widget.layoutDirection='RightToLeft';
widget.setWindowTitle('simple')
widget.show()

#w=qutrubgui.Ui_MainWindow();
w = qutrubgui.Ui_MainWindow();
w.setupUi(widget);
##w.show();
sys.exit(app.exec_())

