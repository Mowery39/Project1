# Form implementation generated from reading ui file 'gui_project1.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vote_for_a_candidate_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.vote_for_a_candidate_label.setGeometry(QtCore.QRect(40, 20, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.vote_for_a_candidate_label.setFont(font)
        self.vote_for_a_candidate_label.setObjectName("vote_for_a_candidate_label")
        self.Candidate_label_header = QtWidgets.QLabel(parent=self.centralwidget)
        self.Candidate_label_header.setGeometry(QtCore.QRect(70, 70, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        self.Candidate_label_header.setFont(font)
        self.Candidate_label_header.setObjectName("Candidate_label_header")
        self.John_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.John_label.setGeometry(QtCore.QRect(60, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.John_label.setFont(font)
        self.John_label.setObjectName("John_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton_jane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_jane.setGeometry(QtCore.QRect(290, 310, 82, 17))
        self.radioButton_jane.setText("")
        self.radioButton_jane.setObjectName("radioButton_jane")
        self.radioButton_john = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_john.setGeometry(QtCore.QRect(290, 260, 82, 17))
        self.radioButton_john.setText("")
        self.radioButton_john.setObjectName("radioButton_john")
        self.lineEdit_ID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(180, 190, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.ID_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(70, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.ID_label.setFont(font)
        self.ID_label.setObjectName("ID_label")
        self.pushButton_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(210, 350, 181, 61))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.label_Error = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(50, 430, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setObjectName("label_Error")
        self.pushButton_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(10, 350, 181, 61))
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 46))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vote Window"))
        self.vote_for_a_candidate_label.setText(_translate("MainWindow", "Vote For A Candidate!"))
        self.Candidate_label_header.setText(_translate("MainWindow", "Candidates Running!"))
        self.John_label.setText(_translate("MainWindow", "John"))
        self.label.setText(_translate("MainWindow", "Jane"))
        self.ID_label.setText(_translate("MainWindow", "ID"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
