# Day 19 — Graph DFS

> 图 DFS、邻接表、连通分量

---

## 📌 核心知识点

### 图的基本表示

```python
# 邻接表（最常用）
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
```

### 图 DFS 模板

```python
def dfs_graph(graph, start):
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
    return visited
```

### 图 vs 树 DFS 的区别

| 特性 | 树 DFS | 图 DFS |
|------|--------|--------|
| 访问标记 | 不需要（树无环） | 需要 visited 标记 |
| 可能 | 全部连通 | 多个连通分量 |
| 方向 | 只有父子 | 可能双向 |

---

## 🧩 题目 1：钥匙和房间

**LeetCode 841 | 难度：Medium**

### 题目描述
有 N 个房间，每个房间里有若干钥匙（能打开其他房间）。初始时只有 0 号房间是打开的，判断是否能进入所有房间。

### 解法：DFS

```python
def canVisitAllRooms(rooms):
    n = len(rooms)
    visited = [False] * n

    def dfs(room):
        visited[room] = True
        for key in rooms[room]:
            if not visited[key]:
                dfs(key)

    dfs(0)
    return all(visited)
```

- **时间复杂度**：O(N + K)，K 为钥匙总数
- **空间复杂度**：O(N)

### 解法 2：BFS（队列）

```python
from collections import deque

def canVisitAllRooms(rooms):
    visited = {0}
    q = deque([0])
    while q:
        room = q.popleft()
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                q.append(key)
    return len(visited) == len(rooms)
```

### 面试要点
- 这是一个**有向图可达性**问题
- 房间 = 节点，钥匙 = 有向边
- 关键是**避免重复访问**（用 visited 集合）

---

## 🧩 题目 2：省份数量

**LeetCode 547 | 难度：Medium**

### 题目描述
有 N 个城市，`isConnected[i][j] = 1` 表示城市 i 和 j 直接相连。求「省份」（连通分量）的数量。

### 解法 1：DFS 连通分量计数

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    provinces = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)          # 启动一次 DFS 遍历整个连通分量
            provinces += 1

    return provinces
```

- **时间复杂度**：O(N²) — 邻接矩阵遍历
- **空间复杂度**：O(N) — visited 数组

### 解法 2：并查集（Union-Find）

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        # 按秩合并
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1

def findCircleNum(isConnected):
    n = len(isConnected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)
    return uf.count
```

### 两种解法对比

| 方法 | 时间复杂度 | 空间复杂度 | 适用场景 |
|------|-----------|-----------|---------|
| DFS | O(N²) | O(N) | 简单直观 |
| 并查集 | O(N²·α(N)) | O(N) | 动态连通性、大量合并操作 |

### 面试话术
> "DFS 适合静态图连通分量计数；并查集的优势在于可以**动态合并**，而且路径压缩 + 按秩合并可以做到近乎 O(1) 的操作。"

---

## 🧩 题目 3：重新规划路线

**LeetCode 1466 | 难度：Medium**

### 题目描述
N 个城市之间有 N-1 条有向道路，所有道路能保证从 0 出发到达所有城市（**忽略方向**）。每条路有一个方向，求最少需要改变多少条路的方向，使得所有城市都能**沿道路方向**到达城市 0。

### 解法：双向建图 + DFS

```python
from collections import defaultdict

def minReorder(n, connections):
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append((b, 1))   # 1 表示原方向 a→b，需要更改
        graph[b].append((a, 0))   # 0 表示原方向 b→a，不需要更改

    visited = [False] * n
    changes = 0

    def dfs(city):
        nonlocal changes
        visited[city] = True
        for neighbor, needs_change in graph[city]:
            if not visited[neighbor]:
                changes += needs_change   # 如果方向是反的，需要改
                dfs(neighbor)

    dfs(0)
    return changes
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(N)

### 核心思想
1. 把**有向图**当作**无向图**遍历
2. 在邻接表中记录边的**原始方向**
3. 从 0 出发 BFS/DFS，如果当前边方向是「离开 0」方向，则需要反转

### 图示理解
```
原始: 0 → 1 ← 2    从 0 出发遍历：
双向建图:                  
0 --1--> 1              0(出发) → 1 (需要改: 1→0)
0 <--0-- 1              1 → 2 (不需要改: 2→1)
1 <--0-- 2              
2 --1--> 1              
```

---

## 🧩 题目 4：除法求值

**LeetCode 399 | 难度：Medium**

### 题目描述
给定算式 `a / b = value` 和一些查询 `x / y`，求每个查询的结果。不能确定则返回 -1.0。

### 解法：带权图 DFS

```python
from collections import defaultdict

def calcEquation(equations, values, queries):
    # 建图：a -> (b, a/b), b -> (a, b/a)
    graph = defaultdict(list)
    for (a, b), val in zip(equations, values):
        graph[a].append((b, val))
        graph[b].append((a, 1.0 / val))

    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor, val in graph[start]:
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return val * result
        return -1.0

    return [dfs(a, b, set()) for a, b in queries]
```

- **时间复杂度**：O(Q × N)，Q 为查询数
- **空间复杂度**：O(N)

### 更优解法：Floyd 或并查集
- **Floyd 全源最短路**：预处理所有可能的除法值，O(N³ + Q)
- **带权并查集**：维护节点到根的比值，O((N+Q)·α(N))

### 关键点
1. 每个节点既是分子也是分母 → 双向建图
2. 边权是除法结果，反向边权是倒数
3. `a / b = a/c × c/b` → DFS 沿路径连乘

---

## ⚡ 今日总结

| 题目 | 核心技巧 | 难度 |
|------|---------|------|
| 钥匙和房间 | 有向图可达性 | ⭐⭐ |
| 省份数量 | 连通分量计数 DFS / 并查集 | ⭐⭐ |
| 重新规划路线 | 双向建图 + 方向标记 | ⭐⭐⭐ |
| 除法求值 | 带权图 DFS / Floyd | ⭐⭐⭐ |

### 面试高频点
- ✅ 图 DFS = 树 DFS + visited 标记
- ✅ 邻接表是图的最常用表示
- ✅ 双向建图技巧（处理有向边反向遍历）
- ✅ 带权图的 DFS：路径累积
