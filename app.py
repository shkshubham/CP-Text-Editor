import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from setting import TabDialog as setdia
from about import TabDialog

import textedit_rc3
import json
if sys.platform.startswith('darwin'):
    rsrcPath = ":/images/mac"
else:
    rsrcPath = ":/images/win"


class Window(QMainWindow):
    def __init__(self, fileName=None, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowIcon(QIcon("text-editor-icon.png"))
        self.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        black_icon_path = "icon\\black"
        white_icon_path = "icon\\white"
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFocus()
        self.setCurrentFileName()


        setting_ = open("setting.json","r")
        json_file = json.loads(setting_.read())
        font_name = json_file["fonts"]["font-name"]
        font_size = int(json_file["fonts"]["font-size"])
        StyleSheet = json_file["themes"]["logo-color"]
        theme_name = str(json_file["themes"]["style"])
        style_name = "Themes/" + theme_name +".ini"

        style_file = open(style_name, "r")
        style_theme = str(style_file.read())
        style_file.close()
        theme_ = str(json_file["themes"]["theme"])
        setting_.close()

        self.setStyleSheet(style_theme)
        QApplication.setStyle(QStyleFactory.create(theme_))
        self.textEdit.setFont(QFont(font_name, font_size))
        self.highlighter = Highlighter(self.textEdit.document())

        if fileName is None:
            fileName = 'Welcome.txt'

        if not self.load(fileName):
            self.new_file()

        self.setGeometry(50,50,500,400)
        self.setWindowTitle("CP Editor")
        self.setWindowIcon(QIcon("text-editor-icon.png"))

        if StyleSheet == "black":
            newAction = QAction(QIcon(black_icon_path+"\_file.png"),"&New",self)
            openAction = QAction(QIcon(black_icon_path+"\_open.png"),"&Open",self)
            saveAction = QAction(QIcon(black_icon_path+"\_save.png"),"&Save",self)
            saveAsAction = QAction(QIcon(black_icon_path+"\_save.png"),"&Save",self)
            printAction = QAction(QIcon(black_icon_path+"\_print.png"),"&Print",self)
            exitAction = QAction(QIcon(black_icon_path+"\_close.png"),"&Exit",self)
            undoAction = QAction(QIcon(black_icon_path+"\_left.png"),"&Undo",self)
            redoAction = QAction(QIcon(black_icon_path+"\_redo.png"),"&Redo",self)
            cutAction = QAction(QIcon(black_icon_path+"\_cut.png"),"&Cut",self)
            copyAction = QAction(QIcon(black_icon_path+"\_copy.png"),"&Copy",self)
            pasteAction = QAction(QIcon(black_icon_path+"\_paste.png"),"&Paste",self)
            fontAction = QAction(QIcon(black_icon_path+"\_font.png"),"&Font..",self)
            aboutAction = QAction(QIcon(black_icon_path+"\_copyright.png"),"&About Us",self)
            boldAction = QAction(QIcon(black_icon_path+"\_bold.png"),"&Bold",self)
            italicAction = QAction(QIcon(black_icon_path+"\_italic.png"),"&Italic",self)
            underlineAction = QAction(QIcon(black_icon_path+"\_underline.png"),"&Underline",self)
            strikeAction = QAction(QIcon(black_icon_path+"\_strike.png"),"&Strike",self)
            superScriptAction = QAction(QIcon(black_icon_path+"\_superscript.png"),"&Super Script",self)
            subscriptAction = QAction(QIcon(black_icon_path+"\_subscript.png"),"&Sub Script",self)
            alignLeft = QAction(QIcon(black_icon_path+"\_align-left.png"),"Align left",self)
            alignCenter = QAction(QIcon(black_icon_path+"\_align-center.png"),"Align center",self)
            alignRight = QAction(QIcon(black_icon_path+"\_align-right.png"),"Align right",self)
            alignJustify = QAction(QIcon(black_icon_path+"\_align-justify.png"),"Align justify",self)
            settingsAction = QAction(QIcon(black_icon_path+"\_settings.png"),"&Settings",self)

        elif StyleSheet == "white":
            newAction = QAction(QIcon(white_icon_path+"\_file.png"),"&New",self)
            openAction = QAction(QIcon(white_icon_path+"\_open.png"),"&Open",self)
            saveAction = QAction(QIcon(white_icon_path+"\_save.png"),"&Save",self)
            saveAsAction = QAction(QIcon(white_icon_path+"\_save.png"),"&Save",self)
            printAction = QAction(QIcon(white_icon_path+"\_print.png"),"&Print",self)
            exitAction = QAction(QIcon(white_icon_path+"\_close.png"),"&Exit",self)
            undoAction = QAction(QIcon(white_icon_path+"\_left.png"),"&Undo",self)
            redoAction = QAction(QIcon(white_icon_path+"\_redo.png"),"&Redo",self)
            cutAction = QAction(QIcon(white_icon_path+"\_cut.png"),"&Cut",self)
            copyAction = QAction(QIcon(white_icon_path+"\_copy.png"),"&Copy",self)
            pasteAction = QAction(QIcon(white_icon_path+"\_paste.png"),"&Paste",self)
            fontAction = QAction(QIcon(white_icon_path+"\_font.png"),"&Font..",self)
            aboutAction = QAction(QIcon(white_icon_path+"\_copyright.png"),"&About Us",self)
            boldAction = QAction(QIcon(white_icon_path+"\_bold.png"),"&Bold",self)
            italicAction = QAction(QIcon(white_icon_path+"\_italic.png"),"&Italic",self)
            underlineAction = QAction(QIcon(white_icon_path+"\_underline.png"),"&Underline",self)
            strikeAction = QAction(QIcon(white_icon_path+"\_strike.png"),"&Strike",self)
            superScriptAction = QAction(QIcon(white_icon_path+"\_superscript.png"),"&Super Script",self)
            subscriptAction = QAction(QIcon(white_icon_path+"\_subscript.png"),"&Sub Script",self)
            alignLeft = QAction(QIcon(white_icon_path+"\_align-left.png"),"Align left",self)
            alignCenter = QAction(QIcon(white_icon_path+"\_align-center.png"),"Align center",self)
            alignRight = QAction(QIcon(white_icon_path+"\_align-right.png"),"Align right",self)
            alignJustify = QAction(QIcon(white_icon_path+"\_align-justify.png"),"Align justify",self)
            settingsAction = QAction(QIcon(white_icon_path+"\_settings.png"),"&Settings",self)

        newAction.setShortcut("Ctrl+n")
        newAction.setStatusTip("New File")
        newAction.triggered.connect(self.new_file)

        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open File")
        openAction.triggered.connect(self.open_file)
        
        saveAction.setShortcut("Ctrl+s")
        saveAction.setStatusTip("Save File")
        saveAction.triggered.connect(self.save_file)

        saveAsAction.setShortcut("Ctrl+Shift+s")
        saveAsAction.setStatusTip("Save As")
        saveAsAction.triggered.connect(self.saveAs_file)



#Edit
        undoAction.setShortcut("Ctrl+Z")
        undoAction.setStatusTip("Undo")
        undoAction.triggered.connect(self.textEdit.undo)


        redoAction.setShortcut("Ctrl+Shift+Z")
        redoAction.setStatusTip("Redo")
        redoAction.triggered.connect(self.textEdit.redo)

        
        cutAction.setShortcut("Ctrl+X")
        cutAction.setStatusTip("Cut")
        cutAction.triggered.connect(self.textEdit.cut)
        
        copyAction.setShortcut("Ctrl+C")
        copyAction.setStatusTip("Copy")
        copyAction.triggered.connect(self.textEdit.copy)
        
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.setStatusTip("Paste")
        pasteAction.triggered.connect(self.textEdit.paste)

        exitAction.setShortcut("Ctrl+Shift+x")
        exitAction.setStatusTip("Exit")
        exitAction.triggered.connect(self.close)


#BISSU action
        boldAction.setShortcut("Ctrl+B")
        boldAction.setStatusTip("Bold")
        boldAction.triggered.connect(self._bold)

        italicAction.setShortcut("Ctrl+I")
        italicAction.setStatusTip("Italic")
        italicAction.triggered.connect(self._italic)

        underlineAction.setShortcut("Ctrl+U")
        underlineAction.setStatusTip("Underline")
        underlineAction.triggered.connect(self._underline)

        strikeAction.setShortcut("Ctrl+Shift+S")
        strikeAction.setStatusTip("Strike Through.png")
        strikeAction.triggered.connect(self._strike)

        superScriptAction.setShortcut("Ctrl+B")
        superScriptAction.setStatusTip("Super Script")
        superScriptAction.triggered.connect(self._superScript)


        subscriptAction.setShortcut("Ctrl+Shift+S")
        subscriptAction.setStatusTip("Sub Script")
        subscriptAction.triggered.connect(self._subscript)

        alignLeft.triggered.connect(self._alignLeft)
        alignCenter.triggered.connect(self._alignCenter)
        alignRight.triggered.connect(self._alignRight)
        alignJustify.triggered.connect(self._alignJustify)


#Format action
        fontAction.setShortcut("Ctrl+F")
        fontAction.setStatusTip("Font")
        fontAction.triggered.connect(self.font_dialog)

#About action

        aboutAction.setShortcut("Ctrl+U")
        aboutAction.setStatusTip("About Us")
        aboutAction.triggered.connect(self.about_dialog)
        settingsAction.setShortcut("Ctrl+p")
        settingsAction.setStatusTip("Settings")
        settingsAction.triggered.connect(self.settings_dialog)
        
        menubar = self.menuBar()

#FileMenu
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(printAction)
        fileMenu.addAction(exitAction)

#EditMenu     
        editMenu = menubar.addMenu("&Edit")
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)
        editMenu.addAction(cutAction)
        editMenu.addAction(copyAction)
        editMenu.addAction(pasteAction)


