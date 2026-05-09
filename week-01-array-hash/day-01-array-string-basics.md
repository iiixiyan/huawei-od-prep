# Day 01: Array/String Basics

## 📖 知识点讲解

### Python 字符串操作基础

字符串在 Python 中是不可变（immutable）的序列类型，底层通过字符数组存储。常用操作：

| 操作 | 方法/语法 | 说明 |
|------|-----------|------|
| 索引 | `s[i]` | O(1) 随机访问 |
| 切片 | `s[i:j:k]` | 左闭右开，O(k) |
| 拼接 | `s1 + s2` | O(n+m)，产生新字符串 |
| 列表互转 | `list(s)`, `''.join(arr)` | 字符数组 ↔ 字符串 |
| 整除判断 | `s1 * k == s2` | 字符串重复构成判断 |

### 辗转相除法（GCD）

```python
def gcd(a: int, b: int) -> int:
    """欧几里得算法求最大公约数"""
    while b:
        a, b = b, a % b
    return a
```

### 双指针模板（交替合并）

```python
def merge_alternately(word1: str, word2: str) -> str:
    i, j = 0, 0
    res = []
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res.append(word1[i])
            i += 1
        if j < len(word2):
            res.append(word2[j])
            j += 1
    return ''.join(res)
```

---

## 🧩 刷题任务

### 题目1：Merge Strings Alternately（交替合并字符串）
**难度**：⭐
**题目描述**：
给你两个字符串 `word1` 和 `word2`。请按交替顺序合并它们：先取 `word1[0]`，再取 `word2[0]`，然后是 `word1[1]`，`word2[1]`，依此类推。如果一个字符串比另一个长，剩余字符直接拼接到末尾。

**思路分析**：
1. 使用双指针 `i`, `j` 分别遍历两个字符串
2. 每次循环交替添加字符，直到两个字符串都遍历完
3. 用列表收集字符最后 `join`，避免频繁字符串拼接

- 时间复杂度：O(n + m)
- 空间复杂度：O(1)（不计输出空间）

**参考代码**：
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        res = []
        
        while i < m or j < n:
            if i < m:
                res.append(word1[i])
                i += 1
            if j < n:
                res.append(word2[j])
                j += 1
        
        return ''.join(res)
```

---

### 题目2：Greatest Common Divisor of Strings（字符串的最大公因子）
**难度**：⭐⭐
**题目描述**：
对于字符串 `s` 和 `t`，如果存在字符串 `x` 使得 `s = x + x + ... + x`（`t` 同理），则称 `x` 是 `s` 和 `t` 的"公因子"。请找到 `str1` 和 `str2` 的最大公因子字符串。若不存在，返回空字符串。

**思路分析**：
1. 如果 `str1 + str2 != str2 + str1`，说明没有公因子，直接返回 `""`
2. 找出 `len(str1)` 和 `len(str2)` 的最大公约数 `g`
3. 返回 `str1[:g]`

核心思想：字符串的 GCD 长度就是两个字符串长度的 GCD。

- 时间复杂度：O(n + m)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 如果拼接结果不等，说明没有公因子
        if str1 + str2 != str2 + str1:
            return ""
        
        # 求长度的最大公约数
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        g = gcd(len(str1), len(str2))
        return str1[:g]
```

---

### 题目3：Kids With the Greatest Number of Candies（拥有最多糖果的孩子）
**难度**：⭐
**题目描述**：
有 `n` 个孩子，每个孩子有 `candies[i]` 颗糖果。现在有 `extraCandies` 颗额外糖果，你可以全部给任意一个孩子。对每个孩子，判断如果把所有额外糖果给他，他能否成为拥有最多糖果的孩子（允许并列最多）。

**思路分析**：
1. 先遍历一次找出当前最大糖果数 `max_candy`
2. 再遍历每个孩子，判断 `candies[i] + extraCandies >= max_candy`

- 时间复杂度：O(n)
- 空间复杂度：O(1)（不计输出空间）

**参考代码**：
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [c + extraCandies >= max_candy for c in candies]
```
