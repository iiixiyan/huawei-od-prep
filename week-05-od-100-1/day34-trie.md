# Day 34: Trie（前缀树）

## 📖 知识点
**Trie(前缀树)** — 高效存储和检索字符串集合的树形数据结构.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```
**核心操作**:
- 插入: 沿着路径逐字符创建节点.
- 搜索: 沿着路径逐字符查找.
- 前缀匹配: 判断是否存在以给定前缀开头的单词.
- 通配符搜索: DFS匹配'.'(任意字符).

## 🧩 刷题任务（6题）

### 1. Implement Trie (Prefix Tree)（⭐⭐） 来源：L75/T150/O
**思路**：实现Trie类的insert,search,startsWith三个方法.用字典存储子节点.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
```

### 2. Search Suggestions System（⭐⭐） 来源：L75
**思路**：对products排序后构建Trie(或直接排序+二分).每个节点存储该前缀下的前3个推荐(按字典序).也可以在Trie节点存推荐列表.
```python
def suggestedProducts(self, products, searchWord):
    products.sort()
    root = {}
    # 构建Trie,每个节点存字典序前三的推荐
    for p in products:
        node = root
        for c in p:
            if c not in node:
                node[c] = {}
            node = node[c]
            if 'suggest' not in node:
                node['suggest'] = []
            if len(node['suggest']) < 3:
                node['suggest'].append(p)
    
    res = []
    node = root
    for c in searchWord:
        if c in node:
            node = node[c]
            res.append(node.get('suggest', []))
        else:
            # 后续都为空
            node = {}
            res.append([])
    return res
```

### 3. Add and Search Word（⭐⭐） 来源：T150
**思路**：支持通配符'.'(匹配任意字符)的Trie.search时遇到'.'需DFS遍历所有子节点.
```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word):
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            c = word[idx]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(node.children[c], idx + 1)
        
        return dfs(self.root, 0)
```

### 4. Word Search II（⭐⭐⭐） 来源：T150
**思路**：Trie + 回溯.先将words构建Trie,然后在board上DFS搜索,同时沿Trie节点移动,匹配到完整单词则加入结果.用'#'标记已访问单元格.
```python
def findWords(self, board, words):
    # 构建Trie
    root = {}
    for w in words:
        node = root
        for c in w:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = w  # 用'#'存储完整单词
    
    m, n = len(board), len(board[0])
    res = []
    
    def dfs(i, j, node):
        if '#' in node:
            res.append(node.pop('#'))  # 去重
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node:
            return
        c, board[i][j] = board[i][j], '*'
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(i+di, j+dj, node[c])
        board[i][j] = c
    
    for i in range(m):
        for j in range(n):
            if board[i][j] in root:
                dfs(i, j, root)
    return res
```

### 5. Replace Words（⭐⭐） 来源：O
**思路**：构建Trie存储词根.对句子每个单词,在Trie中查找最短前缀(词根),找到则替换.
```python
def replaceWords(self, dictionary, sentence):
    root = {}
    for word in dictionary:
        node = root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = True  # 标记为词根结尾
    
    def replace(word):
        node = root
        for i, c in enumerate(word):
            if '*' in node:
                return word[:i]
            if c not in node:
                return word
            node = node[c]
        return word
    
    return ' '.join(replace(w) for w in sentence.split())
```

### 6. Magic Dictionary（⭐⭐） 来源：O
**思路**：前缀树+容错搜索.搜索时允许恰好1个字符不同.在search时跟踪是否已使用一次修改机会.
```python
class MagicDictionary:
    def __init__(self):
        self.root = {}
    
    def buildDict(self, dictionary):
        for w in dictionary:
            node = self.root
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True
    
    def search(self, searchWord):
        def dfs(node, idx, modified):
            if idx == len(searchWord):
                return '#' in node and modified
            c = searchWord[idx]
            for child_char, child_node in node.items():
                if child_char == '#':
                    continue
                if child_char == c:
                    if dfs(child_node, idx + 1, modified):
                        return True
                elif not modified:
                    if dfs(child_node, idx + 1, True):
                        return True
            return False
        
        return dfs(self.root, 0, False)
```

## 📝 总结
- Trie本质: 多叉树,每个节点存子节点映射和结束标记.
- 通配符: '.'匹配任意字符,DFS遍历所有子节点.
- Trie+回溯: 网格搜索时同时推进Trie节点,大幅优化.
- 前缀替换: 沿Trie查找最短前缀.
- 容错搜索: 在DFS中记录修改次数,精确控制错误容忍度.
