# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qutrubgui.ui'
#
# Created: Mon Sep 28 14:46:07 2009
#      by: PyQt5 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os
PWD = os.path.join(os.path.dirname(__file__))
#print PWD
sys.path.append(os.path.join(PWD, '../../support'))
sys.path.append(os.path.join(PWD, '../../'))

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtPrintSupport as QtPrintSupport
import PyQt5.QtWidgets as  QtWidgets
from libqutrub.verb_valid import is_valid_infinitive_verb
from .qutrub_rc import *
import pyarabic.araby as araby
import libqutrub.ar_verb as ar_verb
import libqutrub.verb_db as verb_db
import libqutrub.verb_const as verb_const
import libqutrub.classverb as verbclass
import libqutrub.mosaref_main as mosaref

from .setting import *

class Ui_MainWindow(object):
    font_base=None;
    font_result=None;
    result={}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        self.MainWindow=MainWindow;
        QtCore.QDir.setSearchPaths("res", [QtCore.QDir.currentPath()+"/gui",]);
        # kk in QtCore.QStringList(QtCore.QDir.currentPath()+"/gui"):
        #    print repr(kk)


        self.font_base=None;
        self.result={}
        self.SuggestedVerbList=[];
#-----------------------------------------------
        self.font_base = QtGui.QFont()
        self.font_base.setFamily("KacstOne")
        self.font_base.setPointSize(12)
        self.font_base.setBold(True)
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());
        self.BDictOption=1;


        RightToLeft=1;
        MainWindow.setLayoutDirection(RightToLeft)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")


        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setObjectName("Label")
        self.gridLayout_3.addWidget(self.Label, 1, 1, 1, 1)
        self.Label_2 = QtWidgets.QLabel(self.centralwidget)


        self.Label_2.setObjectName("Label_2")
        self.gridLayout_3.addWidget(self.Label_2, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")


        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")


        self.BPast = QtWidgets.QCheckBox(self.centralwidget)
        self.BPast.setEnabled(False)

        self.BPast.setFont(self.font_base)
        self.BPast.setChecked(True)
        self.BPast.setObjectName("BPast")
        self.gridLayout_5.addWidget(self.BPast, 3, 1, 1, 1)
        self.BFuture = QtWidgets.QCheckBox(self.centralwidget)
        self.BFuture.setEnabled(False)

        self.BFuture.setFont(self.font_base)
        self.BFuture.setChecked(True)
        self.BFuture.setObjectName("BFuture")
        self.gridLayout_5.addWidget(self.BFuture, 3, 2, 1, 1)
        self.BImperative = QtWidgets.QCheckBox(self.centralwidget)
        self.BImperative.setEnabled(False)

        self.BImperative.setFont(self.font_base)
        self.BImperative.setChecked(True)
        self.BImperative.setObjectName("BImperative")
        self.gridLayout_5.addWidget(self.BImperative, 3, 3, 1, 1)



        self.BPassive = QtWidgets.QCheckBox(self.centralwidget)
        self.BPassive.setEnabled(False)

        self.BPassive.setFont(self.font_base)
        self.BPassive.setChecked(True)
        self.BPassive.setObjectName("BPassive")
        self.gridLayout_5.addWidget(self.BPassive, 4, 1, 1, 1)


        self.Tverb = QtWidgets.QLineEdit(self.centralwidget)
        self.Tverb.setEnabled(True)
        self.Tverb.setMaximumSize(QtCore.QSize(200, 40))
        self.Tverb.setFont(self.font_result)

        self.Tverb.setObjectName("Tverb")
        self.gridLayout_5.addWidget(self.Tverb, 0, 0, 1, 1)
        self.gridLayout_5.setColumnStretch(0,3)


        self.CBSuggest = QtWidgets.QComboBox(self.centralwidget)
        self.CBSuggest.setFont(self.font_result)
        self.CBSuggest.setEditable(True)
        self.CBSuggest.setMaximumSize(QtCore.QSize(200, 40))
        self.CBSuggest.setObjectName("CBSuggest")
        self.CBSuggest.hide()

        self.gridLayout_5.addWidget(self.CBSuggest, 1,0, 1, 1)


        self.CBHarakaLabel = QtWidgets.QLabel(self.centralwidget)
        self.CBHarakaLabel.setObjectName("CBHarakaLabel")
        #self.CBHarakaLabel.setText(u"حركة عين الثلاثي في المضارع")
        self.CBHarakaLabel.setFont(self.font_base)
        self.CBHarakaLabel.hide()

        self.CBHaraka = QtWidgets.QComboBox(self.centralwidget)
        self.CBHaraka.setFont(self.font_result)
        self.CBHaraka.setEditable(True)
        self.CBHaraka.setMaximumSize(QtCore.QSize(200, 40))
        self.CBHaraka.setObjectName("CBHaraka")
        self.CBHaraka.addItem(u"فتحة")
        self.CBHaraka.addItem(u"ضمة")
        self.CBHaraka.addItem(u"كسرة")
        self.CBHaraka.setEnabled(False)
        self.CBHaraka.hide()
        self.formLayout_haraka = QtWidgets.QFormLayout()
        self.formLayout_haraka.setObjectName("formLayout_haraka")

        self.formLayout_haraka.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.CBHarakaLabel)
        self.formLayout_haraka.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CBHaraka)
        self.gridLayout_5.addLayout(self.formLayout_haraka, 1, 2, 1, 1)

        self.BFuture_moode = QtWidgets.QCheckBox(self.centralwidget)
        self.BFuture_moode.setEnabled(False)

        self.BFuture_moode.setFont(self.font_base)
        self.BFuture_moode.setChecked(True)
        self.BFuture_moode.setObjectName("BFuture_moode")
        self.gridLayout_5.addWidget(self.BFuture_moode, 4, 3, 1, 1)
        self.BConfirmed = QtWidgets.QCheckBox(self.centralwidget)
        self.BConfirmed.setEnabled(False)

        self.BConfirmed.setFont(self.font_base)
        self.BConfirmed.setChecked(True)
        self.BConfirmed.setObjectName("BConfirmed")
        self.gridLayout_5.addWidget(self.BConfirmed, 4, 2, 1, 1)

