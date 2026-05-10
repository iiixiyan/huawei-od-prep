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

### 1. Number of Islands（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/number-of-islands/)
**难度**：中等
**题目**：给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**示例 1：**
```
输入：grid = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出：1
```
**示例 2：**
```
输入：grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出：3
```
**提示：**

- `m == grid.length`

- `n == grid[i].length`

- `1
**思路**：遍历网格,遇到'1'则岛屿计数+1,用DFS将其所在连通分量全部标记为已访问(置'0').四方向搜索.
**代码**：
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
### 2. Surrounded Regions（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/surrounded-regions/)
**难度**：中等
**题目**：给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` 组成，**捕获**所有**被围绕的区域**：

- **连接：**一个单元格与水平或垂直方向上相邻的单元格连接。

- **区域：连接所有 **`'O'` 的单元格来形成一个区域。

- **围绕：**如果一个区域中的所有 `'O'` 单元格都不在棋盘的边缘，则该区域被包围。这样的区域 **完全**被 `'X'` 单元格包围。

通过**原地**将输入矩阵中的所有 `'O'` 替换为 `'X'` 来**捕获被围绕的区域**。你不需要返回任何值。

**示例 1：**
```
**输入：**board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
**输出：**[['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]
**解释：**
*
在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。
```
**示例 2：**
```
**输入：**board = [['X']]
**输出：**[['X']]
```
**提示：**

- `m == board.length`

- `n == board[i].length`

- `1
**思路**：从边界上的'O'出发DFS,标记所有与边界连通的'O'为临时字符(如'#'),然后遍历全图:剩余的'O'→'X','#'→'O'.
**代码**：
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
### 3. Clone Graph（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/clone-graph/)
**难度**：中等
**题目**：给你无向 **连通 **图中一个节点的引用，请你返回该图的 **深拷贝**（克隆）。

图中的每个节点都包含它的值 `val`（`int`） 和其邻居的列表（`list[Node]`）。

class Node {
public int val;
public List neighbors;
}

**测试用例格式：**

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（`val = 1`），第二个节点值为 2（`val = 2`），以此类推。该图在测试用例中使用邻接列表表示。

**邻接列表**是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将**给定节点的拷贝 **作为对克隆图的引用返回。

**示例 1：**
```
*
输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
```
**示例 2：**
```
*
输入：adjList = [[]]
输出：[[]]
解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
```
**示例 3：**
```
输入：adjList = []
输出：[]
解释：这个图是空的，它不含任何节点。
```
**提示：**

- 这张图中的节点数在 `[0, 100]` 之间。

- `1
**思路**：用哈希表记录原节点→克隆节点的映射.DFS递归克隆:复制值,递归克隆邻居,用映射避免重复克隆.
**代码**：
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
### 4. Number of Provinces（⭐⭐）
**来源**：[L75/O](https://leetcode.cn/problems/number-of-provinces/)
**难度**：中等
**题目**：有 `n` 个城市，其中一些彼此相连，另一些没有相连。如果城市 `a` 与城市 `b` 直接相连，且城市 `b` 与城市 `c` 直接相连，那么城市 `a` 与城市 `c` 间接相连。

**省份**是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 `n x n` 的矩阵 `isConnected` ，其中 `isConnected[i][j] = 1` 表示第 `i` 个城市和第 `j` 个城市直接相连，而 `isConnected[i][j] = 0` 表示二者不直接相连。

返回矩阵中**省份** 的数量。

**示例 1：**
```
*
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
```
**示例 2：**
```
*
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
```
**提示：**

- `1
**思路**：邻接矩阵表示图,DFS计数连通分量.visited数组标记已访问城市.
**代码**：
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
### 5. Evaluate Division（⭐⭐⭐）
**来源**：[L75/O](https://leetcode.cn/problems/evaluate-division/)
**难度**：中等
**题目**：给你一个变量对数组 `equations` 和一个实数值数组 `values` 作为已知条件，其中 `equations[i] = [Ai, Bi]` 和 `values[i]` 共同表示等式 `Ai / Bi = values[i]` 。每个 `Ai` 或 `Bi` 是一个表示单个变量的字符串。

另有一些以数组 `queries` 表示的问题，其中 `queries[j] = [Cj, Dj]` 表示第 `j` 个问题，请你根据已知条件找出 `Cj / Dj = ?` 的结果作为答案。

返回 **所有问题的答案** 。如果存在某个无法确定的答案，则用 `-1.0` 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 `-1.0` 替代这个答案。

**注意：**输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

**注意：**未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。

**示例 1：**
```
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 => -1.0
```
**示例 2：**
```
输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
```
**示例 3：**
```
输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
```
**提示：**

- `1 i.length, Bi.length j.length, Dj.length i, Bi, Cj, Dj` 由小写英文字母与数字组成
**思路**：建带权有向图(变量为节点,a/b=2.0 即 a->b权2.0,b->a权0.5).查询时DFS搜索路径,累计乘积.
**代码**：
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
### 6. Keys and Rooms（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/keys-and-rooms/)
**难度**：中等
**题目**：有 `n` 个房间，房间按从 `0` 到 `n - 1` 编号。最初，除 `0` 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。然而，你不能在没有获得钥匙的时候进入锁住的房间。

当你进入一个房间，你可能会在里面找到一套 **不同的钥匙**，每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。

给你一个数组 `rooms` 其中 `rooms[i]` 是你进入 `i` 号房间可以获得的钥匙集合。如果能进入 **所有** 房间返回 `true`，否则返回 `false`。

**示例 1：**
```
输入：rooms = [[1],[2],[3],[]]
输出：true
解释：
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
```
**示例 2：**
```
输入：rooms = [[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
```
**提示：**

- `n == rooms.length`

- `2
**思路**：DFS模拟开锁过程.用visited记录已进入的房间,从0开始DFS,每进入一个房间获取钥匙加入可访问邻居.最后检查visited长度是否等于总房间数.
**代码**：
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
