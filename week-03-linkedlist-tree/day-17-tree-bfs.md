# Day 17 — Tree BFS

> 层序遍历 BFS 模板

---

## 📌 核心知识点

### 二叉树 BFS 模板

```python
from collections import deque

def bfs(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)        # 处理当前节点
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)              # 处理当前层
    return result
```

### BFS vs DFS 对比

| 特性 | BFS | DFS |
|------|-----|-----|
| 数据机构 | 队列 | 栈（递归） |
| 空间复杂度 | 最宽层 | 树高 |
| 适用场景 | 最短路径、层信息 | 路径枚举、状态传递 |
| 时间 | O(N) | O(N) |

---

## 🧩 题目 1：二叉树的右视图

**LeetCode 199 | 难度：Medium**

### 题目描述
给定一个二叉树，站在右侧看过去，能看到哪些节点？从上到下返回。

### 解法 1：BFS 取每层最右

```python
from collections import deque

def rightSideView(root):
    if not root:
        return []
    q = deque([root])
    view = []
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == level_size - 1:    # 每层最右一个
                view.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return view
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(W)，W 为最大层宽

### 解法 2：DFS（先右后左）

```python
def rightSideView(root):
    view = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(view):       # 第一次到达这一层 → 从右边看第一个
            view.append(node.val)
        dfs(node.right, depth + 1)   # 先右后左
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return view
```

- 不需要队列，空间 O(H)
- 利用 DFS 访问顺序：先右后左，每层第一个访问到的就是右视图节点

### 变体题
- **二叉树的左视图**：BFS 取每层最左，或 DFS 先左后右
- **俯视图**：需要记录水平偏移量

---

## 🧩 题目 2：最大层内和

**LeetCode 1161 | 难度：Medium**

### 题目描述
找出一棵二叉树中**和最大**的那一层（层数从 1 开始），如果有多个，返回最小的层号。

### 解法：BFS 求层和

```python
from collections import deque

def maxLevelSum(root):
    if not root:
        return 0
    q = deque([root])
    max_sum = float('-inf')
    max_level = 1
    level = 0

    while q:
        level += 1
        level_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

    return max_level
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(W)

### 代码要点
1. 用 `len(q)` 固定当前层的大小
2. 每层累加 `level_sum`
3. 更新全局最大时**严格大于**才更新（题目要求等值时返回小层号）
4. 层号从 1 开始计数（根为第 1 层）

### 思考题
> 如果树中可能有负数，初始化的 `max_sum` 应该是什么？
>
> **答**：`float('-inf')`，因为可能出现所有层和都为负数的情况。

---

## 🧩 BFS 在更复杂场景中的应用

### 1. 二叉树的层平均值（LeetCode 637）
每层求均值，BFS 累加后除以 `level_size`。

### 2. N 叉树的层序遍历（LeetCode 429）
BFS 模板中，将 `node.left` / `node.right` 替换为遍历 `node.children`。

### 3. 二叉树的锯齿形层序遍历（LeetCode 103）
BFS + 方向标记：偶数层反转列表。

```python
def zigzagLevelOrder(root):
    if not root:
        return []
    q = deque([root])
    result = []
    left_to_right = True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result
```

---

## ⚡ 今日总结

| 题目 | 核心技巧 | 难度 |
|------|---------|------|
| 二叉树的右视图 | BFS 每层最右 / DFS 先右后左 | ⭐⭐ |
| 最大层内和 | BFS 累加 + 全局最大值 | ⭐⭐ |

### BFS 适用场景总结
- ✅ 需要**分层**处理数据
- ✅ 求**最短路径**（无权图）
- ✅ 求树的**宽度**、**层最大值/平均值**
- ✅ **多源**扩散问题（见 Day 20）

### 面试高频点
- BFS 模板必须**手写熟练**
- 理解 `len(q)` 固定当前层大小的原理
- 能灵活处理「每层最右」「锯齿形」等变体
