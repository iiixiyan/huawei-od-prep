# D21 周复习 — 栈·队列·链表

> 第三周复习日：混合刷题 + 迷你测验，巩固栈、队列、链表三章核心知识点。

---

## 📖 本周知识图谱

```
Week 3: 栈 → 队列 → 链表
├── D15 栈基础: 括号匹配、最小栈、逆波兰式
├── D16 栈进阶: 单调栈(接雨水、柱状图)、表达式
├── D17 队列+设计: 滑动窗口、设计类(循环队列/LRU)
├── D18 链表基础: 环检测、反转、合并、两数相加
├── D19 链表进阶: 重排、回文、深拷贝、奇偶链表
└── D20 链表高阶: K组反转、旋转、分区、扁平化
```

**核心思想速记**：
- **栈**：后进先出，适合括号、表达式求值、单调栈（找下一个更大/更小元素）
- **队列**：先进先出，适合 BFS、滑动窗口
- **链表**：画图！dummy 节点、快慢指针、反转三板斧

---

## 🧩 刷题任务（6题）

### 1. 有效的括号 ✅
**Leetcode 20 · T150** | 难度：⭐⭐ | 标签：栈

**思路**：遇到左括号入栈，遇到右括号检查栈顶是否匹配。最后栈为空则有效。

```python
def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

**复杂度**：O(n) 时间，O(n) 空间

---

### 2. 简化路径 ✅
**Leetcode 71 · T150** | 难度：⭐⭐ | 标签：栈

**思路**：以 `/` 分割路径，用栈处理各个部分。`..` 弹出栈顶，`.` 和空字符串忽略，其余入栈。最后用 `/` 拼接。

```python
def simplifyPath(path: str) -> str:
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)
```

**复杂度**：O(n) 时间，O(n) 空间

---

### 3. 滑动窗口最大值 ✅
**Leetcode 239 · T150** | 难度：⭐⭐⭐ | 标签：队列/单调队列

**思路**：维护单调递减双端队列（存索引）。窗口右移时：① 移除超出窗口左界的索引 ② 移除队尾小于当前值的索引 ③ 当前索引入队 ④ 窗口形成后取队首值。

```python
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()
    res = []
    for i, v in enumerate(nums):
        # 移除超出窗口的索引
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # 维护单调递减
        while dq and nums[dq[-1]] < v:
            dq.pop()
        dq.append(i)
        # 窗口形成后记录结果
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

**复杂度**：O(n) 时间，O(k) 空间

---

### 4. 合并 K 个升序链表 ✅
**Leetcode 23 · T150** | 难度：⭐⭐⭐ | 标签：链表/分治/堆

**思路**：用最小堆（优先队列）每次取最小值。将所有链表头入堆，每次弹出最小节点，将其 next 入堆。

```python
import heapq

def mergeKLists(lists: List[ListNode]) -> ListNode:
    dummy = cur = ListNode(0)
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))

    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

**复杂度**：O(N log k) 时间（N 总节点数，k 链表数），O(k) 空间

---

### 5. 删除链表的倒数第 N 个节点 ✅
**Leetcode 19 · T150** | 难度：⭐⭐ | 标签：链表/快慢指针

**思路**：快慢指针 + dummy。快指针先走 n 步，然后快慢一起走，快指针到末尾时慢指针指向待删节点的前驱。

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```

**复杂度**：O(n) 时间，O(1) 空间

---

### 6. 柱状图中最大的矩形 ✅
**Leetcode 84 · T150** | 难度：⭐⭐⭐ | 标签：单调栈

**思路**：单调递增栈。遍历每个柱子的高度，当当前高度小于栈顶高度时，以栈顶高度为矩形高，左右边界为栈中前一个索引和当前索引。

```python
def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    heights = [0] + heights + [0]  # 前后哨兵

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
```

**复杂度**：O(n) 时间，O(n) 空间

---

## 📝 迷你测验

### 选择题（每题 10 分，共 50 分）

**Q1**：以下哪种数据结构最适合实现浏览器的「后退」功能？
- A. 队列
- B. 栈 ✅
- C. 双端队列
- D. 链表

**Q2**：判断链表是否有环，最常用的技巧是？
- A. 递归
- B. 哈希表
- C. 快慢指针 ✅
- D. 双端队列

**Q3**：单调栈的核心应用场景是？
- A. 括号匹配
- B. 寻找下一个更大/更小元素 ✅
- C. 滑动窗口最大值
- D. 链表反转

**Q4**：以下哪个问题不适合用队列解决？
- A. BFS 层序遍历
- B. 滑动窗口
- C. 逆波兰表达式求值 ✅
- D. 打印机任务调度

**Q5**：删除链表头节点时，为什么推荐使用 dummy 节点？
- A. 加快运行速度
- B. 省去特殊判断头节点的逻辑 ✅
- C. 减少空间复杂度
- D. 防止成环

### 填空题（每题 10 分，共 30 分）

**Q6**：反转链表的核心代码 `cur.next = _____`（填 prev），然后 `prev, cur = cur, nxt`。

**Q7**：当快慢指针在环中相遇后，将慢指针移回 head，然后两指针每次各走 ___ 步，相遇处即环入口。（填 1）

**Q8**：用两个栈实现队列，`push` 操作直接入 stack1，`pop` 操作时如果 stack2 为空，则将 stack1 中所有元素 ___ 到 stack2 再 pop。（填 弹出并压入 / 转移）

### 代码填空题（20 分）

**Q9**：补全「反转链表」代码：
```python
def reverseList(head: ListNode) -> ListNode:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        _____________  # 反转指针 (填: cur.next = prev)
        prev = cur
        cur = nxt
    return prev
```

---

## 📊 本周进度自评

| 章节 | 掌握度 | 薄弱环节 |
|------|--------|---------|
| D15 栈基础 | ⭐⭐⭐⭐⭐ | — |
| D16 栈进阶 | ⭐⭐⭐⭐ | 柱状图题还需练 |
| D17 队列 | ⭐⭐⭐⭐ | LRU 设计细节 |
| D18 链表基础 | ⭐⭐⭐⭐⭐ | — |
| D19 链表进阶 | ⭐⭐⭐⭐ | 深拷贝易错 |
| D20 链表高阶 | ⭐⭐⭐ | K 组反转不够熟练 |

> 💡 **复习建议**：
> - 弱题标记 🔁，下周一回头重刷
> - 链表一定要画图！纸上跑一遍指针变化
> - 单调栈模板背熟：`while stack and nums[stack[-1]] > x: pop and update`
> - 队列设计题注意边界条件（空/满/单元素）
>
> **下周预告**：二叉树 🌲 — 前中后序遍历、层序、BST、最近公共祖先