# a search on a Transitive
        self.BTransitive = QtWidgets.QCheckBox(self.centralwidget)
        self.BTransitive.setFont(self.font_base)
        self.BTransitive.setChecked(True)
        self.BTransitive.setObjectName("BTransitive")
        self.gridLayout_5.addWidget(self.BTransitive, 0, 3, 1, 1)
# a more optionss
        self.BMoreOptions = QtWidgets.QCheckBox(self.centralwidget)
        self.BMoreOptions.setFont(self.font_base)
        self.BMoreOptions.setChecked(False)
        self.BMoreOptions.setObjectName("BMoreOptions")
        #self.BMoreOptions.setText(u"خيارات")
        self.gridLayout_5.addWidget(self.BMoreOptions, 0, 4, 1, 1)
# a search on a dictionary options
        self.BDict = QtWidgets.QCheckBox(self.centralwidget)
        self.BDict.setFont(self.font_base)
        self.BDict.setChecked(self.BDictOption!=0)
        self.BDict.setObjectName("BDict")
        self.BDict.hide()
        #self.BDict.setText(u"البحث في المعجم")
        self.gridLayout_5.addWidget(self.BDict, 1, 3, 1, 1)

        self.BAll = QtWidgets.QCheckBox(self.centralwidget)
        self.BAll.setEnabled(True)

        self.BAll.setFont(self.font_base)
        self.BAll.setChecked(True)
        self.BAll.setTristate(False)
        self.BAll.setObjectName("BAll")
        self.gridLayout_5.addWidget(self.BAll, 0, 2, 1, 1)
        self.BConjugate = QtWidgets.QPushButton(self.centralwidget)

        self.BConjugate.setFont(self.font_base)
        self.BConjugate.setObjectName("BConjugate")
        self.gridLayout_5.addWidget(self.BConjugate, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.TabVoice = QtWidgets.QTabWidget(self.centralwidget)

        self.TabVoice.setFont(self.font_base)
        self.TabVoice.setObjectName("TabVoice")
        self.TabActiveVoice = QtWidgets.QWidget()
        self.TabActiveVoice.setObjectName("TabActiveVoice")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.TabActiveVoice)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TabActiveResult = QtWidgets.QTableWidget(self.TabActiveVoice)

        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.setColumnCount(12)
        self.TabActiveResult.setObjectName("TabActiveResult")
        self.TabActiveResult.setColumnCount(12)
        self.TabActiveResult.setRowCount(14)

        for i in range(14):
            emptyitem = QtWidgets.QTableWidgetItem()
            self.TabActiveResult.setVerticalHeaderItem(i,  emptyitem)
        for i in range(12):
            emptyitem = QtWidgets.QTableWidgetItem()
            self.TabActiveResult.setHorizontalHeaderItem(i,  emptyitem)

        self.gridLayout_2.addWidget(self.TabActiveResult, 0, 0, 1, 1)
        self.TabVoice.addTab(self.TabActiveVoice, "")

        self.TabPassiveVoice = QtWidgets.QWidget()

        self.gridLayout_2p = QtWidgets.QGridLayout(self.TabPassiveVoice)
        self.gridLayout_2p.setObjectName("gridLayout_2p")
        self.TabPassiveVoice.setObjectName("TabPassiveVoice")
        self.TabPassiveResult = QtWidgets.QTableWidget(self.TabPassiveVoice)

        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.setColumnCount(12)
        self.TabPassiveResult.setObjectName("TabPassiveResult")
        self.TabPassiveResult.setColumnCount(12)
        self.TabPassiveResult.setRowCount(14)
        for i in range(14):
            emptyitem = QtWidgets.QTableWidgetItem()
            self.TabPassiveResult.setVerticalHeaderItem(i,  emptyitem)
        for i in range(12):
            emptyitem = QtWidgets.QTableWidgetItem()
            self.TabPassiveResult.setHorizontalHeaderItem(i,  emptyitem)
        self.gridLayout_2p.addWidget(self.TabPassiveResult, 0, 0, 1, 1)

        self.TabVoice.addTab(self.TabPassiveVoice, "")
        self.gridLayout.addWidget(self.TabVoice, 1, 0, 1, 1)

#---------------------------------------
        self.TabVerbAttributs = QtWidgets.QWidget()

        self.gridLayout_vt = QtWidgets.QGridLayout(self.TabVerbAttributs)
        self.gridLayout_vt.setObjectName("gridLayout_vt")
        self.TabVerbAttributs.setObjectName("TabVerbAttributs")
        self.TabVerbAttributsResult = QtWidgets.QTableWidget(self.TabVerbAttributs)

        self.TabVerbAttributsResult.setFont(self.font_result)
        self.TabVerbAttributsResult.setColumnCount(1)
        self.TabVerbAttributsResult.setObjectName("TabVerbAttributsResult")
        self.TabVerbAttributsResult.setRowCount(5)
        emptyitem = QtWidgets.QTableWidgetItem()
        self.TabVerbAttributsResult.setHorizontalHeaderItem(0, emptyitem)
        self.gridLayout_vt.addWidget(self.TabVerbAttributsResult, 0, 0, 1, 1)

        self.TabVoice.addTab(self.TabVerbAttributs, "")
#---------------------------------------
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
# Menu Right to Left
        self.menu.setLayoutDirection(RightToLeft);
        self.menu_2.setLayoutDirection(RightToLeft);
        self.menu_3.setLayoutDirection(RightToLeft);
        self.menu_4.setLayoutDirection(RightToLeft);
        self.menu_5.setLayoutDirection(RightToLeft);

        MainWindow.setMenuBar(self.menubar)
