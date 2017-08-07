import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json

class TabDialog(QDialog):
    def __init__(self):
        super(TabDialog,self).__init__()
        self.setGeometry(50,50,500,400)
        self.setWindowTitle("Setting")
        self.setWindowIcon(QIcon("_setting.png"))
        tabWidget = QTabWidget()
        tabWidget.addTab(GeneralTab(),"General")
        tabWidget.addTab(ThemesTab(), "Themes")
        
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
##        setting_ = open("setting.json","r")
##        json_file = json.loads(setting_.read())
##        theme_name = json_file["themes"]["style"]
##        setting_.close()
##        
##        style_name = "Themes/" + theme_name +".ini"
##        style_file = open(style_name, "r")
##        style_theme = str(style_file.read())
##        style_file.close()
##        self.setStyleSheet(style_theme)
        self.show()

        
class GeneralTab(QWidget):
    def __init__(self):
        super(GeneralTab, self).__init__()
        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        font_name = json_file["fonts"]["font-name"]
        font_size = json_file["fonts"]["font-size"]
        setting_.close()

        self.font_Label = QLabel("Font:")
        self.font_Text = QLabel(font_name)
        self.fsize_Label = QLabel("Font Size:")
        self.fsize_Text = QLabel(font_size)
        self.btn = QPushButton('Font Dialog', self)
        self.btn2 = QPushButton('Size Dialog', self)
        self.btn.clicked.connect(self.fontDialog)
        self.btn2.clicked.connect(self.fontsizeDialog)
        

        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.font_Label)
        mainLayout.addWidget(self.font_Text)
        mainLayout.addWidget(self.btn)
        mainLayout.addWidget(self.fsize_Label)
        mainLayout.addWidget(self.fsize_Text)
        mainLayout.addWidget(self.btn2)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        

    def onChanged(self, text):
        self.tet = self.font_Text.text()
        self.tetsize = self.fsize_Text.text()

    def fontsizeDialog(self, text):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter:')
        
        if ok:
            self.fsize_Text.setText(str(text))
            tetsize = text
            setting_ = open("setting.json","r")
            json_file = json.loads(setting_.read())
            json_file["fonts"]["font-size"] = tetsize
            setting_.close()
            setting_write = open("setting.json","w")
            a =  json.dump(json_file, setting_write)        
            setting_write.close()


    def fontDialog(self):
         
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter:')
        
        if ok:
            self.font_Text.setText(str(text))
            tet = text
            setting_ = open("setting.json","r")
            json_file = json.loads(setting_.read())
            json_file["fonts"]["font-name"] = tet
            setting_.close()
            setting_write = open("setting.json","w")
            a =  json.dump(json_file, setting_write)        
            setting_write.close()
            
class ThemesTab(QWidget):
    def __init__(self):
        super(ThemesTab, self).__init__()
        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        theme_name = json_file["themes"]["theme"]
        icon_name = json_file["themes"]["logo-color"]
        style_name = json_file["themes"]["style"]
        setting_.close()

#-----------------------------------------------------------------------

        self.themeChoice = QLabel(theme_name, self)
        self.themeLabel = QLabel("Themes")        
        self.themeBox = QComboBox(self)
        self.themeBox.addItem("motif")
        self.themeBox.addItem("Windows")
        self.themeBox.addItem("cde")
        self.themeBox.addItem("Plastique")
        self.themeBox.addItem("Cleanlooks")
        self.themeBox.addItem("windowsvista")
        self.themeBox.activated[str].connect(self.theme_choice)

        theme_index = self.themeBox.findText(theme_name,Qt.MatchFixedString)
        if theme_index >= 0:
            self.themeBox.setCurrentIndex(theme_index)

#-----------------------------------------------------------------------
        
        self.iconBox = QComboBox(self)
        self.iconBox.addItem("white")
        self.iconBox.addItem("black")
        self.iconBox.activated[str].connect(self.icon_choice)
        icon_index = self.iconBox.findText(icon_name,Qt.MatchFixedString)
        if icon_index >= 0:
            self.iconBox.setCurrentIndex(icon_index)
        self.iconLabel = QLabel("Icon Theme")


#-----------------------------------------------------------------------
        self.styleChoice = QLabel(style_name, self)
        self.styleLabel = QLabel("Style")
        self.styleBox = QComboBox(self)
        self.styleBox.addItem("Material")
        self.styleBox.addItem("Material_Dark")
        self.styleBox.addItem("Style")
        self.styleBox.addItem("Style2")
        self.styleBox.activated[str].connect(self.style_choice)
        style_index = self.styleBox.findText(style_name,Qt.MatchFixedString)
        if style_index >= 0:
            self.styleBox.setCurrentIndex(style_index)

#---------------------------------------------------------------------------
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.themeLabel)
        self.mainLayout.addWidget(self.themeChoice)
        self.mainLayout.addWidget(self.themeBox)
        self.mainLayout.addWidget(self.iconLabel)
        self.mainLayout.addWidget(self.iconBox)
        self.mainLayout.addWidget(self.styleLabel)
        self.mainLayout.addWidget(self.styleChoice)
        self.mainLayout.addWidget(self.styleBox)
        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)
        


    def theme_choice(self, text):
        self.themeChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))
        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        json_file["themes"]["theme"] = text
        setting_.close()

        setting_write = open("setting.json","w")
        a =  json.dump(json_file, setting_write)        
        setting_write.close()


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))
        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        json_file["themes"]["style"] = text
        setting_.close()

        setting_write = open("setting.json","w")
        a =  json.dump(json_file, setting_write)        
        setting_write.close()

        

    def icon_choice(self, text):
        text = self.iconBox.currentText()
        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        json_file["themes"]["logo-color"] = text
        setting_.close()

        setting_write = open("setting.json","w")
        a =  json.dump(json_file, setting_write)        
        setting_write.close()



    
#app = QApplication(sys.argv)
#win = TabDialog()
#sys.exit(app.exec_())
