class TrieNode:
    def __init__(self):
        self.node = ['/']*26
        self.isEnd = False
        self.word = ''


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
        node.word = str_in
        node.isEnd = True

    def search(self, str_sr):
        node = self.root_node
        for s in str_sr:
            offset = ord(s)-ord('a')
            if node.node[offset] == '/':
                print('No such string. {}'.format(str_sr))
                return
            node = node.node[offset]
        word_list = []
        self.visit_node(node, word_list)
        return word_list

    def visit_node(self, node, word_list):
        if node.isEnd is True:
            word_list.append(node.word)
        hav_aft = 0
        for i in node.node:
            if i != '/':
                self.visit_node(i, word_list)
                hav_aft = 1
        if hav_aft == 0:
            return


if __name__ == "__main__":
    try_trie = Trie()
    try_trie.insert('hello')
    try_trie.insert('her')
    try_trie.insert('hery')
    try_trie.insert('herybaby')
    try_trie.insert('take')
    try_trie.insert('tap')
    print(try_trie.search('her'))
    #try_trie.search('he')
    try_trie.search('his')