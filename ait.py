import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

from random import randint

class AIT(QWidget):

    def __init__(self):
        super().__init__()

        self.label1 = self.create_label("label 1")
        self.label2 = self.create_label("label 2")
        self.equal = self.create_label('=')
        self.operator = self.create_label("")

        
        self.result = self.create_label('', QLineEdit) #QLineEdit("")
        self.result.returnPressed.connect(self.check_result)
        
        self.operation = QHBoxLayout()
        self.operation.addWidget(self.label1)
        self.operation.addWidget(self.operator)
        self.operation.addWidget(self.label2)
        self.operation.addWidget(self.equal)
        self.operation.addWidget(self.result)


        self.button_ok = self.create_button("✅", self.check_result)
        self.button_retry = self.create_button("❌", self.clear_result)
        self.button_next = self.create_button("-->>>", self.generate_random_number)

        
        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.button_ok)
        self.buttons.addWidget(self.button_retry)
        self.buttons.addWidget(self.button_next)


        self.layout = QVBoxLayout()
        self.layout.addLayout(self.operation)
        self.layout.addLayout(self.buttons)

        self.generate_random_number()

        self.setLayout(self.layout)
        self.setWindowTitle("Вычеслител")
        self.setFixedSize(QSize(750, 500))
        self.show()

    def create_button(self, text, func):
        button = QPushButton(text)
        font = QFont()
        font.setPointSize(50)
        button.setFont(font)
        button.setStyleSheet('background-color: grey; border-radius: 50%')
        button.clicked.connect(func)
        return button

    def create_label(self,name,type = QLabel):

        font = QFont()
        font.setPointSize(50)
        label = type(name)
        label.setFont(font)
        return label

    def check_result(self):
        v1 = int(self.label1.text())
        v2 = int(self.label2.text())
        op = self.operator.text()
        if op == '+':
            result = v1 + v2
        else:
            result = v1 - v2
    
        

        if result == int(self.result.text()):
            self.result.setStyleSheet("background-color: green;")
        else:
            self.result.setStyleSheet("background-color: red;") 
 
        


    def clear_result(self):
        self.result.setText("")
        self.result.setStyleSheet("background-color: white")

    def generate_random_number(self):
        self.result.setText("")
        self.result.setStyleSheet("background-color : white")
        val1 = randint(0, 9)
        val2 = randint(0, 9)

        op = ['+', '-'][randint(0,1)]
        if op == '-':
            if val1 < val2:
                val1, val2 = val2, val1
        
        self.label1.setText(str(val1))
        self.label2.setText(str(val2))
        self.operator.setText(op)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    counter = AIT()
    sys.exit(app.exec_())
