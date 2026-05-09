# Day 55-60 — 冲刺复习：核心模板 + 高频易错 + 考前冲刺

> 🚀 **考前最后6天冲刺** | 这是你上考场前最后一份复习资料
> 
> 浓缩所有核心算法模板、常见陷阱、考试策略

---

## 📖 使用指南

| 天数 | 内容 | 建议用时 |
|------|------|---------|
| Day 55 | 核心算法模板速查（上）: DFS/BFS/二分/滑动窗口 | 2h |
| Day 56 | 核心算法模板速查（下）: DP/Union-Find/Trie/单调栈 | 2h |
| Day 57 | 高频易错点 + 输入输出陷阱 | 2h |
| Day 58 | 考前冲刺清单 + 默写模板 | 2h |
| Day 59 | 模拟考试节奏 + 心态调整 | 1h |
| Day 60 | 放松 + 轻复习（只看错题本） | 1h |

---

# 第一部分：核心算法模板速查

---

## 1. DFS（深度优先搜索）

```python
# ---------- 递归模板 ----------
def dfs_recursive(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if visited[r][c] or grid[r][c] == 障碍物:
        return
    
    visited[r][c] = True
    # 处理当前节点
    
    # 四个方向递归
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        dfs_recursive(grid, r+dr, c+dc, visited)

# ---------- 迭代模板（栈） ----------
def dfs_iterative(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    stack = [start]
    visited[start[0]][start[1]] = True
    
    while stack:
        r, c = stack.pop()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))
```

**适用场景**：岛屿数量、连通分量、路径存在性、排列组合（回溯）

**注意**：
- 递归版可能栈溢出，大数据用迭代版
- 回溯需要恢复状态（撤销选择）

---

## 2. BFS（广度优先搜索）

```python
from collections import deque

def bfs(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    q = deque([(start[0], start[1], 0)])  # (r, c, dist)
    visited[start[0]][start[1]] = True
    
    while q:
        r, c, dist = q.popleft()
        
        if (r, c) == target:
            return dist
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != 障碍物:
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
    
    return -1
```

**适用场景**：最短路径、层序遍历、拓扑排序、状态空间搜索

**关键要点**：
- ✅ 入队时标记 visited（不是出队时）
- ✅ 分层BFS用 `for _ in range(len(q))` 处理每层
- ✅ 无权图最短路径用 BFS（权重为1）

---

## 3. 状态压缩 BFS（钥匙与锁问题）

```python
from collections import deque

def bfs_with_key(grid, N, M):
    # 状态: (x, y, key_mask)
    # key_mask 用二进制位表示已拥有的钥匙
    
    # 找起点
    sx = sy = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                sx, sy = i, j
    
    # 用 dict 存距离（节省内存）
    dist = {}
    dist[(sx, sy, 0)] = 0
    q = deque([(sx, sy, 0)])
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    while q:
        x, y, mask = q.popleft()
        d = dist[(x, y, mask)]
        
        if grid[x][y] == 'E':
            return d
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            cell = grid[nx][ny]
            if cell == '1':  # 障碍
                continue
            
            new_mask = mask
            
            if 'A' <= cell <= 'J':  # 钥匙
                bit = ord(cell) - ord('A')
                new_mask = mask | (1 << bit)
            
            if 'a' <= cell <= 'j':  # 锁
                bit = ord(cell) - ord('a')
                if not (mask & (1 << bit)):
                    continue  # 无钥匙
            
            if (nx, ny, new_mask) not in dist:
                dist[(nx, ny, new_mask)] = d + 1
                q.append((nx, ny, new_mask))
    
    return -1
```

**位运算速查**：

| 操作 | 写法 | 含义 |
|------|------|------|
| 检查第k位 | `mask & (1 << k)` | 是否拥有第k种钥匙 |
| 设置第k位 | `mask \| (1 << k)` | 拾取第k种钥匙 |
| 清除第k位 | `mask & ~(1 << k)` | 消耗第k种钥匙 |
| 所有钥匙 | `(1 << K) - 1` | K种钥匙全有 |

---

## 4. 二分查找

```python
# ---------- 标准二分 ----------
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ---------- 第一个 >= target ----------
def lower_bound(nums, target):
    left, right = 0, len(nums)  # 注意 right = len(nums)，搜索区间 [left, right)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left  # 返回第一个 >= target 的索引

# ---------- 第一个 > target ----------
def upper_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left  # 返回第一个 > target 的索引

# ---------- 在有序数组中找目标范围 ----------
def search_range(nums, target):
    first = lower_bound(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = upper_bound(nums, target) - 1
    return [first, last]

# ---------- 二分答案（值域二分） ----------
def feasible(x):
    # 判断 x 是否可行
    pass

def binary_search_answer():
    left, right = 最小值, 最大值
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid    # 找最小值可行解
        else:
            left = mid + 1
    return left
```

