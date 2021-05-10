from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
from Nodes.NodeG import NodeGraph
from Nodes.Node import Node
from PySide6.QtWidgets import *

class TreeSceen(QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        if(event.key() == Qt.Key_Delete):
            for item in self.selectedItems():
                self.removeItem(item)
                del item