class Node:
    def __init__(self, word, codeword):
        self.word = word
        self.codeword = codeword
        self.isWord = False
        self.sibling = None
        self.child = None
    
    def getWord(self):
        return self.word

    def getCodeword(self):
        return self.codeword
    
    def getIsWord(self):
        return self.isWord
    
    def setIsWord(self, isWord):
        self.isWord = isWord
    
    def getSibling(self):
        return self.sibling
    
    def setSibling(self, sibling):
        self.sibling = sibling

    def getChild(self):
        return self.child
    
    def setChild(self, child):
        self.child = child