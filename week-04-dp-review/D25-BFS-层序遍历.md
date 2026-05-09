# Day 25: BFS + 层序遍历

## 📖 知识点
层序遍历（BFS）使用队列实现，模板：初始化队列放入 root，while 队列非空，取出当前层所有节点（for _ in range(len(q))），处理值并将子节点入队。

**层序模板**：
```python
def levelOrder(root):
    if not root: return []
    res, q = [], collections.deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

---

## 🧩 刷题任务（6题）

### 1. Binary Tree Right Side View（⭐⭐）来源：L75 / T150 / O
**思路**：层序遍历，取每层最后一个节点值。也可以用 DFS（根→右→左优先遍历，每层第一个访问到的就是右视图）。
**代码**：
```python
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res, q = [], collections.deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0:           # 每层第一个
                res.append(node.val)
            if node.right: q.append(node.right)  # 先右后左
            if node.left: q.append(node.left)
    return res
```

### 2. Average of Levels in Binary Tree（⭐）来源：T150
**思路**：层序遍历，每层求和后除以该层节点数。
**代码**：
```python
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    res, q = [], collections.deque([root])
    while q:
        total, n = 0, len(q)
        for _ in range(n):
            node = q.popleft()
            total += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(total / n)
    return res
```

### 3. Binary Tree Level Order Traversal（⭐⭐）来源：T150
**思路**：标准层序遍历，每层结果存入列表。
**代码**：
```python
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res, q = [], collections.deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

### 4. Binary Tree Zigzag Level Order Traversal（⭐⭐）来源：T150
**思路**：层序遍历 + 奇偶层反转。偶数层从左到右，奇数层从右到左（用 level 是否反转或双端队列）。
**代码**：
```python
def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res, q, layer = [], collections.deque([root]), 0
    while q:
        level = collections.deque()
        for _ in range(len(q)):
            node = q.popleft()
            if layer % 2 == 0:
                level.append(node.val)   # 从左到右
            else:
                level.appendleft(node.val)  # 从右到左
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(list(level))
        layer += 1
    return res
```

### 5. Maximum Level Sum of a Binary Tree（⭐⭐）来源：L75
**思路**：层序遍历，记录每层和的最大值及其层号。
**代码**：
```python
def maxLevelSum(root: Optional[TreeNode]) -> int:
    max_sum, max_level = -10**9, 1
    q, level = collections.deque([root]), 0
    while q:
        level += 1
        total = 0
        for _ in range(len(q)):
            node = q.popleft()
            total += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if total > max_sum:
            max_sum = total
            max_level = level
    return max_level
```

### 6. Find Bottom Left Tree Value（⭐⭐）来源：O（剑指 Offer）
**思路**：层序遍历，每层第一个节点即为最左节点。按顺序遍历（先右后左取最后一个，或先左后右取第一个）。
**代码**：
```python
def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node.right: q.append(node.right)   # 先右后左
        if node.left: q.append(node.left)
    return node.val  # 最后出队的即为最底层最左节点
```

---

## 📝 总结
Day 25 集中训练 BFS 层序遍历及其变体：标准层序（levelOrder）、zigzag（奇偶反转）、右视图（每层最后一个）、每层平均值、最大层和、最左叶子。核心模板一致——用队列+每层长度控制。变体主要在于每层取元素的顺序和聚合方式。BFS 在树和图中是最高频的遍历方式，务必熟练默写模板。
