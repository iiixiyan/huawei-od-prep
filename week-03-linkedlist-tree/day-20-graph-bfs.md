# Day 20 — Graph BFS

> BFS 最短路、多源 BFS、矩阵 BFS

---

## 📌 核心知识点

### 图 BFS 模板

```python
from collections import deque

def bfs_shortest_path(graph, start):
    q = deque([start])
    visited = {start}
    distance = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if is_target(node):         # 找到目标
                return distance
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        distance += 1
    return -1  # 不可达
```

### BFS 为什么适合最短路径？
- **无权图**中，BFS 第一次访问到目标节点时走的路径一定最短
- 因为 BFS 按层扩展，每层距离 +1

### 矩阵 BFS 模板（四方向）

```python
from collections import deque

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

def matrix_bfs(grid, start):
    m, n = len(grid), len(grid[0])
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if is_target(r, c):
                return steps
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                    if grid[nr][nc] != WALL:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        steps += 1
    return -1
```

---

## 🧩 题目 1：迷宫中离入口最近的出口

**LeetCode 1926 | 难度：Medium**

### 题目描述
`m x n` 迷宫，`+` 是墙，`.` 是路。从入口 `(entrance[0], entrance[1])` 出发，走到**边界**上的 `.`（出口），求最短路径步数。入口本身在边界时不算出口。

### 解法：BFS

```python
from collections import deque

def nearestExit(maze, entrance):
    m, n = len(maze), len(maze[0])
    q = deque([(entrance[0], entrance[1])])
    visited = [[False] * n for _ in range(m)]
    visited[entrance[0]][entrance[1]] = True
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    steps = 0

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            # 检查是否是出口（边界且不是入口）
            if (r == 0 or r == m-1 or c == 0 or c == n-1) and \
               (r, c) != (entrance[0], entrance[1]):
                return steps
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and \
                   not visited[nr][nc] and maze[nr][nc] == '.':
                    visited[nr][nc] = True
                    q.append((nr, nc))
        steps += 1

    return -1
```

- **时间复杂度**：O(m × n)
- **空间复杂度**：O(m × n)

### 关键细节
1. **出口条件**：在边界上且不是入口
2. 用 `visited` 矩阵（比 set 更快）
3. 一旦找到出口立即返回（BFS 第一次就是最短）

### 思考
> 为什么不用 DFS 找最短路径？
>
> **答**：DFS 找到的第一条路径不保证最短，需要遍历所有路径，效率远低于 BFS。DFS 适合「是否存在路径」而非「最短路径」。

---

## 🧩 题目 2：腐烂的橘子

**LeetCode 994 | 难度：Medium**

### 题目描述
`m x n` 网格，`0` 空，`1` 新鲜，`2` 腐烂。每分钟腐烂橘子会向四方向传播腐烂。求所有橘子腐烂的最少分钟数，如果不可能全部腐烂返回 -1。

### 解法：多源 BFS

```python
from collections import deque

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # 统计新鲜橘子数 & 所有腐烂橘子入队（多源）
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    minutes = 0

    # BFS 扩散
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1

    return minutes if fresh == 0 else -1
```

- **时间复杂度**：O(m × n)
- **空间复杂度**：O(m × n)

### 多源 BFS 模板

```
1. 初始化: 找到所有源点入队
2. 层数 = 0
3. 当队列非空且还有未被感染的节点:
    处理当前层的所有节点
    将新感染的节点入队
    层数 + 1
```

### 多源 BFS vs 单源 BFS

| 特性 | 单源 BFS | 多源 BFS |
|------|---------|---------|
| 初始队列 | 一个起点 | 多个起点 |
| 距离含义 | 到单个源的距离 | 到**最近的**源的距离 |
| 典型应用 | 迷宫最短路径 | 腐烂传播、多起点感染 |

### 常见错误
1. ❌ 忘记先统计新鲜橘子数（提前结束条件）
2. ❌ 在 BFS 循环内用 `len(q)` 但忘记 `fresh > 0` 提前终止
3. ❌ 修改 `grid` 时没有同步更新 `fresh` 计数

---

## 🧩 BFS 进阶技巧

### 1. 双向 BFS
已知起点和终点时，可以**交替**从两端 BFS，减少搜索空间。

```
起点 → → → → → → 终点
起点 → → → ← ← ← 终点  (相遇时最短)
```

### 2. 0-1 BFS（双端队列）
当边权只有 0 和 1 时，用 deque：权 0 的边放队首，权 1 的边放队尾。

### 3. A* 搜索
带启发式函数的 BFS（优先队列），适合有明确方向的目标搜索。

---

## ⚡ 今日总结

| 题目 | 核心技巧 | 难度 |
|------|---------|------|
| 迷宫中离入口最近的出口 | 矩阵 BFS + 边界判断 | ⭐⭐ |
| 腐烂的橘子 | 多源 BFS + 计数 | ⭐⭐ |

### BFS 适用场景清单
- ✅ 无权图的**最短路径**
- ✅ **多源**扩散问题
- ✅ 分层处理（按步数/分钟)
- ✅ 矩阵中的连通区域搜索

### 面试高频点
- BFS 模板必须**手写不卡顿**
- 理解「多源 BFS 为什么同时从所有腐烂橘子开始」
- 矩阵 BFS 的方向数组和边界检查
- 能区分 DFS 和 BFS 的适用场景
