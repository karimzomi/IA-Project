from Serialization import Serializable
import json
class Node(Serializable):
    def __init__(self,title=None,State=[3,3,1],h=None,Parent=None):
        super().__init__()
        self.title = title if(title is not None) else str(State)
        self.h = h if(h is not None) else (State[0]+State[1])/2

        #[cannibales,missionnaires,bateau 1]
        self.STATE = State
        #####################################################
        self.G = 0
        self.F = self.h + self.G

        self.children = []
        self.parent = Parent

    @property
    def G(self):
        return self._G
    @G.setter
    def G(self,value):
        self._G = value
        self.F = self.h + self.G

    def addChild(self,node):
        self.children.append(node)
        node.parent = self
    
    def removeChild(self,node):
        self.children.remove(node)
        node.parent = None

    def GetAbsoluteParent(self):
        currentNode = self
        while currentNode.parent is not None:
            currentNode = currentNode.parent
        return currentNode

    def GetParentsList(self):
        currentNode = self
        result = [self.STATE]
        while currentNode.parent is not None:
            currentNode = currentNode.parent
            result.append(currentNode.STATE)
        return result
    
    @property
    def title(self): return self._title
    
    @title.setter
    def title(self, value):
        self._title = value
    
    def serialize(self):
        children = []
        for item in self.children:
            children.append(
                item.serialize()
            )
        return {
            'id':self.id,
            'parentId':self.parent.id if self.parent is not None else None,
            'title':self.title,
            'G':self.G,
            'F':self.F,
            'H':self.h,
            'children':children
        }
    def moveToFile(self,filename="NewNode"):
        with open(filename,"w") as file:
            file.write(json.dumps( self.serialize(),indent=4))
    
    def LoadFromFile(self,filename):
        with open(filename,"r") as file:
            data = file.read()
            data = json.loads(data)
            self.deserialize(data)