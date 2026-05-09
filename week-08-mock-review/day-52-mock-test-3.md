# Day 52 — 限时模考 #3 (200+200分，120分钟)

> ⏱ **模拟真实OD考试环境** | 总分：400分 | 时间：120分钟
> 
> 2 × 200分题 | 压力测试 | 最接近真实考试难度

---

## 考试规则

| 项目 | 说明 |
|------|------|
| 总题数 | 2题（每题200分） |
| 考试时间 | 120分钟 |
| 编程语言 | Python（推荐）/ Java / C++ |
| 输入方式 | 标准输入（stdin） |
| 输出方式 | 标准输出（stdout） |
| 评分方式 | 按隐藏测试用例通过比例给分 |
| 时间分配建议 | 每题50分钟 + 20分钟检查调试 |

---

## Problem 1: 最小覆盖子串 (200分)

### 题目描述

给定两个字符串 `s` 和 `t`。返回 `s` 中包含 `t` 中所有字符的最短子串。如果不存在这样的子串，返回空字符串 `""`。

**注意：**
- 如果存在多个最短子串，返回起始索引最小的那一个
- `t` 中可能包含重复字符，子串需包含相同数量的重复字符

### 输入格式

两行：
- 第一行：字符串 `s`（1 ≤ len(s) ≤ 10⁵）
- 第二行：字符串 `t`（1 ≤ len(t) ≤ 10⁵）

### 输出格式

一行字符串，表示最短覆盖子串。如果不存在，输出空行（即直接输出空字符串，不带空格）。

### 样例

```
输入:
ADOBECODEBANC
ABC

输出:
BANC

解释: "BANC" 包含 A、B、C 三个字符，长度为4
```

```
输入:
a
aa

输出:


解释: "a" 中只有一个 'a'，无法覆盖两个 'a'
```

```
输入:
ab
a

输出:
a
```

### 数据范围

| 参数 | 范围 |
|------|------|
| len(s) | 1 ≤ len ≤ 10⁵ |
| len(t) | 1 ≤ len ≤ 10⁵ |
| 字符集 | 大小写英文字母 + 数字（ASCII可见字符） |

### 解题思路

**滑动窗口（双指针）** O(n) 时间复杂度：

1. **统计需求**：用字典 `need` 统计 `t` 中每个字符的需求量
2. **滑动窗口**：维护 `left` 和 `right` 双指针
   - 右指针不断右移，扩展窗口，加入字符
   - 当窗口满足覆盖条件时，尝试左指针右移，缩小窗口
3. **覆盖条件**：窗口中每个字符的出现次数 ≥ `need` 中的需求量
4. **优化**：用 `need_len` 变量记录还需要匹配的不同字符数，避免每次都检查字典

### 参考代码

```python
from collections import Counter

def min_window(s, t):
    if len(s) < len(t):
        return ""
    
    need = Counter(t)
    need_len = len(need)  # 需要满足的不同字符种类数
    have = {}
    have_len = 0  # 当前已满足的种类数
    
    left = 0
    min_len = float('inf')
    result_left = 0
    
    for right, ch in enumerate(s):
        # 扩展窗口
        have[ch] = have.get(ch, 0) + 1
        
        if ch in need and have[ch] == need[ch]:
            have_len += 1
        
        # 尝试缩小窗口
        while have_len == need_len:
            # 更新最小窗口
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result_left = left
            
            left_ch = s[left]
            have[left_ch] -= 1
            
            if left_ch in need and have[left_ch] < need[left_ch]:
                have_len -= 1
            
            left += 1
    
    return s[result_left:result_left + min_len] if min_len != float('inf') else ""


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(min_window(s, t))
```

### 进阶解法：优化版（用数组代替字典，更快）

```python
def min_window_optimized(s, t):
    if len(s) < len(t):
        return ""
    
    # 使用长度为128的数组（ASCII字符）
    need = [0] * 128
    for ch in t:
        need[ord(ch)] += 1
    
    need_len = sum(1 for x in need if x > 0)
    window = [0] * 128
    have_len = 0
    
    left = 0
    min_len = float('inf')
    result_left = 0
    
    for right, ch in enumerate(s):
        idx = ord(ch)
        window[idx] += 1
        
        if need[idx] > 0 and window[idx] == need[idx]:
            have_len += 1
        
        while have_len == need_len:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result_left = left
            
            left_idx = ord(s[left])
            window[left_idx] -= 1
            if need[left_idx] > 0 and window[left_idx] < need[left_idx]:
                have_len -= 1
            left += 1
    
    return s[result_left:result_left + min_len] if min_len != float('inf') else ""
```

