# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from TreeSceen import TreeSceen
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from TreeGraphics import TreeGraphics

from resources import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget #Content{\n"
"background:#282C34;\n"
"}\n"
"\n"
"#StatusBar,#HeadBar{\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"#MainTitle,#Credits{\n"
"padding-left:15px;\n"
"color: #aaaaaa;\n"
"}\n"
"#HeadButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#HeadButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#HeadButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#HeadButtons #CloseBtn:hover{\n"
"background-color:red;\n"

"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.HeadBar = QFrame(self.centralwidget)
        self.HeadBar.setObjectName(u"HeadBar")
        self.HeadBar.setMinimumSize(QSize(0, 50))
        self.HeadBar.setMaximumSize(QSize(16777215, 50))
        self.HeadBar.setFrameShape(QFrame.StyledPanel)
        self.HeadBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.HeadBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainTitle = QLabel(self.HeadBar)
        self.MainTitle.setObjectName(u"MainTitle")
        font = QFont()
        font.setPointSize(10)
        self.MainTitle.setFont(font)

        self.horizontalLayout.addWidget(self.MainTitle)

        self.HeadButtons = QFrame(self.HeadBar)
        self.HeadButtons.setObjectName(u"HeadButtons")
        self.HeadButtons.setMaximumSize(QSize(100, 16777215))
        self.HeadButtons.setFrameShape(QFrame.StyledPanel)
        self.HeadButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.HeadButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MinimizeBtn = QPushButton(self.HeadButtons)
        self.MinimizeBtn.setObjectName(u"MinimizeBtn")
        self.MinimizeBtn.setMinimumSize(QSize(28, 28))
        self.MinimizeBtn.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.MinimizeBtn)

        self.MaximizeBtn = QPushButton(self.HeadButtons)
        self.MaximizeBtn.setObjectName(u"MaximizeBtn")
        self.MaximizeBtn.setMinimumSize(QSize(28, 28))
        self.MaximizeBtn.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MaximizeBtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.MaximizeBtn)

        self.CloseBtn = QPushButton(self.HeadButtons)
        self.CloseBtn.setObjectName(u"CloseBtn")
        self.CloseBtn.setMinimumSize(QSize(28, 28))
        self.CloseBtn.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseBtn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.CloseBtn)


        self.horizontalLayout.addWidget(self.HeadButtons)


        self.verticalLayout_2.addWidget(self.HeadBar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Content)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MenuBar = QFrame(self.Content)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setMinimumSize(QSize(50, 0))
        self.MenuBar.setMaximumSize(QSize(50, 16777215))
        self.MenuBar.setFrameShape(QFrame.StyledPanel)
        self.MenuBar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.MenuBar)

        self.MainContent = QFrame(self.Content)
        self.MainContent.setObjectName(u"MainContent")
        self.MainContent.setFrameShape(QFrame.StyledPanel)
        self.MainContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainContent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentScene = QFrame(self.MainContent)
        self.ContentScene.setObjectName(u"ContentScene")
        self.ContentScene.setFrameShape(QFrame.StyledPanel)
        self.ContentScene.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ContentScene)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        
        #############################################################
        self.Scene = TreeSceen()
        self.Scene.setBackgroundBrush(QBrush(QColor("#1f1f1f")))
        self.view = TreeGraphics(self.Scene,MainWindow)
        self.btnTest = QPushButton("Add Node")
        self.btnTest1 = QPushButton("Start MC-A*")

        self.verticalLayout_3.addWidget(self.view)
        self.verticalLayout_3.addWidget(self.btnTest)
        self.verticalLayout_3.addWidget(self.btnTest1)

        self.verticalLayout.addWidget(self.ContentScene)

        self.StatusBar = QFrame(self.MainContent)
        self.StatusBar.setObjectName(u"StatusBar")
        self.StatusBar.setMinimumSize(QSize(0, 25))
        self.StatusBar.setMaximumSize(QSize(16777215, 25))
        self.StatusBar.setFont(font)
        self.StatusBar.setFrameShape(QFrame.StyledPanel)
        self.StatusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.StatusBar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Credits = QLabel(self.StatusBar)
        self.Credits.setObjectName(u"Credits")

        self.sizegrip = QSizeGrip(MainWindow)

        self.horizontalLayout_3.addWidget(self.Credits)
        self.horizontalLayout_3.addWidget(self.sizegrip)

        self.verticalLayout.addWidget(self.StatusBar)


        self.horizontalLayout_4.addWidget(self.MainContent)


        self.verticalLayout_2.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainTitle.setText(QCoreApplication.translate("MainWindow", u"Application", None))
        self.MinimizeBtn.setText("")
        self.MaximizeBtn.setText("")
        self.CloseBtn.setText("")
        self.Credits.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

