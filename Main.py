from Mc_shapes import Mc_shapes
from SearchAlgos import MCSearchAStar
from Nodes.Path import Path
from Nodes.PathG import PathG
from Nodes.Node import Node
from Nodes.NodeG import NodeGraph
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Window import Ui_MainWindow
import sys

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cs = []
        self.ms = []
        self.ui.CloseBtn.clicked.connect(self.close)
        self.ui.MinimizeBtn.clicked.connect(self.showMinimized)
        self.ui.MaximizeBtn.clicked.connect(self.Maxmin)
        self.ui.AddNode.clicked.connect(self.AddNode)
        self.ui.StartMC_A.clicked.connect(self.StartMCA)
        self.ui.ClearScreen.clicked.connect(self.ui.TreeScene.clear)
        self.ui.HeadBar.mouseMoveEvent = self.DragMovement
        self.ui.HeadBar.mouseDoubleClickEvent = self.Maxmin
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.mypen = QPen(Qt.black)
        self.mypen.setWidth(1)
        self.DrawAnime()
        self.Path=[]
       
        self.ui.MC_Scene.setSceneRect(0,0,300,300)


        self.show()
    
    def StartMCA(self):
        InitialNode = Node()
        GoalNode = Node(State=[0,0,0])
        ng = NodeGraph(InitialNode)
        self.ui.TreeScene.addItem(ng)
        r = MCSearchAStar(InitialNode,GoalNode)
        self.Path = r[1]
        self.ui.Results_Display.append(r[0])
        self.DrawTree(ng)
        self.ui.StartMC_A.setEnabled(False)
        self.ui.Use_Solution.setEnabled(True)
        self.ui.Use_Solution.clicked.connect(self.StartAnimation)


    def MoveAllForward(self,items):
        def test():
            def func():
                for i in items:
                    try:
                        i.setPos(230,100+30*self.ms.index(i))
                    except ValueError:
                        i.setPos(230,10+30*self.cs.index(i))
                self.Path.pop(-1)
                self.StartAnimation()
            if(len(items) !=  1):
                self.animation1_0.start()
            self.animation0.start()
            self.animationb.start()
            self.animationb.finished.connect(func)
            
        
        if(items != []):
            self.groupAnimation = QSequentialAnimationGroup()   
            self.animation = QPropertyAnimation(items[0],b"pos")
            self.animation.setDuration(1000)
            self.animation.setEndValue(QPointF(self.b.pos().x()+5,self.b.pos().y()+5))

            if(len(items) !=  1):
                self.animation1 = QPropertyAnimation(items[1],b"pos")
                self.animation1.setDuration(1000)
                self.animation1.setEndValue(QPointF(self.b.pos().x()+25,self.b.pos().y()+25))
                self.groupAnimation.addAnimation(self.animation1)

            self.groupAnimation.addAnimation(self.animation)

            self.animationb = QPropertyAnimation(self.b,b"pos")
            self.animationb.setDuration(1000)
            self.animationb.setEndValue(QPointF(150,100))

            self.groupAnimation.start()
            self.animation0 = QPropertyAnimation(items[0],b"pos")
            self.animation0.setDuration(1000)
            self.animation0.setEndValue(QPointF(155,105))

            if(len(items) !=  1):
                self.animation1_0 = QPropertyAnimation(items[1],b"pos")
                self.animation1_0.setDuration(1000)
                self.animation1_0.setEndValue(QPointF(175,125))
            
            self.groupAnimation.finished.connect(test)

            
            
            
    
    def MoveAllBackward(self,items):

        def test():
            def func():
                for i in items:
                    try:
                        i.setPos(30,150+30*self.ms.index(i))
                    except ValueError:
                        i.setPos(30,10+30*self.cs.index(i))
                self.Path.pop(-1)
                self.StartAnimation()



            if(len(items) !=  1):
                self.animation1_0.start()
                
            self.animation0.start()
            self.animationb.start()
            self.animationb.finished.connect(func)
            
        
        if(items != []):
            self.groupAnimation = QSequentialAnimationGroup()   
            self.animation = QPropertyAnimation(items[0],b"pos")
            self.animation.setDuration(1000)
            self.animation.setEndValue(QPointF(self.b.pos().x()+5,self.b.pos().y()+5))

            if(len(items) !=  1):
                self.animation1 = QPropertyAnimation(items[1],b"pos")
                self.animation1.setDuration(1000)
                self.animation1.setEndValue(QPointF(self.b.pos().x()+25,self.b.pos().y()+25))
                self.groupAnimation.addAnimation(self.animation1)
            
            self.groupAnimation.addAnimation(self.animation)

            self.animationb = QPropertyAnimation(self.b,b"pos")
            self.animationb.setDuration(1000)
            self.animationb.setEndValue(QPointF(100,100))

            self.groupAnimation.start()
            self.animation0 = QPropertyAnimation(items[0],b"pos")
            self.animation0.setDuration(1000)
            self.animation0.setEndValue(QPointF(105,105))

            if(len(items) !=  1):
                self.animation1_0 = QPropertyAnimation(items[1],b"pos")
                self.animation1_0.setDuration(1000)
                self.animation1_0.setEndValue(QPointF(125,125))
            self.groupAnimation.finished.connect(test)



    def StartAnimation(self):
        print(self.Path)
        if(self.Path == [] or self.Path[-1] == [0,0,0]):
            return
        p = self.Path[len(self.Path)-2]
        print(p,self.Path[-1])
        if(p[2] == 0):
            items = []
            if(abs(p[0] - self.Path[-1][0]) != 0):
                c=0
                for i in range(0,3):
                    if(c == abs(p[0] - self.Path[-1][0])):
                        break
                    if(self.cs[i].state == 0):
                        self.cs[i].state = 1
                        items.append(self.cs[i])
                        c+=1
            if(abs(p[1] - self.Path[-1][1]) != 0): 
                c=0
                for j in range(0,3):
                    if(c == abs(p[1] - self.Path[-1][1])):
                        break
                    if(self.ms[j].state == 0):
                        self.ms[j].state = 1
                        items.append(self.ms[j])
                        c+=1

            self.MoveAllForward(items)
        if(p[2] == 1):
            items = []
            if(abs(p[0] - self.Path[-1][0]) != 0):
                c=0
                for i in range(0,3):
                    if(c == abs(p[0] - self.Path[-1][0])):
                        break
                    if(self.cs[i].state == 1):
                        self.cs[i].state = 0
                        items.append(self.cs[i])
                        c+=1

            if(abs(p[1] - self.Path[-1][1]) != 0): 
                c=0
                for j in range(0,3):
                    if(c == abs(p[1] - self.Path[-1][1])):
                        break
                    if(self.ms[j].state == 1):
                        self.ms[j].state = 0
                        items.append(self.ms[j])
                        c+=1
            self.MoveAllBackward(items)
        


    def mousePressEvent(self, event:QMouseEvent):
        self.oldPos = event.globalPos()
    
    def DrawAnime(self):
        self.ui.MC_Scene.addRect(10,250,20,20,self.mypen,QBrush(Qt.red))
        self.ui.MC_Scene.addEllipse(10,280,20,20,self.mypen,QBrush(Qt.gray))
        t1 = self.ui.MC_Scene.addText("Canniable")
        t2 = self.ui.MC_Scene.addText("Missionaire")
        t1.setPos(30,250)
        t2.setPos(30,280)

        for i in range(1,4):
            c = Mc_shapes(color=Qt.red)
            c.state = 0
            c.setPos(30,10+(i*30))
            self.ui.MC_Scene.addItem(c)
            self.cs.append(c)
        
        for i in range(1,4):
            m = Mc_shapes(shape="circle",color=Qt.gray)
            m.state = 0
            m.setPos(30,100+(i*30))
            self.ui.MC_Scene.addItem(m)
            self.ms.append(m)

        self.b = Mc_shapes(size=(50,50),color=Qt.black)
        self.b.setPos(100,100)
        self.b.state = 0
        self.ui.MC_Scene.addItem(self.b)
        self.b.setZValue(-1)

        

        


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
        self.ui.TreeScene.addItem(ng)

    def DrawTree(self,Root:NodeGraph):
        L = len(Root.node.children)
        if(L == 0):
            return
        # if(L % 2 == 0):
        for (i,item) in enumerate(Root.node.children):
            itemG = NodeGraph(item)
            itemG.setPos(Root.pos().x() - L*25 + 50*i + 25 ,Root.pos().y()+100)
            edge = Path(Root.node,itemG.node,itemG.node.G - Root.node.G)
            edgebg= PathG(edge,Root,itemG)
            self.ui.TreeScene.addItem(itemG)
            self.ui.TreeScene.addItem(edgebg)
            self.DrawTree(itemG)    
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
