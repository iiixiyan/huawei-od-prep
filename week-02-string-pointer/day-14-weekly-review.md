# Day 14 — 周复习 + 小测

## 今日目标
- 系统回顾本周所有知识点和题型
- 通过小测检验掌握程度
- 查漏补缺，明确薄弱环节

---

## 📋 本周内容总览

| 天数 | 主题 | 核心题目 | 关键技巧 |
|------|------|---------|---------|
| Day 08 | **Stack 基础** | 移除星号、行星碰撞 | 栈模拟、碰撞处理 |
| Day 09 | **Stack 进阶** | 字符串解码 | 双栈处理嵌套 |
| Day 10 | **Queue** | 最近请求次数、Dota2 参议院 | 队列滑动窗口、循环投票 |
| Day 11 | **Linked List 基础** | 删除中间节点、奇偶链表 | 快慢指针、dummy 节点 |
| Day 12 | **Linked List 进阶** | 反转链表、最大孪生和 | 反转、反转+双指针 |
| Day 13 | **综合复习** | 混合题 | 多数据结构组合 |

### 本周重点技巧索引
| 技巧 | 最佳实践题目 | 掌握要求 |
|------|-------------|---------|
| 🥇 栈模拟 | 移除星号、有效括号 | ⭐ 必须掌握 |
| 🥇 单调栈 | 行星碰撞、下一个更大节点 | ⭐ 必须掌握 |
| 🥇 双栈嵌套 | 字符串解码 | ⭐ 必须掌握 |
| 🥇 队列滑动窗口 | 最近的请求次数 | ⭐ 必须掌握 |
| 🥇 快慢指针 | 中间节点、孪生和 | ⭐ 必须掌握 |
| 🥇 链表反转 | 反转链表 | ⭐ 必须掌握 |
| 🥈 双栈实现队列 | 用栈实现队列 | ⭐ 推荐掌握 |
| 🥈 单调队列 | 滑动窗口最大值（扩展） | 🔵 进阶 |

---

## 📝 本周小测（20 题）

### 第一部分：概念题（每题 5 分，共 30 分）

**Q1.** 栈的英文名称和核心特性是什么？
<details>
<summary>查看答案</summary>
Stack（栈），LIFO（Last In, First Out，后进先出）。
</details>

**Q2.** Python 中实现队列最推荐的数据结构是什么？
<details>
<summary>查看答案</summary>
`collections.deque`，两端操作均为 O(1) 时间复杂度。
</details>

**Q3.** 快慢指针中，快指针每次走几步？慢指针每次走几步？
<details>
<summary>查看答案</summary>
快指针每次走 2 步，慢指针每次走 1 步。当快指针到达末尾时，慢指针指向中间节点。
</details>

**Q4.** 链表反转迭代法中，需要几个指针？分别是什么？
<details>
<summary>查看答案</summary>
3 个指针：`prev`（前驱，初始为 None）、`cur`（当前节点，初始为 head）、`next_node`（保存 cur.next 防止丢失）。
</details>

**Q5.** 什么是 dummy 节点？为什么要使用它？
<details>
<summary>查看答案</summary>
dummy 是一个虚拟头节点，指向真正的头节点。使用它简化头节点可能被删除/修改时的边界处理。`dummy = ListNode(0, head)`，最后返回 `dummy.next`。
</details>

**Q6.** 用两个栈实现队列时，两个栈分别叫什么？pop 操作的核心逻辑是什么？
<details>
<summary>查看答案</summary>
input_stack（入队栈）和 output_stack（出队栈）。pop 时，如果 output 为空，将 input 所有元素弹出并压入 output（反转顺序），再从 output 弹出。
</details>

---

### 第二部分：代码填空（每题 10 分，共 40 分）

**Q7.** 补全「从字符串中移除星号」的代码
```python
def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == '*':
            ______  # 请填空
        else:
            ______  # 请填空
    return ''.join(stack)
```
<details>
<summary>查看答案</summary>
<code>stack.pop()</code> 和 <code>stack.append(ch)</code>。遇到星号移除栈顶，否则入栈。
</details>

**Q8.** 补全「快慢指针找中点」的代码
```python
def find_middle(head):
    slow = head
    fast = head
    while ______ and ______:  # 请填空
        slow = slow.next
        fast = fast.next.next
    return slow
```
<details>
<summary>查看答案</summary>
<code>fast</code> 和 <code>fast.next</code>。当 fast 或 fast.next 为 None 时停止。
</details>

**Q9.** 补全「链表反转（迭代）」的代码
```python
def reverseList(head):
    prev = None
    cur = head
    while cur:
        next_node = ______  # 请填空
        cur.next = ______   # 请填空
        prev = cur
        cur = next_node
    return ______           # 请填空
```
<details>
<summary>查看答案</summary>
<code>cur.next</code>（保存下一个），<code>prev</code>（反转指向），<code>prev</code>（返回新头）。
</details>