#---------Actions
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.AExport = QtWidgets.QAction(MainWindow)
        self.AExport.setObjectName("AExport")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExport.setIcon(icon)
        self.AExit = QtWidgets.QAction(MainWindow)
        self.AExit.setObjectName("AExit")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExit.setIcon(icon)
        self.AFont = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("res:resources/images/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AFont.setIcon(icon)
        self.AFont.setObjectName("AFont")
        self.AAbout = QtWidgets.QAction(MainWindow)
        self.AAbout.setObjectName("AAbout")
        self.AManual = QtWidgets.QAction(MainWindow)
        self.AManual.setObjectName("AManual")
        self.ACopy = QtWidgets.QAction(MainWindow)
        self.ACopy.setObjectName("ACopy")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ACopy.setIcon(icon)
        self.AWhoisqutrub = QtWidgets.QAction(MainWindow)
        self.AWhoisqutrub.setObjectName("AWhoisqutrub")
        self.ASetting = QtWidgets.QAction(MainWindow)
        self.ASetting.setObjectName("ASetting")
        self.APrint = QtWidgets.QAction(MainWindow)
        self.APrint.setObjectName("APrint")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrint.setIcon(icon)
        self.APrintPreview = QtWidgets.QAction(MainWindow)
        self.APrintPreview.setObjectName("APrintPreview")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrintPreview.setIcon(icon)
        self.APagesetup = QtWidgets.QAction(MainWindow)
        self.APagesetup.setObjectName("APagesetup")
        self.AZoomIn = QtWidgets.QAction(MainWindow)
        self.AZoomIn.setObjectName("AZoomin")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AZoomIn.setIcon(icon)
        self.AZoomOut = QtWidgets.QAction(MainWindow)
        self.AZoomOut.setObjectName("AZoomOut")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AZoomOut.setIcon(icon)
#-------Menu--------------------
        self.menu.addAction(self.AExport)
#ToDo1
##        self.menu.addAction(self.APagesetup)
        self.menu.addSeparator()

        self.menu.addAction(self.APrint)

#ToDo1
##        self.menu.addAction(self.APrintPreview)
        self.menu.addAction(self.AExit)
        self.menu_2.addAction(self.AFont)
        self.menu_2.addAction(self.AZoomIn)
        self.menu_2.addAction(self.AZoomOut)
        self.menu_3.addAction(self.AAbout)
        self.menu_3.addAction(self.AManual)
        self.menu_3.addAction(self.AWhoisqutrub)
        self.menu_4.addAction(self.ACopy)
        self.menu_5.addAction(self.ASetting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.AFont)
        self.toolBar.addAction(self.ACopy)
        self.toolBar.addAction(self.AExport)
        self.toolBar.addAction(self.APrint)
#ToDo 2
##        self.toolBar.addAction(self.APrintPreview)
        self.toolBar.addAction(self.AZoomIn)
        self.toolBar.addAction(self.AZoomOut)

        self.TabVoice.setCurrentIndex(0)

        self.Tverb.setText(u"كَتَبَ");

        # ~ QtCore.QObject.connect(self.BConjugate, QtCore.SIGNAL("clicked()"), self.display_result)
        # ~ QtCore.QObject.connect(self.Tverb, QtCore.SIGNAL("textChanged(QString)"), self.validate_verb)
        # ~ QtCore.QObject.connect(self.BAll, QtCore.SIGNAL("clicked()"), self.check_alltenses)
        # ~ QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        # ~ QtCore.QObject.connect(self.APrint, QtCore.SIGNAL("triggered()"), self.print_result)
        # ~ QtCore.QObject.connect(self.APrintPreview, QtCore.SIGNAL("triggered()"), self.print_preview)
        # ~ QtCore.QObject.connect(self.AFont, QtCore.SIGNAL("triggered()"), self.change_font)
        # ~ QtCore.QObject.connect(self.AAbout, QtCore.SIGNAL("triggered()"), self.about)
        # ~ QtCore.QObject.connect(self.AWhoisqutrub, QtCore.SIGNAL("triggered()"), self.whoisqutrub)
        # ~ QtCore.QObject.connect(self.AManual, QtCore.SIGNAL("triggered()"), self.manual)
        # ~ QtCore.QObject.connect(self.AExport, QtCore.SIGNAL("triggered()"), self.save_result)
        # ~ QtCore.QObject.connect(self.AZoomIn, QtCore.SIGNAL("triggered()"), self.zoomin)
        # ~ QtCore.QObject.connect(self.AZoomOut, QtCore.SIGNAL("triggered()"), self.zoomout)
        # ~ QtCore.QObject.connect(self.BMoreOptions, QtCore.SIGNAL("clicked()"), self.show_options)
        # ~ QtCore.QObject.connect(self.ASetting, QtCore.SIGNAL("triggered()"), self.set_setting)
        # ~ QtCore.QObject.connect(self.APagesetup, QtCore.SIGNAL("triggered()"), self.page_setup)
        # ~ QtCore.QObject.connect(self.ACopy, QtCore.SIGNAL("triggered()"), self.set_copy)
        # ~ QtCore.QObject.connect(self.CBSuggest, QtCore.SIGNAL("activated(int)"), self.selectSuggest)

        self.BConjugate.clicked.connect(self.display_result)
        # ~ self.Tverb.textChanged(QString)"), self.validate_verb)

        self.Tverb.textChanged.connect(self.validate_verb)
        
        self.BAll.clicked.connect(self.check_alltenses)
        self.AExit.triggered.connect(MainWindow.close)
        self.APrint.triggered.connect(self.print_result)
        self.APrintPreview.triggered.connect(self.print_preview)
        self.AFont.triggered.connect(self.change_font)
        self.AAbout.triggered.connect(self.about)
        self.AWhoisqutrub.triggered.connect(self.whoisqutrub)
        self.AManual.triggered.connect(self.manual)
        self.AExport.triggered.connect(self.save_result)
        self.AZoomIn.triggered.connect(self.zoomin)
        self.AZoomOut.triggered.connect(self.zoomout)
        self.BMoreOptions.clicked.connect(self.show_options)
        self.ASetting.triggered.connect(self.set_setting)
        self.APagesetup.triggered.connect(self.page_setup)
        self.ACopy.triggered.connect(self.set_copy)
        # int
        self.CBSuggest.activated.connect(self.selectSuggest)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #---------

        self.BAll.setChecked(True);
        self.BFuture.setEnabled(False);
        self.BPast.setEnabled(False);
        self.BImperative.setEnabled(False);
        self.BPassive.setEnabled(False);
        self.BConfirmed.setEnabled(False);
        self.BFuture_moode.setEnabled(False);

        self.BFuture.hide();
        self.BPast.hide();
        self.BImperative.hide();
        self.BPassive.hide();
        self.BConfirmed.hide();
        self.BFuture_moode.hide();
# disable unallowed actions
        self.AExport.setEnabled(False)
        self.AFont.setEnabled(False)
        self.ACopy.setEnabled(False)
        self.APrint.setEnabled(False)
        self.APrintPreview.setEnabled(False)
        self.APagesetup.setEnabled(False)
        self.AZoomIn.setEnabled(False)
        self.AZoomOut.setEnabled(False)

        self.result={};
        self.TabVoice.hide();
        # ~ QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("toggled(bool)"), MainWindow.close)
        self.AExit.toggled.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.readSettings();
        self.applySettings();
        self.translator=QtCore.QTranslator();
        if not self.translator.load(self.getLanguageCode(), "gui/resources/languages/",'_.'):
        # if not self.translator.load(self.getLanguageCode(), "res:resources/languages"):
            print("failed loading"); 

        QtWidgets.QApplication.installTranslator(self.translator);
        self.retranslateUi(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:images/qaf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "قطرب: تصريف الأفعال العربية", None))
        self.Label.setText(QtWidgets.QApplication.translate("MainWindow", ",", None, ))
        self.Label_2.setText(QtWidgets.QApplication.translate("MainWindow", ",", None, ))
        self.BPast.setText(QtWidgets.QApplication.translate("MainWindow", "الماضي", None, ))
        self.BFuture.setText(QtWidgets.QApplication.translate("MainWindow", "المضارع", None, ))
        self.BImperative.setText(QtWidgets.QApplication.translate("MainWindow", "الأمر", None, ))
        self.BPassive.setText(QtWidgets.QApplication.translate("MainWindow", "المبني للمجهول", None, ))
        self.Tverb.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html dir=\'rtl\'>\n"
