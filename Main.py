from SearchAlgos import MCSearchAStar
from Nodes.Path import Path
from Nodes.PathG import PathG
from Nodes.Node import Node
from Nodes.NodeG import NodeGraph
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from win import Ui_MainWindow
import sys

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CloseBtn.clicked.connect(self.close)
        self.ui.MinimizeBtn.clicked.connect(self.showMinimized)
        self.ui.MaximizeBtn.clicked.connect(self.Maxmin)
        self.ui.btnTest.clicked.connect(self.AddNode)
        self.ui.btnTest1.clicked.connect(self.StartMCA)
        self.ui.HeadBar.mouseMoveEvent = self.DragMovement
        self.ui.HeadBar.mouseDoubleClickEvent = self.Maxmin
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
    
    def StartMCA(self):
        InitialNode = Node()
        GoalNode = Node(State=[0,0,0])
        ng = NodeGraph(InitialNode)
        self.ui.Scene.addItem(ng)
        MCSearchAStar(InitialNode,GoalNode)
        self.DrawTree(ng)
        
    


    def mousePressEvent(self, event:QMouseEvent):
        self.oldPos = event.globalPos()
    
        
    def Maxmin(self,event):
        if(not self.isMaximized()):
            icon = QIcon()
            icon.addFile(u":/icons/icons/icon_restore.png")
            self.ui.MaximizeBtn.setIcon(icon)
            self.showMaximized()
        else:
            icon = QIcon()
            icon.addFile(u":/icons/icons/icon_maximize.png")
            self.ui.MaximizeBtn.setIcon(icon)
            self.showNormal()

    def DragMovement(self,event:QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
    
    def AddNode(self):
        self.nodes = Node("S")
        ng = NodeGraph(self.nodes)
        self.ui.Scene.addItem(ng)

    def DrawTree(self,Root:NodeGraph):
        if(len(Root.node.children) == 0):
            return   
        for (i,item) in enumerate(Root.node.children):
            itemG = NodeGraph(item)
            itemG.setPos(Root.pos().x()+(50*i),Root.pos().y()+100)
            edge = Path(Root.node,itemG.node,itemG.node.G - Root.node.G)
            edgebg= PathG(edge,Root,itemG)
            self.ui.Scene.addItem(itemG)
            self.ui.Scene.addItem(edgebg)
            self.DrawTree(itemG)    

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
