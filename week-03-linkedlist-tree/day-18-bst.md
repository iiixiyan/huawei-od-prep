# Day 18 — BST（二叉搜索树）

> BST 性质、递归操作

---

## 📌 核心知识点

### BST 性质
```
左子树所有节点 < 根节点 < 右子树所有节点
且左右子树也是 BST
```

### BST 的中序遍历
**BST 的中序遍历结果是升序序列** — 这是 BST 最重要的特性。

```python
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
```

### BST 操作的时间复杂度

| 操作 | 平均 | 最差（退化为链表） |
|------|------|------------------|
| 搜索 | O(log N) | O(N) |
| 插入 | O(log N) | O(N) |
| 删除 | O(log N) | O(N) |

---

## 🧩 题目 1：二叉搜索树中的搜索

**LeetCode 700 | 难度：Easy**

### 题目描述
在 BST 中查找值为 `val` 的节点并返回该节点。

### 解法 1：递归

```python
def searchBST(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
```

### 解法 2：迭代

```python
def searchBST(root, val):
    while root and root.val != val:
        if val < root.val:
            root = root.left
        else:
            root = root.right
    return root
```

- **时间复杂度**：O(H)，H 为树高
- **空间复杂度**：递归 O(H) / 迭代 O(1)

### 面试要点
- 利用 BST 性质（左小右大）剪枝，不需要遍历整棵树
- 迭代版本更优（O(1) 空间）

---

## 🧩 题目 2：删除二叉搜索树中的节点

**LeetCode 450 | 难度：Medium**

### 题目描述
给定一个 BST 的根节点和一个 key，删除 key 对应的节点，并保证删除后的树仍然是 BST。

### 删除的三种情况

```
情况 1: 叶子节点 → 直接删除
情况 2: 只有一个子节点 → 用子节点替换
情况 3: 有两个子节点 → 用「中序后继」或「中序前驱」替换
```

### 完整代码

```python
def deleteNode(root, key):
    if not root:
        return None

    # 1. 查找要删除的节点
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # 找到要删除的节点
        # 情况 1 & 2: 叶子或只有一个子节点
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # 情况 3: 有两个子节点
        # 找到中序后继（右子树的最小节点）
        successor = find_min(root.right)
        root.val = successor.val           # 用后继的值覆盖
        root.right = deleteNode(root.right, successor.val)  # 删除后继

    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
```

- **时间复杂度**：O(H)
- **空间复杂度**：O(H)

### 另一种情况 3 的实现：用中序前驱

```python
# 用左子树的最大节点（中序前驱）替换
predecessor = find_max(root.left)
root.val = predecessor.val
root.left = deleteNode(root.left, predecessor.val)

def find_max(node):
    while node.right:
        node = node.right
    return node
```

### ⚠️ 容易被问到的细节

#### 为什么删除有两个子节点的节点时，用中序后继替换？
因为中序后继是**大于当前节点的最小节点**，用它替换后：
- 左子树所有节点 < 新值 ✅
- 右子树所有节点（除被删除的后继外）> 新值 ✅

#### 删除后为什么还要递归删除后继？
因为后继可能也有子节点，需要递归处理删除。但后继一定**没有左子节点**（否则它就不是最小节点），所以实际只涉及情况 1 或 2。

---

## 🧩 BST 高频变体题

### 1. 验证二叉搜索树（LeetCode 98）

```python
def isValidBST(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (dfs(node.left, min_val, node.val) and
                dfs(node.right, node.val, max_val))
    return dfs(root, float('-inf'), float('inf'))
```

⚠️ 不能用简单的「左 < 根 < 右」递归检查，因为需要保证**全局**范围。

### 2. BST 的最近公共祖先（LeetCode 235）

```python
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

利用 BST 性质，一次遍历即可，无需递归。

### 3. 将有序数组转换为 BST（LeetCode 108）

```python
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root
```

每次取中间元素作为根，递归构建左右子树。

---

## ⚡ 今日总结

| 题目 | 核心技巧 | 难度 |
|------|---------|------|
| BST 搜索 | 利用性质剪枝 | ⭐ |
| 删除 BST 节点 | 三种情况分类讨论 | ⭐⭐⭐ |

### 面试高频点
- ✅ BST 中序遍历 = 升序序列
- ✅ 删除操作是面试**最常考的 BST 操作**
- ✅ 验证 BST 要用**区间传递**而非简单比较
- ✅ 能用 BST 性质解决的问题，一定比通用解法更优
