# Day 55 — 🧪 限时模考 #2
## 100分 + 200分 | 90分钟

---

# 模考说明

| 项目 | 内容 |
|------|------|
| 总时间 | 90 分钟 |
| 题量 | 2 题（100分 + 200分） |
| 总分 | 300 分 |
| 环境 | 可使用本地 IDE，需自行处理输入输出 |
| 建议 | 第1题30分钟，第2题60分钟 |

**考试纪律**: 限时完成，200分题难度较高，建议先做100分题保底。

---

# 题目一：最长连续序列 (100分)

## 问题描述
给定一个未排序的整数数组，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。要求时间复杂度 O(N)。

### 示例
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长数字连续序列是 [1, 2, 3, 4]，长度为 4。

## 输入格式
```
第一行：N (1 ≤ N ≤ 10^5)
第二行：N 个整数 (绝对值 ≤ 10^9)
```

## 输出格式
一个整数，表示最长连续序列的长度。

## 样例输入
```
6
100 4 200 1 3 2
```

## 样例输出
```
4
```

## 评分标准
| 项目 | 分值 |
|------|------|
| 正确理解题意（连续指值连续，非下标连续） | 20分 |
| O(N) 时间复杂度实现 | 40分 |
| 正确处理输入输出 | 20分 |
| 通过所有测试用例 | 20分 |

---

# 题目二：最短路径 — 带障碍物 (200分)

## 问题描述
在一个 N×M 的网格中，0 表示可通行，1 表示障碍物。你可以上下左右移动，每次移动一步，耗时 1 分钟。你有一个特殊技能：可以消除最多 K 个障碍物（将 1 变成 0），每次消除耗时 0 分钟（瞬间完成）。请计算从起点 (0,0) 到终点 (N-1, M-1) 所需的最短时间。如果无法到达，输出 -1。

### 示例
网格:
```
0 1 0
0 1 0
0 0 0
```
K = 1
起点 (0,0), 终点 (2,2)
路径: (0,0)→(0,1)消除→(1,1)消除? 等等，K=1只能消除1个。
实际最短路径: (0,0)→(1,0)→(2,0)→(2,1)→(2,2) 不需要消除，长度4。

如果 K = 0，则必须走全 0 路径。

## 输入格式
```
第一行：N M K (1 ≤ N,M ≤ 100, 0 ≤ K ≤ N×M)
接下来 N 行：每行 M 个整数 (0或1)
```

## 输出格式
一个整数，表示最短时间。如果无法到达，输出 -1。

## 样例输入
```
3 3 1
0 1 0
0 1 0
0 0 0
```

## 样例输出
```
4
```

## 评分标准
| 项目 | 分值 |
|------|------|
| 正确理解状态（位置+已消除数） | 40分 |
| 正确实现 BFS 最短路 | 60分 |
| 处理 K 的约束 | 40分 |
| 代码质量与输入输出 | 30分 |
| 通过所有测试用例 | 30分 |

---

# 答案与解析

## 题目一 题解

### 思路分析
O(N) 解法：用 set 存储所有数字。遍历集合，只对「某数-1不在集合中」的数开始计数（即序列起点），然后不断 +1 检查长度。这样每个数最多被访问两次。

### Python 解法

```python
def longest_consecutive(nums):
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # 只从序列起点开始检查
        if num - 1 not in num_set:
            cur = num
            cur_len = 1
            while cur + 1 in num_set:
                cur += 1
                cur_len += 1
            max_len = max(max_len, cur_len)

    return max_len

if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(longest_consecutive(nums))
```

**复杂度**: O(N) 时间, O(N) 空间

**易错点**:
- 必须用 set 去重
- 只对序列起点进行检查（num-1 not in set）保证 O(N)
- 注意空数组边界情况（N≥1所以不需处理）

---

## 题目二 题解

