# Day 29: 图-DFS

## 📖 知识点
**DFS on Graph** — 深度优先搜索遍历图,使用递归或显式栈.核心模板:
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```
**适用场景**:连通分量计数、可达性判断、环检测、拓扑排序(后序).

## 🧩 刷题任务（6题）

### 1. Number of Islands（⭐⭐） 来源：T150
**思路**：遍历网格,遇到'1'则岛屿计数+1,用DFS将其所在连通分量全部标记为已访问(置'0').四方向搜索.
```python
def numIslands(self, grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count
```

### 2. Surrounded Regions（⭐⭐） 来源：T150
**思路**：从边界上的'O'出发DFS,标记所有与边界连通的'O'为临时字符(如'#'),然后遍历全图:剩余的'O'→'X','#'→'O'.
```python
def solve(self, board):
    if not board:
        return
    m, n = len(board), len(board[0])
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '#'
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(i+di, j+dj)
    
    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)
    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
```

### 3. Clone Graph（⭐⭐） 来源：T150
**思路**：用哈希表记录原节点→克隆节点的映射.DFS递归克隆:复制值,递归克隆邻居,用映射避免重复克隆.
```python
def cloneGraph(self, node):
    if not node:
        return None
    visited = {}
    
    def dfs(n):
        if n in visited:
            return visited[n]
        clone = Node(n.val)
        visited[n] = clone
        for nei in n.neighbors:
            clone.neighbors.append(dfs(nei))
        return clone
    
    return dfs(node)
```

### 4. Number of Provinces（⭐⭐） 来源：L75/O
**思路**：邻接矩阵表示图,DFS计数连通分量.visited数组标记已访问城市.
```python
def findCircleNum(self, isConnected):
    n = len(isConnected)
    visited = [False] * n
    count = 0
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if isConnected[i][j] == 1 and not visited[j]:
                dfs(j)
    
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count
```

### 5. Evaluate Division（⭐⭐⭐） 来源：L75/O
**思路**：建带权有向图(变量为节点,a/b=2.0 即 a->b权2.0,b->a权0.5).查询时DFS搜索路径,累计乘积.
```python
def calcEquation(self, equations, values, queries):
    graph = {}
    for (a, b), v in zip(equations, values):
        graph.setdefault(a, {})[b] = v
        graph.setdefault(b, {})[a] = 1.0 / v
    
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for nei, val in graph[start].items():
            if nei not in visited:
                ans = dfs(nei, end, visited)
                if ans != -1.0:
                    return val * ans
        return -1.0
    
    return [dfs(q[0], q[1], set()) for q in queries]
```

### 6. Keys and Rooms（⭐⭐） 来源：L75
**思路**：DFS模拟开锁过程.用visited记录已进入的房间,从0开始DFS,每进入一个房间获取钥匙加入可访问邻居.最后检查visited长度是否等于总房间数.
```python
def canVisitAllRooms(self, rooms):
    visited = set()
    
    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)
    
    dfs(0)
    return len(visited) == len(rooms)
```

## 📝 总结
- 图DFS核心: visited避免重复,递归或栈实现.
- 网格图的DFS: 注意边界检查和方向数组.
- 带权图: 边存储权重,DFS累积路径值.
- 连通分量计数: 遍历所有节点,对未访问的启动DFS.
