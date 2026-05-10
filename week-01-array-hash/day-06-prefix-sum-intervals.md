# Day 06: 前缀和 + 区间

## 📖 知识点
**前缀和与区间合并**：
- **前缀和模板**：构建数组 `prefix[i]` 表示前 i 个元素的和（或 `prefix[i] = sum(nums[0:i])`）。区间 `[l, r]` 的和 = `prefix[r+1] - prefix[l]`
- **二维前缀和**：`prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + matrix[i][j]`，子矩阵和 = `prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1]`
- **区间合并**：按起点排序，遍历时维护当前合并区间的末尾，判断是否有重叠
- **贪心射气球**：按区间终点排序，每次射中最早结束的区间

## 🧩 刷题任务（6题）

### 1. 寻找最高海拔（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/find-the-highest-altitude/)
**难度**：简单
**题目**：有一个自行车手打算进行一场公路骑行，这条路线总共由 `n + 1` 个不同海拔的点组成。自行车手从海拔为 `0` 的点 `0` 开始骑行。

给你一个长度为 `n` 的整数数组 `gain` ，其中 `gain[i]` 是点 `i` 和点 `i + 1` 的 **净海拔高度差**（`0
- `n == gain.length`

- `1
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
**来源**：[LeetCode](https://leetcode.cn/problems/find-pivot-index/)
**难度**：简单
**题目**：给你一个整数数组 `nums` ，请计算数组的 **中心下标 **。

数组** 中心下标**是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 `0` ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回**最靠近左边** 的那一个。如果数组不存在中心下标，返回 `-1` 。

**示例 1：**
```
输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
```
**示例 2：**
```
输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
```
**示例 3：**
```
输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
```
**提示：**

- `1 4`

- `-1000

**注意：**本题与主站 1991 题相同：https://leetcode.cn/problems/find-the-middle-index-in-array/
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
**来源**：[LeetCode](https://leetcode.cn/problems/range-sum-query-2d-immutable/)
**难度**：中等
**题目**：**给定一个二维矩阵 `matrix`，以下类型的多个请求：

- **计算其子矩形范围内元素的总和，该子矩阵的 **左上角** 为 `(row1, col1)` ，**右下角** 为 `(row2, col2)` 。

实现 `NumMatrix` 类：

- `NumMatrix(int[][] matrix)` 给定整数矩阵 `matrix` 进行初始化

- `int sumRegion(int row1, int col1, int row2, int col2)` 返回 左上角**** `(row1, col1)` 、**右下角**`(row2, col2)` 所描述的子矩阵的元素**总和** 。

**示例 1：**
```
*
输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]
解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
```
**提示：**

- `m == matrix.length`

- `n == matrix[i].length`

- `1

- `-105 5`

- `0 最多调用 `104` 次 `sumRegion` 方法
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
**来源**：[LeetCode](https://leetcode.cn/problems/merge-intervals/)
**难度**：中等
**题目**：以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 *一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间* 。

**示例 1：**
```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```
**示例 2：**
```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```
**示例 3：**
```
输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
```
**提示：**

- `1 4`

- `intervals[i].length == 2`

- `0 i i 4`
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
**来源**：[LeetCode](https://leetcode.cn/problems/insert-interval/)
**难度**：中等
**题目**：给你一个** 无重叠的*** ，*按照区间起始端点排序的区间列表 `intervals`，其中 `intervals[i] = [starti, endi]` 表示第 `i` 个区间的开始和结束，并且 `intervals` 按照 `starti` 升序排列。同样给定一个区间 `newInterval = [start, end]` 表示另一个区间的开始和结束。

在 `intervals` 中插入区间 `newInterval`，使得 `intervals` 依然按照 `starti` 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 `intervals`。

**注意** 你不需要原地修改 `intervals`。你可以创建一个新数组然后返回它。

**示例 1：**
```
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
```
**示例 2：**
```
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
```
**提示：**

- `0 4`

- `intervals[i].length == 2`

- `0 i i 5`

- `intervals` 根据 `starti` 按 **升序** 排列

- `newInterval.length == 2`

- `0 5`
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
**来源**：[LeetCode](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)
**难度**：中等
**题目**：有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 `points` ，其中`points[i] = [xstart, xend]` 表示水平直径在 `xstart` 和 `xend`之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 **完全垂直**地射出。在坐标 `x` 处射出一支箭，若有一个气球的直径的开始和结束坐标为 `xstart`，`xend`， 且满足  `xstart ≤ x ≤ xend`，则该气球会被**引爆**。可以射出的弓箭的数量**没有限制** 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 `points` ，*返回引爆所有气球所必须射出的 **最小** 弓箭数 *。

**示例 1：**
```
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。
```
**示例 2：**
```
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。
```
**示例 3：**
```
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
```
**提示:**

- `1 5`

- `points[i].length == 2`

- `-231 start end 31 - 1`
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
- **前缀和**的核心是空间换时间，预处理 O(n)，查询 O(1)
-**二维前缀和**的容斥原理公式需要记牢：`sum = prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1]`
-**区间合并**三步法：排序 → 判断重叠（`interval[0] > merged[-1][1]`）→ 合并或追加
-**插入区间**是区间合并的变体，关键在于分三段处理
-**射气球** 的贪心策略是"每次射尽量多的气球"，按右端点排序是最优的（类似活动选择问题）
