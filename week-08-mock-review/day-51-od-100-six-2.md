# Day 51 — OD 100分 × 6 实战

## 1. 三叉树高度 (OD)

### 问题描述
给定一棵三叉树（每个节点最多有三个子节点）的前序遍历序列和每个节点的子节点数量序列，请计算树的高度（根节点高度为1）。

前序遍历序列：按前序顺序排列的节点值列表
子节点数量序列：与前序遍历对应的每个节点的子节点数量

### 输入格式
```
第一行：N，节点个数
第二行：N个整数，前序遍历序列
第三行：N个整数，对应每个节点的子节点数量 (0 ≤ cnt ≤ 3)
```

### 输出格式
一个整数，表示树的高度。

### 样例输入
```
7
1 2 4 5 6 3 7
2 0 2 0 0 0 0
```

### 样例输出
```
3
```

### 解题思路
递归构建 + 深度计算。根据前序遍历和子节点数量递归构建子树，同时记录最大深度。

### Python 解法

```python
def build_tree(preorder, children, idx=0, depth=1):
    if idx >= len(preorder):
        return idx, depth
    node = preorder[idx]
    cnt = children[idx]
    max_depth = depth
    cur_idx = idx + 1
    for _ in range(cnt):
        cur_idx, child_depth = build_tree(preorder, children, cur_idx, depth + 1)
        max_depth = max(max_depth, child_depth)
    return cur_idx, max_depth

if __name__ == "__main__":
    n = int(input().strip())
    preorder = list(map(int, input().strip().split()))
    children = list(map(int, input().strip().split()))
    _, height = build_tree(preorder, children)
    print(height)
```

**复杂度**: O(N) 时间, O(N) 栈空间

---

## 2. 最富裕小家庭 (OD)

### 问题描述
在一个家族中，每个成员都有唯一的编号（1-N）。每个成员可能有0个或多个后代。一个小家庭定义为：一对父母和他们的所有直系子女。给定每个成员的财富值和家族的父子关系，请找出财富总和最大的小家庭，输出其财富总和。

### 输入格式
```
第一行：N，成员数量 (1 ≤ N ≤ 10^5)
第二行：N个整数，wealth[i] 表示编号 i+1 的财富
第三行开始每行：A B 表示 A 是 B 的父亲
最后一行：-1 -1
```

### 输出格式
一个整数，最大财富总和。

### 样例输入
```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
-1 -1
```

### 样例输出
```
100
```

### Python 解法

```python
def richest_family(n, wealth, relations):
    children = [[] for _ in range(n + 1)]
    for a, b in relations:
        children[a].append(b)
    max_sum = 0
    for i in range(1, n + 1):
        total = wealth[i - 1]
        for c in children[i]:
            total += wealth[c - 1]
        max_sum = max(max_sum, total)
    return max_sum

if __name__ == "__main__":
    n = int(input().strip())
    wealth = list(map(int, input().strip().split()))
    relations = []
    while True:
        a, b = map(int, input().strip().split())
        if a == -1:
            break
        relations.append((a, b))
    print(richest_family(n, wealth, relations))
```

**复杂度**: O(N) 时间, O(N) 空间

---

## 3. 疫情扩散 (OD-BFS)

### 问题描述
在一个 N×M 的网格中，0 表示空地，1 表示健康人，2 表示已感染者。每天感染者的上下左右四个方向上的健康人会变成感染者。问至少需要多少天才能感染所有健康人？如果无法全部感染，输出 -1。

### 输入格式
```
第一行：N M
接下来 N 行，每行 M 个整数（0/1/2）
```

### 输出格式
一个整数，表示最少天数。

### 样例输入
```
3 3
2 1 1
1 1 0
0 1 1
```

### 样例输出
```
4
```

### Python 解法 (BFS)

```python
from collections import deque

def spread_days(grid, n, m):
    q = deque()
    healthy = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                healthy += 1

    if healthy == 0:
        return 0

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    max_days = 0
    while q:
        x, y, d = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 2
                healthy -= 1
                nd = d + 1
                max_days = max(max_days, nd)
                q.append((nx, ny, nd))

    return -1 if healthy > 0 else max_days

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    print(spread_days(grid, n, m))
```

