class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return "\n".join(self._traverse(self.root))

    def _traverse(self, node, prefix=""):
        result = []
        if node.is_end:
            result.append(f"End of word: {prefix}")
        for key, child in node.children.items():
            result.append
            result.append(f"{prefix + key}")
            result.extend(self._traverse(child, prefix + key + " -> "))
        return result

    def insert(self, strings):
        current = self.root
        for i in strings:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.is_end = True


t = int(input())
trie = Trie()
for _ in range(t):
    arr = input().split()
    trie.insert(arr[1:])
    print(trie)
