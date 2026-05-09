# Day 16 — Tree DFS 进阶

> 前缀和 + 哈希、DP in Tree、递归 LCA

---

## 📌 核心知识点

### 进阶 DFS 技巧
1. **前缀和 + 哈希表**：路径和问题中 O(N) 优化
2. **状态传递**：在递归中传递多个状态值（方向、长度）
3. **自底向上归并**：递归函数返回多个信息（LCA 问题）

---

## 🧩 题目 1：路径总和 III

**LeetCode 437 | 难度：Medium**

### 题目描述
给定一个二叉树和一个目标和 `targetSum`，找出路径**和等于目标值**的路径数目。路径不需要从根开始，也不需要在叶子结束，但方向必须向下（从父到子）。

### 解法 1：双重 DFS（O(N²)）

```python
def pathSum(root, targetSum):
    def dfs_from_node(node, current_sum):
        if not node:
            return 0
        current_sum += node.val
        count = 1 if current_sum == targetSum else 0
        count += dfs_from_node(node.left, current_sum)
        count += dfs_from_node(node.right, current_sum)
        return count

    if not root:
        return 0
    return (dfs_from_node(root, 0) +
            pathSum(root.left, targetSum) +
            pathSum(root.right, targetSum))
```

### 解法 2：前缀和 + 哈希（O(N)）⭐ 最优

```python
from collections import defaultdict

def pathSum(root, targetSum):
    prefix = defaultdict(int)
    prefix[0] = 1  # 空路径和为 0

    def dfs(node, curr_sum):
        if not node:
            return 0
        curr_sum += node.val
        # 当前路径和 - targetSum 在前缀中出现次数 = 合法路径数
        count = prefix[curr_sum - targetSum]
        prefix[curr_sum] += 1            # 记录当前前缀和
        count += dfs(node.left, curr_sum)
        count += dfs(node.right, curr_sum)
        prefix[curr_sum] -= 1            # 回溯！移除当前前缀和
        return count

    return dfs(root, 0)
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(N)

### ⚠️ 为什么需要回溯？
前缀和记录的是**从根到当前节点路径上**的所有前缀和。回溯避免兄弟子树误用当前路径的前缀和。

### 面试话术
> "这道题本质是**一维数组中和为 target 的子数组个数**的树版本。用前缀和 + 哈希可以把 O(N²) 优化到 O(N)。关键是要在递归返回时回溯，移除当前节点的前缀和。"

---

## 🧩 题目 2：最长交错路径

**LeetCode 1372 | 难度：Medium**

### 题目描述
在二叉树中，交错路径定义为：连续三步的方向交替（左→右→左 或 右→左→右）。求最长交错路径的长度（边的数量）。

### 解法：递归状态传递

```python
def longestZigZag(root):
    max_len = 0

    def dfs(node, direction, length):
        """
        direction: 0=左, 1=右 (从父到当前的方向)
        length: 当前交错路径长度
        """
        nonlocal max_len
        if not node:
            return
        max_len = max(max_len, length)
        # 向左走
        if direction == 0:  # 上一步是左，继续左则重置
            dfs(node.left, 0, 1)            # 重新开始
            dfs(node.right, 1, length + 1)  # 交错延续
        else:  # direction == 1, 上一步是右
            dfs(node.left, 0, length + 1)   # 交错延续
            dfs(node.right, 1, 1)           # 重新开始

    dfs(root.left, 0, 1)
    dfs(root.right, 1, 1)
    return max_len
```

### 更简洁的写法

```python
def longestZigZag(root):
    def dfs(node):
        """返回 [从node向左走的最长交错, 从node向右走的最长交错]"""
        if not node:
            return [-1, -1]  # 空节点：-1 表示没有边
        left_left, left_right = dfs(node.left)
        right_left, right_right = dfs(node.right)
        # 从左子节点来：向上一次是左 → 这次向右
        go_left = left_right + 1   # 从node向左
        go_right = right_left + 1  # 从node向右
        nonlocal ans
        ans = max(ans, go_left, go_right)
        return [go_left, go_right]

    ans = 0
    dfs(root)
    return ans
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(H)

### 核心思想
每个节点返回两个值：
- `[0]`：从该节点**向左**走的最长交错长度
- `[1]`：从该节点**向右**走的最长交错长度

子 → 父 的推导：
- 节点向左走 = 左子节点的向右走 + 1
- 节点向右走 = 右子节点的向左走 + 1

---

## 🧩 题目 3：最近公共祖先

**LeetCode 236 | 难度：Medium**

### 题目描述
给定一个二叉树和两个节点 p、q，找到它们的最近公共祖先（LCA）。

### 解法：递归后序

```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root        # p 和 q 分别在左右子树
    return left or right   # 都在同一侧
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(H)

### 三种情况分析

| 情况 | left 返回值 | right 返回值 | 结果 |
|------|------------|-------------|------|
| p、q 在左右各一 | 非空 | 非空 | root |
| p、q 都在左 | 非空 | None | left |
| p、q 都在右 | None | 非空 | right |
| root 就是 p 或 q | root | - | root（提前返回） |

### 面试延伸
- **BST 的 LCA**：利用值大小关系 O(H) 解决
- **二叉树的 LCA（含父指针）**：转化为求两个链表交点
- **N 叉树的 LCA**：遍历所有子节点，找到两个非空即返回

---

## ⚡ 今日总结

| 题目 | 核心技巧 | 难度 |
|------|---------|------|
| 路径总和 III | 前缀和 + 哈希 + 回溯 | ⭐⭐⭐ |
| 最长交错路径 | 双状态后序传递 | ⭐⭐⭐ |
| 最近公共祖先 | 后序递归归并 | ⭐⭐⭐ |

### 面试高频点
- ✅ 前缀和技巧：从数组到树的迁移
- ✅ 树形 DP：子节点「上报」信息给父节点
- ✅ 回溯思想：在递归中「记录 → 递归 → 撤销」
