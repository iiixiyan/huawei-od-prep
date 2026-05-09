# Day 02: 数组进阶操作

## 📖 知识点
**状态机与贪心策略**：
- **状态机**：在股票问题中，用状态变量（持有/不持有）代表不同阶段的决策，通过状态转移方程更新最优解
- **贪心算法**：每一步都做出当前最优选择，从而得到全局最优。适用于具有"最优子结构"的问题
- **跳跃游戏**：维护当前能到达的最远位置，贪心地选择跳跃范围

## 🧩 刷题任务（6题）

### 1. 轮转数组（⭐⭐）
**来源**：T150
**思路**：三次翻转法。先将整体翻转，再翻转前 k 个，再翻转后 n-k 个。注意 k 可能大于 n，先取模 `k %= n`。空间 O(1)。
**代码**：
```python
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    if k == 0:
        return

    def reverse(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
```

### 2. 买卖股票的最佳时机（⭐⭐）
**来源**：L75
**思路**：一次遍历，维护历史最低价 `min_price`，不断计算当前卖出能获得的最大利润 `price - min_price`，更新全局最大利润。
**代码**：
```python
def maxProfit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
```

### 3. 买卖股票的最佳时机 II（⭐⭐）
**来源**：T150
**思路**：**贪心**。可以无限次交易，只要今天比昨天价格高，就在昨天买今天卖。累加所有正收益。相当于把所有上涨的波段的差值和相加。
**代码**：
```python
def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```

### 4. 跳跃游戏（⭐⭐）
**来源**：T150
**思路**：**贪心**。维护当前能到达的最远位置 `max_reach`。遍历每个位置，如果当前位置已经超过 `max_reach` 则无法到达。否则用 `i + nums[i]` 更新 `max_reach`。最后检查 `max_reach >= n-1`。
**代码**：
```python
def canJump(nums: list[int]) -> bool:
    max_reach = 0
    for i, step in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + step)
    return True
```

### 5. 跳跃游戏 II（⭐⭐⭐）
**来源**：T150
**思路**：**贪心 + BFS 思想**。用 `cur_end` 表示当前跳跃能到达的边界，`farthest` 表示在当前步数范围内能到达的最远位置。当遍历到 `cur_end` 时，步数 +1，并将 `cur_end` 更新为 `farthest`。
**代码**：
```python
def jump(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(n - 1):  # 不需要遍历最后一个位置
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

### 6. H 指数（⭐⭐⭐）
**来源**：T150
**思路**：**排序法**。先将引用次数降序排列。从前往后找最大的 h 使得 `citations[h-1] >= h`。也可以使用计数排序（因为引用次数最多为 n）来达到 O(n) 时间复杂度。
**代码**：
```python
def hIndex(citations: list[int]) -> int:
    n = len(citations)
    # 计数排序思想：引用数 > n 的记为 n
    count = [0] * (n + 1)
    for c in citations:
        count[min(c, n)] += 1

    total = 0
    for h in range(n, -1, -1):
        total += count[h]
        if total >= h:
            return h
    return 0
```

## 📝 总结
- **股票问题的核心是状态定义**：`dp[i][持有/不持有]` 或贪心累积正波动
- **贪心的关键是证明最优子结构**：局部最优选择不影响后续全局最优
- 跳跃游戏 II 中，边界更新的方式类似于 BFS 的层序遍历，需要理解「步数」和「可达范围」的关系
- H 指数的计数排序是利用了题目中引用次数的上限为 n 这一约束
