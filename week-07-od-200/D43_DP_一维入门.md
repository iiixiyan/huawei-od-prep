# D43 — DP 一维入门 (6题)

---

## 1. Climbing Stairs (T150)

**状态定义**：`dp[i]` = 爬到第 `i` 阶的方法数
**转移**：`dp[i] = dp[i-1] + dp[i-2]`
**初始**：`dp[1]=1, dp[2]=2`
**优化**：空间压缩到 O(1)

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# 时间 O(n), 空间 O(1)
```

---

## 2. N-th Tribonacci Number (L75)

**状态定义**：`dp[i]` = 第 i 个 Tribonacci 数
**转移**：`dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`
**初始**：`dp[0]=0, dp[1]=1, dp[2]=1`

```python
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

# 时间 O(n), 空间 O(1)
```

---

## 3. Min Cost Climbing Stairs (L75/O)

**状态定义**：`dp[i]` = 到达第 i 阶的最小花费
**转移**：`dp[i] = cost[i] + min(dp[i-1], dp[i-2])`
**终点**：`min(dp[-1], dp[-2])`，因为可以跨过顶部

```python
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    if n == 2:
        return min(cost)
    a, b = cost[0], cost[1]
    for i in range(2, n):
        a, b = b, cost[i] + min(a, b)
    return min(a, b)

# 时间 O(n), 空间 O(1)
```

---

## 4. House Robber (L75/T150/O)

**状态定义**：`dp[i]` = 前 i 间房能偷到的最大金额
**转移**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
**优化**：滚动变量

```python
def rob(nums: list[int]) -> int:
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr

# 时间 O(n), 空间 O(1)
```

---

## 5. House Robber II (O)
**题目**：你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 **围成一圈** ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **在不触动警报装置的情况下** ，今晚能够偷窃到的最高金额。

**示例 1：**

```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

**示例 2：**

```
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 3：**

```
输入：nums = [1,2,3]
输出：3
```

**提示：**

- `1 <= nums.length <= 100`

- `0 <= nums[i] <= 1000`

**难度**：中等

**思路**：环形 → 拆成两个线性的 House Robber
- 情况 A：不抢第 0 间 → `rob(nums[1:])`
- 情况 B：不抢最后 1 间 → `rob(nums[:-1])`
取最大值

```python
def rob_linear(nums: list[int]) -> int:
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr

def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

# 时间 O(n), 空间 O(1)
```

---

## 6. Domino and Tromino (L75)

**状态定义**：
- `dp[i][0]` = 完全铺满 2×i 列的方法数
- `dp[i][1]` = 铺满 2×i 列，但右上角缺一格的方法数
**转移**：
```
dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]
dp[i][1] = dp[i-2][0] + dp[i-1][1]
```
**初始**：`dp[1][0]=1, dp[0][0]=1, dp[1][1]=0, dp[2][1]=1`

```python
def numTilings(n: int) -> int:
    MOD = 10**9 + 7
    if n == 1:
        return 1
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    dp0[0] = dp0[1] = 1
    dp1[1] = 0
    dp1[2] = 1
    for i in range(2, n + 1):
        dp0[i] = (dp0[i - 1] + dp0[i - 2] + 2 * dp1[i - 1]) % MOD
        dp1[i] = (dp0[i - 2] + dp1[i - 1]) % MOD
    return dp0[n]

# 时间 O(n), 空间 O(n) 可压缩到 O(1)
```
