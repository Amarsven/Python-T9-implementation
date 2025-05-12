
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __setitem__(self, word, value):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def with_prefix(self, prefix):
        result = []
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return result
            node = node.children[char]
        self._dfs(node, prefix.lower(), result)
        return result

    def _dfs(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, result)


import time
import sys
import itertools

run_time = time.time()

def t9_prediction(string, t9):
    for word in t.with_prefix(string.lower()):
        if len(word) == len(string):
            t9.append(word)
            return t9

words = [line.strip().decode("utf-8").lower() for line in open(sys.argv[1], "rb")]

t = Trie()
for word in words:
    t[word] = 1

mapping = {1: ['p', 'P', 'q', 'Q', 'r', 'R', 's', 'S'], 2: ['t', 'T', 'u', 'U', 'v', 'V'], 3: ['w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'], 4: ['g', 'G', 'h', 'H', 'i', 'I'], 5: ['j', 'J', 'k', 'K', 'l', 'L'], 6: ['m', 'M', 'n', 'N', 'o', 'O'], 8: ['a', 'A', 'b', 'B', 'c', 'C'], 9: ['d', 'D', 'e', 'E', 'f', 'F']}

while True:
    try:
        user_input = input("Enter numpad digits (use 0 to separate words, or type 'exit' to quit): ")
        if user_input.lower() in ["exit", "quit"]:
            break
        my_inputs = user_input.split("0")
    except:
        continue

    for numbers in my_inputs:
        digits = list(map(int, str(numbers)))
        strings = [''.join(combo).lower() for combo in itertools.product(*(mapping[d] for d in digits if d in mapping))]
        t9 = []
        for string in strings:
            t9_prediction(string, t9)

        t9 = sorted(set(filter(None, t9)))
        if t9:
            print(t9[0], end=" ")

    print("\n")


D = {v: k for k, vlist in mapping.items() for v in vlist}
groups = itertools.groupby(sorted(t9), key=lambda x: D.get(x[0], 0))

# REMOVE THIS FINAL BLOCK
# print("\n")
# for k, g in groups:
#     g = list(g)
#     if len(g) > 1:
#         print(g, end=" ")
#     else:
#         print(g[0], end=" ")

print("\n")

print("Program run time (s):", time.time() - run_time)
