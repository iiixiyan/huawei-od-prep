# Day 41: 综合练习 (树+图+矩阵+贪心)

## 📖 知识点
今日为混合实战，不限单一数据结构和算法。目标是融会贯通前面5天的技巧，在混合题型中快速识别考点。

## 🧩 刷题任务

### 题目1：找等值元素 / 矩阵最近相同值 (OD 100分)
**难度**：⭐⭐
**题目描述**：
给定一个 m×n 的矩阵，对于矩阵中的每个元素，找出矩阵中另一个相同值的元素，使得这两个元素的曼哈顿距离最小。如果不存在相同值的其他元素，输出 -1。输出每个位置的最小距离值矩阵。

**输入**：
```
3 3
1 2 3
4 5 6
7 8 9
```
**输出**：
```
-1 -1 -1
-1 -1 -1
-1 -1 -1
```
（因为所有值都唯一）

**输入**：
```
2 3
1 2 2
3 2 1
```
**输出**：
```
2 1 1
-1 1 2
```

**思路分析**：
1. 建立值到坐标列表的映射：dict[val] = [(r1,c1), (r2,c2), ...]
2. 对于每个值，如果坐标数量 ≥ 2，计算曼哈顿距离
3. 暴力 O(K²) 可过（值相同元素通常不多），或用 BFS 多源搜索
4. 曼哈顿距离 = |r1-r2| + |c1-c2|

**参考代码**：
```python
def min_distance_matrix(matrix, m, n):
    # 建立值到坐标的映射
    val_map = {}
    for i in range(m):
        for j in range(n):
            val = matrix[i][j]
            val_map.setdefault(val, []).append((i, j))
    # 初始化结果矩阵
    res = [[-1] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            val = matrix[i][j]
            positions = val_map[val]
            if len(positions) < 2:
                continue
            min_dist = float('inf')
            for r, c in positions:
                if (r, c) == (i, j):
                    continue
                dist = abs(i - r) + abs(j - c)
                min_dist = min(min_dist, dist)
            res[i][j] = min_dist
    return res

# 测试
m, n = 2, 3
matrix = [[1,2,2],[3,2,1]]
res = min_distance_matrix(matrix, m, n)
for row in res:
    print(' '.join(map(str, row)))
```

**OD备考提示**：建映射是关键第一步。如果相同值很多（如全0矩阵），可优化为BFS多源搜索。

---

### 题目2：查找单入口空闲区域 / 机器人活动区域 (OD 100分)
**难度**：⭐⭐
**题目描述**：
在 m×n 的网格中，0 表示空闲区域，1 表示障碍。入口是位于网格边缘（第一行/最后一行/第一列/最后一列）的 0。如果存在一个连通空闲区域只有一个入口，则该区域为"单入口空闲区域"。求所有单入口空闲区域中，面积最大的值。如果不存在，输出 0。

**输入**：
```
4 4
0 1 1 0
0 0 0 0
1 0 1 0
0 1 0 0
```
**输出**：
```
5
```

**思路分析**：
1. 遍历所有网格边界上的 0（入口），从每个入口 BFS
2. 在 BFS 过程中，记录该连通区域的面积和遇到的入口数
3. 如果入口数 == 1，更新最大面积
4. 用 visited 避免重复搜索

**参考代码**：
```python
from collections import deque

def single_entry_area(grid, m, n):
    visited = [[False] * n for _ in range(m)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    max_area = 0
    for i in range(m):
        for j in range(n):
            # 只从边界上的0开始
            if not (i == 0 or i == m-1 or j == 0 or j == n-1):
                continue
            if grid[i][j] == 0 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                area = 0
                entry_count = 0
                while q:
                    x, y = q.popleft()
                    area += 1
                    # 如果当前在边界上，算一个入口
                    if x == 0 or x == m-1 or y == 0 or y == n-1:
                        entry_count += 1
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                if entry_count == 1:
                    max_area = max(max_area, area)
    return max_area

# 测试
m, n = 4, 4
grid = [
    [0,1,1,0],
    [0,0,0,0],
    [1,0,1,0],
    [0,1,0,0]
]
print(single_entry_area(grid, m, n))  # 5
```

**OD备考提示**：BFS 遍历连通区域的模板。注意 entry_count 是在 BFS 过程中统计的，不是只在边界起始点统计。因为一个连通区域可能有多个边界点都是入口。

## 📝 今日小结
- 综合题往往是矩阵+图遍历的组合
- 建值→坐标映射是高效解法的基础
- BFS 在矩阵中找连通区域是最常见的模式
