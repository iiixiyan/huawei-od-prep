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
**来源**：[L75](https://leetcode.cn/problems/search-in-a-binary-search-tree/)
**难度**：简单
**题目**：给定二叉搜索树（BST）的根节点 `root` 和一个整数值 `val`。

你需要在 BST 中找到节点值等于 `val` 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 `null` 。

**示例 1:**
```
*
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]
```
**示例 2:**
```
*
输入：root = [4,2,7,1,3], val = 5
输出：[]
```
**提示：**

- 树中节点数在 `[1, 5000]` 范围内

- `1 7`

- `root` 是二叉搜索树

- `1 7`
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
**来源**：[L75](https://leetcode.cn/problems/delete-node-in-a-bst/)
**难度**：中等
**题目**：给定一个二叉搜索树的根节点 **root **和一个值 **key**，删除二叉搜索树中的 **key **对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

- 首先找到需要删除的节点；

- 如果找到了，删除它。

**示例 1:**
```
*
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。
```
**示例 2:**
```
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
```
**示例 3:**
```
输入: root = [], key = 0
输出: []
```
**提示:**

- 节点数的范围 `[0, 104]`.

- `-105 5`

- 节点值唯一

- `root` 是合法的二叉搜索树

- `-105 5`

**进阶：** 要求算法时间复杂度为 O(h)，h 为树的高度。
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
**来源**：[T150](https://leetcode.cn/problems/validate-binary-search-tree/)
**难度**：中等
**题目**：给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

- 节点的左子树只包含**严格小于**当前节点的数。

- 节点的右子树只包含 **严格大于** 当前节点的数。

- 所有左子树和右子树自身必须也是二叉搜索树。

**示例 1：**
```
*
输入：root = [2,1,3]
输出：true
```
**示例 2：**
```
*
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
```
**提示：**

- 树中节点数目范围在`[1, 104]` 内

- `-231 31 - 1`
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
**来源**：[T150](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)
**难度**：中等
**题目**：给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素（`k` 从 1 开始计数）。

**示例 1：**
```
*
输入：root = [3,1,4,null,2], k = 1
输出：1
```
**示例 2：**
```
*
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```
**提示：**

- 树中的节点数为 `n` 。

- `1 4`

- `0 4`

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？
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
**来源**：[T150](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)
**难度**：简单
**题目**：给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。

**示例 1：**
```
*
输入：root = [4,2,6,1,3]
输出：1
```
**示例 2：**
```
*
输入：root = [1,0,48,null,null,12,49]
输出：1
```
**提示：**

- 树中节点的数目范围是 `[2, 104]`

- `0 5`

**注意：**本题与 783 https://leetcode.cn/problems/minimum-distance-between-bst-nodes/ 相同
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
**来源**：[O（剑指](https://leetcode.cn/problems/inorder-successor-in-bst/)
**难度**：中等
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
## 📝 总结
Day 26 专攻 BST 五大题型：搜索（二分查找思想）、删除（三情况分类）、验证（中序升序/上下界）、第 K 小（中序计数）、最小差值（中序相邻差）、后继（有右子则最左/否则记录左转节点）。BST 题 90% 用中序遍历解决，务必熟练掌握迭代中序写法。
