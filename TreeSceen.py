from PySide6.QtGui import QBrush, QColor, QKeyEvent
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

class TreeSceen(QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.SceneWidth = 5000
        self.SceneHeight = 5000
        self.initUI()

    def initUI(self):
        self.setSceneRect(-self.SceneWidth//2,-self.SceneHeight//2,self.SceneWidth,self.SceneHeight)
        self.setBackgroundBrush(QBrush(QColor("#1f1f1f")))


    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        if(event.key() == Qt.Key_Delete):
            for item in self.selectedItems():
                self.removeItem(item)
                del item

    
    