### 思路分析
这是一个三维状态的 BFS 最短路径问题。状态 `(x, y, k_used)` 表示在 (x,y) 且已经消除了 k_used 个障碍物。用 `dist[x][y][k+1]` 数组记录最短步数。

当走到障碍物 (grid[nx][ny] == 1) 且 k_used < K 时，可以消除并进入状态 `(nx, ny, k_used + 1)`，步数 +1。
当走到空地 (grid[nx][ny] == 0) 时，直接进入状态 `(nx, ny, k_used)`，步数 +1。

关键: 第一次访问到某个状态时的步数就是最短的（BFS 性质）。

### Python 解法

```python
from collections import deque

def shortest_path(grid, n, m, K):
    INF = float('inf')
    # dist[x][y][k] = 到 (x,y) 且消除了 k 个障碍物的最短步数
    dist = [[[INF] * (K + 1) for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 0

    q = deque([(0, 0, 0)])  # (x, y, k_used)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, k = q.popleft()
        d = dist[x][y][k]

        # 到达终点
        if x == n - 1 and y == m - 1:
            return d

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    # 障碍物，需要消除
                    if k < K and dist[nx][ny][k + 1] == INF:
                        dist[nx][ny][k + 1] = d + 1
                        q.append((nx, ny, k + 1))
                else:
                    # 空地
                    if dist[nx][ny][k] == INF:
                        dist[nx][ny][k] = d + 1
                        q.append((nx, ny, k))

    return -1

if __name__ == "__main__":
    n, m, K = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    print(shortest_path(grid, n, m, K))
```

**复杂度分析**:
- 时间复杂度: O(N × M × K)，每个状态最多访问一次
- 空间复杂度: O(N × M × K)

N,M ≤ 100, K ≤ N×M = 10000，最坏 100×100×10000 = 10^8 状态，可能超内存。

### 优化思路
K 的实际有效值不超过曼哈顿距离或实际需要的消除数。可以用位图或 visited 集合来优化。

另一种优化：使用 Dijkstra（因为边权为1，BFS即可），但将 K 视为资源。

**进一步优化**: K 的有效上限是网格中障碍物数量，但实际不需要超过 N+M（因为最短路径最多需要消除 N+M 个障碍物）。所以令 `K = min(K, n + m)` 可以大幅降低复杂度。

```python
def shortest_path_optimized(grid, n, m, K):
    K = min(K, n + m)  # 有效上限

    from collections import deque

    INF = float('inf')
    dist = [[[INF] * (K + 1) for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 0

    q = deque([(0, 0, 0)])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, k = q.popleft()
        d = dist[x][y][k]

        if x == n - 1 and y == m - 1:
            return d

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    if k < K and dist[nx][ny][k + 1] == INF:
                        dist[nx][ny][k + 1] = d + 1
                        q.append((nx, ny, k + 1))
                else:
                    if dist[nx][ny][k] == INF:
                        dist[nx][ny][k] = d + 1
                        q.append((nx, ny, k))

    return -1
```

优化后复杂度: O(N × M × min(K, N+M)) ≤ 100×100×200 = 2×10^6，非常安全。

**另一种思路**: 0-1 BFS（但这里所有边权都是1，直接用 BFS 就行）

### 易错点
- K 可能为 0，此时不能消除任何障碍物
- 起点或终点本身就是障碍物（题目一般保证起点为0）
- dist 数组维度为 [N][M][K+1]，K 较大时注意内存
- BFS 到达终点时直接返回，不一定需要处理完所有状态

---

# 模考复盘
| 项目 | 建议 |
|------|------|
| 100分题 | 30分钟内完成，用 set 去重 + 只检查起点 |
| 200分题 | 不要被"消除障碍物"吓到，本质是三维 BFS |
| 时间管理 | 200分题如果 45 分钟无进展，先检查简单边界条件 |
| 常见失误 | K 过大导致内存溢出，加 min(K, N+M) 优化 |

**分数预估**: 100分题全对 + 200分题部分正确 → 200~250分
