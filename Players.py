class Players:
    def __init__(self, root):
        self.root = root
        self.previous = None

    def setPrevious(self, previous):
        self.previous = previous
    def getPrevious(self):
        return self.previous
    def setRoot(self, root):
        self.root = root
    def getRoot(self):
        return self.root

