# Day 03: 数组 + 数学

## 📖 知识点
**左右遍历 / 前缀积 / 双指针**：
- **前缀积+后缀积**：将问题分解为"左边所有元素的积 × 右边所有元素的积"，用两次遍历分别计算
- **左右遍历**：在处理接雨水、分糖果等问题时，从左到右和从右到左两次遍历可以分别处理不同方向的约束
- **接雨水双指针**：左右指针向中间移动，记录左右两侧的最大高度，用较矮的一侧决定当前位置的储水量

## 🧩 刷题任务（6题）

### 1. 除自身以外数组的乘积（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/product-of-array-except-self/)
**难度**：中等
**题目**：给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除了 `nums[i]` 之外其余各元素的乘积 。


题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内。


请 **不要使用除法，**且在 `O(n)` 时间复杂度内完成此题。


**示例 1:**


输入: nums = [1,2,3,4]
输出: [24,12,8,6]

**示例 2:**


输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]


**提示：**

- `2 5`

- `-30


**进阶：**你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为 **额外空间。）
**思路**：前缀积 × 后缀积。第一遍从左到右，`answer[i]` 存 `nums[i]` 左边所有数的乘积。第二遍从右到左，用一个变量 `suffix` 记录右边所有数的乘积，乘到 `answer[i]` 上。空间 O(1) 除输出数组外。
**代码**：
**代码**：
```python
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # 前缀积
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # 后缀积
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```
### 2. 加油站（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/gas-station/)
**难度**：中等
**题目**：在一条环路上有 `n` 个加油站，其中第 `i` 个加油站有汽油 `gas[i]`* *升。


你有一辆油箱容量无限的的汽车，从第* *`i`* *个加油站开往第* *`i+1`* *个加油站需要消耗汽油 `cost[i]`* *升。你从其中的一个加油站出发，开始时油箱为空。


给定两个整数数组 `gas` 和 `cost` ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 `-1` 。如果存在解，则 **保证** 它是 **唯一** 的。


**示例 1:**


输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。

**示例 2:**


输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。


**提示:**

- `n == gas.length == cost.length`

- `1 5`

- `0 4`

- 输入保证答案唯一。
**思路**：**贪心**。从 `start` 出发，`total_gas` 记录总剩余油量，`cur_gas` 记录从当前起点出发的累计剩余。如果 `cur_gas < 0`，说明从 `start` 到当前位置之间任何点都无法到达终点，将起点设为 `i+1` 并重置 `cur_gas`。如果 `total_gas < 0` 则无解。
**代码**：
**代码**：
```python
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    start = total_gas = cur_gas = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_gas += diff
        cur_gas += diff
        if cur_gas < 0:
            start = i + 1
            cur_gas = 0
    return start if total_gas >= 0 else -1
```
### 3. 分发糖果（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/candy/)
**难度**：困难
**题目**：`n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。


你需要按照以下要求，给这些孩子分发糖果：

- 每个孩子至少分配到 `1` 个糖果。

- 相邻两个孩子中，评分更高的那个会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。


**示例 1：**


输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。

**示例 2：**


输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。


**提示：**

- `n == ratings.length`

- `1 4`

- `0 4`
**思路**：**左右两次遍历**。先从左到右：如果 `ratings[i] > ratings[i-1]`，则 `candies[i] = candies[i-1] + 1`，否则为 1。再从右到左：如果 `ratings[i] > ratings[i+1]`，则 `candies[i] = max(candies[i], candies[i+1] + 1)`。两次遍历结果取最大值。
**代码**：
**代码**：
```python
def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    # 从左到右
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # 从右到左
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
```
### 4. 接雨水（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/trapping-rain-water/)
**难度**：困难
**题目**：给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


**示例 1：**


*


输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

**示例 2：**


输入：height = [4,2,0,3,2,5]
输出：9


**提示：**

- `n == height.length`

- `1 4`

- `0 5`
**思路**：**双指针**。左右指针向中间移动，维护 `left_max` 和 `right_max`。当 `height[left] < height[right]` 时，左边是短板，当前位置能接的水 = `left_max - height[left]`（如果左指针处高度小于左最大高度）。对称处理右边。不需要额外数组。
**代码**：
**代码**：
```python
def trap(height: list[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```
### 5. 种花问题（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/can-place-flowers/)
**难度**：简单
**题目**：假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。


给你一个整数数组 `flowerbed` 表示花坛，由若干 `0` 和 `1` 组成，其中 `0` 表示没种植花，`1` 表示种植了花。另有一个数 `n`** **，能否在不打破种植规则的情况下种入 `n`** **朵花？能则返回 `true` ，不能则返回 `false` 。


**示例 1：**


输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

**示例 2：**


输入：flowerbed = [1,0,0,0,1], n = 2
输出：false


**提示：**

- `1 4`

- `flowerbed[i]` 为 `0` 或 `1`

- `flowerbed` 中不存在相邻的两朵花

- `0
**思路**：**贪心**。遍历花坛，如果当前位置能种花（`flowerbed[i] == 0` 且左右邻居都没有花），就种下并减少待种数量。注意边界处理：首尾只需要检查一侧。
**代码**：
**代码**：
```python
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
```
### 6. 拥有最多糖果的孩子（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/)
**难度**：简单
**题目**：有 `n` 个有糖果的孩子。给你一个数组 `candies`，其中 `candies[i]` 代表第 `i` 个孩子拥有的糖果数目，和一个整数 `extraCandies` 表示你所有的额外糖果的数量。


返回一个长度为 `n` 的布尔数组 `result`，如果把所有的 `extraCandies` 给第 `i` 个孩子之后，他会拥有所有孩子中 **最多 **的糖果，那么 `result[i]` 为 `true`，否则为 `false`。


注意，允许有多个孩子同时拥有 **最多** 的糖果数目。


**示例 1：**


输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true]
解释：如果你把额外的糖果全部给：
孩子 1，将有 2 + 3 = 5 个糖果，是孩子中最多的。
孩子 2，将有 3 + 3 = 6 个糖果，是孩子中最多的。
孩子 3，将有 5 + 3 = 8 个糖果，是孩子中最多的。
孩子 4，将有 1 + 3 = 4 个糖果，不是孩子中最多的。
孩子 5，将有 3 + 3 = 6 个糖果，是孩子中最多的。

**示例 2：**


输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false]
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。

**示例 3：**


输入：candies = [12,1,12], extraCandies = 10
输出：[true,false,true]


**提示：**

- `n == candies.length`

- `2
**思路**：先找到当前最大值，然后对每个孩子判断 `candies[i] + extraCandies >= max_candies`。
**代码**：
**代码**：
```python
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    return [c + extraCandies >= max_candies for c in candies]
```
## 📝 总结
- **前缀积** 是"除自身以外乘积"问题的标准解法，本质是分解成两个独立子问题
- **左右两次遍历** 适用于同时受左右两侧约束的问题（分糖果、接雨水的单调栈解法也是类似思路）
- **接雨水的双指针法** 是 O(1) 空间的最优解，关键在于理解"短板效应"——由较矮的一侧决定水位
- **加油站问题** 的核心结论是：如果从 A 到 B 无法到达，则 A 到 B 之间任意一点也无法到达终点