"<body>\n"
"<ol>\n"
"  <li>اكتب الفعل مشكولا شكلا تاما\n"
"(الحركات والشدة ) في خانة الفعل مثال\n"
":\n"
"كَتَبَ، كَاتَبَ. </li>\n"
"  <li>ملاحظة إذا كان الفعل مهموز\n"
"الأول على وزن فاعل،مثل آخى يرجى كتابته على الشكل ءَاخَى. </li>\n"
"  <li>إذا كان الفعل ثلاثيا حدد\n"
"حركة عين الفعل في المضارع، مثلا كتب يكتُب تأخذ الحركة ضمة في المضارع.\n"
"إذا كان الفعل غير ثلاثي، تجاهل هذه الميزة. </li>\n"
"  <li>حدد اللزوم والتعدي للفعل، </li>\n"
"  <li>اختر الزمن الذي تريد\n"
"التصريف فيه </li>\n"
"  <li>اضغط على \"صرّف الفعل\".</li>\n"
"</ol>\n"
"</body>", None, ))
        self.BFuture_moode.setText(QtWidgets.QApplication.translate("MainWindow", "المضارع المنصوب والمجزوم", None, ))
        self.BConfirmed.setText(QtWidgets.QApplication.translate("MainWindow", "المؤكد ", None, ))
        self.BTransitive.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">حدد اللزوم والتعدي للفعل</p></body></html>", None, ))
        self.BTransitive.setText(QtWidgets.QApplication.translate("MainWindow", "متعدي", None, ))
        self.BAll.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">اختر الزمن الذي تريد التصريف فيه</p></body></html>", None, ))
        self.BAll.setText(QtWidgets.QApplication.translate("MainWindow", "كل الأزمنة", None, ))
        self.BConjugate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">صرف الفعل</p></body></html>", None, ))
        self.BConjugate.setText(QtWidgets.QApplication.translate("MainWindow", "تصريف", None, ))
        self.CBHarakaLabel.setText(QtWidgets.QApplication.translate("MainWindow","حركة عين الثلاثي في المضارع", None, ))
        self.BMoreOptions.setText(QtWidgets.QApplication.translate("MainWindow","خيارات", None, ))
        self.BDict.setText(QtWidgets.QApplication.translate("MainWindow","البحث في المعجم", None, ))

        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabActiveVoice), QtWidgets.QApplication.translate("MainWindow", "المبني للمعلوم", None, ))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabPassiveVoice), QtWidgets.QApplication.translate("MainWindow", "المبني للمجهول", None, ))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabVerbAttributs), QtWidgets.QApplication.translate("MainWindow", "خصائص الفعل", None, ))
        self.TabVerbAttributsResult.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "القيمة", None, ))

        self.menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "ملف", None, ))
        self.menu_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "عرض", None, ))
        self.menu_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "مساعدة", None, ))
        self.menu_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "تحرير", None, ))
        self.menu_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "أدوات", None, ))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, ))
        self.AExport.setText(QtWidgets.QApplication.translate("MainWindow", "ت&صدير", None, ))
        self.AExit.setText(QtWidgets.QApplication.translate("MainWindow", "&خروج", None, ))
        self.AFont.setText(QtWidgets.QApplication.translate("MainWindow", "خط", None, ))

        self.AAbout.setText(QtWidgets.QApplication.translate("MainWindow", "حول البرنامج", None, ))
        self.AManual.setText(QtWidgets.QApplication.translate("MainWindow", "دليل الاستعمال", None, ))
        self.ACopy.setText(QtWidgets.QApplication.translate("MainWindow", "نسخ", None, ))
        self.AWhoisqutrub.setText(QtWidgets.QApplication.translate("MainWindow", "من هو قطرب؟", None, ))
        self.ASetting.setText(QtWidgets.QApplication.translate("MainWindow", "تفضيلات", None, ))
        self.APrint.setText(QtWidgets.QApplication.translate("MainWindow", "طباعة...", None, ))
        self.APrintPreview.setText(QtWidgets.QApplication.translate("MainWindow", "معاينة الطباعة", None, ))
        self.APagesetup.setText(QtWidgets.QApplication.translate("MainWindow", "إعداد الصفحة", None, ))
        self.AZoomIn.setText(QtWidgets.QApplication.translate("MainWindow", "تكبير", None, ))
        self.AZoomOut.setText(QtWidgets.QApplication.translate("MainWindow", "تصغير", None, ))

    def validate_verb(self):
        word = self.Tverb.text();
        self.CBHaraka.setEnabled(False);
        if word:

            word = word.strip(' ');
            if not araby.is_arabicword(word):

                QtWidgets.QToolTip.showText(self.Tverb.geometry().bottomRight(),
                            QtWidgets.QApplication.translate("MainWindow", "الفعل  غير صالح", None, ),self.Tverb)
                self.Tverb.setStyleSheet ("QLineEdit { color: red;}")


            else:
                self.CBHaraka.setEnabled(ar_verb.is_triliteral_verb(word));
                self.Tverb.setStyleSheet ("QLineEdit { color: black;}")
        else:
            self.Tverb.setStyleSheet ("QLineEdit { color: black;}")


    def check_alltenses(self):
        if self.BAll.checkState()!=0:
            check=True;
            self.BFuture.hide();
            self.BPast.hide();
            self.BImperative.hide();
            self.BPassive.hide();
            self.BConfirmed.hide();
            self.BFuture_moode.hide();
        else:
            check=False;
            self.BFuture.show();
            self.BPast.show();
            self.BImperative.show();
            self.BPassive.show();
            self.BConfirmed.show();
            self.BFuture_moode.show();

        self.BFuture.setEnabled(not check);
        self.BPast.setEnabled(not check);
        self.BImperative.setEnabled(not check);
        self.BPassive.setEnabled(not check);
        self.BConfirmed.setEnabled(not check);
        self.BFuture_moode.setEnabled(not check);

        self.BFuture.setChecked(check);
        self.BPast.setChecked(check);
        self.BImperative.setChecked(check);
        self.BPassive.setChecked(check);
        self.BConfirmed.setChecked(check);
        self.BFuture_moode.setChecked(check);

    def show_options(self):
        if self.BMoreOptions.checkState()!=0:
            self.CBHaraka.show();
            self.CBHarakaLabel.show();
            self.BDict.show();
        else:
            self.CBHaraka.hide();
            self.CBHarakaLabel.hide();
            self.BDict.hide();



    def change_font(self):
        newfont,ok = QtWidgets.QFontDialog.getFont(self.font_result);
        if ok:
            self.font_result=newfont;
            self.TabActiveResult.setFont(self.font_result)
            self.TabActiveResult.update();
            self.TabPassiveResult.setFont(self.font_result)
            self.TabPassiveResult.update();

    def zoomin(self):
        self.font_result.setPointSize(self.font_result.pointSize()+1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();
        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.update();

    def zoomout(self):
        self.font_result.setPointSize(self.font_result.pointSize()-1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();
        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.update();

    def set_copy(self):
        if "TEXT" in self.result:
            QtWidgets.QApplication.clipboard().setText(self.result["TEXT"])


    def page_setup(self):
        pass;
    def print_preview(self):
        if "HTML" in self.result:

            printer = QtPrintSupport.QPrinter()

            self.printpreview = QtPrintSupport.QPrintPreviewDialog(printer, self.centralwidget)
            # ~ QtCore.QObject.self.printpreview, QtCore.SIGNAL("paintRequested(QPrinter *)"), self.generate_preview)
            self.printpreview.paintRequested.connect(self.generate_preview)
            QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

            self.printpreview.exec_();
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                                QtWidgets.QApplication.translate("MainWindow", "لا شيء يمكن طبعه، صرّف أولا", None, ))

#ToDo 1
    def generate_preview(self,other):
        #print "working";

        asd=u"""<b>عربي</b>((self.ui.\ntextEdit.toPlainText())"""#.split('\n')
        document = QtGui.QTextDocument("")
        document.setHtml(self.result["TEXT"]);
        asd=document.toPlainText().split("\n");
        self.printpreview.autoFillBackground()
        painter = QtWidgets.QPainter()
        painter.setLayoutDirection(RightToLeft)
        painter.begin(other)
        x=0
        for s in asd:
            if x == 0:
                pass
            else:
                other.newPage()
            x=1
            painter.setFont(QtWidgets.QFont('Decorative', 25))       # change font
            painter.drawText(100,100,s)                    # printing point
        painter.end()
        return True;


        document = QtGui.QTextDocument("")
        self.result["HTML"]="u<html dir=rtl><body>"+self.result["HTML"]+"</body></html>"
        document.setHtml(self.result["HTML"]);
        printer = QtPrintSupport.QPrinter()

        self.printpreview.autoFillBackground()
        painter = QtWidgets.QPainter()
        painter.begin(printer)
        printer.newPage();

        painter.drawText(100,100,"document.toPlainText(")
        painter.end()


    def print_result(self):
        if "HTML" in self.result:
            data=QtCore.QFile("res:resources/style.css");
            if (data.open(QtCore.QFile.ReadOnly)):
                mySTYLE_SHEET=QtCore.QTextStream(data).readAll();
    ##            text=unicode(text);
            else:
                mySTYLE_SHEET=u"""
body {
    direction: rtl;
    font-family: Arial, "Times New Roman";
    font-size: 16pt;
}
"""
            document = QtGui.QTextDocument("")
            document.setDefaultStyleSheet(mySTYLE_SHEET)
            self.result["HTML"]=u"<html dir=rtl><body dir='rtl'>"+self.result["HTML"]+"</body></html>"
            document.setHtml(self.result["HTML"]);
            printer = QtPrintSupport.QPrinter()

            dlg = QtPrintSupport.QPrintDialog(printer, self.centralwidget)
            if dlg.exec_() != QtWidgets.QDialog.Accepted:
                return

            document.print_(printer)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                               QtWidgets.QApplication.translate("MainWindow", "لا شيء يمكن طبعه، صرّف أولا", None, ))


