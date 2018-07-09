class Tnode(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.wordComplete = False
        self.visitCount = 0
        self.wordfreq = {}
        self.parent = None

class Trie(object):
    def __init__(self):
        self.root = Tnode(-1)

    def insertWord(self, word):
        cpointer = self.root
        for char in word:
            if char in cpointer.children:
                cpointer = cpointer.children[char]
            else:
                newNode = Tnode(char)
                cpointer.children[char] = newNode
                newNode.parent = cpointer
                cpointer = cpointer.children[char]
        cpointer.wordComplete = True

    def search(self, word):
        cpointer = self.root

        if cpointer.children is False:
            return False
            
        for char in word:
            if char in cpointer.children:
                cpointer =  cpointer.children[char]
            else:
                return False

        if cpointer.wordComplete:
            while cpointer.parent is not None:
                if word in cpointer.wordfreq:
                    cpointer.wordfreq[word] = cpointer.wordfreq[word] + 1
                else:
                    cpointer.wordfreq[word] = 1
                print (cpointer.char, cpointer.wordfreq)
                cpointer = cpointer.parent                
            return True
        return False
            
tree = Trie()
tree.insertWord("Hello")
tree.insertWord("Hell")
print(tree.search("Hell"))
print(tree.search("Hello"))
print(tree.search("Hell"))

