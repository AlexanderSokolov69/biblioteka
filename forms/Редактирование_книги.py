# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Редактирование_книги.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookWindow(object):
    def setupUi(self, BookWindow):
        BookWindow.setObjectName("BookWindow")
        BookWindow.resize(530, 414)
        self.frame = QtWidgets.QFrame(BookWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 511, 391))
        self.frame.setStyleSheet("background-color:rgb(170, 255, 127);\n"
"color: rgb(7, 0, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 3, 16);")
        self.label.setObjectName("label")
        self.lineEdit_code = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_code.setGeometry(QtCore.QRect(10, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_code.setFont(font)
        self.lineEdit_code.setText("")
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_name.setGeometry(QtCore.QRect(270, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_autor = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_autor.setGeometry(QtCore.QRect(10, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_autor.setFont(font)
        self.lineEdit_autor.setText("")
        self.lineEdit_autor.setObjectName("lineEdit_autor")
        self.lineEdit_source = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_source.setGeometry(QtCore.QRect(270, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_source.setFont(font)
        self.lineEdit_source.setText("")
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.lineEdit_limit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_limit.setGeometry(QtCore.QRect(10, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_limit.setFont(font)
        self.lineEdit_limit.setText("")
        self.lineEdit_limit.setObjectName("lineEdit_limit")
        self.lineEdit_cat = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cat.setGeometry(QtCore.QRect(270, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_cat.setFont(font)
        self.lineEdit_cat.setText("")
        self.lineEdit_cat.setObjectName("lineEdit_cat")
        self.lineEdit_comment = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_comment.setGeometry(QtCore.QRect(30, 270, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_comment.setFont(font)
        self.lineEdit_comment.setText("")
        self.lineEdit_comment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 4, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 211, 16))
        self.label_2.setStyleSheet("color: rgb(255, 0, 8);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 211, 16))
        self.label_3.setStyleSheet("color: rgb(255, 0, 8);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 211, 16))
        self.label_4.setStyleSheet("color: rgb(255, 16, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 211, 16))
        self.label_5.setStyleSheet("color: rgb(255, 16, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(280, 50, 211, 16))
        self.label_6.setStyleSheet("color: rgb(255, 16, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(280, 120, 211, 16))
        self.label_7.setStyleSheet("color: rgb(255, 16, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(280, 190, 211, 16))
        self.label_8.setStyleSheet("color: rgb(255, 16, 0);")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(BookWindow)
        QtCore.QMetaObject.connectSlotsByName(BookWindow)

    def retranslateUi(self, BookWindow):
        _translate = QtCore.QCoreApplication.translate
        BookWindow.setWindowTitle(_translate("BookWindow", "Редактирование_книги"))
        self.label.setText(_translate("BookWindow", "Редактирование"))
        self.pushButton.setText(_translate("BookWindow", "Сохранить"))
        self.label_2.setText(_translate("BookWindow", "Код книги:"))
        self.label_3.setText(_translate("BookWindow", "Автор:"))
        self.label_4.setText(_translate("BookWindow", "Возрастное ограничение:"))
        self.label_5.setText(_translate("BookWindow", "Аннотация:"))
        self.label_6.setText(_translate("BookWindow", "Название"))
        self.label_7.setText(_translate("BookWindow", "Издательство:"))
        self.label_8.setText(_translate("BookWindow", "Каталог:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookWindow = QtWidgets.QDialog()
    ui = Ui_BookWindow()
    ui.setupUi(BookWindow)
    BookWindow.show()
    sys.exit(app.exec_())