#FormatMenu
        formatMenu = menubar.addMenu("&Format")
        formatMenu.addAction(fontAction)


#ViewMenu
        #viewMenu = menubar.addMenu("&View")


#HelpMenu
        helpMenu = menubar.addMenu("&Help")
        helpMenu.addAction(aboutAction)
        helpMenu.addAction(settingsAction)

#-------------------------------------------------------------------xx------------------------------------------------------------------------------------
#-------------------------------------------------------------------xx------------------------------------------------------------------------------------


#--------------------------------------------------------------------ToolBar------------------------------------------------------------------------------

#ToolBar


        self.file_toolbar = self.addToolBar("File")
        self.file_toolbar.addAction(newAction)
        self.file_toolbar.addAction(openAction)
        self.file_toolbar.addAction(saveAction)
        self.file_toolbar.addAction(saveAsAction)
        #self.file_toolbar.addAction(printAction)
        self.file_toolbar.addAction(exitAction)

        self.toolbar = self.addToolBar("Edit")
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(redoAction)
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)

        
        self.toolbar = self.addToolBar("Format")
        self.toolbar.addAction(fontAction)


        self.toolbar.addAction(boldAction)
        self.toolbar.addAction(italicAction)
        self.toolbar.addAction(underlineAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(strikeAction)
        self.toolbar.addAction(superScriptAction)
        self.toolbar.addAction(subscriptAction)
        self.toolbar.addSeparator()

        self.toolbar.addAction(alignLeft)
        self.toolbar.addAction(alignCenter)
        self.toolbar.addAction(alignRight)
        self.toolbar.addAction(alignJustify)
        self.toolbar.addSeparator()


#-------------------------------------------------StatusBar------------------------------
        self.status = self.statusBar()
        self.textEdit.cursorPositionChanged.connect(self.CursorPosition)

        #statusbar = QStatusBar()
        #self.setStatusBar(statusbar)

        self.show()


    def CursorPosition(self):
        line = self.textEdit.textCursor().blockNumber()
        col = self.textEdit.textCursor().columnNumber()
        linecol = ("Line: "+str(line)+" | "+"Column: "+str(col))
        self.status.showMessage(linecol)
        

    def load(self, f):
        if not QFile.exists(f):
            return False

        fh = QFile(f)
        if not fh.open(QFile.ReadOnly):
            return False

        data = fh.readAll()
        codec = QTextCodec.codecForHtml(data)
        unistr = codec.toUnicode(data)

        if Qt.mightBeRichText(unistr):
            self.textEdit.setHtml(unistr)
        else:
            self.textEdit.setPlainText(unistr)

        self.setCurrentFileName(f)
        return True

    def maybeSave(self):
        if not self.textEdit.document().isModified():
            return True
        if self.fileName.startswith(":/"):
            return True
        ret = QMessageBox.warning(self, "Application","The document has been modified.\n"
                "Do you want to save your changes?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        if ret == QMessageBox.Save:
            return self.save_file()

        if ret == QMessageBox.Cancel:
            return False

        return True


    def setCurrentFileName(self, fileName=''):
        self.fileName = fileName
        self.textEdit.document().setModified(False)
        if not fileName:
            shownName = 'untitled.txt'
        else:
            #shownName = QFileInfo(fileName).fileName()
            shownName = self.fileName
        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "CP Editor")))
        self.setWindowModified(False)

    def new_file(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFileName()

        
    def open_file(self):
        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory  "))
        #print (file)
        fileName = QFileDialog.getOpenFileName(self, "Open file",".","(*.*)")
        if fileName:
            self.load(fileName)

    def save_file(self):
        if not self.fileName:
            return self.saveAs_file()
        if self.fileName:
            file = open(self.fileName, "w")
            success = data = self.textEdit.toPlainText() 
            file.write(data)
            file.close()
            if success:
                self.textEdit.document().setModified(False)
            return success
        
        #writer = QTextDocumentWriter(self.fileName)
        #success = writer.write(self.textEdit.document())
        

    def saveAs_file(self):
        fn = QFileDialog.getSaveFileName(self, "Save file")

        if not fn:
            return False

        lfn = fn.lower()
        #if not lfn.endswith(('.txt', '.py', '.html')):
        # The default.
            #fn += '.txt'
        self.setCurrentFileName(fn)
        return self.save_file()

    def _bold (self):
        if self.textEdit.fontWeight() == QFont.Bold:

            self.textEdit.setFontWeight(QFont.Normal)

        else:

            self.textEdit.setFontWeight(QFont.Bold)

    def _italic(self):
        
        state = self.textEdit.fontItalic()
        self.textEdit.setFontItalic(not state)

    def _underline (self):
        state = self.textEdit.fontUnderline()
        self.textEdit.setFontUnderline(not state)

    def _strike(self):
        fmt = self.textEdit.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.textEdit.setCurrentCharFormat(fmt)

    def _superScript(self):
        fmt = self.textEdit.currentCharFormat()
        align = fmt.verticalAlignment()
        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)
        self.textEdit.setCurrentCharFormat(fmt)

    def _subscript(self):
        fmt = self.textEdit.currentCharFormat()
        align = fmt.verticalAlignment()
        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)
        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)
        self.textEdit.setCurrentCharFormat(fmt)


    def _alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    def _alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def _alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def _alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def settings_dialog(self):
        tab = setdia()
        tab.exec_()

    def about_dialog(self):
        tab = TabDialog()
        tab.exec_()


    def styleChoice(self, text):
        self.stylechoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))
        
    def close(self):
        choice = QMessageBox.question(self, "Quit","You Are Really Wanna Quit...",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass



class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)


        quotationColor = "rgb(195,232,141)"
        classfunctionColor = "rgb(255,203,107)"
        keywordColor = "rgb(183,146,234)"
        functionColor = "rgb(137,215,217)"
        commentColor = "rgb(247,118,105)"


        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor(183,146,234))
        keywordFormat.setFontWeight(QFont.Bold)
        keywordPatterns = ["\\bFalse\\b", "\\bNone\\b", "\\bTrue\\b", "\\band\\b", "\\bas\\b",
                           "\\bassert\\b", "\\bbreak\\b", "\\bcontinue\\b",
                           "\\bdel\\b", "\\belif\\b", "\\belse\\b", "\\bexcept\\b", "\\bfinally\\b",
                           "\\bfor\\b", "\\bfrom\\b", "\\bglobal\\b", "\\bif\\b", "\\bimport\\b",
                           "\\bin\\b", "\\bis\\b", "\\blambda\\b", "\\bnonlocal\\b", "\\bnot\\b",
                           "\\bor\\b", "\\bpass\\b", "\\braise\\b", "\\breturn\\b", "\\btry\\b",
                           "\\bwhile\\b", "\\bwith\\b", "\\byield\\b", "\\print\\b"] 
        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]


        classRegExp = "\\bclass\s[A-Za-z_]+\\b"
        classFormat = QTextCharFormat()
        classFormat.setForeground(QColor(255,203,107))
        classFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(classRegExp), classFormat))


        defRegExp = "\\bdef\s[A-Za-z_]+\\b"
        defFormat = QTextCharFormat()
        defFormat.setForeground(QColor(255,203,107))
        defFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(defRegExp), defFormat))


        singleLineCommentExp = "#[^\n]*"
        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(QColor(247,118,105))
        self.highlightingRules.append((QRegExp(singleLineCommentExp), singleLineCommentFormat))


        quotationExp = "\".*\""
        
        quotationFormat = QTextCharFormat()
        #quotationFormat.setFontItalic(True)
        quotationFormat.setForeground(QColor(195,232,141))
        self.highlightingRules.append((QRegExp(quotationExp), quotationFormat))
    

        functionExp = "\\[A-Za-z0-9_]+(?=\\()"
        functionFormat = QTextCharFormat()
        functionFormat.setForeground(QColor(137,215,217))
        functionFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(functionExp), functionFormat))
        

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
