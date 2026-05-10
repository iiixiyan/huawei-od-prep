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

### 1. Course Schedule（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/course-schedule/)
**难度**：中等
**题目**：你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程  `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```
**示例 2：**
```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```
**提示：**

- `1 i, bi
**思路**：拓扑排序(Kahn算法).计算入度,将入度为0的节点入队,逐个出队并减少邻居入度.最后检查修完的课程数是否等于总课程数.
**代码**：
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
### 2. Course Schedule II（⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/course-schedule/)
**难度**：中等
**题目**：你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程  `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```
**示例 2：**
```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```
**提示：**

- `1 i, bi
**思路**：拓扑排序并返回课程顺序.与上题同理,出队时记录到结果列表.若存在环(修不完所有课程)返回空列表.
**代码**：
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
### 3. Snakes and Ladders（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/snakes-and-ladders/)
**难度**：中等
**题目**：给你一个大小为 `n x n` 的整数矩阵 `board` ，方格按从 `1` 到 `n2` 编号，编号遵循 转行交替方式 ，**从左下角开始**（即，从 `board[n - 1][0]` 开始）的每一行改变方向。

你一开始位于棋盘上的方格  `1`。每一回合，玩家需要从当前方格 `curr` 开始出发，按下述要求前进：

- 选定目标方格 `next` ，目标方格的编号在范围 `[curr + 1, min(curr + 6, n2)]` 。

- 该选择模拟了掷**六面体骰子**的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。

- 传送玩家：如果目标方格 `next` 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 `next` 。

- 当玩家到达编号 `n2` 的方格时，游戏结束。

如果 `board[r][c] != -1` ，位于 `r` 行 `c` 列的棋盘格中可能存在 “蛇” 或 “梯子”。那个蛇或梯子的目的地将会是 `board[r][c]`。编号为 `1` 和 `n2` 的方格不是任何蛇或梯子的起点。

注意，玩家在每次掷骰的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也**不能**继续移动。

- 举个例子，假设棋盘是 `[[-1,4],[-1,3]]` ，第一次移动，玩家的目标方格是 `2` 。那么这个玩家将会顺着梯子到达方格 `3` ，但**不能** 顺着方格 `3` 上的梯子前往方格 `4` 。（简单来说，类似飞行棋，玩家掷出骰子点数后移动对应格数，遇到单向的路径（即梯子或蛇）可以直接跳到路径的终点，但如果多个路径首尾相连，也不能连续跳多个路径）

返回达到编号为 `n2` 的方格所需的最少掷骰次数，如果不可能，则返回 `-1`。

**示例 1：**
```
*
输入：board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。
最后决定移动到方格 36 , 游戏结束。
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。
```
**示例 2：**
```
输入：board = [[-1,-1],[-1,3]]
输出：1
```
**提示：**

- `n == board.length == board[i].length`

- `2 2]` 内

- 编号为 `1` 和 `n2` 的方格上没有蛇或梯子
**思路**：BFS求最短步数.棋盘编号从1到N²,每步走1~6格,踩到梯子/蛇则直接传送到目标格.用visited避免重访.
**代码**：
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
### 4. Minimum Genetic Mutation（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/minimum-genetic-mutation/)
**难度**：中等
**题目**：基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 `'A'`、`'C'`、`'G'` 和 `'T'` 之一。

假设我们需要调查从基因序列 `start` 变为 `end` 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

- 例如，`"AACCGGTT" --> "AACCGGTA"` 就是一次基因变化。

另有一个基因库 `bank` 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 `bank` 中）

给你两个基因序列 `start` 和 `end` ，以及一个基因库 `bank` ，请你找出并返回能够使 `start` 变化为 `end` 所需的最少变化次数。如果无法完成此基因变化，返回 `-1` 。

注意：起始基因序列 `start` 默认是有效的，但是它并不一定会出现在基因库中。

**示例 1：**
```
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
```
**示例 2：**
```
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
```
**示例 3：**
```
输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3
```
**提示：**

- `start.length == 8`

- `end.length == 8`

- `0
**思路**：BFS求最短突变路径.每次改变一个碱基,突变结果必须在bank集合中.BFS逐层扩展,首次到达endGene即为最短步数.
**代码**：
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
### 5. Word Ladder（⭐⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/word-ladder/)
**难度**：困难
**题目**：字典 `wordList` 中从单词 `beginWord`  *到 `endWord` 的 **转换序列 **是一个按下述规格形成的序列 `beginWord -> s1 -> s2 -> ... -> sk`：

- 每一对相邻的单词只差一个字母。

-  对于 `1  `si` 都在 `wordList` 中。注意， `beginWord`  *不需要在 `wordList` 中。

- `sk == endWord`

给你两个单词* *`beginWord`  *和 `endWord` 和一个字典 `wordList` ，返回 *从 `beginWord` 到 `endWord` 的 **最短转换序列**中的**单词数目*** 。如果不存在这样的转换序列，返回 `0` 。

**示例 1：**
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
```
**示例 2：**
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
```
**提示：**

- `1
**思路**：双向BFS优化.从beginWord和endWord同时BFS,每次扩展较小的一层.每个单词改变一个字母,邻接词必须在wordList中.
**代码**：
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
### 6. Rotting Oranges（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/rotting-oranges/)
**难度**：中等
**题目**：在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；

- 值 `1` 代表新鲜橘子；

- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。

**示例 1：**
```
*****
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
```
**示例 2：**
```
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
```
**示例 3：**
```
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```
**提示：**

- `m == grid.length`

- `n == grid[i].length`

- `1
**思路**：多源BFS.将所有初始腐烂橘子入队,记录新鲜橘子数.BFS逐分钟传播腐烂,每层时间+1.若最后仍有新鲜橘子返回-1.
**代码**：
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
