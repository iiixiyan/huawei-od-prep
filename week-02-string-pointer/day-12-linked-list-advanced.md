# Day 12 — Linked List 进阶：反转与孪生和

## 今日目标
- 掌握链表反转的迭代和递归实现
- 学会「快慢指针+反转」组合技巧
- 解决链表孪生和问题

---

## 📚 知识点：链表反转

### 为什么反转很重要？
反转是链表操作的 **核心基本功**，很多复杂链表问题都需要反转作为子步骤：
- 回文链表判断 ← 反转后半
- 重排链表 ← 反转后半
- 孪生和 ← 反转后半
- K 个一组翻转链表 ← 多次反转

### 反转的两种实现

#### 方法一：迭代法（推荐，面试首选）
```
思路：用三个指针 prev, cur, next 遍历调整指向

步骤：
1. 保存 cur.next 到 next
2. 将 cur.next 指向 prev
3. prev 前移到 cur
4. cur 前移到 next

初始: null → 1 → 2 → 3 → 4 → null
      prev  cur  next
      
最终: null ← 1 ← 2 ← 3 ← 4 ← null
                                    prev  cur
```

#### 方法二：递归法（思路优雅，但栈空间 O(n)）
```
reverse(head) = reverse(head.next) 的最后一个节点
然后将 head 接到末尾
```

---

## 🧩 题目 1：反转链表

**LeetCode 206. Reverse Linked List**

### 问题描述
反转一个单链表。

**示例**
```
输入: head = [1,2,3,4,5]
输出: [5,4,3,2,1]

输入: head = [1,2]
输出: [2,1]

输入: head = []
输出: []
```

### 代码实现

#### 迭代法
```python
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    
    while cur:
        next_node = cur.next  # 保存下一个节点
        cur.next = prev       # 反转指针
        prev = cur            # prev 前移
        cur = next_node       # cur 前移
    
    return prev  # 新头节点
```

#### 递归法
```python
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # 空链表或只有一个节点
    if not head or not head.next:
        return head
    
    # 反转后续链表
    new_head = reverseList(head.next)
    
    # 将当前节点接到末尾
    head.next.next = head
    head.next = None
    
    return new_head
```

**复杂度分析**
| 方法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 迭代 | O(n) | O(1) ✅ |
| 递归 | O(n) | O(n) |

> **OD 建议**：熟练掌握迭代法，递归法作为进阶理解。

### 图解过程
```
迭代反转 [1, 2, 3, 4, 5]:

第0步: null ← 1 → 2 → 3 → 4 → 5 → null
       prev  cur

第1步: null ← 1   2 → 3 → 4 → 5 → null
              prev  cur

第2步: null ← 1 ← 2   3 → 4 → 5 → null
                    prev  cur

第3步: null ← 1 ← 2 ← 3   4 → 5 → null
                          prev  cur

第4步: null ← 1 ← 2 ← 3 ← 4   5 → null
                                prev  cur

第5步: null ← 1 ← 2 ← 3 ← 4 ← 5
                                      prev

返回 prev (5)
```

---

## 🧩 题目 2：链表最大孪生和

**LeetCode 2130. Maximum Twin Sum of a Linked List**

### 问题描述
在一个长度为 n 的链表中（n 为偶数），第 i 个节点和第 `(n-1-i)` 个节点互为 **孪生节点**。

孪生和 = 孪生节点值之和。求最大孪生和。

**示例**
```
输入: head = [5,4,2,1]
输出: 6
解释: 
  孪生对: (5,1)=6, (4,2)=6
  最大和 = 6

输入: head = [4,2,2,3]
输出: 7
解释:
  孪生对: (4,3)=7, (2,2)=4
  最大和 = 7

输入: head = [1,100000]
输出: 100001
```

### 思路分析
🚀 **快慢指针 + 反转后半 + 双指针求和**

三步法：
1. **快慢指针**：找到链表中间节点（前半尾/后半头）
2. **反转后半部分**：方便从两端向中间遍历
3. **双指针求和**：同时遍历前半和反转后的后半，记录最大值

### 图解
```
输入: [5, 4, 2, 1]

第1步：快慢指针找中点
  5 → 4 → 2 → 1
  s        f
  slow=4, fast=1 (前半: 5→4, 后半: 2→1)

第2步：反转后半
  后半: 2 → 1 → null → 反转后: 1 → 2 → null

第3步：双指针求和
  前半: 5 → 4
  后半: 1 → 2
  5+1=6, 4+2=6
  最大 = 6 ✅
```

### 代码实现
```python
def pairSum(head: Optional[ListNode]) -> int:
    # 第1步：快慢指针找中点（前半部分的末尾）
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow 现在是后半部分的起始节点
    
    # 第2步：反转后半部分
    prev = None
    cur = slow
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    second_half = prev  # 反转后的后半部分头
    
    # 第3步：双指针求最大孪生和
    max_sum = 0
    first = head
    second = second_half
    while second:  # 后半部分长度 == 前半部分长度
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next
    
    return max_sum
```

**复杂度分析**
- 时间复杂度：O(n)，三次遍历（找中点 + 反转 + 求和）
- 空间复杂度：O(1)，只用了几个指针

---

## 📝 链表反转的四大应用场景

| 场景 | 问题 | 核心操作 |
|------|------|---------|
| **全部反转** | 反转链表 | 全链表反转 |
| **部分反转** | 反转链表 II | 反转 [left, right] 区间 |
| **分段反转** | K 个一组翻转链表 | 按组多次反转 |
| **配合找中点** | 孪生和/回文/重排 | 反转后半 + 双指针 |

### 反转链表模板（迭代）
```python
def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

### 找中点+反转后半 组合模板
```python
def solve_with_reverse_second_half(head):
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
    
    # 3. 双指针操作
    first = head
    while second:
        # ... 处理 first 和 second
        first = first.next
        second = second.next
```

---

## 💪 课后练习

| 题目 | 难度 | 推荐用时 | 考察点 |
|------|------|---------|--------|
| LeetCode 206. 反转链表 | 🟢 简单 | 10min | 反转基础 |
| LeetCode 2130. 链表最大孪生和 | 🟠 中等 | 20min | 反转+双指针 |
| LeetCode 234. 回文链表 | 🟢 简单 | 15min | 反转后半+比较 |
| LeetCode 143. 重排链表 | 🟠 中等 | 20min | 反转后半+合并 |
| LeetCode 92. 反转链表 II | 🟠 中等 | 20min | 部分反转 |
| LeetCode 25. K 个一组翻转链表 | 🔴 困难 | 30min | 分段反转 |

### 易错提醒
1. ⚠️ 反转时 **先保存 next 再修改指针**，否则会丢失后续节点
2. ⚠️ 找中点时，快慢指针的终止条件 `while fast and fast.next`
3. ⚠️ 孪生和问题确保 n 为偶数，反转后半用 slow（不要用 dummy）

> **OD 高频指数**：⭐⭐⭐⭐⭐（链表反转是必考题，孪生和是近年新题热点）
