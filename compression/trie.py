from node import Node

class Outcomes:
    PRESENT = 0
    ABSENT = 1
    UNKNOWN = 2


class Trie:
    def __init__(self):
        self.root = Node('', '')
        self.size = 0

    def getSize(self):
        return self.size
    

    def search(self, word):
        outcome = Outcomes.UNKNOWN
        i = 0
        current: Node = self.root.getChild()

        while outcome == Outcomes.UNKNOWN:
            if current is None: outcome = Outcomes.ABSENT
            elif current.getWord() == word[i]:
                if i == len(word) - 1: outcome = Outcomes.PRESENT
                else:
                    current = current.getChild()
                    i += 1
            else: current = current.getSibling()

        if outcome != Outcomes.PRESENT: return None
        if current.getIsWord(): return current.getCodeword()
        else: return None

    
    def insert(self, word: str, codeword: str):
        i = 0
        current: Node = self.root
        next: Node = current.getChild()

        while i < len(word):
            if next is not None and next.getWord() == word[i]:
                current = next
                next = current.getChild()
                i += 1
            elif next is not None: next = next.getSibling()
            else:
                x: Node = Node(word[i], codeword)
                x.setSibling(current.getChild())
                current.setChild(x)
                current = x
                next = current.getChild()
                i += 1

        current.setIsWord(True)
        self.size += 1


    def _dfs(self, node: Node, codeword: str, word=''):
        if node.getCodeword() == codeword: return word + node.getWord()
        if node.getChild() is not None:
            res = self._dfs(node.getChild(), codeword, word = word + node.getWord())
            if res: return res
        if node.getSibling() is not None:
            res = self._dfs(node.getSibling(), codeword, word = word)
            if res: return res
        
        return False
    

    def look_up(self, codeword):
        return self._dfs(self.root.getChild(), str(int(codeword, 2)))