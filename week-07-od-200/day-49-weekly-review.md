# Day 49: 周复习 — 200分错题复盘 + 专项练习

## 📖 本周学习内容总览

| 天数 | 题目 | 类别 | 核心知识点 |
|------|------|------|-----------|
| Day 43 | 中文分词模拟器 | 字符串 | Trie树 + DFS/DP回溯 |
| Day 44 | 二进制差异数 | 数组/位运算 | 位运算性质 + 子集枚举 |
| Day 45 | 创建二叉树 | 树/图 | BST建树 + 层次遍历 |
| Day 46 | 最大平分数组 | DP | 状态压缩 + 回溯剪枝 |
| Day 47 | 模拟目录管理功能 | 模拟 | 树结构模拟 + 路径解析 |
| Day 48 | 贪心歌手 & 空栈压数 | 综合 | TSP状态压缩DP + 栈模拟 |

---

## 🎯 高频错误复盘

### 错误1：Trie树实现细节漏了
**问题**：中文分词模拟器中，忘记处理 `is_end` 标记，导致只匹配了前缀而非完整词。
**解法**：Trie 节点必须明确区分「路径节点」和「单词结束节点」。

### 错误2：子集枚举中的重复统计
**问题**：二进制差异数中，枚举补集子集时未去重，导致 (x,y) 和 (y,x) 被算了两次。
**解法**：加 `if y > x` 条件或最后 `ans //= 2`。

### 错误3：二叉树插入深度约束理解偏了
**问题**：创建二叉树时，把「深度不够就插入」和「深度到了但位置被占就插入失败」搞混。
**解法**：画图模拟每个步骤，按规则逐条翻译成代码。

### 错误4：状态压缩DP的状态转移边界
**问题**：最大平分数组中，DFS回溯的剪枝条件 `if cur_sum == 0: return False` 漏了会导致指数级超时。
**解法**：这个剪枝至关重要——第一个元素放不进当前子集说明此路不通，直接返回。

### 错误5：路径解析的绝对/相对路径处理
**问题**：目录管理中，`cd /a/b` 绝对路径处理错误，没有从根重新开始。
**解法**：绝对路径以 `/` 开头，必须重置当前路径到根再遍历。

### 错误6：栈合并的循环条件
**问题**：空栈压数中，合并后的新数可能与新的栈顶再次相等，需要 `while` 而非 `if`。
**解法**：用 `while stack and stack[-1] == x` 反复合并。

---

## 🧪 专项练习

### 练习1：Trie + DFS 综合
**题目**：给定词典 ["cat","cats","and","sand","dog"]，字符串 "catsanddog"，输出所有分词方案。
**要求**：手写 Trie 插入 + DFS 搜索，5分钟内完成。

<details>
<summary>参考答案</summary>

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, w):
        n = self.root
        for c in w:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.is_end = True
    def search(self, s, start):
        n = self.root
        ends = []
        for i in range(start, len(s)):
            if s[i] not in n.children:
                break
            n = n.children[s[i]]
            if n.is_end:
                ends.append(i+1)
        return ends

def word_break(s, wordDict):
    trie = Trie()
    for w in wordDict:
        trie.insert(w)
    res = []
    def dfs(st, path):
        if st == len(s):
            res.append(' '.join(path))
            return
        for end in trie.search(s, st):
            dfs(end, path + [s[st:end]])
    dfs(0, [])
    return res
```
</details>

---

### 练习2：位运算子集枚举
**题目**：给定数 x=13（二进制 1101），枚举其所有子集（包括 0 和自身），并打印。
**要求**：使用 `sub = (sub-1) & x` 技巧，3分钟内完成。

<details>
<summary>参考答案</summary>

```python
x = 13
sub = x
while True:
    print(bin(sub), sub)
    if sub == 0:
        break
    sub = (sub - 1) & x
# 输出: 0b1101 13, 0b1100 12, 0b1001 9, 0b1000 8, 0b0101 5, 0b0100 4, 0b0001 1, 0b0000 0
```
</details>

---

### 练习3：栈合并模拟
**题目**：输入 `3 3 3`，模拟空栈压数过程，写出每步结果。
**要求**：手推，2分钟内完成。

<details>
<summary>参考答案</summary>

- 入 3: [3]
- 入 3: 栈顶3==3 → 弹出3,3，得 (3+3)*2=12，入12 → [12]
- 入 3: 栈顶12≠3 → 直接入 → [12, 3]
- 最终: [12, 3]
</details>

---

### 练习4：状态压缩DP模板
**题目**：手写 TSP 问题（旅行商）的状态压缩 DP 模板。
**要求**：5分钟内写出 `dp[mask][last]` 的转移框架。

<details>
<summary>参考答案</summary>

```python
N = 5
dist = [[0]*N for _ in range(N)]  # 距离矩阵
INF = float('inf')
size = 1 << N
dp = [[INF]*N for _ in range(size)]
dp[1][0] = 0  # 从0出发

for mask in range(1, size):
    for last in range(N):
        if dp[mask][last] == INF:
            continue
        for nxt in range(N):
            if mask & (1 << nxt):
                continue
            new = mask | (1 << nxt)
            dp[new][nxt] = min(dp[new][nxt], dp[mask][last] + dist[last][nxt])

# 回到起点
ans = min(dp[size-1][i] + dist[i][0] for i in range(N))
```
</details>

---

### 练习5：目录管理完整实现
**题目**：在 15 分钟内，不参考任何资料，完整实现 Day 47 的目录管理器（含 mkdir, cd, pwd, ls, rmdir）。

---

## 📊 200分题型速查表

| 题型 | 数据范围信号 | 常见解法 | 时间复杂度 |
|------|-------------|---------|-----------|
| **字符串** | 句子长 ≤ 100, 词典 ≤ 500 | Trie + DP/DFS | O(L × 词长) |
| **位运算** | 数值 ≤ 2^20, N ≤ 10^5 | 子集枚举/SOS DP | O(N × 2^popcount) |
| **树** | N ≤ 1000 | 模拟建树 + BFS | O(N × H) |
| **图/状态压缩** | N ≤ 15 | 状态压缩 DP | O(N² × 2^N) |
| **模拟** | 命令数 ≤ 1000 | 按规则模拟 | O(命令数) |
| **栈** | N ≤ 10^5 | 栈模拟 | O(N) |
| **背包/划分** | N ≤ 15 | 回溯剪枝/DP | O(N × 2^N) |

---

## 💡 考前提醒

1. **200分题的时间分配**：每道题建议最多 50 分钟，实在没思路就写暴力拿部分分。
2. **输入输出格式**：注意题目要求的输出格式，多一个空格都可能判错。
3. **Python 性能优化**：用 `sys.stdin.read()` 快速读入；递归深度超限时用 `sys.setrecursionlimit()`。
4. **调试策略**：先写核心逻辑，再加边界条件。无法本地运行时，在脑中模拟小数据。
5. **心态调整**：200分题不会全做正常，拿 60%-70% 的分数已经很不错。优先保证 100分题全对。
