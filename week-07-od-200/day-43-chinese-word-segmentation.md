# Day 43: 中文分词模拟器（200分·字符串类）

## 📖 前置知识
- **字典树（Trie）**：高效存储和检索字符串集合，支持前缀匹配。核心操作：插入 O(L)、查找 O(L)。
- **动态规划（DP）**：本题用 DP 判断字符串能否被正确切分。`dp[i]` 表示前 i 个字符能否被成功分词。
- **贪心策略 vs DP**：中文分词不能简单用贪心（最长匹配），可能存在多种切分方式，需结合字典判断。

## 🧩 刷题任务

### 题目：中文分词模拟器（200分）

**题目描述**：
给定一个包含若干中文词汇的词典（每个词由中文汉字组成，不含空格），和一个待分词的中文句子（不含标点符号），请实现一个中文分词模拟器。

要求输出所有可能的分词方案。若无法分词，输出空列表。

你需要实现：
1. 词典中的词可以重复使用（每个词可用多次）
2. 输出所有可能的分词方式，词之间用空格分隔
3. 多组结果按字典序排序输出

**输入描述**：
第一行：词典中的词，用空格分隔
第二行：待分词的句子（连续汉字）

**输出描述**：
所有可能的分词方案，每行一种方案，词间用空格分隔。若无法分词，输出 `[]`。

**样例输入**：
```
我们 大家 大学生 学生 大学 学
我们大学生
```

**样例输出**：
```
我们 大学 生
我们 大学生
```

**解释**：两种分词方式均符合词典。

**数据范围**：
- 词典长度 ≤ 500
- 句子长度 ≤ 100
- 每个词长度 ≤ 20

---

**思路分析**：

**核心步骤**：
1. **建 Trie 树**：将词典中的所有词插入 Trie，加速匹配过程。
2. **DFS + 回溯**：
   - 从句子起始位置 i 开始，在 Trie 中查找所有以 i 开头且存在于词典中的词。
   - 对每个匹配到的词，记录到当前路径中，递归处理剩余部分。
   - 若递归到句子末尾（i == len(s)），将当前路径加入结果。
3. **剪枝**：用 `memo[i]` 记忆从位置 i 开始是否有可行解，避免重复搜索。

**复杂度**：
- 时间：O(N × K × 分支因子)，其中 N 为句子长度，K 为词的平均查找长度。实际因剪枝性能尚可。
- 空间：O(词典总字符数 + 递归栈)

---

**参考代码**：
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
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search_prefixes(self, s, start):
        """返回从start位置开始，所有匹配到的词尾下标"""
        node = self.root
        res = []
        for i in range(start, len(s)):
            ch = s[i]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_end:
                res.append(i + 1)  # 匹配结束位置（不包含）
        return res

def segment(dict_words, sentence):
    trie = Trie()
    for w in dict_words:
        trie.insert(w)

    n = len(sentence)
    memo = [None] * (n + 1)  # None=未访问, False=不可达, True=可达
    result = []

    def dfs(start, path):
        if start == n:
            result.append(' '.join(path))
            return True
        if memo[start] is False:
            return False
        found = False
        for end in trie.search_prefixes(sentence, start):
            word = sentence[start:end]
            path.append(word)
            if dfs(end, path):
                found = True
            path.pop()
        memo[start] = found
        return found

    dfs(0, [])
    if not result:
        return ['[]']
    return sorted(result)

# 处理输入
words = input().strip().split()
sentence = input().strip()
res = segment(words, sentence)
for line in res:
    print(line)
```

---

**OD备考提示**：
- **200分题目**常涉及多个知识点的结合（本题 = Trie + DFS + DP）。不要被「中文」迷惑，核心是字符串匹配 + 搜索。
- **结果排序**：务必按照字典序输出结果，否则扣分。
- **剪枝优化**：`memo` 数组是避免超时的关键，不加剪枝在句子长、词典大时会 TLE。
- **边界情况**：句子长度为0、词典为空、句子中有词典中没有的字符等情况需处理。
- **部分得分策略**：如果无法完成全部优化，先保证暴力DFS能跑通小数据，拿到部分分。
