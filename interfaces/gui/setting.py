# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created: Fri Oct 02 19:27:28 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

RightToLeft=1;
DefaultFont = QtGui.QFont()
DefaultFont.setFamily("Arial")
DefaultFont.setPointSize(24)
DefaultFont.setBold(True)
CurrentLanguage="ar";

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());

        self.Dialog=Dialog;

        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 202)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.SettingFontResultLabel = QtWidgets.QLabel(Dialog)
        self.SettingFontResultLabel.setObjectName("SettingFontResultLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.SettingFontResultLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TSettingFontResult = QtWidgets.QLineEdit(Dialog)
        self.TSettingFontResult.setObjectName("TSettingFontResult")
        self.horizontalLayout.addWidget(self.TSettingFontResult)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BModifyFontResult = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BModifyFontResult.sizePolicy().hasHeightForWidth())
        self.BModifyFontResult.setSizePolicy(sizePolicy)
        self.BModifyFontResult.setObjectName("BModifyFontResult")
        self.horizontalLayout_2.addWidget(self.BModifyFontResult)
        self.BFontResultDefault = QtWidgets.QPushButton(Dialog)
        self.BFontResultDefault.setObjectName("BFontResultDefault")
        self.horizontalLayout_2.addWidget(self.BFontResultDefault)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.CBLanguageLabel = QtWidgets.QLabel(Dialog)
        self.CBLanguageLabel.setObjectName("CBLanguageLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CBLanguageLabel)
        self.CBLanguage = QtWidgets.QComboBox(Dialog)
        self.CBLanguage.setEnabled(True)
        self.CBLanguage.setObjectName("CBLanguage")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.CBLanguage.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CBLanguage)
        self.BDictSetting = QtWidgets.QCheckBox(Dialog)
        self.BDictSetting.setChecked(True)
        self.BDictSetting.setObjectName("BDictSetting")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BDictSetting)
        self.BHarakatColor = QtWidgets.QCheckBox(Dialog)
        self.BHarakatColor.setEnabled(False)
        self.BHarakatColor.setChecked(False)
        self.BHarakatColor.setObjectName("BHarakatColor")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.BHarakatColor)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        # ~ QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        # ~ QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.Dialog.reject)
        # ~ QtCore.QObject.connect(self.BModifyFontResult, QtCore.SIGNAL("clicked()"),self.change_font)
        # ~ QtCore.QObject.connect(self.BFontResultDefault, QtCore.SIGNAL("clicked()"),self.restore_default_font)
        # ~ QtCore.QObject.connect(self.CBLanguage, QtCore.SIGNAL("activated(int)"), self.selectLanguage)       
        # ~ QtCore.QObject.connect(self.BDictSetting, QtCore.SIGNAL("stateChanged(int)"), self.setDictSetting)
        self.buttonBox.accepted.connect( self.accept)
        self.buttonBox.rejected.connect( self.Dialog.reject)
        self.BModifyFontResult.clicked.connect(self.change_font)
        self.BFontResultDefault.clicked.connect(self.restore_default_font)
        # ~ self.CBLanguage.activated(int)"), self.selectLanguage)       
        self.CBLanguage.activated.connect(self.selectLanguage)       
        # ~ self.BDictSetting.stateChanged(int)"), self.setDictSetting)
        self.BDictSetting.stateChanged.connect( self.setDictSetting)        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
# execution
        fonttext=self.font_result.family()+"[%s]"%str(self.font_result.pointSize())
        self.TSettingFontResult.setText(fonttext)
        Dialog.setLayoutDirection(RightToLeft);
