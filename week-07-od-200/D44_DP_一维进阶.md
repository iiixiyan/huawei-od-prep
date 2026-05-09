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

**思路**：转化 → 能否选出若干元素凑成总和的一半（0-1 背包）  
**状态**：`dp[s]` = 能否凑出和为 s 的子集  
**转移**：`dp[s] = dp[s] or dp[s - num]`

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

---

## 5. Target Sum (O)

**思路**：转化成 0-1 背包  
`sum(正数) - sum(负数) = target`  
`sum(正数) = (total + target) // 2`  
找能凑成 `(total + target) // 2` 的方法数

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

---

## 6. Combination Sum IV (O)

**思路**：完全背包求排列数  
**状态**：`dp[i]` = 凑成 i 的组合数（顺序不同视为不同）  
**转移**：外循环金额，内循环物品

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
