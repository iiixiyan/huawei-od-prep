# Day 11 — Linked List 基础

## 今日目标
- 掌握链表（Linked List）的基本结构和遍历
- 熟练使用 **快慢指针** 技巧
- 学会链表节点的删除和拆分操作

---

## 📚 知识点：链表基础

### 链表节点定义
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 节点值
        self.next = next    # 指向下一个节点
```

### 链表 vs 数组

| 操作 | 数组 | 链表 |
|------|------|------|
| 随机访问 | O(1) ✅ | O(n) ❌ |
| 插入/删除头部 | O(n) ❌ | O(1) ✅ |
| 插入/删除尾部 | O(1)* | O(1)** |
| 空间 | 连续内存 | 分散内存+指针开销 |

*均摊复杂度，**需维护尾指针

### 链表操作核心技巧

#### 快慢指针（Floyd's Algorithm）
```python
slow = head
fast = head

# 快指针每次走两步，慢指针每次走一步
while fast and fast.next:
    slow = slow.next      # 慢指针走一步
    fast = fast.next.next # 快指针走两步
```

**快慢指针的经典用途：**
| 用途 | 条件 | 效果 |
|------|------|------|
| 找中点 | fast 到末尾 | slow 指向中间节点 |
| 判环 | fast 追上 slow | 有环 |
| 找环入口 | 相遇后从头再走 | 环的入口节点 |
| 找倒数第 k 个 | 快指针先走 k 步 | slow 指向目标 |

---

## 🧩 题目 1：删除链表的中间节点

**LeetCode 2095. Delete the Middle Node of a Linked List**

### 问题描述
给你一个链表的头节点 `head`，删除 **中间节点** 并返回修改后的链表头。

- n 个节点的链表，中间节点是第 `⌊n / 2⌋` 个节点（从 0 开始）

**示例**
```
输入: head = [1,3,4,7,1,2,6]
输出: [1,3,4,1,2,6]
解释: 中间节点是 7（索引 3 = ⌊7/2⌋），删除 7

输入: head = [1,2,3,4]
输出: [1,2,4]
解释: 中间节点是 3（索引 2 = ⌊4/2⌋）

输入: head = [2,1]
输出: [2]
解释: 中间节点是 1（索引 1 = ⌊2/2⌋）
```

### 思路分析
🚀 **快慢指针找中点 + 记录前驱**

步骤：
1. 用快慢指针找到中间节点的 **前一个节点**（pre_mid）
2. 将 `pre_mid.next = pre_mid.next.next` 跳过中间节点

找前驱的技巧：让慢指针从 **dummy 节点** 开始走，或者用 `prev` 指针跟踪。

### 代码实现
```python
def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None  # 只有一个节点或空，删除后为空
    
    # 快慢指针，dummy 节点让慢指针从「前一个节点」开始
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = head
    
    # fast 走到末尾时，slow 正好在中间节点的前一个
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 删除中间节点
    slow.next = slow.next.next
    
    return dummy.next
```

**复杂度分析**
- 时间复杂度：O(n)，一次遍历
- 空间复杂度：O(1)，只用了几个指针

---

## 🧩 题目 2：奇偶链表

**LeetCode 328. Odd Even Linked List**

### 问题描述
给定一个单链表，将所有索引为 **奇数** 的节点和 **偶数** 的节点分别排在一起。

- 第一个节点索引为奇数（1）
- 第二个节点索引为偶数（2）
- 奇偶分组后，偶数节点跟在所有奇数节点后面
- 保持相对顺序

**示例**
```
输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]
解释: 奇数索引: 1→3→5, 偶数索引: 2→4 → 合并

输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]
```

### 思路分析
🚀 **双指针拆链+合并**

1. 用两个指针 `odd` 和 `even` 分别遍历奇偶节点
2. 将奇数节点接到奇数链，偶数节点接到偶数链
3. 最后奇数链末尾指向偶数链头部

### 图解
```
初始: 1 → 2 → 3 → 4 → 5
odd=head(1), even=head.next(2), even_head=2

第1步: odd(1).next = odd.next.next = 3
       1 → 3 ... 2 → 4 → 5
       odd = 3
       even(2).next = even.next.next = 4
       2 → 4 → 5
       even = 4

第2步: odd(3).next = 5
       1 → 3 → 5
       odd = 5
       even(4).next = None
       2 → 4
       even = None → 结束

合并: odd(5).next = even_head(2)
      1 → 3 → 5 → 2 → 4
```

### 代码实现
```python
def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    
    odd = head                # 奇数节点指针
    even = head.next          # 偶数节点指针
    even_head = even          # 保存偶数链头
    
    while even and even.next:
        # 连接奇数节点
        odd.next = even.next
        odd = odd.next
        
        # 连接偶数节点
        even.next = odd.next
        even = even.next
    
    # 奇数链尾部指向偶数链头部
    odd.next = even_head
    
    return head
```

**复杂度分析**
- 时间复杂度：O(n)，一次遍历
- 空间复杂度：O(1)

---

## 📝 链表操作模板汇总

### 1. 遍历链表
```python
cur = head
while cur:
    print(cur.val)
    cur = cur.next
```

### 2. 使用 dummy 节点（虚拟头节点）
```python
dummy = ListNode(0)
dummy.next = head
# 操作 dummy.next ...
return dummy.next  # 即使 head 被修改也能正确返回
```

### 3. 快慢指针找中点
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # 奇数个返回中间，偶数个返回后一个中点
```

### 4. 找中点前驱（用于删除）
```python
def find_middle_prev(head):
    dummy = ListNode(0, head)
    slow, fast = dummy, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # 中间节点的前一个
```

---

## 💪 课后练习

| 题目 | 难度 | 推荐用时 | 考察点 |
|------|------|---------|--------|
| LeetCode 2095. 删除链表的中间节点 | 🟠 中等 | 15min | 快慢指针+删除 |
| LeetCode 328. 奇偶链表 | 🟠 中等 | 15min | 指针操作 |
| LeetCode 876. 链表的中间结点 | 🟢 简单 | 5min | 快慢指针基础 |
| LeetCode 203. 移除链表元素 | 🟢 简单 | 10min | dummy节点 |
| LeetCode 83. 删除排序链表中的重复元素 | 🟢 简单 | 10min | 链表遍历 |

> **OD 高频指数**：⭐⭐⭐⭐⭐（链表操作是基础必考，快慢指针是高频技巧）