**适用场景**：有序数组搜索、求平方根、旋转数组搜索、二分答案（最小化最大值/最大化最小值）

---

## 5. 滑动窗口

```python
# ---------- 固定窗口大小 ----------
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# ---------- 可变窗口（求最长/最短满足条件的子数组） ----------
def variable_window(s, condition_func):
    left = 0
    result = 0  # 或 float('inf') 求最短
    window = {}  # 或 Counter
    
    for right, ch in enumerate(s):
        # 扩展窗口
        window[ch] = window.get(ch, 0) + 1
        
        # 收缩窗口（当不满足条件时）
        while not condition_func(window):
            left_ch = s[left]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            left += 1
        
        # 更新结果
        result = max(result, right - left + 1)  # 求最长
        # result = min(result, right - left + 1)  # 求最短
    
    return result

# ---------- 最小覆盖子串模板 ----------
def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    need_len = len(need)
    window = {}
    have_len = 0
    
    left = 0
    min_len = float('inf')
    result = ""
    
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have_len += 1
        
        while have_len == need_len:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]
            
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have_len -= 1
            left += 1
    
    return result
```

---

## 6. 动态规划（DP）常见模式

### 6.1 一维DP

```python
# 爬楼梯 / 斐波那契
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 滚动数组优化
def fib_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 最大子数组和 (Kadane算法)
def max_subarray(nums):
    cur_max = global_max = nums[0]
    for num in nums[1:]:
        cur_max = max(num, cur_max + num)
        global_max = max(global_max, cur_max)
    return global_max
```

### 6.2 背包DP

```python
# 01背包
def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # 逆序
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# 完全背包
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # 正序
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# 多重背包（二进制优化）
def knapsack_multi(weights, values, counts, capacity):
    # 将多重背包拆成01背包
    new_weights, new_values = [], []
    for i in range(len(weights)):
        k = 1
        while k <= counts[i]:
            new_weights.append(weights[i] * k)
            new_values.append(values[i] * k)
            counts[i] -= k
            k <<= 1
        if counts[i] > 0:
            new_weights.append(weights[i] * counts[i])
            new_values.append(values[i] * counts[i])
    return knapsack_01(new_weights, new_values, capacity)
```

### 6.3 区间DP

```python
# 合并石子/戳气球
def interval_dp(nums):
    n = len(nums)
    # 常用 dp[i][j] 表示区间 [i, j] 上的最优值
    dp = [[0] * n for _ in range(n)]
    
    # 枚举区间长度
    for length in range(2, n + 1):  # 区间长度
        for i in range(n - length + 1):
            j = i + length - 1
            # 枚举分割点
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j] + cost(i, j, k))
    
    return dp[0][n-1]
```

### 6.4 LIS（最长递增子序列）

```python
# O(n²) DP
def lis_n2(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# O(n log n) 贪心+二分
def lis_nlogn(nums):
    import bisect
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)  # 严格递增用 bisect_left
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)
```

### 6.5 LCS（最长公共子序列）

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

---

## 7. 并查集 (Union-Find)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # 连通分量数
    
    def find(self, x):
        # 路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        # 按秩合并
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# 使用场景
uf = UnionFind(n)
# 遍历边，合并连通分量
for u, v in edges:
    uf.union(u, v)
# 连通分量数 = uf.count
# 是否连通 = uf.connected(a, b)
```

---

## 8. 字典树 (Trie)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

**适用场景**：单词搜索、前缀匹配、字符串自动补全、IP路由

---

## 9. 单调栈 (Monotonic Stack)

```python
# ---------- 下一个更大元素 ----------
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # 单调递减栈（栈底到栈顶递减）
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result

# ---------- 下一个更小元素 ----------
def next_smaller_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # 单调递增栈
    
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result

# ---------- 柱状图中最大矩形 ----------
def largest_rectangle(heights):
    heights = [0] + heights + [0]  # 添加哨兵
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

---

## 10. 排序 + 双指针

```python
# ---------- 三数之和 ----------
def three_sum(nums, target=0):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # 跳过重复
        
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    
    return result

# ---------- 合并区间 ----------
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [list(intervals[0])]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

---

## 11. 回溯算法

```python
# ---------- 全排列 ----------
def permute(nums):
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    
    backtrack([])
    return result

