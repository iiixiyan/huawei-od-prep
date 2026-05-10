# D45 — DP 二维 (6题)

---

## 1. Unique Paths (L75/T150/O)
**来源**：[LeetCode](https://leetcode.cn/problems/unique-paths/)
**难度**：中等
**题目**：一个机器人位于一个 `m x n`* *网格的左上角 （起始点在下图中标记为 “Start” ）。


机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。


问总共有多少条不同的路径？

**示例 1：**

*
输入：m = 3, n = 7
输出：28

**示例 2：**


输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

**示例 3：**


输入：m = 7, n = 3
输出：28

**示例 4：**


输入：m = 3, n = 3
输出：6

**提示：**

- `1 9`

**状态定义**：`dp[i][j]` = 到达 (i,j) 的路径数
**转移**：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`
**优化**：一维滚动数组

```python
def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]

# 时间 O(m*n), 空间 O(n)
```

---

## 2. Unique Paths II (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/unique-paths-ii/)
**难度**：中等
**题目**：给定一个 `m x n` 的整数数组 `grid`。一个机器人初始位于 **左上角**（即 `grid[0][0]`）。机器人尝试移动到 **右下角**（即 `grid[m - 1][n - 1]`）。机器人每次只能向下或者向右移动一步。


网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。机器人的移动路径中不能包含 **任何** 有障碍物的方格。


返回机器人能够到达右下角的不同路径数量。


测试用例保证答案小于等于 `2 * 109`。

**示例 1：**

*
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

**示例 2：**

*
输入：obstacleGrid = [[0,1],[0,0]]
输出：1

**提示：**

- `m == obstacleGrid.length`

- `n == obstacleGrid[i].length`

- `1

**思路**：有障碍物时 `dp[i][j] = 0`
**转移**：`if obstacleGrid[i][j] == 0: dp[j] += dp[j-1]`

```python
def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
    return dp[-1]

# 时间 O(m*n), 空间 O(n)
```

---

## 3. Minimum Path Sum (T150/O)
**来源**：[](https://leetcode.cn/problems/path-sum/)
**难度**：简单
**题目**：给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。


**叶子节点** 是指没有子节点的节点。


**示例 1：**

*
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。

**示例 2：**

*
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。

**示例 3：**


输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。


**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内

- `-1000
**思路**：**状态定义**：`dp[i][j]` = 到 (i,j) 的最小路径和
**转移**：`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`
**代码**：
```python
def minPathSum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]

# 时间 O(m*n), 空间 O(1) 原地修改
```
## 4. Triangle (T150/O)

**思路**：自底向上 DP，`dp[j] = triangle[i][j] + min(dp[j], dp[j+1])`

```python
def minimumTotal(triangle: list[list[int]]) -> int:
    dp = triangle[-1][:]  # 最后一行
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]

# 时间 O(n^2), 空间 O(n)
```

---

## 5. Longest Common Subsequence (L75/O)

**状态定义**：`dp[i][j]` = text1[:i] 和 text2[:j] 的 LCS 长度
**转移**：
```
if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# 时间 O(m*n), 空间 O(m*n) 可优化到 O(n)
```

---

## 6. Interleaving String (T150/O)

**状态定义**：`dp[i][j]` = s1[:i] 和 s2[:j] 能否交错成 s3[:i+j]
**转移**：
```
dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or
           (dp[i][j-1] and s2[j-1]==s3[i+j-1])
```

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n, k = len(s1), len(s2), len(s3)
    if m + n != k:
        return False
    dp = [False] * (n + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            elif j == 0:
                dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
            else:
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
    return dp[n]

# 时间 O(m*n), 空间 O(n)
```