##    def set_setting(self):
##        QtWidgets.QMessageBox.warning(self.centralwidget,U"عذرا",
##                                u"غير متوفر حاليا")
    def set_setting(self):
        init_Dialog=QtWidgets.QDialog(self.centralwidget)
        Dialog=Ui_Dialog();
        Dialog.setupUi(init_Dialog);
        if init_Dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.readSettings();
            self.retranslateUi(self.MainWindow)
            self.applySettings();

    def readSettings(self):
        settings = QtCore.QSettings("Arabeyes.org", "Qutrub")
        family=settings.value("font_base_family", QtCore.QVariant("Traditional Arabic"))
        size= settings.value("font_base_size", 12);
        size = int(size)
        bold= settings.value("font_base_bold", True)
        bold = True if bold == "True" else False
        self.font_result.setFamily(family)
        self.font_result.setPointSize(size)
        self.font_result.setBold(bold)
        #read of dictsetting options
        dictsetting =settings.value("DictSetting", 1);
        # ~ if not ok:dictsetting=1;
        self.BDictOption = dictsetting;
        langindex = settings.value("Language", 1);
        # ~ if not ok:langindex=1;
        self.Language=langindex;
        #print self.Language        
    def applySettings(self):

        self.BDict.setChecked(self.BDictOption!=0)
        self.TabActiveResult.update();
        self.TabPassiveResult.update();
        self.retranslateUi(self.MainWindow)        

    def page_setup(self):
        QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "عذرا", None, ),
                                QtWidgets.QApplication.translate("MainWindow", "غير متوفر حاليا", None, ))

    def whoisqutrub(self):
        data=QtCore.QFile("res:resources/languages/"+self.getLanguageCode()+"/qutrub_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=QtWidgets.QApplication.translate("MainWindow", "لا يمكن فتح ملف المساعدة", None, )

        Dialog=QtWidgets.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", 'من هو قطرب؟', None, ))
        gridLayout = QtWidgets.QGridLayout(Dialog)
        gridLayout.setObjectName("gridLayout")
        textBrowser = QtWidgets.QTextBrowser(Dialog)
        textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(textBrowser, 0, 0, 1, 1)
        buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)
        buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        textBrowser.setText(text)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();

    def manual(self):
        data=QtCore.QFile("res:resources/languages/"+self.getLanguageCode()+"/help_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=QtWidgets.QApplication.translate("MainWindow", "لا يمكن فتح ملف المساعدة", None, )

        Dialog=QtWidgets.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "دليل الاستخدام", None, ))
        gridLayout = QtWidgets.QGridLayout(Dialog)
        gridLayout.setObjectName("gridLayout")
        textBrowser = QtWidgets.QTextBrowser(Dialog)
        textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(textBrowser, 0, 0, 1, 1)
        buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)


        buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        text2 = text
        #print type(text2)
        textBrowser.setText(text2)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();
    def about(self):
        RightToLeft=1;
        msgBox=QtWidgets.QMessageBox(self.centralwidget);
        msgBox.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "عن برنامج قطرب", None, ));
