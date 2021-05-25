from PySide6.QtCore import QRectF
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Animeview(QGraphicsView):
    def __init__(self, grscene:QGraphicsScene ,parent=None):
        super().__init__(parent)
        self.grscene = grscene

        self.cannibales = []
        self.missionaires = []

        self.mypen = QPen(Qt.black)
        self.mypen.setWidth(2)

        self.mybluebrush = QBrush(Qt.blue)
        self.myGreenbrush = QBrush(Qt.green)

        self.initUI()
        self.setScene(grscene)

    def drawBackground(self, painter:QPainter, rect: QRectF) -> None:
        super().drawBackground(painter, rect)
        painter.setPen(self.mypen)
        painter.setBrush(self.myGreenbrush)
        painter.drawRect(int(rect.left()),int(rect.top()),self.size().width()/3,self.size().height())
        painter.setBrush(self.mybluebrush)
        painter.drawRect(int(rect.left() + self.size().width()/3),int(rect.top()),self.size().width()/3,self.size().height())
        painter.setBrush(self.myGreenbrush)
        painter.drawRect(int(rect.left() + self.size().width()*2/3),int(rect.top()),self.size().width()/3,self.size().height())
       
    def initUI(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        
        

    

    




