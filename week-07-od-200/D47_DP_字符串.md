# D47 — DP 字符串 (6题)

---

## 1. Palindromic Substrings (O)

**思路**：中心扩展法，统计所有回文子串  
每个字符或每对相邻字符作为中心向两边扩展

```python
def countSubstrings(s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        # 奇数长度回文
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        # 偶数长度回文
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans

# 时间 O(n^2), 空间 O(1)
```

---

## 2. Longest Fibonacci Subsequence (O)

**思路**：`dp[j][k]` = 以 arr[j], arr[k] 结尾的最长斐波那契子序列长度  
**转移**：如果存在 `i` 使得 `arr[i] + arr[j] == arr[k]`，则  
`dp[j][k] = max(dp[j][k], dp[i][j] + 1)`  
**初始**：任意两个元素可组成长度 2 的序列

```python
def lenLongestFibSubseq(arr: list[int]) -> int:
    n = len(arr)
    idx = {x: i for i, x in enumerate(arr)}
    dp = [[2] * n for _ in range(n)]
    ans = 0
    for k in range(n):
        for j in range(k):
            target = arr[k] - arr[j]
            if target in idx and idx[target] < j:
                i = idx[target]
                dp[j][k] = dp[i][j] + 1
                ans = max(ans, dp[j][k])
    return ans if ans >= 3 else 0

# 时间 O(n^2), 空间 O(n^2)
```

---

## 3. Palindrome Partitioning II (O)

**思路**：两次 DP  
1. `isPal[i][j]` = s[i:j+1] 是否回文  
2. `dp[i]` = s[:i+1] 的最少分割次数

```python
def minCut(s: str) -> int:
    n = len(s)
    isPal = [[False] * n for _ in range(n)]
    dp = [n] * n
    for i in range(n):
        for j in range(i + 1):
            if s[i] == s[j] and (i - j <= 2 or isPal[j + 1][i - 1]):
                isPal[j][i] = True
    for i in range(n):
        if isPal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if isPal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

# 时间 O(n^2), 空间 O(n^2)
```

---

## 4. Paint House (O)

**状态定义**：`dp[i][j]` = 第 i 间房刷颜色 j 的最小花费（j=0,1,2）  
**转移**：当前颜色不能和前一间相同  
`dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])`

```python
def minCost(costs: list[list[int]]) -> int:
    if not costs:
        return 0
    n = len(costs)
    dp = [costs[0][0], costs[0][1], costs[0][2]]
    for i in range(1, n):
        r = costs[i][0] + min(dp[1], dp[2])
        g = costs[i][1] + min(dp[0], dp[2])
        b = costs[i][2] + min(dp[0], dp[1])
        dp = [r, g, b]
    return min(dp)

# 时间 O(n), 空间 O(1)
```

---

## 5. Minimum Flips to Make String Monotone (O)

**思路**：最终字符串形式为 0...01...1  
遍历每个位置作为分界点，统计左侧 1 的数量 + 右侧 0 的数量

```python
def minFlipsMonoIncr(s: str) -> int:
    ones = 0
    zeros = s.count('0')
    ans = zeros  # 全翻成 1
    for c in s:
        if c == '0':
            zeros -= 1
        else:
            ones += 1
        ans = min(ans, ones + zeros)
    return ans

# 时间 O(n), 空间 O(1)
```

---

## 6. Distinct Subsequences (O)

**状态定义**：`dp[i][j]` = s[:i] 中 t[:j] 作为子序列出现的次数  
**转移**：
```
if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
else: dp[i][j] = dp[i-1][j]
```

```python
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        prev = 1  # dp[i-1][0]
        for j in range(1, n + 1):
            cur = dp[j]
            if s[i - 1] == t[j - 1]:
                dp[j] += prev
            prev = cur
    return dp[n]

# 时间 O(m*n), 空间 O(n)
```
