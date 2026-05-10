# D44 — DP 一维进阶 (6题)

---

## 1. Word Break (T150)

**思路**：`dp[i]` = s[:i] 能否被拆分成字典中的词
**转移**：`dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`
**剪枝**：只检查长度不超过最长单词的 j

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    max_len = max(len(w) for w in wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]

# 时间 O(n * max_len), 空间 O(n + wordDict)
```

---

## 2. Coin Change (T150/O)

**状态定义**：`dp[i]` = 凑成金额 i 的最少硬币数
**转移**：`dp[i] = min(dp[i - coin] + 1 for coin in coins if i >= coin)`
**初始**：`dp[0] = 0`，其余为 `inf`

```python
def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# 时间 O(amount * len(coins)), 空间 O(amount)
```

---

## 3. Longest Increasing Subsequence (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/longest-increasing-subsequence/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。


**子序列 **是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

**示例 1：**


输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

**示例 2：**


输入：nums = [0,1,0,3,2,3]
输出：4

**示例 3：**


输入：nums = [7,7,7,7,7,7,7]
输出：1

**提示：**

- `1 4 4`

**进阶：**

- 你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

**状态定义**：`dp[i]` = 以 nums[i] 结尾的 LIS 长度
**转移**：`dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])`
**优化**：`patience sorting` → O(n log n)

```python
def lengthOfLIS(nums: list[int]) -> int:
    tails = []
    for x in nums:
        idx = __import__('bisect').bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)

# 时间 O(n log n), 空间 O(n)
```

---

## 4. Partition Equal Subset Sum (O)
**来源**：[O](https://leetcode.cn/problems/partition-equal-subset-sum/)
**难度**：中等
**题目**：给你一个 **只包含正整数 **的 **非空 **数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。


 


**示例 1：**


输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

**示例 2：**


输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

 


**提示：**

- `1
**思路**：转化 → 能否选出若干元素凑成总和的一半（0-1 背包）
**代码**：
```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total & 1:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
    return dp[target]

# 时间 O(n * target), 空间 O(target)
```
## 5. Target Sum (O)
**来源**：[O](https://leetcode.cn/problems/target-sum/)
**难度**：中等
**题目**：给你一个非负整数数组 `nums` 和一个整数 `target` 。


向数组中的每个整数前添加 `'+'` 或 `'-'` ，然后串联起所有整数，可以构造一个 **表达式** ：

- 例如，`nums = [2, 1]` ，可以在 `2` 之前添加 `'+'` ，在 `1` 之前添加 `'-'` ，然后串联起来得到表达式 `"+2-1"` 。

返回可以通过上述方法构造的、运算结果等于 `target` 的不同 **表达式** 的数目。


**示例 1：**


输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

**示例 2：**


输入：nums = [1], target = 1
输出：1


**提示：**

- `1
**思路**：转化成 0-1 背包 `sum(正数) - sum(负数) = target` `sum(正数) = (total + target) // 2` 找能凑成 `(total + target) // 2` 的方法数
**代码**：
```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    total = sum(nums)
    if total < abs(target) or (total + target) & 1:
        return 0
    s = (total + target) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    for num in nums:
        for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[s]

# 时间 O(n * s), 空间 O(s)
```
## 6. Combination Sum IV (O)
**来源**：[O](https://leetcode.cn/problems/combination-sum/)
**难度**：中等
**题目**：给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有* ***不同组合** ，并以列表形式返回。你可以按 **任意顺序** 返回这些组合。


`candidates` 中的 **同一个** 数字可以 **无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。


对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。


**示例 1：**


输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

**示例 2：**


输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

**示例 3：**


输入: candidates = [2], target = 1
输出: []


**提示：**

- `1
**思路**：完全背包求排列数
**代码**：
```python
def combinationSum4(nums: list[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]

# 时间 O(target * len(nums)), 空间 O(target)
```