**复杂度**: O(N×M) 时间, O(N×M) 空间

---

## 4. 服务器广播 (OD)

### 问题描述
有 N 台服务器，服务器之间通过连接进行广播。如果服务器 A 和 B 直接连接，A 向 B 发一条消息即可通信。如果 A 和 B 不直接连接，但可以通过中间服务器转发。给定 N×N 的邻接矩阵（1表示直接连接），问最少需要向多少台服务器发送初始消息，才能让所有服务器都收到消息。

### 输入格式
```
第一行：N (1 ≤ N ≤ 200)
接下来 N 行：每行 N 个整数（0或1）
```

### 输出格式
一个整数，表示最少初始发送的服务器数量。

### 样例输入
```
4
1 1 0 0
1 1 0 0
0 0 1 1
0 0 1 1
```

### 样例输出
```
2
```

### 解题思路
等价于求连通分量数。DFS/BFS/并查集均可。

### Python 解法 (DFS)

```python
def min_broadcast(adj, n):
    visited = [False] * n
    count = 0

    def dfs(u):
        visited[u] = True
        for v in range(n):
            if adj[u][v] == 1 and not visited[v]:
                dfs(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

if __name__ == "__main__":
    n = int(input().strip())
    adj = [list(map(int, input().strip().split())) for _ in range(n)]
    print(min_broadcast(adj, n))
```

**复杂度**: O(N²) 时间, O(N) 空间

---

## 5. 找等值元素 (OD)

### 问题描述
给定一个整数矩阵，找出所有出现次数超过矩阵元素总数一半的元素。如果有多个，按值从小到大输出；如果没有，输出 -1。

### 输入格式
```
第一行：N M (N行 M列, 1 ≤ N,M ≤ 100)
接下来 N 行：每行 M 个整数
```

### 输出格式
一行整数，空格分隔，或 -1。

### 样例输入
```
2 3
1 2 2
2 3 3
```

### 样例输出
```
2
```

### Python 解法

```python
def find_majority(matrix, n, m):
    total = n * m
    half = total // 2
    freq = {}
    for row in matrix:
        for val in row:
            freq[val] = freq.get(val, 0) + 1
    result = [k for k, v in freq.items() if v > half]
    if not result:
        return -1
    return " ".join(map(str, sorted(result)))

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    print(find_majority(matrix, n, m))
```

**复杂度**: O(N×M) 时间, O(N×M) 空间

---

## 6. 单入口空闲区域 (OD)

### 问题描述
在一个 N×M 的网格中，O 表示空闲区域，X 表示障碍物。有一个唯一的入口（在网格边界上），从入口进入后，可以上下左右移动。问最大的连通空闲区域面积（包含的 O 的数量）。如果入口被障碍物挡住（入口本身是 X），输出 -1。

### 输入格式
```
第一行：N M
第二行：入口坐标 x y (0-indexed)
接下来 N 行：每行 M 个字符（O 或 X）
```

### 输出格式
一个整数，表示最大连通空闲区域面积。

### 样例输入
```
4 4
0 2
O O O X
O X O X
X O O X
O O X X
```

### 样例输出
```
5
```

### Python 解法 (BFS/DFS)

```python
def max_free_area(grid, n, m, start_x, start_y):
    if grid[start_x][start_y] == 'X':
        return -1

    from collections import deque
    q = deque([(start_x, start_y)])
    grid[start_x][start_y] = 'V'  # visited
    count = 1
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'O':
                grid[nx][ny] = 'V'
                count += 1
                q.append((nx, ny))
    return count

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    sx, sy = map(int, input().strip().split())
    grid = [list(input().strip().split()) for _ in range(n)]
    print(max_free_area(grid, n, m, sx, sy))
```

**复杂度**: O(N×M) 时间, O(N×M) 空间