### 评分对照

| 测试用例类型 | 分值 | 说明 |
|-------------|------|------|
| t为s的子串 | 25分 | 直接匹配 |
| 需要重新排列 | 30分 | 字符乱序出现 |
| 含重复字符 | 30分 | t中有重复 |
| 不存在覆盖 | 25分 | 返回空串 |
| 相同长度 | 25分 | s=t，完全匹配 |
| 大字符串性能 | 30分 | s长度10⁵ |
| 多解选最左 | 35分 | 多个最短子串，选左起 |

---

## Problem 2: 二叉树中的最大路径和 (200分)

### 题目描述

**路径**被定义为一条从树中任意节点出发，沿父节点-子节点连接，到达任意节点的序列。同一节点在一条路径序列中**至多出现一次**。该路径**至少包含一个节点**，且不一定经过根节点。

给定一棵二叉树的根节点 `root`，求其最大路径和（路径上所有节点值之和）。

### 输入格式

按层序遍历输入二叉树节点值，空节点用 `null` 表示。

第一行：一个整数 `n`，表示节点总数（按层序遍历序列长度）  
第二行：`n` 个值，用空格分隔，可以是整数或 `null`

### 输出格式

一个整数，表示最大路径和。

### 样例

```
输入:
7
1 2 3 null null 4 5

输出:
12

解释:
树结构:
     1
    / \
   2   3
      / \
     4   5

最大路径: 4 -> 3 -> 5 或 4 -> 3 -> 1 -> 2 (12)
```

```
输入:
7
-10 9 20 null null 15 7

输出:
42

解释:
   -10
   / \
  9   20
     /  \
    15   7

最大路径: 15 -> 20 -> 7 = 42
```

### 数据范围

| 参数 | 范围 |
|------|------|
| 节点数 n | 1 ≤ n ≤ 3×10⁴ |
| 节点值 | -1000 ≤ val ≤ 1000 |

### 解题思路

**二叉树DFS + 后序遍历**：

核心思想：对于每个节点，计算"包含该节点的最大路径和"，分两种情况：

1. **作为路径终点**（用于向上传递）：`max(左子树贡献, 右子树贡献, 0) + node.val`
   - 取 max(..., 0) 是因为负子树贡献可以舍弃
2. **作为路径最高点**（更新全局答案）：`左贡献 + 右贡献 + node.val`
   - 这里不取 max(..., 0)，因为左右可以同时走

**关键点**：
- 路径可以不走子树（贡献为0表示舍弃该子树）
- 路径不能分叉（不能既走左又走右再向上走）
- 用全局变量或非局部变量记录最大值

### 参考代码

```python
import sys
sys.setrecursionlimit(1000000)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values, n):
    """根据层序遍历序列构建二叉树"""
    if n == 0 or values[0] == 'null':
        return None
    
    nodes = []
    for v in values:
        if v == 'null':
            nodes.append(None)
        else:
            nodes.append(TreeNode(int(v)))
    
    # 连接父子关系
    i, j = 0, 1  # i为父节点索引，j为子节点索引
    while i < n and j < n:
        if nodes[i] is not None:
            if j < n:
                nodes[i].left = nodes[j]
                j += 1
            if j < n:
                nodes[i].right = nodes[j]
                j += 1
        i += 1
    
    return nodes[0]


def max_path_sum(root):
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # 后序遍历：先计算左右子树
        left_gain = max(dfs(node.left), 0)   # 舍弃负增益
        right_gain = max(dfs(node.right), 0)
        
        # 以当前节点为最高点的路径和
        current_path = node.val + left_gain + right_gain
        
        # 更新全局最大值
        max_sum = max(max_sum, current_path)
        
        # 返回给父节点的贡献（只能选一条分支）
        return node.val + max(left_gain, right_gain)
    
    dfs(root)
    return max_sum


if __name__ == "__main__":
    n = int(input().strip())
    values = input().strip().split()
    
    root = build_tree(values, n)
    print(max_path_sum(root))
```

