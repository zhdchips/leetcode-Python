class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if not c in node.children:
                newTrie = Trie()
                node.children[c] = newTrie
            node = node.children[c]
        node.end = True

    def searchNode(self, word: str) -> Trie:
        node = self
        for c in word:
            if not c in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self.searchNode(word)
        return node is not None and node.end

        

    def startsWith(self, prefix: str) -> bool:
        node = self.searchNode(prefix)
        return node is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)