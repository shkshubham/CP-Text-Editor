import sys
import cx_Freeze

executables = [cx_Freeze.Executable("app.py",base="Win32GUI",shortcutName="Notepad",shortcutDir="DesktopFolder",icon="icon.ico",targetName="CP.exe",)]

includefiles = ["setting.json","Welcome.txt", "icon","Themes","textedit.qrc", "text-editor-icon.png"]


cx_Freeze.setup(
    name="CP Editor",
    version ="1.0",
    author="Shubham Shukla",
    options={"build_exe":{"packages":[], 'include_files':includefiles}},
    description = "Notepad by Shubham Shukla",
    executables = executables
    )
