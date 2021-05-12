from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Mc_shapes(QGraphicsObject):
    def __init__(self,color,shape="rect",size=(20,20),parent=None):
        super().__init__(parent=parent)
        self.mypen = QPen(Qt.black)
        self.mypen.setWidth(1)
        self.mcshape = shape
        self.mcsize = size
        self.color = color


    def boundingRect(self):
        return QRectF(0,0,self.mcsize[0],self.mcsize[1])

    def paint(self, painter:QPainter,option,widget):
        path = QPainterPath()
        if(self.mcshape == "circle"):
            path.addEllipse(0,0,self.mcsize[0],self.mcsize[1])
            painter.setPen(self.mypen)
            painter.setBrush(QBrush(self.color))
            painter.drawPath(path.simplified())
        else:
            path.addRect(0,0,self.mcsize[0],self.mcsize[1])
            painter.setPen(self.mypen)
            painter.setBrush(QBrush(self.color))
            painter.drawPath(path.simplified())

