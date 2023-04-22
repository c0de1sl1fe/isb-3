import sys
import os

from PyQt5.QtWidgets import (QShortcut, QAction, QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout,
                             QRadioButton, QFileDialog, qApp, QDesktopWidget, QMessageBox,
                             QTabWidget, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QKeySequence

class Example(QWidget):
    def __init__(self) -> None:
        '''Constructor'''
        super().__init__()

        self.initUI()

    # def __iter__(self) -> Self:
    #     '''something'''
    #     return self

    def initUI(self) -> None:
        '''support constructor function'''

        self.shortcut_exit = QShortcut(QKeySequence('esc'), self)
        self.shortcut_exit.activated.connect(qApp.quit)

        
        self.setWindowTitle('Lab3')
        self.setWindowIcon(QIcon('6112_Logo_git_prefinal.jpg'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()

        tabs.addTab(self.__generalTab(), "general")
        tabs.addTab(self.__generateKeys(), "GenKeys")
        tabs.addTab(self.__encryptionTab(), "EncryptionTab")
        tabs.addTab(self.__decryptionTab(), "DecryptionTab")
        # self.__iterator.setPath(self.__path)
        layout.addWidget(tabs)

        self.setGeometry(400, 400, 450, 400)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.show()

    # Main window with hello-words and descripition what's going on
    def __generalTab(self) -> QWidget:
        '''main window with hello-words and descripition what's going on'''
        custom_font = QFont()
        custom_font.setPixelSize(40)
        generalTab = QWidget()
        layout = QVBoxLayout()
        text = QVBoxLayout()
        line1 = QLabel("Hello there!")
        line1.setFont(custom_font)
        
        custom_font.setPixelSize(20)
        line2 = QLabel('''At GenerateKeys you can generate and save keys\n - 1.1: Generate key for sym alg\n - 1.2: Generate key for assym alg\n - 1.3: sirialyze assym key\n - 1.4: Incrypt public key via private key and save
                        \nAt EncryptionTab you can:\n - 2.1: Decipher symmetric keys\n - 2.2: Cipher you text and save it
                        \nAt Decipher data of hybrid system:\n - 3.1: Decipher symmetric key\n - 3.2: ''')
        line2.setFont(custom_font)
        text.addWidget(line1)
        text.addWidget(line2)
        layout.addLayout(text)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab
    def __generateKeys(self)->QWidget:

        generalTab = QWidget()
        layout = QVBoxLayout()
        text = QHBoxLayout()
        line1 = QLabel("Hello there!")
        buttom = QPushButton("test")
        buttom.adjustSize()
        text.addWidget(buttom)
        text.addWidget(line1)


        layout.addLayout(text)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab
    def __encryptionTab(self)->QWidget:

        generalTab = QWidget()
        layout = QVBoxLayout()
        text = QVBoxLayout()
        line1 = QLabel("Hello there!")
       

        text.addWidget(line1)

        layout.addLayout(text)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab
    def __decryptionTab(self)->QWidget:
   
        generalTab = QWidget()
        layout = QVBoxLayout()
        text = QVBoxLayout()
        line1 = QLabel("Hello there!")
       

        text.addWidget(line1)

        layout.addLayout(text)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab
    # image tab where user choose directory and see the img via _next_
   

    def __onClicked(self) -> None:
        '''change class name'''
        # radioButton = self.sender()
        # if radioButton.isChecked():
        #     print("Class is %s" % (radioButton.name))
        #     self.__iterator.setName(radioButton.name)
        #     self.__name = radioButton.name

    def __inputPath(self) -> None:
        print(1)
    #     '''service function'''
    #     print("input path")
    #     tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
    #     if not "dataset" in tmp or not "zebra" in tmp or not "bay horse" in tmp or not "test" in tmp:
    #         print("error")
    #         QMessageBox.critical(
    #             self, "Wrong dir", "please choose dir with dataset", QMessageBox.Ok)
    #     else:
    #         print("prev dir is ", self.__path)
    #         self.__path = tmp 
    #         print("new dir is ", self.__path)

   
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
