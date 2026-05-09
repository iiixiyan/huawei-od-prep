# Day 56 — 🏁 终极冲刺
## 11大算法模板 + 高频易错 + Python速查 + 考前Checklist

---

# 目录
1. [11核心算法模板速查](#1-11核心算法模板速查)
2. [OD高频易错点](#2-od高频易错点)
3. [Python速查](#3-python速查)
4. [考前Checklist](#4-考前checklist)
5. [复杂度速查表](#5-复杂度速查表)

---

# 1. 11核心算法模板速查

## 1.1 DFS (深度优先搜索)

### 树/图的DFS
```python
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

### 网格DFS (岛屿问题)
```python
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = 0  # 标记已访问
    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
        dfs(grid, i + di, j + dj)
```

### 排列/组合 DFS (回溯)
```python
def permute(nums):
    res, path, used = [], [], [False] * len(nums)
    def dfs():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False
    dfs()
    return res
```

---

## 1.2 BFS (广度优先搜索)

### 最短路径 (无权图)
```python
from collections import deque

def bfs(start, target):
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == target:
                return steps
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        steps += 1
    return -1
```

### 多源BFS (如感染/腐烂问题)
```python
def multi_source_bfs(grid):
    q = deque()
    fresh = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    # ... BFS 同标准模板
```

---

## 1.3 二分查找

### 标准二分
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 左边界/右边界
```python
def lower_bound(nums, target):  # 第一个 ≥ target 的位置
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(nums, target):  # 第一个 > target 的位置
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left
```

### 浮点数二分
```python
def float_binary_search():
    lo, hi = 0.0, 1e9
    for _ in range(100):  # 固定迭代次数
        mid = (lo + hi) / 2
        if check(mid):
            hi = mid
        else:
            lo = mid
    return lo
```

---

## 1.4 滑动窗口

### 定长窗口
```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### 可变窗口 (求满足条件的最长/最短)
```python
def min_window(s, t):
    """最小覆盖子串"""
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = 0
    min_len = float('inf')
    start = 0

    for right, ch in enumerate(s):
        if ch in need:
            need[ch] -= 1
            if need[ch] >= 0:
                missing -= 1

        while missing == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            left_ch = s[left]
            if left_ch in need:
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
            left += 1

    return s[start:start + min_len] if min_len != float('inf') else ""
```

### 滑动窗口通用框架
```python
left = 0
for right in range(len(arr)):
    # 右移窗口，加入 arr[right]
    while not_ok():  # 窗口不满足条件
        # 移除 arr[left]
        left += 1
    # 更新答案 (此时窗口满足条件)
```

---

## 1.5 动态规划 (4大模式)

### 模式1: 线性DP (最长递增子序列)
```python
def length_of_LIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

**优化 (二分)**: `tails[k]` 表示长度为 k+1 的 LIS 的最小结尾值。

```python
def length_of_LIS_optimized(nums):
    tails = []
    for num in nums:
        i = 0
        j = len(tails)
        while i < j:
            mid = (i + j) // 2
            if tails[mid] < num:
                i = mid + 1
            else:
                j = mid
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)
```

### 模式2: 区间DP (回文/合并)
```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
```

### 模式3: 背包DP
```python
# 0-1背包 (每个物品取一次)
def zero_one_knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(W, w - 1, -1):  # 从大到小
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]

# 完全背包 (每个物品取无限次)
def complete_knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(w, W + 1):  # 从小到大
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]

# 多重背包 (每个物品有限次)
def multiple_knapsack(weights, values, counts, W):
    dp = [0] * (W + 1)
    for w, v, c in zip(weights, values, counts):
        # 二进制优化
        k = 1
        while k <= c:
            for j in range(W, k * w - 1, -1):
                dp[j] = max(dp[j], dp[j - k * w] + k * v)
            c -= k
            k <<= 1
        if c > 0:
            for j in range(W, c * w - 1, -1):
                dp[j] = max(dp[j], dp[j - c * w] + c * v)
    return dp[W]
```

### 模式4: 状态压缩DP (TSP/子集)
```python
# 示例: 最短Hamilton路径 (TSP)
def tsp(dist, n):
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # 从0出发，状态为只访问了0
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask >> u) & 1:
                continue
            for v in range(n):
                if (mask >> v) & 1:
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
    return min(dp[(1 << n) - 1][i] + dist[i][0] for i in range(1, n))
```

---

## 1.6 并查集 (Union-Find)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # 按秩合并
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]
```

**应用**: 连通分量、最小生成树(Kruskal)、冗余连接

---

## 1.7 前缀树 (Trie)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # 经过该节点的单词数

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
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

    def delete(self, word):
        """删除单词（假设存在）"""
        def _delete(node, word, i):
            if i == len(word):
                node.is_end = False
                return
            ch = word[i]
            _delete(node.children[ch], word, i + 1)
            node.children[ch].count -= 1
            if node.children[ch].count == 0:
                del node.children[ch]

        _delete(self.root, word, 0)
```

**应用**: 单词搜索、自动补全、前缀匹配、最大XOR对

---

## 1.8 单调栈

### 下一个更大元素
```python
def next_greater_element(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # 存索引
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
    return res
```

### 接雨水
```python
def trap(height):
    stack = []
    water = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            h = min(height[left], height[i]) - height[bottom]
            water += width * h
        stack.append(i)
    return water
```

### 柱状图中最大矩形
```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights = [0] + heights + [0]  # 哨兵
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
```

**核心思想**: 栈内保持单调递增/递减，遇到破坏单调性的元素时出栈计算。

---

## 1.9 回溯 (Backtracking)

```python
def backtrack(candidates, target):
    res = []

    def dfs(path, remaining, start):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            # 剪枝: 同层相同值跳过 (避免重复组合)
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            dfs(path, remaining - candidates[i], i + 1)  # i+1: 不能重复使用
            path.pop()

    candidates.sort()
    dfs([], target, 0)
    return res
```

### 回溯通用模板
```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        if 选择不合法: continue
        做选择
        backtrack(新路径, 新选择列表)
        撤销选择
```

---

## 1.10 排序 + 双指针

### 两数之和 (排序后)
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

### 三数之和
```python
def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res
```

### 接雨水 (双指针法)
```python
def trap_two_pointer(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```

---

## 1.11 拓扑排序 (Kahn算法)

```python
from collections import deque

def topological_sort(n, edges):
    indegree = [0] * n
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return result if len(result) == n else []  # 有环返回空
```

---

# 2. OD高频易错点

## 2.1 输入解析陷阱

```
# ❌ 错误: 忘记 strip
n = int(input())

# ✅ 正确:
n = int(input().strip())

# ❌ 错误: 多空格情况
# 输入: "1   2   3"
# list(map(int, input().split()))  ✅ 自动处理多空格

# ⚠️ 行数不定时的读取
lines = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        # 有时用哨兵值判断结束
        a, b = map(int, line.split())
        if a == -1 and b == -1:
            break
        lines.append((a, b))
    except EOFError:
        break
```

## 2.2 边界条件

```
# 需要特别检查的边界:
1. N=1 的情况 (单元素数组、单节点树)
2. 空数组/空图
3. 最大值/最小值约束 (int溢出? Python不用担心)
4. 负数的处理
5. 完全无序/完全有序的输入
6. 所有元素相等
7. K=0 的情况 (如消除障碍物)
8. 目标在起点/终点
```

## 2.3 超时/内存溢出规避

```
# 常见超时原因及解决方案:
1. O(N²) 暴力 → 改为 O(N log N) 或 O(N)
2. DFS 递归过深 → 改为 BFS 或迭代
3. 重复计算 → 加缓存 (lru_cache / memo)
4. 频繁字符串拼接 → 用 list + ''.join()
5. 大量数据排序 → 用计数排序/内置 sorted()

# Python 性能建议:
- 用 sys.stdin.read() 一次读取所有输入
- 避免在循环内 import
- 局部变量引用加速 (local_var = global_var)
- 用 set/dict 代替 list 做查找
- 列表推导式优于 for+append
```

## 2.4 特殊输入格式

```
# 1. 矩阵读取
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 2. 树结构 (类似: 父节点列表, 子节点列表)
parent = list(map(int, input().split()))  # parent[i] 是节点i的父节点

# 3. 多个测试用例
T = int(input())
for _ in range(T):
    n = int(input())
    # 处理每个用例

# 4. 图 (节点编号从1开始)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 索引从1开始
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
```

## 2.5 常见逻辑错误

```
# 1. 0-index vs 1-index 混用
# 解决: 统一使用 0-index，输入时减1

# 2. BFS 忘记标记已访问
# 解决: 入队时就标记，不要出队时标记

# 3. DP 数组维度和初始化错误
# 解决: 画DP表格明确维度含义

# 4. 并查集忘记路径压缩
# 解决: find 函数必须带路径压缩

# 5. 回溯忘记剪枝导致超时
# 解决: 排序 + 同层去重 + 可行性剪枝
```

---

# 3. Python速查

## 3.1 常用内置函数

```python
# 数学
abs(x)           # 绝对值
max/min(iter)    # 最大/最小值
sum(iter)        # 求和
pow(x, y, mod)   # 快速幂取模
divmod(a, b)     # (a//b, a%b)
round(x, n)      # 四舍五入到n位小数

# 类型转换
int(x, base=10)  # 字符串转整数，支持进制
ord(ch)          # 字符转ASCII码
chr(code)        # ASCII码转字符
bin(x)           # 转二进制字符串 '0b101'
hex(x)           # 转十六进制
list(map(int, s.split()))  # 字符串列表转整数列表

# 迭代工具
all(iter)        # 所有元素为True
any(iter)        # 任意元素为True
enumerate(iter)  # (index, value) 迭代
zip(*iterables)  # 并行迭代多个可迭代对象
sorted(iter, key=..., reverse=True)  # 排序
reversed(seq)    # 反转序列
filter(func, iter)  # 过滤
map(func, iter)     # 映射
```

## 3.2 collections 模块

```python
from collections import Counter, defaultdict, deque, OrderedDict

# Counter — 计数
cnt = Counter("aabbbcc")
cnt.most_common(2)   # [('b', 3), ('a', 2)]
cnt['a'] += 1        # 增加计数
list(cnt.elements()) # 展开为列表

# defaultdict — 自动默认值
d = defaultdict(list)   # d[x].append(y) 无需初始化
d = defaultdict(int)    # d[x] += 1 无需初始化
d = defaultdict(set)    # d[x].add(y) 无需初始化

# deque — 双端队列 O(1) 两端操作
q = deque()
q.append(x)       # 右端添加
q.appendleft(x)   # 左端添加
q.pop()           # 右端弹出
q.popleft()       # 左端弹出
q.rotate(k)       # 循环右移k步

# OrderedDict — 有序字典 (Python 3.7+ dict已有序)
od = OrderedDict()
od.move_to_end(key)  # 将key移到末尾
```

## 3.3 itertools 模块

```python
from itertools import permutations, combinations, product, accumulate, chain, groupby

# 排列: 所有可能的排列
list(permutations([1,2,3], 2))  # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 组合: 所有可能的组合
list(combinations([1,2,3], 2))  # [(1,2),(1,3),(2,3)]

# 笛卡尔积
list(product([1,2], ['a','b']))  # [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

# 前缀和
list(accumulate([1,2,3,4]))  # [1, 3, 6, 10]

# 展平嵌套列表
list(chain.from_iterable([[1,2],[3,4]]))  # [1,2,3,4]

# 分组
for key, group in groupby(sorted(data)):
    print(key, list(group))
```

## 3.4 堆 (heapq)

```python
import heapq

# 默认最小堆
heap = []
heapq.heappush(heap, 5)      # 入堆
smallest = heapq.heappop(heap)  # 出堆

# 最大堆: 存负数
heapq.heappush(heap, -x)
max_val = -heapq.heappop(heap)

# 取前K大/小
heapq.nlargest(k, iterable)  # 前K大
heapq.nsmallest(k, iterable) # 前K小

# 堆化
heapq.heapify(list_)  # O(N) 建堆
```

## 3.5 位运算速查

```python
# 常用位操作
x & (x - 1)          # 清除最低位的1
x & -x               # 取最低位的1
(x >> i) & 1         # 取第i位
x | (1 << i)         # 设置第i位为1
x & ~(1 << i)        # 设置第i位为0
x ^ (1 << i)         # 翻转第i位
x.bit_count()        # Python 3.8+: 二进制中1的个数
x.bit_length()       # 二进制位数

# 枚举子集
mask = 0b1011
sub = mask
while sub:
    # 处理子集 sub
    sub = (sub - 1) & mask

# 判断是否为2的幂
x > 0 and (x & (x - 1)) == 0
```

## 3.6 性能加速技巧

```python
# 1. 一次性读取所有输入
import sys
data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))

# 2. 大数组用数组模块
from array import array
arr = array('i', [0]) * 1000000  # 比 list 省内存

# 3. 递归限制
import sys
sys.setrecursionlimit(1000000)

# 4. lru_cache 自动记忆化
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# 5. 三元表达式
res = a if condition else b

# 6. 快速交换
a, b = b, a

# 7. 去重保持顺序
list(dict.fromkeys(items))
```

---

# 4. 考前Checklist

## 4.1 考前24小时

```
✅ 复习11个算法模板 (15分钟过一遍)
✅ 刷2-3道手感题 (热手)
✅ 准备环境:
   - Python 版本确认 (3.8+)
   - IDE/编辑器打开并测试
   - 输入输出测试 (print/input)
✅ 休息:
   - 保证7小时睡眠
   - 设好闹钟
   - 提前30分钟到考场
```

## 4.2 考试中时间管理

```
┌──────────────────────────────────────────────┐
│           90分钟考试时间分配                    │
├──────────────────────────────────────────────┤
│ 0-5min   通读所有题目，标记难度                │
│ 5-35min  做第1题 (100分)                     │
│ 35-40min 休息+饮水+检查第1题                  │
│ 40-80min 做第2题 (200分)                     │
│ 80-90min 检查所有题目+边界条件                │
└──────────────────────────────────────────────┘

遇到卡壳超过15分钟 → 先跳过做下一题
至少留5分钟最后检查
```

## 4.3 做题步骤模板

```
1️⃣ 读题 (2min)
   - 输入输出格式
   - 数据范围 (N, M, K)
   - 时间限制/空间限制

2️⃣ 选算法 (3min)
   - 暴力能否过? (N ≤ 1000 可接受 O(N²))
   - 需要优化? (N ≥ 10^5 需要 O(N) 或 O(N log N))
   - 匹配算法模板

3️⃣ 写代码 (15-20min)
   - 先写输入输出框架
   - 再写核心逻辑
   - 最后加边界处理

4️⃣ 测试 (5min)
   - 跑样例
   - 测边界 (N=1, K=0, 空, 全等)
   - 测极端情况 (最大N, 最大K)
```

## 4.4 常见考试策略

```
✅ DO:
- 先做100分题，保底
- 用 print 调试
- 局部变量优化速度
- 复杂度过不去时尝试空间换时间

❌ DON'T:
- 不要在一个题上死磕超过30分钟
- 不要忘记 import 模块
- 不要忘记处理多测试用例
- 不要提交前忘记去掉调试代码
- 不要用 input() 在循环中读大数据 (用 sys.stdin.read)
```

## 4.5 考前最后10分钟

```
📋 快速检查:
□ 所有 import 都已写
□ 函数定义在调用之前
□ 递归深度没超限
□ 大数组没有 O(N²) 空间
□ 索引没有越界
□ 0-index vs 1-index 一致
□ 负数/空值/边界已处理
□ 变量名没有拼写错误
□ 所有分支都有 return
□ 样例通过
```

---

# 5. 复杂度速查表

## 5.1 时间复杂度

| 算法 | 平均 | 最坏 | 空间 |
|------|------|------|------|
| 二分查找 | O(log N) | O(log N) | O(1) |
| 快速排序 | O(N log N) | O(N²) | O(log N) |
| 归并排序 | O(N log N) | O(N log N) | O(N) |
| 堆排序 | O(N log N) | O(N log N) | O(1) |
| 计数排序 | O(N + K) | O(N + K) | O(K) |
| DFS/BFS | O(V + E) | O(V + E) | O(V) |
| Dijkstra | O((V+E) log V) | O((V+E) log V) | O(V) |
| Floyd | O(V³) | O(V³) | O(V²) |
| Kruskal | O(E log E) | O(E log E) | O(V) |
| Prim | O(E log V) | O(E log V) | O(V) |
| KMP | O(N + M) | O(N + M) | O(M) |
| 并查集 | O(α(N)) | O(α(N)) | O(N) |

## 5.2 数据规模与可行算法速判

```
N ≤ 20      → O(2^N), O(N!)      → 状态压缩/回溯
N ≤ 100     → O(N³)              → Floyd/区间DP
N ≤ 1000    → O(N²)              → 暴力/两层循环DP
N ≤ 10^5    → O(N log N)         → 排序/二分/堆
N ≤ 10^6    → O(N)               → 线性扫描/哈希
N ≤ 10^8    → O(log N)           → 数学公式/二分
```

## 5.3 Python操作复杂度

| 操作 | 复杂度 |
|------|--------|
| list[i] 访问/赋值 | O(1) |
| list.append/pop | O(1) 均摊 |
| list.pop(i) / insert | O(N) |
| list.index / in | O(N) |
| set/dict in 操作 | O(1) 均摊 |
| set/dict add/remove | O(1) 均摊 |
| str + 拼接 | O(N) |
| str.join(list) | O(N) |
| sorted(list) | O(N log N) |
| heapq.heappush/pop | O(log N) |
| deque.popleft/append | O(1) |
| collections.Counter | O(N) |

## 5.4 常见N值对应极限运算量

| N | O(N) | O(N log N) | O(N²) | O(N³) | O(2^N) |
|---|------|------------|-------|-------|--------|
| 10 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 100 | ✓ | ✓ | ✓ | ✓ | ✗ |
| 1,000 | ✓ | ✓ | ✓ | ✗ | ✗ |
| 10,000 | ✓ | ✓ | ✗ | ✗ | ✗ |
| 100,000 | ✓ | ✓ | ✗ | ✗ | ✗ |
| 1,000,000 | ✓ | ✗ | ✗ | ✗ | ✗ |

---

# 📌 最后的话

> **OD考试核心三要素:**
> 1. **读题准** — 理解输入输出，确认数据范围
> 2. **选对法** — 匹配算法模板，不追求最优解，追求可过解
> 3. **写得稳** — 边界处理，0-index统一，输入输出格式正确
>
> **心态:**
> - 100分题保底，200分题冲刺
> - 卡壳15分钟就跳过
> - 留5分钟检查边界
>
> **祝考试顺利！🎉**

---

*本文件是 Week 8 终极冲刺复习资料，涵盖了OD考试所需的全部核心知识点。*