# ---------- 组合 ----------
def combine(n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result

# ---------- 子集 ----------
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

---

# 第二部分：高频易错点

---

## 📌 输入输出陷阱

| 陷阱 | 错误写法 | 正确写法 |
|------|---------|---------|
| 忽略换行符 | `input().split()` 没问题，但如果是 `sys.stdin.read()` 需注意 | `sys.stdin.read().split()` |
| 多行读取中断 | 用 `input()` 多次调用 | 用 `sys.stdin.read().splitlines()` 一次读入 |
| 整数转列表 | `list(map(int, s))` 会拆成单个数字 | `list(map(int, s.split()))` |
| 提交前保留调试输出 | `print("debug:", x)` | 删掉或注释掉 |
| 输出末尾多余空格 | `print(" ".join(map(str, res)) + " ")` | `print(" ".join(map(str, res)))` |
| 输出示例大小写 | 题目要求大写 `YES/NO`，输出 `Yes/No` | 严格按题目要求 |
| 读取空行 | `input()` 读空行返回 `""` | 用 `strip()` 判断是否为空 |

## 📌 常见算法错误

| 错误 | 场景 | 正确做法 |
|------|------|---------|
| BFS出队标记visited | 同一节点被多次入队 | 入队时立即标记 |
| 忘记排序 | 二分查找在无序数组上 | 先排序再二分 |
| 递归无终止条件 | 无限递归 | 检查 `if not node: return` |
| 变量作用域混淆 | 嵌套函数中修改外层变量 | 用 `nonlocal` 或 `global` |
| 整数除法 | Python `//` 向负无穷取整 | 向零取整用 `int(a / b)` |
| 字符串拼接 | 循环内 `s += ch` O(n²) | 用 `list` + `''.join()` |
| 字典遍历修改 | 遍历时增删dict元素 | 用 `list(dict.items())` 快照 |
| 浮点数比较 | `0.1 + 0.2 == 0.3` 为 False | `abs(a - b) < 1e-9` |

## 📌 Python 特有陷阱

```python
# 1. 可变默认参数
def f(lst=[]):  # ❌ 默认参数是可变对象，多次调用会累积
    lst.append(1)
    return lst

def f(lst=None):  # ✅
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# 2. 整数除法向负无穷取整
print(-3 // 2)  # -2 (不是 -1)
print(int(-3 / 2))  # -1 ✅ 向零取整

# 3. 浅拷贝 vs 深拷贝
dp = [[0] * n] * m  # ❌ 所有行是同一个list
dp = [[0] * n for _ in range(m)]  # ✅

# 4. 列表推导式中变量泄漏（Python 2，Python 3已修复）

# 5. input() 比 sys.stdin.readline() 慢
# 大数据用 sys.stdin.readline()
```

---

# 第三部分：考前冲刺 Checklist

---

## ✅ 考前3天

- [ ] 默写所有核心算法模板（不看参考）
- [ ] 完成至少一套完整模考（卡时间）
- [ ] 整理错题本，标记易错点
- [ ] 熟悉 Python 标准库（bisect, collections, heapq, itertools, math）

## ✅ 考前1天

- [ ] 只看错题本和模板速查
- [ ] 不要做新题！不要做新题！不要做新题！
- [ ] 准备考试环境：IDE、输入法、网络
- [ ] 早睡，保证8小时睡眠

## ✅ 考前1小时

- [ ] 检查考试设备
- [ ] 准备草稿纸和笔
- [ ] 喝水、上厕所
- [ ] 深呼吸，调整心态

## ✅ 考试中

- [ ] 前5分钟浏览所有题目
- [ ] 先做最简单的题，拿稳分数
- [ ] 每题都写代码，哪怕暴力解
- [ ] 留时间检查输入输出格式
- [ ] 提交前删除调试代码

---

# 第四部分：心态调整 & 应试技巧

---

## 🧠 遇到不会的题怎么办？

```
1. 深呼吸（3秒）
2. 重读题目，圈出关键词
3. 想暴力解法（至少能过部分测试用例）
4. 列出所有已知条件
5. 从小规模开始推导模式
6. 写注释说明思路（即使代码没写完）
```

## ⏱ 时间管理口诀

```
前五分钟，浏览全题；
先易后难，稳扎稳打；
暴力保底，优化加分；
最后检查，格式优先。
```

## 💪 考试心态

| 想法 | 替代思维 |
|------|---------|
| "这题太难了，我完了" | "我先写暴力解，拿部分分" |
| "别人都做完了，我还在想" | "我的节奏就是最好的节奏" |
| "我肯定过不了" | "每做一题就离目标更近一步" |
| "这题我见过，但想不起来了" | "从暴力解开始推导" |
| "我代码有bug怎么办" | "先写核心逻辑，再测试调试" |

---

# 第五部分：附录

---

## 📊 时间复杂度速查表

| 数据结构 | 操作 | 时间复杂度 |
|---------|------|-----------|
| 数组（list） | 索引/赋值 | O(1) |
| | 查找（未排序） | O(n) |
| | 插入/删除（末尾） | O(1) |
| | 插入/删除（开头） | O(n) |
| 链表 | 查找 | O(n) |
| | 插入/删除（已知位置） | O(1) |
| 栈（list/deque） | push/pop | O(1) |
| 队列（deque） | push/pop左右 | O(1) |
| 哈希表（dict） | 查找/插入/删除 | O(1) 平均 |
| 集合（set） | 查找/插入/删除 | O(1) 平均 |
| 二叉搜索树（平衡） | 查找/插入/删除 | O(log n) |
| 堆（heapq） | 推入/弹出 | O(log n) |
| | 建堆 | O(n) |
| 排序（Timsort） | 最佳/平均/最差 | O(n)/O(n log n)/O(n log n) |

## 📊 常见算法复杂度

| 算法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 线性扫描 | O(n) | O(1) |
| 二分查找 | O(log n) | O(1) |
| 双指针 | O(n) | O(1) |
| 滑动窗口 | O(n) | O(k) |
| 排序 | O(n log n) | O(1)~O(n) |
| DFS/BFS （网格） | O(n × m) | O(n × m) |
| DP 一维 | O(n) ~ O(n²) | O(n) ~ O(n²) |
| 背包DP | O(n × capacity) | O(capacity) |
| Dijkstra | O((V+E) log V) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| 并查集 | O(α(n)) 近乎O(1) | O(n) |
| KMP | O(n + m) | O(m) |

---

## 💻 Python 常用内置函数速查

### 常用模块

```python
import math
math.gcd(a, b)          # 最大公约数
math.lcm(a, b)          # 最小公倍数 (Python 3.9+)
math.sqrt(x)            # 平方根
math.ceil(x) / floor(x) # 向上/向下取整
math.comb(n, k)         # 组合数 C(n,k)
math.perm(n, k)         # 排列数 P(n,k)

import bisect
bisect.bisect_left(arr, x)   # 第一个 >= x 的位置
bisect.bisect_right(arr, x)  # 第一个 > x 的位置
bisect.insort(arr, x)        # 插入并保持有序

from collections import Counter, defaultdict, deque, OrderedDict

import heapq
heapq.heappush(heap, item)   # 推入
heapq.heappop(heap)          # 弹出最小值
heapq.heapify(lst)           # 建堆 O(n)
heapq.nlargest(k, lst)       # 前k大
heapq.nsmallest(k, lst)      # 前k小

import itertools
itertools.permutations(lst, k)   # 排列
itertools.combinations(lst, k)   # 组合
itertools.product(lst1, lst2)    # 笛卡尔积
itertools.chain(lst1, lst2)      # 合并迭代器
itertools.groupby(lst, key_func) # 分组

from functools import lru_cache, cmp_to_key

import sys
sys.setrecursionlimit(1000000)
sys.stdin.readline()
sys.stdout.write(str(x) + '\n')
```

### 字符串操作

```python
s.isdigit() / s.isalpha() / s.isalnum()  # 判断类型
s.strip() / s.lstrip() / s.rstrip()      # 去空格
s.split(sep) / sep.join(list)            # 分割/合并
s.startswith(prefix) / s.endswith(suffix) # 前后缀
s.replace(old, new)                      # 替换
s.upper() / s.lower()                    # 大小写
ord(ch) / chr(code)                      # 字符↔ASCII
```

### 列表操作

```python
sorted(lst, key=lambda x: ..., reverse=True)
reversed(lst)             # 反转迭代器
enumerate(lst)            # (index, value) 迭代
zip(lst1, lst2)           # 并行迭代
map(func, lst)            # 映射
filter(func, lst)         # 过滤
any(iterable) / all(iterable)  # 存在/全部
sum(lst) / max(lst) / min(lst) # 聚合
lst.sort(key=..., reverse=...)  # 原地排序
```

---

## 🎯 最后寄语

> **"台上一分钟，台下十年功。"**
>
> 这60天的准备，是你最大的底气。
>
> **考试中记住三件事：**
> 1. **稳** — 不要慌，每一分钟都有效利用
> 2. **拿分** — 暴力解也是分，写了就有希望
> 3. **检查** — 输出格式对了吗？边界考虑了吗？
>
> **祝你考试顺利，成功上岸！🚀**

---

*—— 华为OD备考完整资料 · 2026 · Nous Research*
