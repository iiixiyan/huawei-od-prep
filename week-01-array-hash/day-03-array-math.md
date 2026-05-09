# Day 03: 数组 + 数学

## 📖 知识点
**左右遍历 / 前缀积 / 双指针**：
- **前缀积+后缀积**：将问题分解为"左边所有元素的积 × 右边所有元素的积"，用两次遍历分别计算
- **左右遍历**：在处理接雨水、分糖果等问题时，从左到右和从右到左两次遍历可以分别处理不同方向的约束
- **接雨水双指针**：左右指针向中间移动，记录左右两侧的最大高度，用较矮的一侧决定当前位置的储水量

## 🧩 刷题任务（6题）

### 1. 除自身以外数组的乘积（⭐⭐⭐）
**来源**：L75
**思路**：前缀积 × 后缀积。第一遍从左到右，`answer[i]` 存 `nums[i]` 左边所有数的乘积。第二遍从右到左，用一个变量 `suffix` 记录右边所有数的乘积，乘到 `answer[i]` 上。空间 O(1) 除输出数组外。
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
**来源**：T150
**思路**：**贪心**。从 `start` 出发，`total_gas` 记录总剩余油量，`cur_gas` 记录从当前起点出发的累计剩余。如果 `cur_gas < 0`，说明从 `start` 到当前位置之间任何点都无法到达终点，将起点设为 `i+1` 并重置 `cur_gas`。如果 `total_gas < 0` 则无解。
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
**来源**：T150
**思路**：**左右两次遍历**。先从左到右：如果 `ratings[i] > ratings[i-1]`，则 `candies[i] = candies[i-1] + 1`，否则为 1。再从右到左：如果 `ratings[i] > ratings[i+1]`，则 `candies[i] = max(candies[i], candies[i+1] + 1)`。两次遍历结果取最大值。
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
**来源**：T150
**思路**：**双指针**。左右指针向中间移动，维护 `left_max` 和 `right_max`。当 `height[left] < height[right]` 时，左边是短板，当前位置能接的水 = `left_max - height[left]`（如果左指针处高度小于左最大高度）。对称处理右边。不需要额外数组。
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
**来源**：L75
**思路**：**贪心**。遍历花坛，如果当前位置能种花（`flowerbed[i] == 0` 且左右邻居都没有花），就种下并减少待种数量。注意边界处理：首尾只需要检查一侧。
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
**来源**：L75
**思路**：先找到当前最大值，然后对每个孩子判断 `candies[i] + extraCandies >= max_candies`。
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
