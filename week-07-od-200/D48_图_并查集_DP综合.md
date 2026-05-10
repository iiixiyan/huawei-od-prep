# D48 — 图 + 并查集 + DP 综合 (6题)

---

## 1. Max Area of Island (O)
**题目**：给你一个大小为 `m x n` 的二进制矩阵 `grid` 。

**岛屿** 是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在 **水平或者竖直的四个方向上 **相邻。你可以假设 `grid` 的四个边缘都被 `0`（代表水）包围着。

岛屿的面积是岛上值为 `1` 的单元格的数目。

计算并返回 `grid` 中最大的岛屿面积。如果没有岛屿，则返回面积为 `0` 。

**示例 1：**

*

```
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
```

**难度**：中等

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
**题目**：给定一个 `m x n` 整数矩阵 `matrix` ，找出其中 **最长递增路径** 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 **不能** 在 **对角线** 方向上移动或移动到 **边界外**（即不允许环绕）。

**示例 1：**

*

```
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。
```

**示例 2：**

*

```
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
```

**示例 3：**

```
输入：matrix = [[1]]
输出：1
```

**提示：**

- `m == matrix.length`

- `n == matrix[i].length`

- `1 31 - 1`

**难度**：困难

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
**题目**：树可以看成是一个连通且 **无环 **的 **无向 **图。

给定一个图，该图从一棵 `n` 个节点 (节点值 `1～n`) 的树中添加一条边后获得。添加的边的两个不同顶点编号在 `1` 到 `n` 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 `n` 的二维数组 `edges` ，`edges[i] = [ai, bi]` 表示图中在 `ai` 和 `bi` 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 `n` 个节点的树。如果有多个答案，则返回数组 `edges` 中最后出现的那个。

**示例 1：**

*

```
输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]
```

**示例 2：**

*

```
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
```

**提示:**

- `n == edges.length`

- `3 <= n <= 1000`

- `edges[i].length == 2`

- `1 <= ai < bi <= edges.length`

- `ai != bi`

- `edges` 中无重复元素

- 给定的图是连通的

**难度**：中等

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
**题目**：如果交换字符串 `X` 中的两个不同位置的字母，使得它和字符串 `Y` 相等，那么称 `X` 和 `Y` 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，`"tars"` 和 `"rats"` 是相似的 (交换 `0` 与 `2` 的位置)； `"rats"` 和 `"arts"` 也是相似的，但是 `"star"` 不与 `"tars"`，`"rats"`，或 `"arts"` 相似。

总之，它们通过相似性形成了两个关联组：`{"tars", "rats", "arts"}` 和 `{"star"}`。注意，`"tars"` 和 `"arts"` 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 `strs`。列表中的每个字符串都是 `strs` 中其它所有字符串的一个字母异位词。请问 `strs` 中有多少个相似字符串组？

**难度**：困难

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
