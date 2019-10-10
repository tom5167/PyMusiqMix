from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(381, 205)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(118, 50, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 50, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 90, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(118, 90, 111, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_4 = QtGui.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 90, 69, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 130, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.comboBox_5 = QtGui.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(118, 130, 111, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_6 = QtGui.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(20, 130, 69, 22))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 170, 111, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 170, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        self.comboBox_7 = QtGui.QComboBox(Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(20, 170, 81, 20))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))


        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 10, 75, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.clean)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def clean(self):
        user = ""
        with open("log.txt","r") as c:
            user = c.read()
        print user
        with open(user+".txt","a") as c:
            c.write(str(self.comboBox_2.currentIndex()))
            c.write(str(self.comboBox.currentIndex()))
            c.write(self.lineEdit.text()+"\n")
            self.lineEdit.setText("")

            c.write(str(self.comboBox_4.currentIndex()))
            c.write(str(self.comboBox_3.currentIndex()))
            c.write(self.lineEdit_2.text()+"\n")
            self.lineEdit_2.setText("")

            c.write(str(self.comboBox_6.currentIndex()))
            c.write(str(self.comboBox_5.currentIndex()))
            c.write(self.lineEdit_3.text()+"\n")
            self.lineEdit_3.setText("")

            c.write('3')
            c.write(str(self.comboBox_7.currentIndex()))
            c.write(self.lineEdit_4.text())
            self.lineEdit_4.setText("")
            c.write(self.lineEdit_5.text()+"\n")
            self.lineEdit_5.setText("")
        return
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Constraints", None))
        self.comboBox.setItemText(0, _translate("Dialog", "title", None))
        self.comboBox.setItemText(1, _translate("Dialog", "artist", None))
        self.comboBox.setItemText(2, _translate("Dialog", "album", None))
        self.comboBox.setItemText(3, _translate("Dialog", "year", None))
        self.comboBox.setItemText(4, _translate("Dialog", "genre", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "include", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "exclude", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "title", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "artist", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "album", None))
        self.comboBox_3.setItemText(3, _translate("Dialog", "year", None))
        self.comboBox_3.setItemText(4, _translate("Dialog", "genre", None))
        self.comboBox_4.setItemText(0, _translate("Dialog", "include", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "exclude", None))
        self.comboBox_5.setItemText(0, _translate("Dialog", "title", None))
        self.comboBox_5.setItemText(1, _translate("Dialog", "artist", None))
        self.comboBox_5.setItemText(2, _translate("Dialog", "album", None))
        self.comboBox_5.setItemText(3, _translate("Dialog", "year", None))
        self.comboBox_5.setItemText(4, _translate("Dialog", "genre", None))
        self.comboBox_6.setItemText(0, _translate("Dialog", "include", None))
        self.comboBox_6.setItemText(1, _translate("Dialog", "exclude", None))
        self.comboBox_7.setItemText(0, _translate("Dialog", "include year", None))
        self.comboBox_7.setItemText(1, _translate("Dialog", "exclude year", None))
        self.pushButton.setText(_translate("Dialog", "Save", None))
        
