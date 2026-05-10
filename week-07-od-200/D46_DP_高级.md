# D46 — DP 高级 (6题)

---

## 1. Edit Distance (L75/T150)

**题目**：给你两个单词 `word1` 和 `word2`， *请返回将 `word1` 转换成 `word2` 所使用的最少操作数*  。

你可以对一个单词进行如下三种操作：

- 插入一个字符

- 删除一个字符

- 替换一个字符

**示例 1：**

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

**提示：**

- `0 <= word1.length, word2.length <= 500`

- `word1` 和 `word2` 由小写英文字母组成

**难度**：中等

**状态定义**：`dp[i][j]` = word1[:i] → word2[:j] 的最小编辑距离
**转移**：
```
if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
else: dp[i][j] = 1 + min(dp[i-1][j],    # 删除
                          dp[i][j-1],    # 插入
                          dp[i-1][j-1])  # 替换
```

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

# 时间 O(m*n), 空间 O(m*n) 可压缩到 O(n)
```

---

## 2. Best Time to Buy and Sell Stock with Transaction Fee (L75)

**状态定义**：
- `hold` = 手上有股票时的最大利润
- `cash` = 手上无股票时的最大利润
**转移**：
- `cash = max(cash, hold + price - fee)`
- `hold = max(hold, cash - price)`

```python
def maxProfit(prices: list[int], fee: int) -> int:
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash

# 时间 O(n), 空间 O(1)
```

---

## 3. Best Time to Buy and Sell Stock III (T150)

**思路**：限 2 笔交易，四种状态
- `buy1, sell1, buy2, sell2`

```python
def maxProfit(prices: list[int]) -> int:
    buy1 = buy2 = float('inf')
    sell1 = sell2 = 0
    for p in prices:
        buy1 = min(buy1, p)
        sell1 = max(sell1, p - buy1)
        buy2 = min(buy2, p - sell1)  # 第二次买入成本 = 价格 - 第一次利润
        sell2 = max(sell2, p - buy2)
    return sell2

# 时间 O(n), 空间 O(1)
```

---

## 4. Best Time to Buy and Sell Stock IV (T150)

**思路**：推广到 k 次交易，当 k ≥ n/2 时退化为无限次
`buy[j]`, `sell[j]` 表示第 j 次交易后的状态

```python
def maxProfit(k: int, prices: list[int]) -> int:
    n = len(prices)
    if n < 2 or k == 0:
        return 0
    if k >= n // 2:  # 无限次交易
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
    buy = [float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    for p in prices:
        for j in range(1, k + 1):
            buy[j] = min(buy[j], p - sell[j - 1])
            sell[j] = max(sell[j], p - buy[j])
    return sell[k]

# 时间 O(n*k), 空间 O(k)
```

---

## 5. Maximal Square (T150)

**状态定义**：`dp[i][j]` = 以 (i,j) 为右下角的最大全 1 正方形边长
**转移**：
```
if matrix[i][j] == '1':
    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

```python
def maximalSquare(matrix: list[list[str]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                max_side = max(max_side, dp[i][j])
    return max_side * max_side

# 时间 O(m*n), 空间 O(m*n) 可压缩到 O(n)
```

---

## 6. Longest Palindromic Substring (T150)

**题目**：给你一个字符串 `s`，找到 `s` 中最长的 回文 子串。

**示例 1：**

```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

**示例 2：**

```
输入：s = "cbbd"
输出："bb"
```

**提示：**

- `1 <= s.length <= 1000`

- `s` 仅由数字和英文字母组成

**难度**：中等

**思路**：中心扩展法（比 DP 更优）
DP 版：`dp[i][j]` = s[i:j+1] 是否回文

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    start, max_len = 0, 1
    for i in range(n):
        # 奇数扩展
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
        # 偶数扩展
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
    return s[start:start + max_len]

# 时间 O(n^2), 空间 O(1)
```