##          msgBox.setTextFormat(QrCore.QRichText);

        data=QtCore.QFile("res:resources/languages/"+self.getLanguageCode()+"/about.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text_about=textstream.readAll();
        else:
#            text=u"لا يمكن فتح ملف المساعدة"
            text_about=u"""<h1>فكرة</h1>
يقوم البرنامج
بتصريف الأفعال المدخلة مع بعض المعلومات
الضرورية لتوليد جميع أشكال التصريف في الأزمنة المختلفة.<br>
هدف البرنامج هو تمكين تصريف الأفعال العربية تصريفا آليا مبسطا.<br>
</p>
<b>موقع المشروع</b>
<a href="http://qutrub.arabeyes.org">http://qutrub.arabeyes.org</a><br>
<b>المطور </b>
<a href="mailto:taha_zerrouki@gawab.com">طه زروقي</a><br>
<hr/>
<h3>شكر خاص </h3>
<ul>
  <li>برمجة الويب :مصطفى عمارة  (<a href='http://moustafaemara.wordpress.com/'>moustafaemara.wordpress.com</a>) </li>
  <li>تصميم الشعار : عصام حمود (<a href="http://hamoudart.com/">hamoudart.com/</a>)</li>
<li>عيون العرب <a href='http://www.arabeyes.org'>arabeyes.org</a></li>
<li>التقنيين العرب <a href='http://www.arabtechies.net'>arabtechies.net</a></li>
</ul>

"""
        msgBox.setText(text_about);
        msgBox.setLayoutDirection(RightToLeft);
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok);
        msgBox.setIconPixmap(QtGui.QPixmap("res:resources/images/logo.png"));
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok);
        msgBox.exec_();
