# D47 — DP 字符串 (6题)

---

## 1. Palindromic Substrings (O)
**来源**：[O](https://leetcode.cn/problems/palindromic-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。


**回文字符串** 是正着读和倒过来读一样的字符串。


**子字符串** 是字符串中的由连续字符组成的一个序列。


**示例 1：**


输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

**示例 2：**


输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"


**提示：**

- `1
**思路**：中心扩展法，统计所有回文子串 每个字符或每对相邻字符作为中心向两边扩展
**代码**：
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
## 2. Longest Fibonacci Subsequence (O)
**来源**：[O](https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/)
**难度**：中等
**题目**：如果序列 `x1, x2, ..., xn` 满足下列条件，就说它是 *斐波那契式 *的：

- `n >= 3`

- 对于所有 `i + 2 i + xi+1 == xi+2`

给定一个 **严格递增 **的正整数数组形成序列 `arr` ，找到 `arr` 中最长的斐波那契式的子序列的长度。如果不存在，返回  `0` 。


**子序列** 是通过从另一个序列 `arr` 中删除任意数量的元素（包括删除 0 个元素）得到的，同时不改变剩余元素顺序。例如，`[3, 5, 8]` 是 `[3, 4, 5, 6, 7, 8]` 的子序列。


**示例 1：**


输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。

**示例 2：**


输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。


**提示：**

- `3 9`
**思路**：`dp[j][k]` = 以 arr[j], arr[k] 结尾的最长斐波那契子序列长度 `dp[j][k] = max(dp[j][k], dp[i][j] + 1)`
**代码**：
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
## 3. Palindrome Partitioning II (O)
**来源**：[O](https://leetcode.cn/problems/palindrome-partitioning-ii/)
**难度**：困难
**题目**：给你一个字符串 `s`，请你将 `s` 分割成一些子串，使每个子串都是回文串。


返回符合要求的 **最少分割次数** 。


**示例 1：**


输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

**示例 2：**


输入：s = "a"
输出：0

**示例 3：**


输入：s = "ab"
输出：1


**提示：**

- `1
**思路**：两次 DP 1. `isPal[i][j]` = s[i:j+1] 是否回文 2. `dp[i]` = s[:i+1] 的最少分割次数
**代码**：
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
## 4. Paint House (O)
**来源**：[O](https://leetcode.cn/problems/paint-house/)
**难度**：中等
**思路**：**状态定义**：`dp[i][j]` = 第 i 间房刷颜色 j 的最小花费（j=0,1,2）
**转移**：当前颜色不能和前一间相同
**代码**：
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
## 5. Minimum Flips to Make String Monotone (O)
**来源**：[O](https://leetcode.cn/problems/minimum-flips-to-make-string-monotone-increasing/)
**思路**：最终字符串形式为 0...01...1 遍历每个位置作为分界点，统计左侧 1 的数量 + 右侧 0 的数量
**代码**：
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
## 6. Distinct Subsequences (O)
**来源**：[O](https://leetcode.cn/problems/distinct-subsequences/)
**难度**：困难
**题目**：给你两个字符串 `s`** **和 `t` ，统计并返回在 `s` 的 **子序列** 中 `t` 出现的个数。


测试用例保证结果在 32 位有符号整数范围内。


**示例 1：**


输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit

**示例 2：**


输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag
babgbag
babgbag
babgbag
babgbag


**提示：**

- `1
**思路**：**状态定义**：`dp[i][j]` = s[:i] 中 t[:j] 作为子序列出现的次数
**转移**：
**代码**：
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