# readSetting
        self.readSettings();
        self.set_font_box();

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "تفضيلات"))
        self.SettingFontResultLabel.setText(QtWidgets.QApplication.translate("Dialog", "خط عرض النتائج"))
        self.BModifyFontResult.setText(QtWidgets.QApplication.translate("Dialog", "تعديل", ))
        self.BFontResultDefault.setText(QtWidgets.QApplication.translate("Dialog", "استعادة الخط الافتراضي", ))
        # the langauge application label  must be in english
        self.CBLanguageLabel.setText("Language")
        self.CBLanguage.setItemText(0, QtWidgets.QApplication.translate("Dialog", "العربية", ))
        self.CBLanguage.setItemText(1, QtWidgets.QApplication.translate("Dialog", "English", ))
        self.CBLanguage.setItemText(2, QtWidgets.QApplication.translate("Dialog", "Deutch", ))
        self.CBLanguage.setItemText(3, QtWidgets.QApplication.translate("Dialog", "Français", ))
        self.CBLanguage.setItemText(4, QtWidgets.QApplication.translate("Dialog", "أردو", ))
        self.CBLanguage.setItemText(5, QtWidgets.QApplication.translate("Dialog", "فارسي", ))
        self.CBLanguage.setItemText(6, QtWidgets.QApplication.translate("Dialog", "Japanese", ))
        self.CBLanguage.setItemText(7, QtWidgets.QApplication.translate("Dialog", "Malay", ))       
        self.BDictSetting.setText(QtWidgets.QApplication.translate("Dialog", "البحث دائما في معجم الأفعال الثلاثية", ))
        self.BHarakatColor.setText(QtWidgets.QApplication.translate("Dialog", "إظهار علامات التشكيل بلون مختلف", ))


    def change_font(self):
        newfont,ok = QtWidgets.QFontDialog.getFont(self.font_result);
        if ok:
            self.font_result=newfont;
            self.set_font_box();

    def readSettings(self):
        settings = QtCore.QSettings("Arabeyes.org", "Qutrub")
        family=settings.value("font_base_family", QtCore.QVariant("Traditional Arabic"))
        size =settings.value("font_base_size", QtCore.QVariant(12));
        size = int(size)
        bold = settings.value("font_base_bold", QtCore.QVariant(True))
        bold = True if bold == "True" else False
        self.font_result.setFamily(family)
        self.font_result.setPointSize(size)
        self.font_result.setBold(bold)
        #read of dictsetting options
        dictsetting=settings.value("DictSetting", QtCore.QVariant(1));
        # ~ if not ok:dictsetting=1;
        dictsetting = int(dictsetting)
        self.BDictSetting.setCheckState(dictsetting);

        langindex=settings.value("Language", QtCore.QVariant(0));
        # ~ if not ok:langindex=0;
        langindex=int(langindex);
        self.CBLanguage.setCurrentIndex(langindex);


    def writeSettings(self):
        settings = QtCore.QSettings("Arabeyes.org", "Qutrub")
        settings.setValue("font_base_family", QtCore.QVariant(self.font_result.family()))
        settings.setValue("font_base_size", QtCore.QVariant(self.font_result.pointSize()))
        settings.setValue("font_base_bold", QtCore.QVariant(self.font_result.bold()))
        #write of dictsetting options
        settings.setValue("DictSetting", QtCore.QVariant(self.BDictSetting.checkState()));
        settings.setValue("Language", QtCore.QVariant(self.CBLanguage.currentIndex()));

    def restore_default_font(self):
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());
        self.set_font_box();

    def set_font_box(self):
        fonttext=self.font_result.family()+"[%s]"%str(self.font_result.pointSize())
        self.TSettingFontResult.setText(fonttext)

    def selectLanguage(self):
        index=self.CBLanguage.currentIndex();
        self.CBLanguage.setCurrentIndex(index);
        languages={ 0:  "ar",  
 1:  "en",  
 2:  "de",  
 3:  "fr",  
 4:  "ur",  
 5:  "fa",  
 6:  "jp", 
 7:  "ms",}
        if index in languages:
            CurrentLanguage=languages[index];
            print(CurrentLanguage);

    def setDictSetting(self):
        self.DictSetting=(self.BDictSetting.checkState()!=0)

    def accept(self):
        self.writeSettings();
        self.Dialog.accept();

