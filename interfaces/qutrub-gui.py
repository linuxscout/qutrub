# -*- coding: utf-8 -*-
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui 

#import gui.qutrubgui as qutrubgui 
from gui.qutrubgui import *


import sys

app = QtGui.QApplication(sys.argv)

widget = QtGui.QMainWindow()
##widget.resize(250, 150)
widget.layoutDirection='RightToLeft';
widget.setWindowTitle('simple')
widget.show()

#w=qutrubgui.Ui_MainWindow();
w=Ui_MainWindow();
w.setupUi(widget);
##w.show();
sys.exit(app.exec_())