##          QtWidgets.QMessageBox.about(self.centralwidget,U"عن البرنامج",
##                                u"اسم ملف غير مناسب %s"%filename);
    def save_result(self):
        filename_tuple = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget,
        QtWidgets.QApplication.translate("MainWindow", "حفظ ملف", None, ),"untitled","HTML document (*.html *.htm);;Text file (*.txt);;Text Unicode comma separeted format file (*.csv);;XML file (*.xml);;TeX file (*.tex)");
        filename = filename_tuple[0]
        if filename:
            # ~ filename= str(filename)

            fields = filename.split(".");

            if len(fields)>=2:
                extention = fields.pop();
            else:
                extention="html";
                filename+="."+extention
            text=""

            if extention.lower() in ('html','tex','txt','xml','csv'):
                display_format=extention.upper();
            #Add text generation
                if not extention.upper() in self.result:
                    QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                               QtWidgets.QApplication.translate("MainWindow", "لا بيانات للتصدير، صرّف أولا", None, ))
                    return None;
                text+=self.result[extention.upper()];
            else:
                QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                               QtWidgets.QApplication.translate("MainWindow", "اسم ملف غير مناسب %s"%filename, None, ))
            try:
                file_saved=open(filename,'w+');
                if file_saved:
                    file_saved.write(text);
                    file_saved.flush();
                    file_saved.close();

                else:
                    QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                                QtWidgets.QApplication.translate("MainWindow", "لا يمكن فتح الملف %s"%filename, None, ))
            except:
                QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                                QtWidgets.QApplication.translate("MainWindow", "لا يمكن فتح الملف %s"%filename, None, ))
    def getLanguageCode(self,):
        languages={ 0:  "ar",  
 1:  "en",  
 2:  "de",  
 3:  "fr",  
 4:  "ur",  
 5:  "fa",  
 6:  "jp", 
 7:  "ms", }
 
        if self.Language in languages:
            return languages[self.Language];
        return "ar";
    def getLanguageFile(self,):
        langfile="language_ar.qm";
        languages={ 0:  "ar",  
 1:  "en",  
 2:  "de",  
 3:  "fr",  
 4:  "ur",  
 5:  "fa",  
 6:  "jp", }
        if self.Language in languages:
            langfile="language_"+languages[self.Language]+".qm";
            #print langfile
        return langfile;        

    def get_index_haraka(self,haraka):
        if haraka==u"فتحة":
            iharaka=0;
        elif haraka==u"ضمة":
            iharaka=1;
        elif haraka==u"كسرة":
            iharaka=2;
        else:
            iharaka=0;
        return iharaka;

    def selectSuggest(self):
        index=self.CBSuggest.currentIndex();
        if self.SuggestedVerbList!=None and len(self.SuggestedVerbList)>0:
            suggested_word=self.SuggestedVerbList[index]["verb"]
            suggested_haraka=self.SuggestedVerbList[index]["haraka"]
            suggested_transitive=self.SuggestedVerbList[index]["transitive"]
            self.Tverb.setText(suggested_word);
            self.CBHaraka.setCurrentIndex(self.get_index_haraka(suggested_haraka));
            self.display_result();


    def display_result(self):

        word = self.Tverb.text();
        if word:

            # ~ word=unicode(word);
            word = word.strip();
            if not is_valid_infinitive_verb(word):
                
                QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                            QtWidgets.QApplication.translate("MainWindow", "الفعل %1 غير صالح2", None, ).arg(word))
                self.Tverb.clear();
                self.Tverb.setFocus();

            else:
                #=u"فتحة"
                
                haraka= self.CBHaraka.currentText();
                display_format =  'CSV';
                all = (self.BAll.checkState()!=0)
                past = (self.BPast.checkState()!=0)
                future = (self.BFuture.checkState()!=0)
                imperative = (self.BImperative.checkState()!=0)
                passive = (self.BPassive.checkState()!=0)
                confirmed = (self.BConfirmed.checkState()!=0)
                future_moode = (self.BFuture_moode.checkState()!=0)
                transitive = (self.BTransitive.checkState()!=0)

                if (not all) and (not future) and (not past) and (not imperative) and (not passive) and (not future_moode) and (not confirmed) :
                    QtWidgets.QMessageBox.warning(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                           QtWidgets.QApplication.translate("MainWindow", "اختر زمنا واحدا على الأقل", None, ))
                else:

                # suggest is used to give more suggestion for triliteral verbs
                    suggest="";
                    self.CBSuggest.clear()
                    search_triverb_dict=(self.BDict.checkState()!=0)
                    if ar_verb.is_triliteral_verb(word) and search_triverb_dict:
            # search the future haraka for the triliteral verb
##                        db_base_path=os.path.join(_base_directory(req),"libqutrub/");
                        #db_base_path=".";
                        #liste_verb=find_triliteral_verb(db_base_path,word,haraka);
                        liste_verb= verb_db.find_alltriverb(word,haraka,True);
#                        for v in liste_verb:
#                            print liste_verb[0]['verb'].encode('utf8');
            # if there are more verb forms, select the first one
                        self.SuggestedVerbList=liste_verb;
                        if  liste_verb!=None and len(liste_verb)>0:
                            word=liste_verb[0]["verb"]
                            haraka=liste_verb[0]["haraka"]
                            transitive=liste_verb[0]["transitive"]
                            if len(liste_verb)>1:
                                suggest=u"هل تقصد؟<br/>"
                                self.CBSuggest.show()