**Q10.** 补全「行星碰撞」的核心逻辑
```python
def asteroidCollision(asteroids):
    stack = []
    for ast in asteroids:
        if ast > 0:
            ______  # 请填空
        else:
            while stack and ______ and ______:  # 请填空
                stack.pop()
            if stack and stack[-1] > 0 and stack[-1] == -ast:
                ______  # 请填空
            elif not stack or stack[-1] < 0:
                ______  # 请填空
    return stack
```
<details>
<summary>查看答案</summary>
<code>stack.append(ast)</code>（右行入栈），<code>stack[-1] > 0</code>（栈顶右行）和 <code>stack[-1] < -ast</code>（栈顶更小），<code>stack.pop()</code>（相等都毁灭），<code>stack.append(ast)</code>（左行入栈）。
</details>

---

### 第三部分：算法分析（每题 10 分，共 20 分）

**Q11.** 以下代码的时间复杂度和空间复杂度分别是多少？
```python
def decodeString(s: str) -> str:
    stack = []
    for ch in s:
        if ch == ']':
            # 解码过程...
            pass
        else:
            stack.append(ch)
    return ''.join(stack)
```
<details>
<summary>查看答案</summary>
时间复杂度：O(n) 或 O(S)，其中 n 是输入长度，S 是解码后长度（严格来说是 O(S) 因为输出可能比输入长很多）。
空间复杂度：O(S)，栈中可能存储解码后的全部字符。
</details>

**Q12.** 用两个栈实现队列，push 操作 O(1)，pop 操作均摊 O(1)。解释为什么 pop 是均摊 O(1) 而不是最坏 O(1)？
<details>
<summary>查看答案</summary>
因为当 output 栈为空时，pop 需要将 input 栈的全部 n 个元素转移到 output 栈，这一次操作是 O(n)。但之后连续 n-1 次 pop 都是 O(1)。所以均摊下来，每个元素的出队成本是 O(1)。这就是**均摊分析（Amortized Analysis）**的思想。
</details>

---

### 第四部分：综合题（10 分）

**Q13.** 设计一个算法判断链表是否为回文链表。要求：时间复杂度 O(n)，空间复杂度 O(1)。

<details>
<summary>思路与解答</summary>

**思路：快慢指针 + 反转后半**

1. 快慢指针找到链表中间节点（slow）
2. 反转以 slow 为头的后半部分
3. 双指针遍历前半部分和反转后的后半部分，比较值是否相等
4. 恢复链表（可选）

```python
def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return True
    
    # 1. 快慢指针找中点
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2. 反转后半
    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    second = prev
    
    # 3. 双指针比较
    first = head
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True
```
</details>

---

### 第五部分：附加挑战题（选做，每题额外 10 分）

**Q14.** 链表排序 — LeetCode 148. Sort List
<details>
<summary>提示</summary>
归并排序思路：快慢指针找中点 → 分割为两个链表 → 递归排序 → 合并有序链表。时间复杂度 O(n log n)，空间复杂度 O(log n)（递归栈）。
</details>

**Q15.** LFU 缓存 — LeetCode 460. LFU Cache
<details>
<summary>提示</summary>
双哈希表 + 双向链表。每个频率维护一个双向链表，用哈希表跟踪节点位置。OD 中不常考，但考察综合数据结构设计能力。
</details>

---

## ✅ 自我评估表

| 题目 | 能独立 AC | 看提示后 AC | 不理解 |
|------|:---------:|:-----------:|:------:|
| 移除星号 (Day 08) | ☐ | ☐ | ☐ |
| 行星碰撞 (Day 08) | ☐ | ☐ | ☐ |
| 字符串解码 (Day 09) | ☐ | ☐ | ☐ |
| 最近请求次数 (Day 10) | ☐ | ☐ | ☐ |
| Dota2 参议院 (Day 10) | ☐ | ☐ | ☐ |
| 删除中间节点 (Day 11) | ☐ | ☐ | ☐ |
| 奇偶链表 (Day 11) | ☐ | ☐ | ☐ |
| 反转链表 (Day 12) | ☐ | ☐ | ☐ |
| 最大孪生和 (Day 12) | ☐ | ☐ | ☐ |
| 用栈实现队列 (Day 13) | ☐ | ☐ | ☐ |
| 有效括号 (Day 13) | ☐ | ☐ | ☐ |

> **评估标准**：
> - 🔥 10+ 题能独立 AC → 本周内容掌握扎实，可以进入下周
> - 🔥 6-9 题能独立 AC → 基本掌握，薄弱环节需要复习
> - 🔥 < 6 题能独立 AC → 建议重做 Day 08-13 的题目

---

## 📅 下周预告：Week 3 — 二叉树

### 下周三部曲
| 天数 | 主题 | 核心内容 |
|------|------|---------|
| Day 15-16 | **二叉树基础** | 前/中/后序遍历、层序遍历 |
| Day 17-18 | **二叉搜索树** | BST 验证、查找、插入、删除 |
| Day 19-20 | **二叉树进阶** | 最近公共祖先、序列化、路径和 |
| Day 21 | **周复习+小测** | 二叉树综合测试 |

### 预习建议
- 理解递归遍历二叉树的基本框架
- 尝试手写前序、中序、后序的递归代码
- 了解 BFS（层序遍历）的基本思想

---

> 🌟 **备考寄语**：Week 2 的栈、队列、链表是华为 OD 机考的 **必考内容**。这些数据结构看似简单，但组合起来可以解决非常复杂的实际问题。熟练掌握后，你的编码能力会上一个台阶。再接再厉！💪
