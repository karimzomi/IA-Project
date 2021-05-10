from PySide6.QtGui import QContextMenuEvent, QKeyEvent, QPainter
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from Nodes.NodeG import NodeGraph
from Nodes.Node import Node

class TreeGraphics(QGraphicsView):
    def __init__(self, grscene:QGraphicsScene ,parent=None):
        super().__init__(parent)
        self.grscene = grscene
        self.initUI()
        self.setScene(grscene)
    

    def initUI(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setDragMode(QGraphicsView.RubberBandDrag)

    # def contextMenuEvent(self, event:QContextMenuEvent):
    #     item = self.itemAt(event.globalPos()) 
    #     if(item is None):
    #         contextmenu = QMenu()
    #         Add_Node = contextmenu.addAction("Add_Node")
    #         action = contextmenu.exec_(event.globalPos())
    #         if action == Add_Node:
    #             self.AddNode()

    def AddNode(self,Pos):
        self.nodes = Node("S")
        ng = NodeGraph(self.nodes)
        ng.setPos(Pos.x(),Pos.y())
        self.scene().addItem(ng)
        
    