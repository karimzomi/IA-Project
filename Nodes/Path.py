class Path():
    def __init__(self,nodeB,nodeE,cost:int):
        self.nodeB = nodeB
        self.nodeE = nodeE
        self.cost = cost
    
    @property
    def cost(self): return self._cost
    @cost.setter
    def cost(self,value):
        self._cost = value
        self.nodeE.G = (self.nodeB.G + self._cost)
        self.nodeE.F = self.nodeE.h + self.nodeE.G

    