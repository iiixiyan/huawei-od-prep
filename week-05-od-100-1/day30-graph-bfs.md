# Day 30: 图-BFS

## 📖 知识点
**BFS on Graph** — 广度优先搜索,使用队列逐层遍历.适用于最短路径(无权图)、拓扑排序、层次遍历.
```python
from collections import deque
def bfs(start):
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        steps += 1
    return steps
```

## 🧩 刷题任务（6题）

### 1. Course Schedule（⭐⭐） 来源：T150
**思路**：拓扑排序(Kahn算法).计算入度,将入度为0的节点入队,逐个出队并减少邻居入度.最后检查修完的课程数是否等于总课程数.
```python
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return count == numCourses
```

### 2. Course Schedule II（⭐⭐） 来源：T150/O
**思路**：拓扑排序并返回课程顺序.与上题同理,出队时记录到结果列表.若存在环(修不完所有课程)返回空列表.
```python
def findOrder(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return res if len(res) == numCourses else []
```

### 3. Snakes and Ladders（⭐⭐⭐） 来源：T150
**思路**：BFS求最短步数.棋盘编号从1到N²,每步走1~6格,踩到梯子/蛇则直接传送到目标格.用visited避免重访.
```python
def snakesAndLadders(self, board):
    n = len(board)
    # 将棋盘编号映射到坐标
    def get_pos(num):
        r = (num - 1) // n
        c = (num - 1) % n
        if r % 2 == 1:  # 奇数行从右往左
            c = n - 1 - c
        return n - 1 - r, c
    
    q = deque([(1, 0)])  # (格子编号,步数)
    visited = set([1])
    while q:
        num, steps = q.popleft()
        if num == n * n:
            return steps
        for nxt in range(num + 1, min(num + 6, n * n) + 1):
            r, c = get_pos(nxt)
            dest = board[r][c] if board[r][c] != -1 else nxt
            if dest not in visited:
                visited.add(dest)
                q.append((dest, steps + 1))
    return -1
```

### 4. Minimum Genetic Mutation（⭐⭐） 来源：T150
**思路**：BFS求最短突变路径.每次改变一个碱基,突变结果必须在bank集合中.BFS逐层扩展,首次到达endGene即为最短步数.
```python
def minMutation(self, startGene, endGene, bank):
    bankSet = set(bank)
    if endGene not in bankSet:
        return -1
    genes = ['A', 'C', 'G', 'T']
    q = deque([(startGene, 0)])
    visited = {startGene}
    while q:
        gene, steps = q.popleft()
        if gene == endGene:
            return steps
        for i in range(8):
            for g in genes:
                if g == gene[i]:
                    continue
                nxt = gene[:i] + g + gene[i+1:]
                if nxt in bankSet and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
    return -1
```

### 5. Word Ladder（⭐⭐⭐） 来源：T150/O
**思路**：双向BFS优化.从beginWord和endWord同时BFS,每次扩展较小的一层.每个单词改变一个字母,邻接词必须在wordList中.
```python
def ladderLength(self, beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    forward = {beginWord}
    backward = {endWord}
    visited = set()
    steps = 1
    
    while forward and backward:
        if len(forward) > len(backward):
            forward, backward = backward, forward
        next_level = set()
        for word in forward:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    nxt = word[:i] + c + word[i+1:]
                    if nxt in backward:
                        return steps + 1
                    if nxt in wordSet and nxt not in visited:
                        visited.add(nxt)
                        next_level.add(nxt)
        forward = next_level
        steps += 1
    return 0
```

### 6. Rotting Oranges（⭐⭐） 来源：L75
**思路**：多源BFS.将所有初始腐烂橘子入队,记录新鲜橘子数.BFS逐分钟传播腐烂,每层时间+1.若最后仍有新鲜橘子返回-1.
```python
def orangesRotting(self, grid):
    m, n = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    q.append((ni, nj))
        minutes += 1
    return minutes if fresh == 0 else -1
```

## 📝 总结
- BFS求无权图最短路径: 第一次到达目标即为最短.
- 拓扑排序: 入度表+Kahn队列,检测环.
- 双向BFS: 大幅减少搜索空间(Word Ladder).
- 多源BFS: 将多个起点同时入队(Rotting Oranges).
