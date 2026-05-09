# Day 13 — 综合复习：栈 + 队列 + 链表混合题

## 今日目标
- 将本周学过的栈、队列、链表知识融会贯通
- 解决需要组合多种数据结构的综合题
- 培养「一题多解」的思维模式

---

## 📚 知识框架回顾

### 本周数据结构总览

```
        Week 2 — 线性数据结构
        ┌─────────────────────┐
        │                     │
    ┌───┴───┐          ┌─────┴────┐
    │ 栈    │          │  队列    │
    │ LIFO  │          │  FIFO    │
    ├───────┤          ├──────────┤
    │push   │          │append    │
    │pop    │          │popleft   │
    │stack[-1]│        │queue[0]  │
    └───┬───┘          └─────┬────┘
        │                     │
        └─────────┬───────────┘
                  │
          ┌───────┴───────┐
          │   链表        │
          │   ListNode    │
          ├───────────────┤
          │快慢指针       │
          │反转           │
          │dummy节点      │
          └───────────────┘
```

### 组合技：数据结构混合使用模式

| 组合模式 | 典型问题 | 关键思路 |
|---------|---------|---------|
| **栈 + 链表** | 括号匹配 + 链表遍历 | 用栈记录待匹配的括号位置 |
| **队列 + 链表** | 链表层序遍历 | BFS 队列处理链表节点 |
| **栈 + 队列** | 用栈实现队列 / 用队列实现栈 | 两个栈=队列，一个队列=栈 |
| **快慢指针 + 栈** | 链表回文判断 | 前半入栈，后半遍历对比 |

---

## 🧩 混合题 1：用栈实现队列

**LeetCode 232. Implement Queue using Stacks**

### 问题描述
用两个栈实现一个 FIFO 队列。

### 思路分析
两个栈分工：
- `input_stack`：入队时压入
- `output_stack`：出队时反转顺序

**核心思想**：当 output 栈为空时，将 input 栈全部弹出压入 output 栈，这样元素顺序就反转为 FIFO。

### 代码实现
```python
class MyQueue:
    def __init__(self):
        self.input = []   # 入队栈
        self.output = []  # 出队栈
    
    def push(self, x: int) -> None:
        self.input.append(x)
    
    def pop(self) -> int:
        self._transfer()
        return self.output.pop()
    
    def peek(self) -> int:
        self._transfer()
        return self.output[-1]
    
    def empty(self) -> bool:
        return not self.input and not self.output
    
    def _transfer(self):
        """将 input 栈的元素转移到 output 栈"""
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

# 使用示例
q = MyQueue()
q.push(1)    # input: [1], output: []
q.push(2)    # input: [1,2], output: []
q.peek()     # → 转移 → output: [2,1], 返回 1
q.pop()      # → 返回 1, output: [2]
q.empty()    # → False
```

**OD 高频考点**：华为 OD 笔试中常考「用栈实现队列」或「用队列实现栈」的实现题。

---

## 🧩 混合题 2：用队列实现栈

**LeetCode 225. Implement Stack using Queues**

### 问题描述
用两个队列实现一个 LIFO 栈。

### 思路分析
- 主队列 `q1` 存放元素
- 辅助队列 `q2` 用于反转顺序
- **关键是 push 操作**：新元素先入 q2，然后将 q1 全部移到 q2，最后交换 q1 和 q2

### 代码实现
```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self) -> int:
        return self.q1.popleft()
    
    def top(self) -> int:
        return self.q1[0]
    
    def empty(self) -> bool:
        return not self.q1
```

---

## 🧩 混合题 3：括号匹配（栈 + 哈希映射）

**LeetCode 20. Valid Parentheses**

### 问题描述
判断括号 `()`, `{}`, `[]` 是否正确闭合。

```python
def isValid(s: str) -> bool:
    # 括号映射
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for ch in s:
        if ch in mapping:  # 右括号
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:  # 左括号
            stack.append(ch)
    
    return not stack  # 栈为空说明全部匹配
```

---

## 🧩 混合题 4：链表中的下一个更大节点

**LeetCode 1019. Next Greater Node In Linked List**

### 问题描述
给定一个链表，返回每个节点在 **链表后续** 中第一个比它大的值，不存在则为 0。

### 思路分析
🚀 **链表遍历 + 单调栈**

1. 先将链表转为数组（方便索引定位）
2. 用递减单调栈处理数组
3. 栈中存索引，遇到更大值时依次弹出

```python
def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    # 链表转数组
    nums = []
    cur = head
    while cur:
        nums.append(cur.val)
        cur = cur.next
    
    n = len(nums)
    result = [0] * n
    stack = []  # 存索引，单调递减
    
    for i in range(n):
        # 当前值比栈顶索引对应的值大 → 弹出并更新结果
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

**复杂度分析**
- 时间复杂度：O(n)
- 空间复杂度：O(n)

---

## 🧩 混合题 5：设计浏览器历史记录

**LeetCode 1472. Design Browser History**

### 问题描述
实现支持前进和后退的浏览器历史记录。

### 思路分析
🚀 **双栈 or 链表**

**方案一：双栈**
```python
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  # 后退栈
        self.forward_stack = []    # 前进栈
    
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forward_stack.clear()  # 访问新页面清空前进
    
    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.forward_stack.append(self.history.pop())
            steps -= 1
        return self.history[-1]
    
    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.history.append(self.forward_stack.pop())
            steps -= 1
        return self.history[-1]
```

**方案二：双向链表（更适合本题）**
- 每个节点有 `prev` 和 `next` 指针
- `current` 指针指向当前页面
- `visit` 时清除当前之后的所有节点（断开 next）
- `back/forward` 沿着 `prev/next` 移动

---

## 📝 本周重点公式速查

### 栈操作
```python
stack = []           # 创建
stack.append(x)      # 入栈
stack.pop()          # 出栈
stack[-1]            # 栈顶
len(stack) == 0      # 判空
```

### 队列操作
```python
from collections import deque
q = deque()          # 创建
q.append(x)          # 入队（右端）
q.popleft()          # 出队（左端）
q[0]                 # 队首
len(q) == 0          # 判空
```

### 链表操作
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 快慢指针
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# 反转
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt

# dummy 节点
dummy = ListNode(0, head)
return dummy.next
```

---

## 💪 课后练习

| 题目 | 难度 | 推荐用时 | 涉及知识点 |
|------|------|---------|-----------|
| LeetCode 232. 用栈实现队列 | 🟢 简单 | 15min | 栈+队列 |
| LeetCode 225. 用队列实现栈 | 🟢 简单 | 15min | 队列+栈 |
| LeetCode 20. 有效的括号 | 🟢 简单 | 10min | 栈+哈希 |
| LeetCode 1019. 链表中的下一个更大节点 | 🟠 中等 | 20min | 链表+单调栈 |
| LeetCode 1472. 设计浏览器历史记录 | 🟠 中等 | 20min | 栈或链表 |
| LeetCode 143. 重排链表 | 🟠 中等 | 20min | 快慢指针+反转+合并 |

> **OD 高分策略**：混合题往往是一道题考察多个知识点，解题时先拆解成标准子问题，分步解决。
