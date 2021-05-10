from SearchAlgos import GeneralSearchAStar,MCSearchAStar
from Nodes.Path import Path
from Nodes.Node import Node
from Nodes.PathG import PathG
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class NodeGraph(QGraphicsItem):
    def __init__(self,node:Node,parent=None):
        super().__init__(parent)

        self._title_color = Qt.white
        self._title_font = QFont("Ubuntu", 10)

        self.width = 50
        self.height = 50

        self._pen_default = QPen(Qt.red)
        self._pen_selected = QPen(QColor("#FFFFA637"))

        self._brush_title = QBrush(QColor("#FF313131"))
        self._brush_background = QBrush(QColor("#E3212121"))

        self.node = node
        self.edges = []
        self.title = node.title
        self.initH()
        self.initTitle()
        self.initUI()
    def boundingRect(self):
        return QRectF(0,0,self.width,self.height).normalized()

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
     
    
    def mouseReleaseEvent(self, event:QGraphicsSceneMouseEvent) :
        super().mouseReleaseEvent(event)
        self.setSelected(False)

    def AppendEdge(self,*args):
        for i in args: self.edges.append(i)

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setPlainText(self._title)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        self.title_item.setTextInteractionFlags(Qt.TextEditable)
        self.UpdateNode()
        self.title_item.keyReleaseEvent = self.UpdateNode
        # self.title_item.setFlag(QGraphicsItem.ItemIsMovable)
    def initH(self):
        self.h_item = QGraphicsTextItem(self)
        self.h_item.setPlainText(f"h({self.node.h})")
        self.hposx = (self.boundingRect().width() / 2) - ( self.h_item.boundingRect().width() /2) 
        self.hposy = (self.boundingRect().height() / 2) -( self.h_item.boundingRect().height() /2) + 15
        self.h_item.setPos(self.hposx,self.hposy)
        self.h_item.setDefaultTextColor(self._title_color)
        self.h_item.setFont(self._title_font)
    
    

    @property
    def title(self): return self._title

    @title.setter
    def title(self, value):
        self._title = value
    
    def paint(self, painter:QPainter, QStyleOptionGraphicsItem, widget=None):
       self.setToolTip(f"{self.node.title}\nH = {self.node.h}\nG = {self.node.G}")
       path_title = QPainterPath()
       path_title.addEllipse(0,0,50,50)
       painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
       painter.setBrush(self._brush_title)
       painter.drawPath(path_title.simplified())
    
    def contextMenuEvent(self, event:QGraphicsSceneContextMenuEvent):
        contextmenu = QMenu()
        Addchild = contextmenu.addAction("Add Child")
        SetH = contextmenu.addAction("Set H")
        Search = contextmenu.addAction("Search To Here")
        SaveTheTree = contextmenu.addAction("Save")
        action = contextmenu.exec_(event.screenPos())
        if action == Addchild:
            node = Node("B")
            self.node.addChild(node)
            edgep = Path(self.node,node,cost=5)
            n = NodeGraph(node)
            n.setPos(self.pos().x(),self.pos().y()+ 100)
            edge = PathG(edgep,StartNode=self,EndNode=n)
            self.scene().addItem(n)
            self.scene().addItem(edge)
        elif action == SetH:
            #Widget Creation
            self.t = QSpinBox()
            self.t.setButtonSymbols(QAbstractSpinBox.NoButtons)
            self.t.setStyleSheet("""
            QSpinBox{
                background-color: rgb(27, 29, 35);
                border-radius: 5px;
                border: 2px solid white;
                padding: 5px;
    	        padding-left: 10px;
                color:white;
            }
""")
            self.defaultKeymethode = self.t.keyPressEvent
            self.t.keyPressEvent = self.UpdateNodeH
            self.xt = self.scene().addWidget(self.t)
            self.xt.setPos(self.pos().x() + 50,self.pos().y())
        elif action == Search:
            GeneralSearchAStar(self.node.GetAbsoluteParent(),self.node)
        elif action == SaveTheTree:
            self.node.moveToFile()





    def UpdateNodeH(self,event:QKeyEvent):
        if(event.key() == 16777220 or event.key() == 16777221):
            self.node.h = self.t.value()
            self.h_item.setPlainText(f"h({self.node.h})")
            self.scene().removeItem(self.xt)
            self.UpdateNode()
            del self.t
            del self.xt
            return
        self.defaultKeymethode(event)

    def UpdateNode(self,event=None):
        self.tposx = (self.boundingRect().width() / 2) - ( self.title_item.boundingRect().width() /2) 
        self.tposy = (self.boundingRect().height() / 2) -( self.title_item.boundingRect().height() /2)
        self.hposx = (self.boundingRect().width() / 2) - ( self.h_item.boundingRect().width() /2) 
        self.hposy = (self.boundingRect().height() / 2) -( self.h_item.boundingRect().height() /2) + 15
        self.h_item.setPos(self.hposx,self.hposy)
        self.title_item.setPos(self.tposx,self.tposy)
        self.node.title = self.title_item.toPlainText()
