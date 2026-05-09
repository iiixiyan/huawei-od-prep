# Day 31: 图进阶

## 📖 知识点
- **多源BFS**: 多个起点同时入队,适合求每个位置到最近起点的距离(01-Matrix).
- **二分图判定**: DFS/BFS二染色,相邻节点不同色.
- **隐式图BFS**: 状态作为节点,合法转换作为边(Open the Lock).
- **DAG所有路径**: DFS回溯求所有从源到汇的路径.

## 🧩 刷题任务（6题）

### 1. Reorder Routes（⭐⭐） 来源：L75
**思路**：建双向图,标记边的原始方向.从0出发DFS,若遇到反向走的边则需要反转(计数+1).
```python
def minReorder(self, n, connections):
    graph = [[] for _ in range(n)]
    for a, b in connections:
        graph[a].append((b, 1))   # 正向
        graph[b].append((a, 0))   # 反向
    
    def dfs(node, parent):
        count = 0
        for nei, direction in graph[node]:
            if nei == parent:
                continue
            if direction == 1:  # 需要反转
                count += 1
            count += dfs(nei, node)
        return count
    
    return dfs(0, -1)
```

### 2. Nearest Exit from Entrance in Maze（⭐⭐） 来源：L75
**思路**：BFS从入口走迷宫,遇到在边界的'.'即为出口(入口本身不算).返回最短步数.
```python
def nearestExit(self, maze, entrance):
    m, n = len(maze), len(maze[0])
    q = deque([(entrance[0], entrance[1], 0)])
    visited = set([(entrance[0], entrance[1])])
    
    while q:
        i, j, steps = q.popleft()
        if (i == 0 or i == m-1 or j == 0 or j == n-1) and [i, j] != entrance:
            return steps
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == '.' and (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((ni, nj, steps+1))
    return -1
```

### 3. All Paths From Source to Target（⭐⭐） 来源：O
**思路**：DAG上DFS回溯.从0出发,记录当前路径,到达n-1时保存路径.
```python
def allPathsSourceTarget(self, graph):
    n = len(graph)
    res = []
    
    def dfs(node, path):
        if node == n - 1:
            res.append(path[:])
            return
        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            path.pop()
    
    dfs(0, [0])
    return res
```

### 4. 01 Matrix（⭐⭐） 来源：O
**思路**：多源BFS.所有0入队(距离0),BFS逐层扩散更新1的距离.每个位置第一次被访问时距离最短.
```python
def updateMatrix(self, mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    dist = [[-1] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))
    
    while q:
        i, j = q.popleft()
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

### 5. Is Graph Bipartite?（⭐⭐） 来源：O
**思路**：二染色法.DFS对每个未染色节点染色0,邻接点染为1-当前色.若邻接点已染同色则不是二分图.
```python
def isBipartite(self, graph):
    n = len(graph)
    color = [-1] * n
    
    def dfs(node, c):
        if color[node] != -1:
            return color[node] == c
        color[node] = c
        for nei in graph[node]:
            if not dfs(nei, 1 - c):
                return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    return True
```

### 6. Open the Lock（⭐⭐⭐） 来源：O
**思路**：隐式图BFS.每个密码状态(0000~9999)为节点,每次转动一位(±1).deadends不可访问,求从0000到target的最短步数.
```python
def openLock(self, deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1
    
    q = deque([("0000", 0)])
    visited = set(["0000"])
    
    while q:
        state, steps = q.popleft()
        if state == target:
            return steps
        
        for i in range(4):
            for d in [-1, 1]:
                nxt = list(state)
                nxt[i] = str((int(nxt[i]) + d) % 10)
                nxt = "".join(nxt)
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
    return -1
```

## 📝 总结
- 多源BFS: 所有源点一起入队,距离同步更新.
- 二分图判定: 二染色,相邻异色,DFS/BFS均可.
- 隐式图: 状态定义+合法转移=BFS搜索.
- DAG回溯: 简单DFS,不需要visited(无环).
