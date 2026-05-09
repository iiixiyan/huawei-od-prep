# Day 53 — 错题回顾 Phase 1 (LeetCode 75 核心复盘)

> 📚 **回顾 Weeks 1-4** | 算法基础 + LeetCode 75 经典题型
> 
> 快速过一遍核心知识点、常见错误、模板速查

---

## 一、八周课程各阶段速览

| 周次 | 主题 | 核心算法 |
|------|------|---------|
| Week 1 | 数组 & 哈希表 | 双指针、滑动窗口、前缀和 |
| Week 2 | 链表 & 栈 & 队列 | 链表反转、单调栈、队列 |
| Week 3 | 树 & 图 | DFS、BFS、二叉树遍历、二叉搜索树 |
| Week 4 | 动态规划 & 贪心 & 二分查找 | DP 模板、01背包、二分变体 |

---

## 二、按主题整理的常见错误

### 🔹 数组 & 双指针

| 常见错误 | 示例 | 正确做法 |
|---------|------|---------|
| 数组越界 | `for i in range(n): if nums[i] == nums[i+1]` | 检查 `i+1 < n` |
| 忘记排序 | 两数之和用双指针但不排序 | 哈希表 O(n) 或先排序 |
| 双指针更新错误 | 三数之和中 left/right 更新后不跳过重复 | 更新后 `while left < right and nums[left]==nums[left-1]: left+=1` |
| 边界取值 | 二分查找 mid 计算溢出 | `mid = left + (right - left) // 2` |

### 🔹 链表

| 常见错误 | 说明 |
|---------|------|
| 忘记处理空链表 | 始终检查 head is None |
| 反转链表断链 | 用 `prev, curr, next` 三指针 |
| 快慢指针死循环 | 快指针每次走2步，检查 `fast and fast.next` |
| 环形链表检测 | slow/fast 相遇后，head 和 slow 同步走找入口 |

### 🔹 栈 & 单调栈

| 常见错误 | 说明 |
|---------|------|
| 单调栈相等元素处理 | 是严格单调还是非严格？题目要求决定 |
| 括号匹配栈空pop | 先检查栈是否为空再 pop |
| 单调递增/递减混淆 | 求下一个更大元素→单调递减栈 |

### 🔹 树 & 图

| 常见错误 | 说明 |
|---------|------|
| 递归未设终止条件 | 忘记 `if not root: return` |
| BFS 不设 visited | 图中可能成环，必须标记 |
| 中序/前序/后序混淆 | 记位置：根在左前/中/右后 |
| 递归深度溢出 | Python 默认 1000，设 `sys.setrecursionlimit(10000)` |

### 🔹 动态规划

| 常见错误 | 说明 |
|---------|------|
| DP 数组初始化错误 | 大小应为 n+1 还是 n？ |
| 状态转移界条件 | `i-1` 或 `i-2` 需检查是否 >= 0 |
| 忘记处理 base case | `dp[0]`, `dp[1]` 初始值 |
| 贪心错误当DP做 | 局部最优不等于全局最优时不能用贪心 |

### 🔹 二分查找

| 常见错误 | 说明 |
|---------|------|
| 死循环 | `while left < right` 配合 `mid` 取整方向 |
| mid 计算溢出 | `(left+right)//2` 在 C++/Java 可能溢出 |
| 边界条件错误 | 返回 left 还是 right？检查循环退出后的值 |
| 找左边界/右边界混淆 | `if nums[mid] >= target: right = mid` 或反之 |

---

## 三、10 道快速自测题（简答）

**Q1**: 滑动窗口求最长无重复子串时，窗口收缩的条件是什么？  
<details><summary>答案</summary>当窗口中出现了重复字符时收缩左边界，直到重复字符被移出窗口。</details>

**Q2**: 二分查找中，`while left < right` 和 `while left <= right` 有什么区别？  
<details><summary>答案</summary>`left < right` 退出时 `left == right`，需要再检查一次；`left <= right` 退出时 `left > right`，区间已空。通常 `left <= right` 配合 `mid ± 1` 更安全。</details>

**Q3**: 在二维网格中做 BFS 时，如何避免重复访问？  
<details><summary>答案</summary>用 `visited` 数组或矩阵，初始化为 `False`，入队时标记为 `True`（不要出队时标记，否则会大量重复入队）。</details>

**Q4**: DP 中的「滚动数组」优化适合什么场景？  
<details><summary>答案</summary>当状态转移只依赖前一行或前两行时，可以用滚动数组将 O(n) 空间降到 O(1)。例如斐波那契、背包问题的空间优化。</details>

**Q5**: 反转链表的迭代法中，三个指针分别是什么？各自的作用是什么？  
<details><summary>答案</summary>`prev=None`（已反转部分的头），`curr=head`（当前处理节点），`next_temp=curr.next`（保存原链表下一节点）。核心：先存 next，再改指向，然后整体前移。</details>

**Q6**: 二叉树的层序遍历用什么数据结构？输出结果通常是怎样的形式？  
<details><summary>答案</summary>用队列（collections.deque），每次处理一层的所有节点。输出通常是嵌套列表 `[[level1], [level2], ...]`。</details>

