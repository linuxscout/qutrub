# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created: Fri Oct 02 19:27:28 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

RightToLeft=1;
DefaultFont = QtGui.QFont()
DefaultFont.setFamily("Traditional Arabic")
DefaultFont.setPointSize(24)
DefaultFont.setBold(True)
CurrentLanguage="ar";

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());

        self.Dialog=Dialog;

        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 202)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.SettingFontResultLabel = QtGui.QLabel(Dialog)
        self.SettingFontResultLabel.setObjectName("SettingFontResultLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.SettingFontResultLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TSettingFontResult = QtGui.QLineEdit(Dialog)
        self.TSettingFontResult.setObjectName("TSettingFontResult")
        self.horizontalLayout.addWidget(self.TSettingFontResult)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BModifyFontResult = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BModifyFontResult.sizePolicy().hasHeightForWidth())
        self.BModifyFontResult.setSizePolicy(sizePolicy)
        self.BModifyFontResult.setObjectName("BModifyFontResult")
        self.horizontalLayout_2.addWidget(self.BModifyFontResult)
        self.BFontResultDefault = QtGui.QPushButton(Dialog)
        self.BFontResultDefault.setObjectName("BFontResultDefault")
        self.horizontalLayout_2.addWidget(self.BFontResultDefault)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.CBLanguageLabel = QtGui.QLabel(Dialog)
        self.CBLanguageLabel.setObjectName("CBLanguageLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.CBLanguageLabel)
        self.CBLanguage = QtGui.QComboBox(Dialog)
        self.CBLanguage.setEnabled(True)
        self.CBLanguage.setObjectName("CBLanguage")
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.CBLanguage)
        self.BDictSetting = QtGui.QCheckBox(Dialog)
        self.BDictSetting.setChecked(True)
        self.BDictSetting.setObjectName("BDictSetting")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.BDictSetting)
        self.BHarakatColor = QtGui.QCheckBox(Dialog)
        self.BHarakatColor.setEnabled(False)
        self.BHarakatColor.setChecked(False)
        self.BHarakatColor.setObjectName("BHarakatColor")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.BHarakatColor)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.Dialog.reject)
        QtCore.QObject.connect(self.BModifyFontResult, QtCore.SIGNAL("clicked()"),self.change_font)
        QtCore.QObject.connect(self.BFontResultDefault, QtCore.SIGNAL("clicked()"),self.restore_default_font)
        QtCore.QObject.connect(self.CBLanguage, QtCore.SIGNAL("activated(int)"), self.selectLanguage)		
        QtCore.QObject.connect(self.BDictSetting, QtCore.SIGNAL("stateChanged(int)"), self.setDictSetting)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
# execution
        fonttext=self.font_result.family()+"[%s]"%str(self.font_result.pointSize())
        self.TSettingFontResult.setText(fonttext)
        Dialog.setLayoutDirection(RightToLeft);
# readSetting
        self.readSettings();
        self.set_font_box();

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "تفضيلات", None, QtGui.QApplication.UnicodeUTF8))
        self.SettingFontResultLabel.setText(QtGui.QApplication.translate("Dialog", "خط عرض النتائج", None, QtGui.QApplication.UnicodeUTF8))
        self.BModifyFontResult.setText(QtGui.QApplication.translate("Dialog", "تعديل", None, QtGui.QApplication.UnicodeUTF8))
        self.BFontResultDefault.setText(QtGui.QApplication.translate("Dialog", "استعادة الخط الافتراضي", None, QtGui.QApplication.UnicodeUTF8))
        # the langauge application label  must be in english
        self.CBLanguageLabel.setText("Language")
        self.CBLanguage.setItemText(0, QtGui.QApplication.translate("Dialog", "العربية", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(1, QtGui.QApplication.translate("Dialog", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(2, QtGui.QApplication.translate("Dialog", "Deutch", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(3, QtGui.QApplication.translate("Dialog", "Français", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(4, QtGui.QApplication.translate("Dialog", "أردو", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(5, QtGui.QApplication.translate("Dialog", "فارسي", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(6, QtGui.QApplication.translate("Dialog", "Japanese", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(7, QtGui.QApplication.translate("Dialog", "Malay", None, QtGui.QApplication.UnicodeUTF8))		
        self.BDictSetting.setText(QtGui.QApplication.translate("Dialog", "البحث دائما في معجم الأفعال الثلاثية", None, QtGui.QApplication.UnicodeUTF8))
        self.BHarakatColor.setText(QtGui.QApplication.translate("Dialog", "إظهار علامات التشكيل بلون مختلف", None, QtGui.QApplication.UnicodeUTF8))


    def change_font(self):
        newfont,ok = QtGui.QFontDialog.getFont(self.font_result);
        if ok:
            self.font_result=newfont;
            self.set_font_box();

    def readSettings(self):
        settings = QtCore.QSettings("Arabeyes.org", "Qutrub")
        family=settings.value("font_base_family", QtCore.QVariant(QtCore.QString("Traditional Arabic"))).toString()
        size,ok=settings.value("font_base_size", QtCore.QVariant(12)).toInt();
        if not ok:size=12;
        bold=settings.value("font_base_bold", QtCore.QVariant(True)).toBool()
        self.font_result.setFamily(family)
        self.font_result.setPointSize(size)
        self.font_result.setBold(bold)
        #read of dictsetting options
        dictsetting,ok=settings.value("DictSetting", QtCore.QVariant(1)).toInt();
        if not ok:dictsetting=1;
        self.BDictSetting.setCheckState(dictsetting);

        langindex,ok=settings.value("Language", QtCore.QVariant(0)).toInt();
        if not ok:langindex=0;
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
        if languages.has_key(index):
        	CurrentLanguage=languages[index];
        	print CurrentLanguage;

    def setDictSetting(self):
        self.DictSetting=(self.BDictSetting.checkState()!=0)

    def accept(self):
        self.writeSettings();
        self.Dialog.accept();

