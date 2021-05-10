from Nodes.Node import Node
from GeneratePossibleNode import ProblemMC
import time

def PrintList(l,s="O"):
    result = f"{s}"+"{"
    for i in l:
        result +=f"{i.title}({i.G},{i.F},{i.h})"
    print(result+"}")

def ContainNode(List,node):
    j = 0
    for i in List:
        if(i.title == node.title):return j
        j+=1
    return -1

def GeneralSearchAStar(node:Node,Goal:Node):
    currentNode = node
    OpenList = [currentNode]
    CloseList = []
    PrintList(OpenList)
    PrintList(CloseList,"F")
    while currentNode != Goal and (ContainNode(OpenList,Goal) == -1):
        currentNode = OpenList.pop(0)
        for item in currentNode.children:
            f = ContainNode(CloseList,item)
            if(f != -1):
                if(CloseList[f].F > item.F):
                    OpenList.append(item)
                continue
            k = ContainNode(OpenList,item)
            if (k != -1):
                if(OpenList[k].F > item.F):
                    OpenList[k] = item
            else:
                OpenList.append(item)
        
        OpenList.sort(key=lambda node: node.F)
        CloseList.append(currentNode)
        PrintList(OpenList)
        PrintList(CloseList,"F")
    return OpenList

def MCSearchAStar(node:Node,Goal:Node):
    currentNode = node
    OpenList = [currentNode]
    CloseList = []
    PrintList(OpenList)
    PrintList(CloseList,"F") 
    while (ContainNode(OpenList,Goal) == -1):
        currentNode = OpenList.pop(0)
        ProblemMC().GeneratePossibleNodes(currentNode)

        for item in currentNode.children:
            f = ContainNode(CloseList,item)

            if(f != -1):
                if(CloseList[f].F > item.F):
                    OpenList.append(item)
                continue

            k = ContainNode(OpenList,item)
            if (k != -1):
                if(OpenList[k].F > item.F):
                    OpenList[k] = item
            else:
                OpenList.append(item)
        
        OpenList.sort(key=lambda node: node.F)

        CloseList.append(currentNode)
        PrintList(OpenList)
        PrintList(CloseList,"F")

# s = time.time()
# x = Node()
# x1 = Node(State=[0,0,0])
# MCSearchAStar(x,x1)
# print(time.time() - s)


