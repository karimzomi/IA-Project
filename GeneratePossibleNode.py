from Nodes.Node import Node

class ProblemMC():
    def __init__(self):
        self.movesToRight = [[-2, 0], [-1, -1], [0, -2], [-1, 0], [0, -1]]
        self.movesToLeft = [[2, 0], [1, 1], [0, 2], [1, 0], [0, 1]]

    def GeneratePossibleNodes(self,node:Node):
        state = node.STATE
        # result = []
        if(state[2] == 1):
            moves = self.movesToRight
            boat = 0
        else:
            moves =  self.movesToLeft
            boat = 1
        for i in moves:
            x = [state[0]+i[0],state[1]+i[1],boat]
            if(self.CheckState(x)):
                # result.append(x)
                Child = Node(h=(x[0]+x[1])/2,State=x)
                node.addChild(Child)
                Child.G = Child.parent.G + abs(i[0])+abs(i[1])
        # return result

    def CheckState(self,state): 
        if state[1] > state[0] and not state[0] == 0:
            return False

        if state[1] < state[0] and not state[0] == 3:
            return False

        if state[0] > 3 or state[0] < 0:
            return False
        if state[1] > 3 or state[1] < 0:
            return False
        if state[2] > 1 or state[2] < 0:
            return False

        return True


# C=2 M=1  ----------- c=1 m=2