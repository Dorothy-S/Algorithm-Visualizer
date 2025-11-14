# Ternary Trie Node
class TernaryNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end = False


# Ternary Trie
class TernaryTrie:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if word:
            self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        ch = word[index]

        if node is None:
            node = TernaryNode(ch)

        if ch < node.char:
            node.left = self._insert(node.left, word, index)
        elif ch > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.middle = self._insert(node.middle, word, index + 1)
            else:
                node.is_end = True

        return node

    # Autocomplete
    def autocomplete(self, prefix):
        results = []
        node = self._search(self.root, prefix, 0)

        if node:
            if node.is_end:
                results.append(prefix)
            self._dfs(node.middle, prefix, results)

        return results

    # Search for prefix
    def _search(self, node, prefix, index):
        if node is None or index >= len(prefix):
            return None

        ch = prefix[index]

        if ch < node.char:
            return self._search(node.left, prefix, index)
        elif ch > node.char:
            return self._search(node.right, prefix, index)
        else:
            if index == len(prefix) - 1:
                return node
            return self._search(node.middle, prefix, index + 1)

    # DFS from a node
    def _dfs(self, node, path, results):
        if node is None:
            return

        # Explore left subtree
        self._dfs(node.left, path, results)

        # If end of a word, add it
        if node.is_end:
            results.append(path + node.char)

        # Continue middle path
        self._dfs(node.middle, path + node.char, results)

        # Explore right subtree
        self._dfs(node.right, path, results)


# Test
print("\nTernary Trie Example")
words = ["Sample", "Samplers", "Same", "Sampling", "Summer", "Sad"]

ternary_trie = TernaryTrie()

for w in words:
    ternary_trie.insert(w)

print("Suggestions for 'Sam':", ternary_trie.autocomplete("Sam"))
