# Day 38: 树&DFS — 树的遍历 & 高度计算

## 📖 知识点
**树 DFS 核心**：
- **前序/中序/后序**：递归访问左右子树
- **二叉树高度**：`height = 1 + max(left_height, right_height)`
- **构建哈夫曼树**：每次选两个最小权值节点合并，新节点权值=和，放入集合中重复
- **三叉搜索树**：比较当前节点值，决定左/中/右子树方向
- **最富裕的小家庭**（家族树）：DFS 累加子节点到父节点权值

## 🧩 刷题任务

### 题目1：计算三叉搜索树的高度 (OD C卷/E卷 100分)
**难度**：⭐⭐
**题目描述**：
实现一个三叉搜索树，每个节点有三个子节点：left（值 < 当前节点值-500）、middle（|值-当前节点值| ≤ 500）、right（值 > 当前节点值+500）。依次插入给定序列中的整数，求最终树的高度（根节点高度为0）。

**输入**：
```
10 500 1000 200 600 1500
```
**输出**：
```
3
```

**思路分析**：
1. 定义节点类，包含 val, left, mid, right 指针
2. 插入规则：
   - 如果 `new_val < node.val - 500` → 进入 left
   - 如果 `new_val > node.val + 500` → 进入 right
   - 否则（|new_val - node.val| ≤ 500）→ 进入 middle
3. 递归插入，同时维护当前深度，更新全局最大深度
4. 根节点深度为0

**参考代码**：
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

class TriSearchTree:
    def __init__(self):
        self.root = None
        self.max_depth = 0

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        self._insert(self.root, val, 0)

    def _insert(self, node, val, depth):
        self.max_depth = max(self.max_depth, depth + 1)
        if val < node.val - 500:
            if node.left:
                self._insert(node.left, val, depth + 1)
            else:
                node.left = Node(val)
        elif val > node.val + 500:
            if node.right:
                self._insert(node.right, val, depth + 1)
            else:
                node.right = Node(val)
        else:
            if node.mid:
                self._insert(node.mid, val, depth + 1)
            else:
                node.mid = Node(val)

    def get_height(self):
        return self.max_depth

# 测试
nums = [10, 500, 1000, 200, 600, 1500]
tree = TriSearchTree()
for n in nums:
    tree.insert(n)
print(tree.get_height())  # 3
```

**OD备考提示**：关键在于理解插入规则的分支条件。高度从0开始计数。注意根节点插入时深度不变。

---

### 题目2：最富裕的小家庭 (OD 100分)
**难度**：⭐⭐
**题目描述**：
给定一棵家族树（用父节点编号表示），每个成员有个人财产值。一个小家庭定义为一个父节点及其所有直接子节点（不含孙子节点）。求所有小家庭中总财产的最大值。

**输入**：
```
6
1 2 3 4 5 6
1 2
1 3
2 4
2 5
3 6
```
第一行家庭成员数 N，第二行每人财产，后面 N-1 行表示父子关系。输出最大小家庭财产和。

**输出**：
```
15
```
（解释：节点2的小家庭=2+4+5=11，节点3的小家庭=3+6=9，节点1的小家庭=1+2+3=6，最大15？实际节点1的是1+2+3=6，节点2的是2+4+5=11，节点3的是3+6=9，最大11）

**思路分析**：
1. 构建邻接表存储每个节点的子节点列表
2. 遍历每个节点（作为父节点），累加其自身财产 + 所有直接子节点财产
3. 记录最大值
4. 注意：非叶节点和叶节点都要考虑，但叶节点的小家庭只有自己

**参考代码**：
```python
def max_family_wealth(n, wealth, relations):
    children = [[] for _ in range(n + 1)]
    for parent, child in relations:
        children[parent].append(child)
    ans = 0
    for i in range(1, n + 1):
        total = wealth[i - 1]  # 父节点自身
        for c in children[i]:
            total += wealth[c - 1]
        ans = max(ans, total)
    return ans

# 测试
n = 6
wealth = [1, 2, 3, 4, 5, 6]
relations = [(1,2),(1,3),(2,4),(2,5),(3,6)]
print(max_family_wealth(n, wealth, relations))  # 11
```

**OD备考提示**：`-1` 偏移是常见坑点，注意题目编号从1开始但数组从0开始。直接用 children 列表比建图更简单。

## 📝 今日小结
- 三叉搜索树：三种分支规则要记清
- 家族树/小家庭：DFS累加子节点权值
- 哈夫曼树：优先队列（heapq）取两个最小合并
