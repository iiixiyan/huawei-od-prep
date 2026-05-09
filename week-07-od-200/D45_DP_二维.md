# D45 — DP 二维 (6题)

---

## 1. Unique Paths (L75/T150/O)

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

**状态定义**：`dp[i][j]` = 到 (i,j) 的最小路径和  
**转移**：`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`  
**原地**：可修改原数组节省空间

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

---

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
