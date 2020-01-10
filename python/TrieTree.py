class TrieNode:
    def __init__(self):
        self.node = ['/']*26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, str_in):
        node = self.root_node
        for s in str_in:
            offset = ord(s)-ord('a')
            if node.node[offset] == '/':
                node.node[offset] = TrieNode()
            node = node.node[offset]
        node.isEnd = True

    def search(self, str_sr):
        node = self.root_node
        for s in str_sr:
            offset = ord(s)-ord('a')
            if node.node[offset] == '/':
                print('No such string. {}'.format(str_sr))
                return
            node = node.node[offset]
        if node.isEnd is True:
            print('Complete.')
            return str_sr
        else:
            print('Not complete.')
            return str_sr


if __name__ == "__main__":
    try_trie = Trie()
    try_trie.insert('hello')
    try_trie.insert('her')
    try_trie.insert('take')
    try_trie.insert('tap')
    try_trie.search('her')
    try_trie.search('he')
    try_trie.search('his')