### 核心算法图解

```
        节点X
        /   \
   左子树   右子树
   (贡献)   (贡献)

对于节点X：
  - 经过X的最大路径 = left_gain + X.val + right_gain  (更新全局)
  - 给父节点的贡献 = X.val + max(left_gain, right_gain)  (向上传递)
  
其中 left_gain = max(dfs(左子树), 0)  -- 负数舍弃
```

### 评分对照

| 测试用例类型 | 分值 | 说明 |
|-------------|------|------|
| 单节点 | 20分 | 只有根节点 |
| 全正数 | 25分 | 所有节点值 > 0 |
| 全负数 | 25分 | 所有节点值 < 0，选最大值 |
| 混合正负 | 30分 | 一般情况 |
| 线性树 | 25分 | 退化为链表 |
| 完全二叉树 | 25分 | 标准形状 |
| 大数/复杂 | 25分 | n=30000，多种形状 |
| 建树正确性 | 25分 | 层序遍历建树是否正确 |

---

## 答案速查

### Problem 1 核心测试用例

| s | t | 预期输出 |
|---|----|---------|
| `a` | `a` | `a` |
| `abc` | `ac` | `abc` |
| `aa` | `aa` | `aa` |
| `a` | `b` | `` |
| `ADOBECODEBANC` | `ABC` | `BANC` |
| `abcdef` | `xyz` | `` |
| `abccba` | `abc` | `abc` (或 `cba`，选最左) |

### Problem 2 核心测试用例

| 树结构 | 预期输出 |
|--------|---------|
| `[1]` | 1 |
| `[-5]` | -5 |
| `[1,2,3]` | 6 (2+1+3) |
| `[-10,9,20,null,null,15,7]` | 42 |
| `[-3]` | -3 |
| `[1,-2,-3,1,3,-2,null,-1]` | 3 |

---

## 自我评估清单

### 时间管理
- [ ] Problem 1 在 50 分钟内完成
- [ ] Problem 2 在 50 分钟内完成
- [ ] 留出 20 分钟调试和优化

### Problem 1 检查项
- [ ] 滑动窗口左闭右开还是左闭右闭确定清楚
- [ ] `have_len` 的更新逻辑正确（增加和减少条件对称）
- [ ] 重复字符的处理正确
- [ ] 多解时选了起始索引最小的
- [ ] 不存在时输出空字符串
- [ ] 时间复杂度 O(n) —— 不能 O(n²)

### Problem 2 检查项
- [ ] 递归深度问题：n=30000 时 Python 默认递归深度1000会栈溢出，需 `sys.setrecursionlimit`
- [ ] 最大路径和初始值设为 `float('-inf')` 而非 0（全负数情况）
- [ ] 左右子树的贡献取 `max(贡献, 0)` —— 舍弃负贡献
- [ ] 向上传递时只能选 `max(左, 右) + 当前值`，不能两边都走
- [ ] 建树时 `null` 的处理正确
- [ ] 层序遍历建树的索引关系：父节点 i，左子节点在 j，右子节点在 j+1

### 易错点总结

| 易错点 | 说明 | 如何避免 |
|--------|------|---------|
| 滑动窗口条件判断 | have[ch] == need[ch] 是相等判断，不是 >= | 初始化为0，递增计数 |
| 二叉树贡献传递 | 只能传单边最大值 | 画图理解：路径不能分叉 |
| 全负数树 | 最大路径是单个最大节点 | max_sum 初始化为 -inf |
| 层序建树 | null 节点占位但不分配孩子 | 用 i, j 双索引 |

### 得分记录

| 项目 | 满分 | 自评得分 |
|------|------|---------|
| Problem 1 | 200 | ____ |
| Problem 2 | 200 | ____ |
| **总分** | **400** | **____** |
| **目标** | **≥320** | **____** |

---

> 📌 **最后冲刺**：这是最难的模考。如果两个题目都做不完，重点关注：
> 1. 至少完成一题的最优解（拿满200分）
> 2. 另一题写暴力解法，争取部分分数（通常30-50%）
> 3. 留时间检查输入输出格式
>
> **OD考试中，200分题通常有多个子任务，部分正确也能拿分，不要轻易放弃！**