##                                self.CBSuggestLabel.show()
            # the other forms are suggested

                            for i in range(0,len(liste_verb)):

                                suggested_word=liste_verb[i]["verb"]
                                suggested_haraka=liste_verb[i]["haraka"]
                                suggested_transitive=liste_verb[i]["transitive"]
                                future_form= mosaref.get_future_form(suggested_word,suggested_haraka);
            #                    display_format=display_format.decode("utf8");
                                #suggest=u"""<a href='?verb=%s&haraka=%s&transitive=%s&all=1&display_format=HTML'>%s %s</a><br/>"""%(suggested_word,suggested_haraka,suggested_transitive,suggested_word,future_form);
                                suggest=suggested_word+u"-"+future_form+u"(%s)"%suggested_haraka#+"[%s]"%suggested_transitive;
            # if the verb does'nt exist in the triliteral verb dictionary
            #            else:suggest=u"غير وارد في المعجم<br/>"
            #----------show suggest
                                self.CBSuggest.addItem(suggest)
                            self.CBSuggest.showPopup();
                        else:
                            if liste_verb==None:
                                QtWidgets.QMessageBox.critical(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                                u"مسار قاعدة البيانات غير صحيح %s"%db_base_path)
                                suggest=db_base_path
                            else:

                                QtWidgets.QMessageBox.critical(self.centralwidget,QtWidgets.QApplication.translate("MainWindow", "خطأ", None, ),
                                QtWidgets.QApplication.translate("MainWindow", "الفعل غير موجود في قائمة الأفعال الثلاثية", None, ))
                    else:
                        self.CBSuggest.hide();
                    self.CBHaraka.setCurrentIndex(self.get_index_haraka(haraka))
                    self.do_sarf(word,haraka,all,past,future,passive,imperative,future_moode,confirmed,transitive,"TABLE")
                    self.display_result_in_grid();


    def display_result_in_grid(self):
        rslt_tab = self.result["TABLE"];
        # display in grid
        self.TabActiveResult.clear();
        self.TabPassiveResult.clear();
        ##hide all columns
        for j in range(12):
            self.TabActiveResult.hideColumn(j)
            self.TabPassiveResult.hideColumn(j)
        # display tenses in columns labels
        for j in range(1,len(rslt_tab[0])):
            self.TabActiveResult.setHorizontalHeaderItem(j-1,QtWidgets.QTableWidgetItem(rslt_tab[0][j]))
            self.TabPassiveResult.setHorizontalHeaderItem(j-1,QtWidgets.QTableWidgetItem(rslt_tab[0][j]))
            if rslt_tab[0][j] in verb_const.TableIndicativeTense:
                self.TabActiveResult.showColumn(j-1)
                self.TabPassiveResult.hideColumn(j-1)
            else:
                self.TabActiveResult.hideColumn(j-1)
                self.TabPassiveResult.showColumn(j-1)

        ##        # display pronouns in rows labels
        for i in range(1,len(rslt_tab)):
            self.TabActiveResult.setVerticalHeaderItem(i-1,QtWidgets.QTableWidgetItem(rslt_tab[i][0]))
            self.TabPassiveResult.setVerticalHeaderItem(i-1,QtWidgets.QTableWidgetItem(rslt_tab[i][0]))
        for i in range(1,15):
          for j in range(1,len(rslt_tab[i])):
                self.TabActiveResult.setItem(i-1,j-1,QtWidgets.QTableWidgetItem(rslt_tab[i][j]))
                self.TabPassiveResult.setItem(i-1,j-1,QtWidgets.QTableWidgetItem(rslt_tab[i][j]))
        # resize cells to content
        self.TabActiveResult.resizeColumnsToContents();
        self.TabActiveResult.resizeRowsToContents();
        self.TabPassiveResult.resizeColumnsToContents();
        self.TabPassiveResult.resizeRowsToContents();

        #---------display verb attributs
        verbattributs=self.verb_attribut;
        # display in grid
        self.TabVerbAttributsResult.clear();
        ##hide all columns

        # display tenses in columns labels
        j=0;
        for key in verbattributs.keys():
            self.TabVerbAttributsResult.setVerticalHeaderItem(j,QtWidgets.QTableWidgetItem(key));
            self.TabVerbAttributsResult.setItem(j,0,QtWidgets.QTableWidgetItem(verbattributs[key]))
            j+=1;

        self.TabVerbAttributsResult.resizeColumnsToContents();
        self.TabVerbAttributsResult.resizeRowsToContents();

        #show result /
        self.TabVoice.show();
        self.MainWindow.showMaximized();
        self.TabVoice.setCurrentIndex(0);
        self.centralwidget.update();

# enable actions
        self.AExport.setEnabled(True)
        self.AFont.setEnabled(True)
        self.ACopy.setEnabled(True)
        self.APrint.setEnabled(True)
        self.APrintPreview.setEnabled(True)
        self.APagesetup.setEnabled(True)
        self.AZoomIn.setEnabled(True)
        self.AZoomOut.setEnabled(True)
        self.centralwidget.update();


    def do_sarf(self,word,future_type,all=True,past=False,future=False,passive=False,imperative=False,future_moode=False,confirmed=False,transitive=False,display_format="HTML"):
        valid=is_valid_infinitive_verb(word)
        listetenses=[];
        if valid:
            future_type= ar_verb.get_future_type_by_name(future_type);
            bab_sarf=0;
            vb=verbclass.VerbClass(word,transitive,future_type);
            #vb.verb_class();
            vb.set_display(display_format);
        #test the uniformate function
            if all :
                if transitive :
##                    print "transitive";
                    listetenses= verb_const.TABLE_TENSE
                    result= vb.conjugate_all_tenses();
                else:
##                    print "intransitive";
                    listetenses = verb_const.TableIndicativeTense;
##                    print len(TableIndicativeTense)
                    result= vb.conjugate_all_tenses(listetenses);
            else :
                listetenses=[];
                if past : listetenses.append(verb_const.TensePast);
                if (past and passive and transitive) : listetenses.append(verb_const.TensePassivePast)
                if future : listetenses.append(verb_const.TenseFuture);
                if (future and passive and transitive) : listetenses.append(verb_const.TensePassiveFuture)
                if (future_moode) :
                    listetenses.append(verb_const.TenseSubjunctiveFuture)
                    listetenses.append(verb_const.TenseJussiveFuture)
                if (confirmed) :
                    if (future):listetenses.append(verb_const.TenseConfirmedFuture);
                    if (imperative):listetenses.append(verb_const.TenseConfirmedImperative);
                if (future and passive and transitive and confirmed) :
                    listetenses.append(verb_const.TensePassiveConfirmedFuture);
                if (passive and transitive and future_moode) :
                    listetenses.append(verb_const.TensePassiveSubjunctiveFuture)
                    listetenses.append(verb_const.TensePassiveJussiveFuture)
                if imperative : listetenses.append(verb_const.TenseImperative)
                result =vb.conjugate_all_tenses(listetenses);


            self.result["HTML"]=vb.conj_display.display("HTML",listetenses)
            self.result["TABLE"]=vb.conj_display.display("TABLE",listetenses)
            self.result["TEXT"]=vb.conj_display.display("TEXT",listetenses)
            self.result["TEX"]=vb.conj_display.display("TEX",listetenses)
            self.result["CSV"]=vb.conj_display.display("CSV",listetenses)
            self.result["XML"]=vb.conj_display.display("XML",listetenses)
            self.verb_attribut=vb.conj_display.get_verb_attributs();

            return result;
        else: return None;


from . import qutrub_rc
