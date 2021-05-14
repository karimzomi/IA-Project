# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Animeview import Animeview
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from TreeGraphics import TreeGraphics
from TreeSceen import TreeSceen

import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 720)
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
"}\n"
"#Content QPushButton{\n"
"background-color:transparent;\n"
"color:white;\n"
"border:2px solid gray;\n"
"border-radius:10px;\n"
"padding:10px ;\n"
"}\n"
"#Content QPushButton:hover{\n"
"background-color: rgb(44, 49, 57); \n"
"}\n"
"#Content QPushButton:pressed{\n"
"background-color: gray; \n"
"}\n"
"#Content QPushButton:disabled{\n"
"background-color: rgb(33, 37, 43); \n"
"color:rgba(255,255,255,0.4"
                        ");\n"
"}\n"
"#Content QLabel{\n"
"color:white;\n"
"}\n"
"#Content QTextEdit{\n"
"background:black;\n"
"color:white;\n"
"border:2px solid gray;\n"
"border-radius:10px;\n"
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
        self.gridLayout = QGridLayout(self.ContentScene)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.Tree_container = QFrame(self.ContentScene)
        self.Tree_container.setObjectName(u"Tree_container")
        self.Tree_container.setFrameShape(QFrame.StyledPanel)
        self.Tree_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Tree_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.Tree_container)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.TreeScene = TreeSceen()
        self.graphicsView = TreeGraphics(self.TreeScene,self.Tree_container)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setRenderHints(QPainter.Antialiasing|QPainter.SmoothPixmapTransform|QPainter.TextAntialiasing)
        self.graphicsView.setDragMode(QGraphicsView.RubberBandDrag)

        self.verticalLayout_4.addWidget(self.graphicsView)

        self.Btns_container2 = QFrame(self.Tree_container)
        self.Btns_container2.setObjectName(u"Btns_container2")
        self.Btns_container2.setMinimumSize(QSize(400, 50))
        self.Btns_container2.setMaximumSize(QSize(500, 16777215))
        self.Btns_container2.setFrameShape(QFrame.StyledPanel)
        self.Btns_container2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Btns_container2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.AddNode = QPushButton(self.Btns_container2)
        self.AddNode.setObjectName(u"AddNode")

        self.horizontalLayout_5.addWidget(self.AddNode)

        self.ClearScreen = QPushButton(self.Btns_container2)
        self.ClearScreen.setObjectName(u"ClearScreen")

        self.horizontalLayout_5.addWidget(self.ClearScreen)


        self.verticalLayout_4.addWidget(self.Btns_container2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.Tree_container, 1, 0, 1, 1)

        self.Game_container = QFrame(self.ContentScene)
        self.Game_container.setObjectName(u"Game_container")
        self.Game_container.setMaximumSize(QSize(300, 16777215))
        self.Game_container.setFrameShape(QFrame.StyledPanel)
        self.Game_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Game_container)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Game_container)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.MC_Scene = QGraphicsScene()
        self.MC_view = Animeview(self.MC_Scene,self.Game_container)
        self.MC_view.setObjectName(u"MC_view")
        self.MC_view.setMaximumSize(QSize(300, 16777215))
        self.MC_view.setMinimumSize(QSize(300, 0))

        self.verticalLayout_3.addWidget(self.MC_view)

        self.Btns_Container = QFrame(self.Game_container)
        self.Btns_Container.setObjectName(u"Btns_Container")
        self.Btns_Container.setMinimumSize(QSize(0, 50))
        self.Btns_Container.setFrameShape(QFrame.StyledPanel)
        self.Btns_Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Btns_Container)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.StartMC_A = QPushButton(self.Btns_Container)
        self.StartMC_A.setObjectName(u"StartMC_A")

        self.horizontalLayout_6.addWidget(self.StartMC_A)

        self.Use_Solution = QPushButton(self.Btns_Container)
        self.Use_Solution.setObjectName(u"Use_Solution")
        self.Use_Solution.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.Use_Solution)


        self.verticalLayout_3.addWidget(self.Btns_Container)


        self.gridLayout.addWidget(self.Game_container, 1, 1, 1, 1)

        self.Results_Display = QTextEdit(self.ContentScene)
        self.Results_Display.setObjectName(u"Results_Display")
        self.Results_Display.setMaximumSize(QSize(16777215, 200))
        self.Results_Display.setMinimumSize(QSize(0, 200))
        self.Results_Display.setFont(QFont("Ubuntu",15))
        self.Results_Display.setReadOnly(True)

        self.gridLayout.addWidget(self.Results_Display, 0, 0, 1, 2)


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

        self.horizontalLayout_3.addWidget(self.Credits)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tree Section", None))
        self.AddNode.setText(QCoreApplication.translate("MainWindow", u"Add Node", None))
        self.ClearScreen.setText(QCoreApplication.translate("MainWindow", u"Clear Tree Screen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Game Section", None))
        self.StartMC_A.setText(QCoreApplication.translate("MainWindow", u"StartMC_A*", None))
        self.Use_Solution.setText(QCoreApplication.translate("MainWindow", u"Use Solution", None))
        self.Credits.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