**Q7**: 什么时候用「贪心」而不是「DP」？  
<details><summary>答案</summary>当局部最优选择能导致全局最优解时（问题有最优子结构 + 贪心选择性质）。比如找零问题中硬币面额成倍数关系时可用贪心，否则用 DP。</details>

**Q8**: 单调递增栈和单调递减栈分别用来解决什么类型的问题？  
<details><summary>答案</summary>单调递增栈（栈底到栈顶递增）：找下一个更小元素。单调递减栈：找下一个更大元素。</details>

**Q9**: 前缀和数组的构建方式？一维和二维的区别？  
<details><summary>答案</summary>一维：`pref[i] = pref[i-1] + nums[i-1]`，区间 [l, r] 和为 `pref[r+1] - pref[l]`。二维：`pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + matrix[i-1][j-1]`，矩形和为三个减两个加。</details>

**Q10**: 合并两个有序链表时，用递归和迭代各有什么优缺点？  
<details><summary>答案</summary>递归：代码简洁，但空间 O(n)（递归栈）；迭代：代码略长，但空间 O(1)。面试时优先用迭代。</details>

---

## 四、核心算法模板速查

### 1. 滑动窗口 (Sliding Window)

```python
def sliding_window(s):
    left = 0
    window = {}
    result = 0
    
    for right, ch in enumerate(s):
        # 扩展窗口
        window[ch] = window.get(ch, 0) + 1
        
        # 收缩窗口条件
        while 需要收缩的条件:
            left_ch = s[left]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            left += 1
        
        # 更新结果
        result = max(result, right - left + 1)
    
    return result
```

### 2. 双指针 (Two Pointers)

```python
# 相向双指针（如三数之和）
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

# 同向双指针（如删除排序数组重复项）
def remove_duplicates(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### 3. 动态规划模板 (DP)

```python
# 一维DP模板
def dp_1d(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # 或 n
    dp[0] = 0           # base case
    
    for i in range(1, n + 1):
        # 状态转移，取决于具体问题
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    
    return dp[n]

# 01背包模板
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# 完全背包模板
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(weights[i], capacity + 1):  # 正序遍历
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```

### 4. BFS 模板

```python
from collections import deque

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    q = deque([start])
    visited[start[0]][start[1]] = True
    steps = 0
    
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            
            if 到达目标:
                return steps
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and 可通行:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        steps += 1
    
    return -1
```

### 5. DFS 模板

```python
def dfs(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    def search(r, c):
        if 越界 or 已访问 or 不可通行:
            return
        visited[r][c] = True
        # 处理当前节点
        for dr, dc in dirs:
            search(r + dr, c + dc)
    
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c] and 需要搜索:
                search(r, c)
```

### 6. 二分查找模板

```python
# 标准二分查找
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

# 找左边界（第一个 >= target）
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

# 找右边界（第一个 > target）
def upper_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left
```

### 7. 回溯模板

```python
def backtracking(nums):
    result = []
    
    def backtrack(path, remaining, start):
        # 满足条件时记录
        if 满足条件:
            result.append(path[:])
            return
        
        for i in range(start, len(remaining)):
            # 剪枝
            if 需要剪枝:
                continue
            
            # 做选择
            path.append(remaining[i])
            
            # 递归
            backtrack(path, remaining, i + 1)  # 组合
            # backtrack(path, remaining, i)     # 可重复选
            # backtrack(path, remaining, 0)     # 排列(需used数组)
            
            # 撤销选择
            path.pop()
    
    backtrack([], nums, 0)
    return result
```

---

## 五、LeetCode 75 核心题索引（Week 1-4）

| 编号 | 题目 | 核心考点 | 推荐用时 |
|------|------|---------|---------|
| 1 | 两数之和 | 哈希表 | 5min |
| 2 | 三数之和 | 排序+双指针 | 15min |
| 3 | 无重复字符的最长子串 | 滑动窗口 | 15min |
| 4 | 最长回文子串 | 中心扩展/DP | 20min |
| 5 | 盛最多水的容器 | 双指针 | 10min |
| 6 | 有效的括号 | 栈 | 5min |
| 7 | 合并两个有序链表 | 递归/迭代 | 10min |
| 8 | 反转链表 | 三指针迭代 | 10min |
| 9 | 二叉树中序遍历 | 递归/栈 | 10min |
| 10 | 二叉树的层序遍历 | BFS队列 | 15min |
| 11 | 二叉树最大深度 | DFS递归 | 5min |
| 12 | 验证二叉搜索树 | 中序遍历/范围递归 | 15min |
| 13 | 岛屿数量 | DFS/BFS | 15min |
| 14 | 爬楼梯 | DP | 5min |
| 15 | 最大子数组和 | Kadane | 10min |
| 16 | 零钱兑换 | 完全背包DP | 20min |
| 17 | 最长递增子序列 | LIS DP/二分 | 15min |
| 18 | 二分查找 | 标准二分 | 5min |
| 19 | 在排序数组中找元素的第一个和最后一个位置 | 二分边界 | 15min |
| 20 | 组合总和 | 回溯 | 20min |

---

> 📌 **复习建议**：
> - 每道题用 5 分钟在脑中过一遍思路
> - 如果卡住超过 2 分钟无法想起来，标记为"需重做"
> - 重点复习 3-5 道标记的题目
> - **模板要默写**，闭眼能写出来才算掌握
