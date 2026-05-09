# Day 06: 前缀和 + 区间

## 📖 知识点
**前缀和与区间合并**：
- **前缀和模板**：构建数组 `prefix[i]` 表示前 i 个元素的和（或 `prefix[i] = sum(nums[0:i])`）。区间 `[l, r]` 的和 = `prefix[r+1] - prefix[l]`
- **二维前缀和**：`prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + matrix[i][j]`，子矩阵和 = `prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1]`
- **区间合并**：按起点排序，遍历时维护当前合并区间的末尾，判断是否有重叠
- **贪心射气球**：按区间终点排序，每次射中最早结束的区间

## 🧩 刷题任务（6题）

### 1. 寻找最高海拔（⭐）
**来源**：L75
**思路**：简单前缀和问题。从海拔 0 开始，遍历 gain 数组累加海拔变化，记录过程中的最大值。
**代码**：
```python
def largestAltitude(gain: list[int]) -> int:
    current = 0
    max_alt = 0
    for g in gain:
        current += g
        max_alt = max(max_alt, current)
    return max_alt
```

### 2. 寻找数组的中心下标（⭐⭐）
**来源**：O / T150
**思路**：先计算总和 total，再从左到右遍历。维护 `left_sum`，当前索引右边的和为 `total - left_sum - nums[i]`。当 `left_sum == total - left_sum - nums[i]` 时返回。注意左右边界的情况。
**代码**：
```python
def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1
```

### 3. 二维区域和检索 - 矩阵不可变（⭐⭐⭐）
**来源**：O
**思路**：预处理二维前缀和数组 `prefix`，其中 `prefix[i+1][j+1]` 表示从 (0,0) 到 (i,j) 的子矩阵和。查询时用容斥原理计算任意子矩阵的和。
**代码**：
```python
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.prefix[i + 1][j + 1] = self.prefix[i][j + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefix
        return (p[row2 + 1][col2 + 1]
                - p[row1][col2 + 1]
                - p[row2 + 1][col1]
                + p[row1][col1])
```

### 4. 合并区间（⭐⭐⭐）
**来源**：T150 / O
**思路**：先将区间按左端点排序。遍历区间，如果当前区间的左端点大于 merged 中最后一个区间的右端点，则不重叠，直接加入；否则重叠，更新最后一个区间的右端点为两者最大值。
**代码**：
```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```

### 5. 插入区间（⭐⭐⭐）
**来源**：T150
**思路**：分三个阶段处理：先加入所有不与 newInterval 重叠且在其左侧的区间；然后合并所有与 newInterval 重叠的区间（更新 newInterval 的左右端点）；最后加入所有在其右侧的区间。
**代码**：
```python
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    i, n = 0, len(intervals)
    # 第一阶段：不重叠且在左侧
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    # 第二阶段：合并重叠区间
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    # 第三阶段：剩余区间
    while i < n:
        result.append(intervals[i])
        i += 1
    return result
```

### 6. 用最少数量的箭引爆气球（⭐⭐⭐）
**来源**：L75 / T150
**思路**：**贪心**。按区间右端点排序，第一支箭射在第一个区间的右端点，然后遍历剩余区间，如果当前区间的左端点 > 箭的位置（即上一箭射不中），则需要新箭并更新箭的位置。
**代码**：
```python
def findMinArrowShots(points: list[list[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    arrow_pos = points[0][1]
    for start, end in points[1:]:
        if start > arrow_pos:
            arrows += 1
            arrow_pos = end
    return arrows
```

## 📝 总结
- **前缀和** 的核心是空间换时间，预处理 O(n)，查询 O(1)
- **二维前缀和** 的容斥原理公式需要记牢：`sum = prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1]`
- **区间合并** 三步法：排序 → 判断重叠（`interval[0] > merged[-1][1]`）→ 合并或追加
- **插入区间** 是区间合并的变体，关键在于分三段处理
- **射气球** 的贪心策略是"每次射尽量多的气球"，按右端点排序是最优的（类似活动选择问题）
