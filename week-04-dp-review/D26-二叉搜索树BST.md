# Day 26: 二叉搜索树（BST）

## 📖 知识点
BST 核心性质：左子树所有节点 < 根 < 右子树所有节点。中序遍历 BST 得到**升序序列**，这是解决大多数 BST 问题的钥匙。常见操作：搜索（O(h)）、插入（O(h)）、删除（O(h)，分三种情况 — 无子、单子、双子（找前驱/后继替换））。

**中序遍历模板**：
```python
def inorder(root, res):
    if not root: return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)
```

---

## 🧩 刷题任务（6题）

### 1. Search in a Binary Search Tree（⭐）来源：L75
**思路**：利用 BST 性质比较大小，递归或迭代搜索。
**代码**：
```python
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)
```

### 2. Delete Node in a BST（⭐⭐⭐）来源：L75
**思路**：递归找到要删除的节点。分三种情况：无子节点（直接删）、单子节点（子节点替代）、双子节点（找右子树最小节点/中序后继替换值后删除该后继）。
**代码**：
```python
def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right  # 无左或单右
        if not root.right:
            return root.left   # 无右或单左
        # 双子节点：找右子树最小节点
        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val            # 替换值
        root.right = deleteNode(root.right, cur.val)  # 删除后继
    return root
```

### 3. Validate Binary Search Tree（⭐⭐）来源：T150
**思路**：中序遍历检查是否升序（pre < cur）。或递归传递上下界 (min, max)。
**代码**：
```python
def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
    return dfs(root, -10**18, 10**18)
```

### 4. Kth Smallest Element in a BST（⭐⭐）来源：T150
**思路**：中序遍历 BST 得到升序序列，第 k 个元素即为答案。可用递归计数或迭代栈提前终止（更优）。
**代码**：
```python
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
```

### 5. Minimum Absolute Difference in BST（⭐）来源：T150
**思路**：中序遍历 BST 得到升序序列，相邻元素差值最小即为答案。用 prev 记录前一个节点值。
**代码**：
```python
def getMinimumDifference(root: Optional[TreeNode]) -> int:
    prev, ans = None, 10**9
    
    def dfs(node):
        nonlocal prev, ans
        if not node:
            return
        dfs(node.left)
        if prev is not None:
            ans = min(ans, node.val - prev)
        prev = node.val
        dfs(node.right)
    
    dfs(root)
    return ans
```

### 6. Inorder Successor in BST（⭐⭐）来源：O（剑指 Offer）
**思路**：中序后继是大于 p 的最小节点。递归/迭代：若 p 有右子树，后继为右子树最左节点；否则沿根向下搜索，记录最后一个向左转的节点。
**代码**：
```python
def inorderSuccessor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    successor = None
    while root:
        if p.val < root.val:
            successor = root          # 候选
            root = root.left
        else:
            root = root.right
    return successor
```

---

## 📝 总结
Day 26 专攻 BST 五大题型：搜索（二分查找思想）、删除（三情况分类）、验证（中序升序/上下界）、第 K 小（中序计数）、最小差值（中序相邻差）、后继（有右子则最左/否则记录左转节点）。BST 题 90% 用中序遍历解决，务必熟练掌握迭代中序写法。
