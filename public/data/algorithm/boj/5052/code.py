import sys

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        current = self.root
        for i in number:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
            if current.is_end:
                return False
        if current.children:
            return False
        current.is_end = True
        return True


def is_consistent(numbers):
    trie = Trie()
    for number in numbers:
        if not trie.insert(number):
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    nums = sorted([input().strip() for _ in range(n)])
    print(is_consistent(nums))
