# D20 链表高阶 — 6题

> 链表进阶操作：区间反转、K 组反转、去重、旋转、划分、多级链表展开。

---

## 1. 反转链表 II ✅
**Leetcode 92 · T150**

**问题**：反转链表中第 left 到第 right 个节点之间的部分。

**思路**：穿针引线法。找到 left 的前驱节点（prev），然后对区间内的节点执行头插法反转。先定位到 left 位置，然后逐个将后面的节点插入到 prev 之后。

```python
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    # 1. 走到 left 前一个节点
    for _ in range(left - 1):
        prev = prev.next
    # 2. 头插法反转 [left, right]
    cur = prev.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：头插法时 `cur.next` 指向 nxt 的下一个；`nxt.next = prev.next` 而不是 `cur`；使用 dummy 处理 left=1 的情况。

---

## 2. K 个一组反转链表 ✅
**Leetcode 25 · T150**

**问题**：每 k 个节点一组反转链表，不足 k 个不反转。

**思路**：先计算链表长度，分组反转。每组内用 prev/cur/nxt 三指针反转，组间用 tail 衔接。

```python
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # 计算长度
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(n // k):
        # 反转当前组 k 个节点
        cur = prev.next
        for _ in range(k - 1):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        # 移动 prev 到组尾（即反转后的最后一个节点）
        prev = cur

    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：每组反转后 prev 定位到 cur（反转前的第一个节点，反转后是最后一个）；头插法逻辑同反转链表 II；提前算长度避免额外遍历判断。

---

## 3. 删除排序链表中的重复元素 II ✅
**Leetcode 82 · T150**

**问题**：删除排序链表中所有重复的节点（不留任何重复值），只保留原始链表中没有重复出现的数字。

**思路**：dummy + 双指针。prev 指向确定不重复的节点，cur 遍历检测重复。

```python
def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    cur = head
    while cur:
        # 跳过重复节点
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        # 判断是否有重复
        if prev.next == cur:       # 无重复
            prev = prev.next
        else:                      # 有重复，跳过所有
            prev.next = cur.next
        cur = cur.next
    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：`prev.next == cur` 判断是否跳过（无重复时 prev 的下一个就是 cur）；有重复时 `prev.next = cur.next` 删除整段；注意 cur 最终移向 cur.next。

---

## 4. 旋转链表 ✅
**Leetcode 61 · T150**

**问题**：将链表每个节点向右移动 k 个位置。

**思路**：闭合成环再断开。先遍历求长度，将 k 取模。找到新头的前驱（第 n - k%n - 1 个节点），断开得到新头。

```python
def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    # 1. 求长度并找到尾节点
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1

    # 2. 连成环
    tail.next = head

    # 3. 找到新头的前驱 (n - k%n) 步
    k %= n
    steps = n - k
    prev = head
    for _ in range(steps - 1):
        prev = prev.next

    # 4. 断开
    new_head = prev.next
    prev.next = None
    return new_head
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：k 可能很大，需要对 n 取模；断开位置是第 n - k%n 个节点（从 0 开始计数）；空链表或单节点直接返回。

---

## 5. 分隔链表 ✅
**Leetcode 86 · T150**

**问题**：给定一个值 x，将链表划分，所有小于 x 的节点排在大于等于 x 的节点之前，保持原有相对顺序。

**思路**：双链表法。维护 small 链表和 large 链表，遍历原链表分别拼接，最后 small 尾接 large 头。

```python
def partition(head: ListNode, x: int) -> ListNode:
    small = ListNode(0)
    large = ListNode(0)
    p1, p2 = small, large

    while head:
        if head.val < x:
            p1.next = head
            p1 = p1.next
        else:
            p2.next = head
            p2 = p2.next
        head = head.next

    p2.next = None          # 防止大链表尾还指向原链表
    p1.next = large.next    # 小链表尾接大链表头
    return small.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：`p2.next = None` 防止成环（大链表最后一个节点可能还指向小链表节点）；small 和 large 都使用 dummy 节点；保持相对顺序（稳定划分）。

---

## 6. 扁平化多级双向链表 ✅
**Leetcode 430 · O**

**问题**：多级双向链表中，节点除了 next/prev 还有 child 指针。将链表扁平化，使所有节点出现在单一级别（child 变为 next）。

**思路**：DFS / 迭代。遇到有 child 的节点，将 child 链展平插入到当前节点和 next 之间。递归处理 child 子链表。

```python
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Node') -> 'Node':
    if not head:
        return head

    dummy = Node(0, None, head, None)
    stack = [head]
    prev = dummy

    while stack:
        cur = stack.pop()
        # 连接 prev <-> cur
        cur.prev = prev
        prev.next = cur

        # 先压 next（后出），再压 child（先出）
        if cur.next:
            stack.append(cur.next)
            cur.next = None        # 断开原 next
        if cur.child:
            stack.append(cur.child)
            cur.child = None       # 清空 child

        prev = cur

    dummy.next.prev = None
    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(n)（栈递归深度）

**易错点**：用栈时要先推 next 再推 child（child 需要先展开）；每个节点处理完要清空 child 指针；双向链表的 prev 指针也要正确连接。

---

## 📦 今日总结

| 题型 | 核心技巧 | 复杂度 |
|------|---------|--------|
| 反转链表 II | 头插法 / 穿针引线 | O(n) O(1) |
| K 个一组反转 | 分组头插 + 组间衔接 | O(n) O(1) |
| 删除重复 II | 双指针跳过重复段 | O(n) O(1) |
| 旋转链表 | 成环再断开 | O(n) O(1) |
| 分隔链表 | 双链表法 + 拼接 | O(n) O(1) |
| 扁平化多级链表 | 栈模拟 DFS / 递归 | O(n) O(n) |

> 💡 **链表高阶技巧**：
> 1. **头插法**：反转区间的通用方法，对 [left, right] 内每个节点依次插入到 left 前驱之后
> 2. **成环再断开**：旋转链表的核心思路，避免多次遍历
> 3. **双链表法**：对链表进行条件划分时，维护两条独立链表再拼接
> 4. **栈辅助 DFS**：处理多级结构时很有用，注意入栈顺序
