# Day 45: 创建二叉树（200分·树/图类）

## 📖 前置知识
- **二叉树基础**：前序/中序/后序/层序遍历，建树方式
- **二叉搜索树（BST）**：左子树 < 根 < 右子树的性质
- **递归建树**：根据数组/序列构建二叉树
- **层次遍历（BFS）**：使用队列按层遍历

## 🧩 刷题任务

### 题目：创建二叉树（200分）

**题目描述**：
请按下列规则创建一棵二叉树并输出其层次遍历结果。

给定一个二维整数数组，每个元素 `[value, level]` 表示：
- `value`：待插入的节点值
- `level`：该节点在树中的深度（根节点深度为 0）

插入规则：
1. 第一个元素作为根节点
2. 后续元素按给定顺序依次插入，插入时从根节点开始，按照以下规则寻找插入位置：
   - 若当前节点值 > 待插入节点值，向左子树走
   - 若当前节点值 < 待插入节点值，向右子树走
   - 若相等，插入失败（跳过）
3. 走到目标位置的 **父节点** 时，检查左右子节点是否为空，将新节点插入为空的一侧
4. 如果左右子节点都不为空，则 **继续向下寻找**
5. 如果到达深度 level 时还没有空位，则插入失败

**输入描述**：
第一行：整数 N（1 ≤ N ≤ 1000）
接下来 N 行：每行两个整数 value 和 level（value 范围 [1, 1000]，level 范围 [0, 100]）

**输出描述**：
一行：层次遍历结果，节点间用空格分隔。若二叉树为空则输出 "null"。

**样例输入**：
```
7
10 0
5 1
3 2
8 2
15 1
12 2
20 2
```

**样例输出**：
```
10 5 15 3 8 12 20
```

**解释**：
- 根节点 10 (level 0)
- 5 (level 1) 比10小 → 左子
- 3 (level 2) 比10小→左, 比5小→左子
- 8 (level 2) 比10小→左, 比5大→右子
- 15 (level 1) 比10大→右子
- 12 (level 2) 比10大→右, 比15小→左子
- 20 (level 2) 比10大→右, 比15大→右子

---

**思路分析**：

**核心难点**：
本题不是简单的 BST 插入，而是要求节点插入到 **指定的深度 level**。这意味着当我们在 BST 中寻找位置时，如果找到的位置深度小于指定的 level，且该位置子节点已满，需要继续向下走。

**模拟建树步骤**：
1. 定义树节点结构：`value`, `left`, `right`, `depth`
2. 读取根节点 `[val, level]` 创建根
3. 对后续每个节点 `[val, target_level]`：
   - 从根开始查找，当前深度 `cur_depth = 0`
   - 每次比较 val 与当前节点值决定向左/向右
   - 检查目标位置的子节点：
     - 如果为空 → 插入，成功
     - 如果不为空：
       - 如果当前深度+1 < target_level，继续向下走（深入）
       - 如果当前深度+1 == target_level，但子节点已被占用 → 插入失败
4. 层次遍历输出

**复杂度**：
- 时间：O(N × H)，H 为树高，最坏 O(N²)
- 空间：O(N)

---

**参考代码**：
```python
class TreeNode:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None

    # 第一个节点作为根
    root = TreeNode(nodes[0][0], nodes[0][1])

    for val, target_depth in nodes[1:]:
        cur = root
        cur_depth = 0
        inserted = False

        while not inserted:
            # 比较值决定方向
            if val < cur.val:
                if cur.left is None:
                    # 如果目标深度匹配，插入
                    if cur_depth + 1 == target_depth:
                        cur.left = TreeNode(val, target_depth)
                        inserted = True
                    else:
                        # 深度不够，但左子为空——插入（根据规则，在此深度插入）
                        # 注意：有些版本要求必须到达指定深度
                        cur.left = TreeNode(val, target_depth)
                        inserted = True
                else:
                    # 左子已存在
                    if cur_depth + 1 < target_depth:
                        cur = cur.left
                        cur_depth += 1
                    elif cur_depth + 1 == target_depth:
                        # 目标深度但左子被占，尝试右子
                        if cur.right is None:
                            cur.right = TreeNode(val, target_depth)
                            inserted = True
                        else:
                            # 左右都被占，继续向下（虽然深度已到，但规则说继续向下）
                            # 但通常这里表示插入失败
                            break  # 插入失败
                    else:
                        break  # 插入失败
            else:  # val >= cur.val
                if cur.right is None:
                    if cur_depth + 1 == target_depth:
                        cur.right = TreeNode(val, target_depth)
                        inserted = True
                    else:
                        cur.right = TreeNode(val, target_depth)
                        inserted = True
                else:
                    if cur_depth + 1 < target_depth:
                        cur = cur.right
                        cur_depth += 1
                    elif cur_depth + 1 == target_depth:
                        if cur.left is None:
                            cur.left = TreeNode(val, target_depth)
                            inserted = True
                        else:
                            break
                    else:
                        break

    return root

def level_order(root):
    if not root:
        return []
    from collections import deque
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        res.append(str(node.val))
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

# 输入处理
N = int(input())
pairs = []
for _ in range(N):
    v, l = map(int, input().split())
    pairs.append((v, l))

root = build_tree(pairs)
result = level_order(root)
if result:
    print(' '.join(result))
else:
    print('null')
```

---

**OD备考提示**：
- **模拟题重在理解规则**：本题看似树结构，实际是模拟题。**先画图理清规则再写代码**，切忌一上来就写。
- **边界情况**：
  - 只有根节点
  - 所有节点都在同一深度（level=0）
  - 插入节点值与已有节点相等（跳过）
- **调试技巧**：插入完成后可加一个中序遍历验证 BST 性质，帮助发现错误。
- **层序遍历模板**：BFS 用队列（`collections.deque`），这是常数考点，务必熟记。
- 200分树的题目常考：建树 + 遍历 的组合，本题是典型代表。
