# D48 — 图 + 并查集 + DP 综合 (6题)

---

## 1. Max Area of Island (O)

**思路**：DFS/BFS 遍历每个岛屿，记录最大面积

```python
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = 0
                stack = [(i, j)]
                grid[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                ans = max(ans, area)
    return ans

# 时间 O(m*n), 空间 O(m*n)
```

---

## 2. Longest Increasing Path in a Matrix (O)

**思路**：记忆化 DFS + DP  
`dp[i][j]` = 从 (i,j) 出发的最长递增路径长度  
递归搜索四个方向，满足值严格递增

```python
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]

    def dfs(i: int, j: int) -> int:
        if dp[i][j]:
            return dp[i][j]
        best = 1
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                best = max(best, 1 + dfs(ni, nj))
        dp[i][j] = best
        return best

    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))
    return ans

# 时间 O(m*n), 空间 O(m*n)
```

---

## 3. Redundant Connection (O)

**思路**：并查集，遍历边，若两端已连通则此边冗余

```python
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    parent = list(range(n + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]
    return []

# 时间 O(n·α(n)), 空间 O(n)
```

---

## 4. Alien Dictionary (O)

**思路**：拓扑排序  
1. 比较相邻单词，找出字符顺序关系  
2. 建图 + 入度表  
3. BFS 拓扑排序

```python
def alienOrder(words: list[str]) -> str:
    adj = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in adj}
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        if len(a) > len(b) and a[:len(b)] == b:
            return ""
        for c1, c2 in zip(a, b):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    indeg[c2] = indeg.get(c2, 0) + 1
                break
    q = [c for c in indeg if indeg[c] == 0]
    res = []
    while q:
        c = q.pop(0)
        res.append(c)
        for nei in adj[c]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return "".join(res) if len(res) == len(adj) else ""

# 时间 O(C) 总字符数, 空间 O(1) 最多 26 个字符
```

---

## 5. Sequence Reconstruction (O)

**思路**：检查 `org` 是否为由 `seqs` 唯一确定的拓扑排序  
1. 建图，统计每个节点的前驱集合  
2. BFS 验证唯一性：每层队列大小只能为 1

```python
def sequenceReconstruction(org: list[int], seqs: list[list[int]]) -> bool:
    n = len(org)
    pos = {x: i for i, x in enumerate(org)}
    indeg = [0] * (n + 1)
    graph = [set() for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for seq in seqs:
        for x in seq:
            if x < 1 or x > n:
                return False
            visited[x] = True
        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i + 1]
            if b not in graph[a]:
                graph[a].add(b)
                indeg[b] += 1

    if not all(visited[1:]):
        return False

    from collections import deque
    q = deque([x for x in range(1, n + 1) if indeg[x] == 0])
    res = []
    while q:
        if len(q) > 1:
            return False
        x = q.popleft()
        res.append(x)
        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return res == org

# 时间 O(N + E), 空间 O(N + E)
```

---

## 6. Similar String Groups (O)

**思路**：并查集  
两字符串相似（仅交换两个字符或完全相同）则合并  
返回连通分量数

```python
def numSimilarGroups(strs: list[str]) -> int:
    n = len(strs)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    def similar(a: str, b: str) -> bool:
        diff = 0
        for ca, cb in zip(a, b):
            if ca != cb:
                diff += 1
                if diff > 2:
                    return False
        return diff == 0 or diff == 2

    for i in range(n):
        for j in range(i + 1, n):
            if similar(strs[i], strs[j]):
                union(i, j)

    return len({find(i) for i in range(n)})

# 时间 O(n² * L), L = 字符串长度, 空间 O(n)
```
