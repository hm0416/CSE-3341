class ParseTree:
    def __init__(self, rightNode, leftNode, nodeName):
        self.rightNode = rightNode
        self.leftNode = leftNode
        self.nodeName = nodeName

    def printTree(self, treeNode):
        tree = ""
        if treeNode.rightNode != None:
            tree += self.printTree(treeNode.rightNode)
        if treeNode.leftNode != None:
            tree += self.printTree(treeNode.leftNode)
        tree += " " + treeNode.nodeName + " "

        return tree