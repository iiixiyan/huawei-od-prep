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
**来源**：[L75](https://leetcode.cn/problems/binary-tree-right-side-view/)
**难度**：中等
**题目**：给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**示例 1：**
```
**输入：**root = [1,2,3,null,5,null,4]
**输出：**[1,3,4]
**解释：**
*
```
**示例 2：**
```
**输入：**root = [1,2,3,4,null,null,null,5]
**输出：**[1,3,4,5]
**解释：**
*
```
**示例 3：**
```
**输入：**root = [1,null,3]
**输出：**[1,3]
```
**示例 4：**
```
**输入：**root = []
**输出：**[]
```
**提示:**

- 二叉树的节点个数的范围是 `[0,100]`

- `-100
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
**来源**：[T150](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)
**难度**：简单
**题目**：给定一个非空二叉树的根节点 `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10-5` 以内的答案可以被接受。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：[3.00000,14.50000,11.00000]
解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。
```
**示例 2:**
```
*
输入：root = [3,9,20,15,7]
输出：[3.00000,14.50000,11.00000]
```
**提示：**

- 树中节点数量在 `[1, 104]` 范围内

- `-231 31 - 1`
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
**来源**：[T150](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
**难度**：中等
**题目**：给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```
**示例 2：**
```
输入：root = [1]
输出：[[1]]
```
**示例 3：**
```
输入：root = []
输出：[]
```
**提示：**

- 树中节点数目在范围 `[0, 2000]` 内

- `-1000
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
**来源**：[T150](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
**难度**：中等
**题目**：给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
```
**示例 2：**
```
输入：root = [1]
输出：[[1]]
```
**示例 3：**
```
输入：root = []
输出：[]
```
**提示：**

- 树中节点数目在范围 `[0, 2000]` 内

- `-100
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
**来源**：[L75](https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/)
**难度**：中等
**题目**：给你一个二叉树的根节点 `root`。设根节点位于二叉树的第 `1` 层，而根节点的子节点位于第 `2` 层，依此类推。

返回总和 **最大**的那一层的层号 `x`。如果有多层的总和一样大，返回其中**最小** 的层号 `x`。

**示例 1：**
```
*****
输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
```
**示例 2：**
```
输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2
```
**提示：**

- 树中的节点数在 `[1, 104]`范围内

- `-105 5`
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
**来源**：[O（剑指](https://leetcode.cn/problems/find-bottom-left-tree-value/)
**难度**：中等
**题目**：给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边 **节点的值。

假设二叉树中至少有一个节点。

**示例 1:**
```
*
输入: root = [2,1,3]
输出: 1
```
**示例 2:**
```
*
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
```
**提示:**

- 二叉树的节点个数的范围是 `[1,104]`

- `-231 31 - 1`
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
## 📝 总结
Day 25 集中训练 BFS 层序遍历及其变体：标准层序（levelOrder）、zigzag（奇偶反转）、右视图（每层最后一个）、每层平均值、最大层和、最左叶子。核心模板一致——用队列+每层长度控制。变体主要在于每层取元素的顺序和聚合方式。BFS 在树和图中是最高频的遍历方式，务必熟练默写模板。
