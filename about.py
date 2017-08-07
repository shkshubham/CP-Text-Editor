import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json

class TabDialog(QDialog):
    def __init__(self):
        super(TabDialog,self).__init__()
        self.setWindowTitle("About")
        self.setWindowIcon(QIcon("_setting.png"))   
        intro = QLabel("Developed by Shubham Shukla")
        roll = QLabel("CSE 4th year 138005370021")
        pyth = QLabel("using Python plugin PYQT")
        thank = QLabel("Thank You!!")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(intro)
        mainLayout.addWidget(roll)
        mainLayout.addWidget(pyth)
        mainLayout.addWidget(thank)
        
        self.setLayout(mainLayout)
        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        theme_name = json_file["themes"]["style"]
        setting_.close()
        
        style_name = "Themes/" + theme_name +".ini"
        style_file = open(style_name, "r")
        style_theme = str(style_file.read())
        style_file.close()
        self.setStyleSheet(style_theme)
        self.show()
