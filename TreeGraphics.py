from PySide6.QtGui import QPainter
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
        self.setRenderHints(QPainter.Antialiasing  | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.RubberBandDrag)

    def AddNode(self,Pos):
        self.nodes = Node("S")
        ng = NodeGraph(self.nodes)
        ng.setPos(Pos.x(),Pos.y())
        self.scene().addItem(ng)