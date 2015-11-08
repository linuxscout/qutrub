# -*- coding: utf-8 -*-

from qutrubgui import *


import sys

app = QtGui.QApplication(sys.argv)

widget = QtGui.QMainWindow()
##widget.resize(250, 150)
widget.layoutDirection='RightToLeft';
widget.setWindowTitle('simple')
widget.show()

w=Ui_MainWindow();
w.setupUi(widget);
##w.show();
sys.exit(app.exec_())