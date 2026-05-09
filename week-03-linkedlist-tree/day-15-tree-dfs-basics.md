# Day 15 — Tree DFS 基础

> 递归遍历树、DFS 模板

---

## 📌 核心知识点

### 二叉树 DFS 模板

```python
def dfs(root):
    if not root:
        return
    # 前序: 处理当前节点
    dfs(root.left)
    # 中序: 处理当前节点
    dfs(root.right)
    # 后序: 处理当前节点
```

### 三种遍历顺序对比

| 遍历方式 | 顺序 | 用途 |
|---------|------|------|
| 前序 | 根 → 左 → 右 | 构造、复制树 |
| 中序 | 左 → 根 → 右 | BST 有序输出 |
| 后序 | 左 → 右 → 根 | 从叶子向上计算 |

---

## 🧩 题目 1：二叉树的最大深度

**LeetCode 104 | 难度：Easy**

### 题目描述
给定一个二叉树，找出其最大深度（根节点到最远叶子节点的最长路径上的节点数）。

### 解法 1：递归（最简）

```python
def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1
```

- **时间复杂度**：O(N)，每个节点访问一次
- **空间复杂度**：O(H)，H 为树高（递归栈深度）

### 解法 2：迭代（BFS 层序遍历）

```python
from collections import deque

def maxDepth(root):
    if not root:
        return 0
    q = deque([root])
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return depth
```

### 面试要点
- 递归解法简洁，但面试中要考虑**栈溢出**风险（树退化为链表时）
- 迭代解法用「层数」计数，比递归更安全
- **变形题**：N 叉树的最大深度 → 遍历所有子节点取 max

---

## 🧩 题目 2：叶子相似的树

**LeetCode 872 | 难度：Easy**

### 题目描述
一棵树的「叶子序列」是从左到右收集所有叶子节点的值。判断两棵树的叶子序列是否相同。

### 解法：DFS 收集叶子

```python
def leafSimilar(root1, root2):
    def collect_leaves(root, leaves):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        collect_leaves(root.left, leaves)
        collect_leaves(root.right, leaves)

    leaves1, leaves2 = [], []
    collect_leaves(root1, leaves1)
    collect_leaves(root2, leaves2)
    return leaves1 == leaves2
```

- **时间复杂度**：O(N + M)
- **空间复杂度**：O(N + M)

### 优化思路
- 可以用**生成器**逐个 yield 叶子，发现不同就提前终止（节省空间）
- 但面试写清晰易懂的版本更重要

---

## 🧩 题目 3：统计好节点数目

**LeetCode 1448 | 难度：Medium**

### 题目描述
「好节点」定义为：从根到该节点的路径上，没有节点的值比它大。统计二叉树中好节点的个数。

### 解法：带路径最大值的 DFS

```python
def goodNodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        count = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        return count

    return dfs(root, root.val) if root else 0
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(H)

### 核心思想
1. 从根到当前节点，维护路径上的**最大值**
2. 当前节点值 ≥ 路径最大值 → 好节点
3. 更新最大值后递归左右子树

### 变体：路径上最小值的好节点
只需把 `>=` 改成 `<=`，`max` 改成 `min` 即可。

---

## ⚡ 今日总结

| 题目 | 核心技巧 | 难度 |
|------|---------|------|
| 二叉树的最大深度 | 后序递归 / BFS 层数 | ⭐ |
| 叶子相似的树 | DFS 收集 + 比较 | ⭐ |
| 统计好节点数目 | 路径最大值传递 | ⭐⭐ |

### 面试高频点
- ✅ 熟练掌握递归 DFS 三种顺序
- ✅ 理解递归 vs 迭代的优劣
- ✅ 能处理「路径状态传递」类问题（如 Day 15 的好节点）
