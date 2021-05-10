from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Nodes.Path import Path

class PathG(QGraphicsPathItem):
    def __init__(self,Path:Path,StartNode,EndNode,parent=None):
        super().__init__(parent)
        self.Nodespath = Path
        self._color = Qt.red
        self._color_selected = QColor("#FFFFA637")

        self._pen = QPen(self._color)
        self.pen_selected = QPen(self._color_selected)
        self._pen.setWidth(2)
        self.pen_selected.setWidth(2)

        self.StartNode = StartNode
        self.EndNode = EndNode
        self.StartNodePos=[]
        self.EndNodePos = []

        self.StartNodePos.append(StartNode.pos().x() + 25)
        self.StartNodePos.append(StartNode.pos().y() + 50)
        self.EndNodePos.append(EndNode.pos().x() - 20)
        self.EndNodePos.append(EndNode.pos().y() - 20)


        self.initTitle()
        self.updatepath()
        self.brush = QBrush(self._color)
        self.initUI()



    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setZValue(-1)
    
    def paint(self, painter:QPainter, QStyleOptionGraphicsItem, widget=None):
        self.updatepath()
        painter.setPen(self._pen if not self.isSelected() else self.pen_selected)
        painter.setBrush(Qt.NoBrush)
        path = QPainterPath()
        path.addEllipse(self.EndNodePos[0]-2.5,self.EndNodePos[1],5,5)
        painter.drawPath(path)
        painter.drawPath(self.path())

    def updatepath(self):
        self.StartNodePos[0] = self.StartNode.pos().x() + 25
        self.StartNodePos[1] = self.StartNode.pos().y() + 50
        self.EndNodePos[0] = self.EndNode.pos().x() + self.EndNode.boundingRect().width() /2  
        self.EndNodePos[1] = self.EndNode.pos().y() - 5

        self.CostG_posx = (self.StartNodePos[0] + self.EndNodePos[0]) /2
        self.CostG_posy = (self.StartNodePos[1] + self.EndNodePos[1]) /2
        self.CostG.setPos(self.CostG_posx,self.CostG_posy)

        path = QPainterPath(QPointF(self.StartNodePos[0],self.StartNodePos[1]))
        path.lineTo( self.EndNodePos[0],self.EndNodePos[1])
        self.setPath(path)

    def initTitle(self):
        self.CostG = QGraphicsTextItem(self)
        self.CostG.setPlainText(str(self.Nodespath.cost))
        self.CostG.setTextInteractionFlags(Qt.TextEditable)
        self.CostG.setDefaultTextColor(Qt.white)
        self.CostG.keyReleaseEvent = self.UpdateCost

    def UpdateCost(self,event:QKeyEvent):
        if(event.key() == 16777220 or event.key() == 16777221):
            try:
                self.CostG.clearFocus()
                Value = int(self.CostG.toPlainText())
                self.Nodespath.cost = Value
            except ValueError as e:
                self.CostG.setPlainText(str(self.Nodespath.cost))
    