# Day 37: 图&BFS — 最短路径 & 岛屿问题

## 📖 知识点
**图 BFS 核心套路**：
- **BFS 模板**：queue = deque([(start)]), visited 标记已访问，逐层扩展邻居
- **最短路径**：BFS 天然保证无权图的最短路径（首次到达即最短）
- **多源 BFS**：初始把多个源点全部入队，适用于"感染""传播"类问题
- **岛屿类问题**：遍历网格，遇到陆地(1)则 BFS/DFS 标记整片岛屿，计数+1
- **方向数组**：`dirs = [(0,1),(0,-1),(1,0),(-1,0)]` 或 `dirs = [(1,0),(-1,0),(0,1),(0,-1)]`

## 🧩 刷题任务

### 题目1：矩阵扩散 / 计算疫情扩散时间 (OD 100分)
**难度**：⭐⭐
**题目描述**：
一个 n×m 的网格，0 表示未感染区域，1 表示已感染区域。每天每个感染区域会向其上下左右四个方向的相邻未感染区域传播。问最少需要多少天，所有区域都被感染？如果始终无法全部感染，输出 -1。

**输入**：
```
4 4
0 1 0 0
0 0 0 0
0 0 0 0
0 0 0 1
```
**输出**：
```
4
```

**思路分析**：
1. 多源 BFS：将所有初始为 1 的位置入队
2. 记录一个 days 变量，每层 BFS days+1
3. 当队列为空时，检查是否还有 0 未感染
4. 注意：如果一开始没有感染源（全是0），返回 -1

**参考代码**：
```python
from collections import deque

def infection_days(grid, n, m):
    q = deque()
    total = n * m
    infected = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j, 0))
                infected += 1
    if infected == 0:
        return -1
    if infected == total:
        return 0
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    max_days = 0
    while q:
        x, y, d = q.popleft()
        max_days = max(max_days, d)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                infected += 1
                q.append((nx, ny, d + 1))
    return max_days if infected == total else -1

# 测试
n, m = 4, 4
grid = [
    [0,1,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,1]
]
print(infection_days(grid, n, m))  # 4
```

**OD备考提示**：多源 BFS 模板题。注意最后检查是否全部感染。天数统计在入队时记录（d+1）更准确。

---

### 题目2：服务器广播 / Linux发行版的数量 (OD 100分)
**难度**：⭐⭐
**题目描述**：
给定一个 n×n 的连通矩阵 conn，conn[i][j]=1 表示服务器 i 和 j 直接相连。相互连通的服务器属于同一个广播域。问总共有多少个独立的广播域（即连通分量数）？

**输入**：
```
4
1 1 0 0
1 1 0 0
0 0 1 1
0 0 1 1
```
**输出**：
```
2
```

**思路分析**：
1. 构建邻接表或直接用矩阵遍历
2. BFS/DFS 遍历所有未访问节点，每启动一次搜索就计数+1
3. 使用 visited 数组标记已访问的服务器
4. 本质就是求无向图的连通分量个数

**参考代码**：
```python
from collections import deque

def count_broadcast_domains(conn, n):
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            q = deque([i])
            visited[i] = True
            while q:
                node = q.popleft()
                for j in range(n):
                    if conn[node][j] == 1 and not visited[j]:
                        visited[j] = True
                        q.append(j)
    return count

# 测试
n = 4
conn = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,1]
]
print(count_broadcast_domains(conn, n))  # 2
```

**OD备考提示**：连通分量题非常高频！也可以用并查集（Union-Find）实现，BFS/DFS 更直观。注意矩阵是对称的，遍历时只读上三角即可，但为了简洁直接遍历全矩阵。

## 📝 今日小结
- 多源 BFS 模板：全部源点入队，逐层扩展
- 连通分量计数：DFS/BFS 遍历 + visited 标记
- 方向数组写法要熟练，注意边界检查
