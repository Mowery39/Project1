from idlelib.configdialog import is_int

from PyQt6.QtWidgets import QMainWindow
from gui import *
import csv


# Still need To check to files to see if ID was already submitted/add new ones to files
# Need to figure out how to clear the radio button
# When finished with files, figure out how to chnage the color and add pop up that says, Alr voted!
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.setupUi(self)

        self.pushButton_submit.clicked.connect(lambda: self.submit())
        self.pushButton_clear.clicked.connect(lambda: self.clear())

    def submit(self) -> None:
        ID = (self.lineEdit_ID.text())
        if self.radioButton_jane.isChecked() or self.radioButton_john.isChecked():
            if is_int(ID):
                if len(ID) == 8:
                    if any(ID in x for x in self.rows):
                        self.label_Error.setText('Error: The ID Was Already Given')
                    else:
                        self.label_Error.setText('Voted!')
                        self.rows.append(f'{ID}')
                        with open('id_checker.csv', mode='a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(['ID'])
                            for vote in self.rows:
                                file.write(f'{vote}\n')
                                print(f'Id Was {ID}')
                else:
                    self.label_Error.setText('Error: ID should only be 8 digits')
            else:
                self.label_Error.setText('Should only contain Numbers')
        else:
            self.label_Error.setText('Error Please select a candidate')

    def clear(self):
        for radioButton in [self.radioButton_jane, self.radioButton_john]:
            radioButton.setAutoExclusive(False)
            radioButton.setChecked(False)
            radioButton.setAutoExclusive(True)
        self.lineEdit_ID.clear()
        self.label_Error.clear()
