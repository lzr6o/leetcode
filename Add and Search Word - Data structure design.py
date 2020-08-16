class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.trie
        for c in word:
            if not c in node:
                node[c] = {}
            node = node[c]
        node["$"] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if not c in node:
                    # if the current character is "."
                    # check all possible nodes at this level
                    if c==".":
                        for x in node:
                            if x!="$" and search_in_node(word[i+1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != "."
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[c]
            return "$" in node
        return search_in_node(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)