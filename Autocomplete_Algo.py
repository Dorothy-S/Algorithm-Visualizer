# Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# Standard Trie
class StandardTrie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word into trie
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    # Search prefix and return all words that start with that prefix
    def autocomplete(self, prefix):
        results = []
        curr = self.root

        # First go to the end of the prefix
        for ch in prefix:
            if ch not in curr.children:
                return results  # empty list
            curr = curr.children[ch]

        # DFS from this node
        self._dfs(curr, prefix, results)
        return results

    # DFS helper function
    def _dfs(self, node, path, results):
        if node.is_end:
            results.append(path)

        for ch in node.children:
            self._dfs(node.children[ch], path + ch, results)


# Test
print("Standard Trie Example")

words = ["Sample", "Samplers", "Same", "Sampling", "Summer", "Sad"]
std_trie = StandardTrie()

for w in words:
    std_trie.insert(w)

print("Suggestions for 'Sam':", std_trie.autocomplete("Sam"))
