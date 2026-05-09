# Day 07: 周复习

## 📖 知识点
本周覆盖的核心知识点总览：

| 类别 | 知识点 | 代表题型 |
|------|--------|----------|
| 双指针 | 快慢指针、头尾指针、读写指针 | 移除元素、去重、合并有序数组 |
| 贪心 | 局部最优 → 全局最优 | 股票 II、跳跃游戏、加油站、射气球 |
| 左右遍历 | 前缀+后缀 | 除自身以外数组乘积、分糖果 |
| 哈希集合 | O(1) 查找、去重 | 两数之和、最长连续序列 |
| 哈希映射 | 双射、分组、计数 | 同构字符串、字母异位词分组 |
| 前缀和 | 一维/二维、区间和快速查询 | 中心下标、二维区域和检索 |
| 区间合并 | 排序+合并 | 合并区间、插入区间 |

## 🧩 刷题任务（6题 - 混合复习）

### 1. 移动零
**来源**：T150
**思路**：快慢指针，类似移除元素。slow 指向下一个非零元素应该放置的位置，fast 遍历数组。遇到非零元素就交换到 slow 位置。
**代码**：
```python
def moveZeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

### 2. 有效的数独
**来源**：T150
**思路**：用三个集合数组分别记录每行、每列、每个 3×3 子数独中出现的数字。遍历时检查当前数字是否已在对应行/列/子数独中出现过。子数独索引 = (row // 3) * 3 + (col // 3)。
**代码**：
```python
def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            box_idx = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    return True
```

### 3. 盛最多水的容器
**来源**：L75
**思路**：双指针从两端向中间移动，计算当前面积 = 较矮高度 × 宽度。每次移动较矮的那一侧指针，因为宽度减小，只有高度可能变大才有可能得到更大面积。
**代码**：
```python
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
```

### 4. O(1) 时间插入、删除和获取随机元素
**来源**：T150
**思路**：组合使用哈希表（值→索引）和动态数组。插入时在数组末尾追加并记录索引；删除时将待删元素与末尾元素交换再删除（O(1)），更新哈希表；随机取用 random.choice。
**代码**：
```python
import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last_val = self.nums[-1]
        # 将最后一个元素移到被删除的位置
        self.nums[idx] = last_val
        self.val_to_idx[last_val] = idx
        # 删除最后一个元素
        self.nums.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

### 5. 缺失的第一个正数
**来源**：T150
**思路**：**原地哈希**。将数组视为哈希表：把数字 x 放到下标 x-1 的位置。遍历数组，如果 `1 <= nums[i] <= n` 且 `nums[i] != nums[nums[i]-1]`，则交换。最后遍历，第一个 `nums[i] != i+1` 的位置即为答案。
**代码**：
```python
def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        correct_idx = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```

### 6. 生命游戏
**来源**：T150
**思路**：**原地标记法**。用特殊状态表示变化：2 表示从活→死，-1 表示从死→活。统计每个细胞周围 8 个方向的活细胞数，根据规则更新。第二次遍历将特殊状态转换回 0/1。
**代码**：
```python
def gameOfLife(board: list[list[int]]) -> None:
    m, n = len(board), len(board[0])
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1),
                  (0,1), (1,-1), (1,0), (1,1)]

    def count_live(r: int, c: int) -> int:
        cnt = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                cnt += 1
        return cnt

    for r in range(m):
        for c in range(n):
            live = count_live(r, c)
            if board[r][c] == 1 and (live < 2 or live > 3):
                board[r][c] = 2  # 活→死
            if board[r][c] == 0 and live == 3:
                board[r][c] = -1  # 死→活

    for r in range(m):
        for c in range(n):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == -1:
                board[r][c] = 1
```

## 📝 小测验

每题快速自测，检查能否在 30 秒内说出答案：

1. 合并两个有序数组（从后往前）的时间复杂度？空间复杂度？
2. 快慢指针删除重复元素时，slow 和 fast 分别代表什么？
3. Boyer-Moore 投票算法的前提条件是什么？
4. 接雨水的双指针法中，哪一侧决定当前水位？
5. 最长连续序列的优化关键是什么？
6. 字母异位词分组有哪两种常见的 key 设计？
7. 二维前缀和的容斥原理公式是什么？
8. 区间合并的第一步是什么？
9. 原地哈希的核心思想是什么？（缺失的第一个正数）
10. 随机集合删除元素时如何保证 O(1)？

**答案**：
1. O(m+n), O(1)
2. slow 指向已处理（写入）位置末尾，fast 遍历未处理部分
3. 多数元素出现次数 > n/2
4. 较矮的一侧
5. 只从序列起点（num-1 不在 set 中）开始计数
6. 排序后的字符串、长度为 26 的计数元组
7. `sum = p[i2+1][j2+1] - p[i1][j2+1] - p[i2+1][j1] + p[i1][j1]`
8. 按区间左端点排序
9. 将数组本身当作哈希表，把数字 x 放到下标 x-1 的位置
10. 将待删元素与末尾元素交换，再删除末尾元素并更新哈希表

## 📝 本周总结

Week 1 覆盖了数组和哈希表最核心的面试题型，主要收获：

1. **双指针**是数组原地操作的最重要技巧，贯穿整个数组章节
2. **哈希表**提供了 O(1) 的查找能力，是时间换空间的最佳体现
3. **贪心 + 排序**在区间问题和跳跃游戏中非常高效
4. **前缀和**将区间和查询从 O(n) 优化到 O(1)
5. **原地哈希**利用数组本身作为哈希表，空间 O(1)

建议掌握程度：D01-D03 需要达到 bug-free 手写，D04-D06 需要理解核心思路并能 10 分钟内写出代码，D07 为综合能力测试。
