# Day 21 — 周复习 + 小测

> Week 3 总结回顾：二叉树 & 图 DFS/BFS

---

## 📋 本周知识体系

```
Week 3: 二叉树 & 图 DFS/BFS
│
├── 二叉树 DFS
│   ├── Day 15: 基础 DFS（最大深度、叶子收集、路径最大值）
│   └── Day 16: 进阶 DFS（前缀和、树形DP、LCA）
│
├── 二叉树 BFS
│   └── Day 17: 层序遍历（右视图、最大层和）
│
├── BST
│   └── Day 18: BST 搜索 & 删除
│
├── 图 DFS
│   └── Day 19: 可达性、连通分量、双向建图、带权图
│
└── 图 BFS
    └── Day 20: 矩阵最短路、多源 BFS
```

---

## 🧠 核心概念速查

### 递归 DFS 三种顺序

```python
# 前序: 根 → 左 → 右    （构造、复制）
# 中序: 左 → 根 → 右    （BST 有序输出）
# 后序: 左 → 右 → 根    （自底向上归并）
```

### BFS 层序遍历

```python
q = deque([root])
while q:
    for _ in range(len(q)):
        node = q.popleft()
        # 处理当前节点
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
```

### 图 DFS vs 图 BFS

| | DFS | BFS |
|--|-----|-----|
| 数据结构 | 栈（递归） | 队列 |
| 核心操作 | visited 标记 | visited + 分层 |
| 最短路径 | ❌ | ✅ 无权图 |
| 连通分量 | ✅ 自然适用 | ✅ 适用 |
| 空间（矩阵） | O(m×n) 最差 | O(min(m,n)) |

---

## 📝 小测（15 题）

### 一、选择题（每题 1 分）

**1. 二叉树的前序遍历中，访问顺序是？**
A. 左→根→右   B. 根→左→右   C. 左→右→根   D. 根→右→左

**2. 以下哪个不是 BST 的特性？**
A. 左子树所有节点小于根
B. 右子树所有节点大于根
C. 中序遍历是升序
D. 任意节点的左右子树高度差不超过 1

**3. 在无权图中求最短路径，应该使用？**
A. DFS   B. BFS   C. 都可以  D. 都不行

**4. 二叉树的「右视图」可以用什么方法得到？**
A. 前序遍历   B. 中序遍历   C. BFS 取每层最右   D. 后序遍历

**5. 多源 BFS 与单源 BFS 的主要区别是？**
A. 时间复杂度不同   B. 初始队列有多个元素   C. 不能求最短路径   D. 不需要 visited

**6. 删除 BST 中一个有左右子树的节点，正确的做法是？**
A. 直接删除，左右子树丢弃
B. 用左子节点替换
C. 用中序后继或前驱替换
D. 删除整个树

**7. 「省份数量」问题的本质是？**
A. 最短路径  B. 连通分量计数  C. 最小生成树  D. 拓扑排序

### 二、填空题（每题 2 分）

**8. 二叉树的最大深度递归解法的递推关系是：**
`maxDepth(root) = ________________________________`

**9. 「路径总和 III」中，将 O(N²) 优化到 O(N) 的核心技巧是：__________________`

**10. 图 DFS 与树 DFS 相比，多了一个关键步骤：____________`

**11. 判断一个树是否是 BST 时，不能只判断 `left.val < root.val < right.val`，而需要传递 _________________`

### 三、代码填空题（每题 3 分）

**12. 补全 LCA 代码：**
```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        _____________
    return ______________
```

**13. 补全腐烂橘子 BFS 核心逻辑：**
```python
def orangesRotting(grid):
    q = deque()
    fresh = 0
    # 初始化：找到所有腐烂橘子入队，统计新鲜橘子
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    minutes = 0
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    ____________  # 标记腐烂
                    ____________  # 减少新鲜计数
                    ____________  # 入队
        minutes += 1
    return minutes if fresh == 0 else -1
```

**14. 补全 BST 删除（有两个子节点的情况）：**
```python
# 找到要删除的节点 root
if root.left and root.right:
    # 找中序后继
    successor = root.right
    while successor.left:
        successor = successor.left
    root.val = successor.val
    root.right = __________________
```

### 四、简答题（每题 3 分）

**15. 简述「前缀和 + 哈希」优化「路径总和 III」的原理。为什么需要回溯？**

---

## ✅ 答案

### 选择题
1. **B** — 前序：根→左→右
2. **D** — 左右子树高度差不超过 1 是 AVL 树的特性，不是 BST 的
3. **B** — BFS 按层遍历，第一次到达即最短
4. **C** — BFS 取每层最右，或 DFS 先右后左
5. **B** — 多源 BFS 初始队列有多个源点
6. **C** — 用中序后继（右子树最小）或前驱（左子树最大）替换
7. **B** — 求图中连通分量个数

### 填空题
8. `max(maxDepth(root.left), maxDepth(root.right)) + 1`
9. **前缀和 + 哈希表**
10. **使用 visited 标记已访问节点**
11. **全局上下界（min_val, max_val）**

### 代码填空
12.
```python
    return root        # left and right 都非空
    return left or right  # 至少一个非空
```

13.
```python
    grid[nr][nc] = 2    # 标记腐烂
    fresh -= 1          # 减少新鲜计数
    q.append((nr, nc))  # 入队
```

14.
```python
    root.right = deleteNode(root.right, successor.val)
```

### 简答题
**15.「路径总和 III」前缀和原理：**
- 定义 `prefix_sum` 表示从根到当前节点的路径和
- 对于当前节点，以它为终点的合法路径数 = 前缀和中 `curr_sum - targetSum` 出现的次数
- 用哈希表记录每个前缀和的出现次数
- **需要回溯**：因为当我们递归完左子树进入右子树时，左子树路径上的前缀和不应该影响右子树的计算。如果不回溯，哈希表中会残留左子树的前缀和，导致右子树误用。

---

## 📊 本周学习自评表

| 知识点 | 掌握程度 | 需强化 |
|--------|---------|--------|
| Tree DFS 基础（最大深度、叶子） | □ □ □ □ □ | |
| Tree DFS 进阶（前缀和、LCA） | □ □ □ □ □ | |
| Tree BFS（层序） | □ □ □ □ □ | |
| BST 操作 | □ □ □ □ □ | |
| Graph DFS（连通分量、双向建图） | □ □ □ □ □ | |
| Graph BFS（矩阵、多源） | □ □ □ □ □ | |
| 综合代码手写能力 | □ □ □ □ □ | |

> **下期预告：Week 4 — 动态规划入门（背包 & 线性 DP）**

---

## 🔁 本周错题本模板

```
## 错题记录
日期：____
题号：____
错误原因：□ 思路不清  □ 边界条件  □ 代码实现  □ 时间复杂度过高
正确解法概要：
________________________________
________________________________
```
