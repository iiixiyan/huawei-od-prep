# D20 链表高阶 — 6题

> 链表进阶操作：区间反转、K 组反转、去重、旋转、划分、多级链表展开。

---

## 1. 反转链表 II ✅
**来源**：[LeetCode](https://leetcode.cn/problems/reverse-linked-list-ii/)
**难度**：中等
**题目**：给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left
- 链表中节点数目为 `n`

- `1

**进阶：** 你可以使用一趟扫描完成反转吗？
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
**来源**：[LeetCode](https://leetcode.cn/problems/reverse-nodes-in-k-group/)
**难度**：困难
**题目**：给你链表的头节点 `head` ，每 `k`  *个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k`  *的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1：**
```
*
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```
**示例 2：**
```
*
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```
**提示：**

- 链表中的节点数目为 `n`

- `1

**进阶：**你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？
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
**来源**：[LeetCode](https://leetcode.cn/problems/sort-list/)
**难度**：中等
**题目**：给你链表的头结点 `head` ，请将其按 **升序**排列并返回**排序后的链表** 。

**示例 1：**
```
*
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```
**示例 2：**
```
*
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```
**示例 3：**
```
输入：head = []
输出：[]
```
**提示：**

- 链表中节点的数目在范围 `[0, 5 * 104]` 内

- `-105 5`

**进阶：**你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
**思路**：dummy + 双指针。prev 指向确定不重复的节点，cur 遍历检测重复。
**代码**：
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
## 4. 旋转链表 ✅
**来源**：[LeetCode](https://leetcode.cn/problems/rotate-list/)
**难度**：中等
**题目**：给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动 `k`  *个位置。

**示例 1：**
```
*
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
```
**示例 2：**
```
*
输入：head = [0,1,2], k = 4
输出：[2,0,1]
```
**提示：**

- 链表中节点的数目在范围 `[0, 500]` 内

- `-100 9`
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
**来源**：[LeetCode](https://leetcode.cn/problems/partition-list/)
**难度**：中等
**题目**：给你一个链表的头节点 `head` 和一个特定值* *`x` ，请你对链表进行分隔，使得所有 **小于**`x` 的节点都出现在**大于或等于**`x` 的节点之前。

你应当**保留** 两个分区中每个节点的初始相对位置。

**示例 1：**
```
*
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```
**示例 2：**
```
输入：head = [2,1], x = 2
输出：[1,2]
```
**提示：**

- 链表中节点的数目在范围 `[0, 200]` 内

- `-100
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
**来源**：[LeetCode](https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/)
**难度**：中等
**题目**：你会得到一个双链表，其中包含的节点有一个下一个指针、一个前一个指针和一个额外的 **子指针**。这个子指针可能指向一个单独的双向链表，也包含这些特殊的节点。这些子列表可以有一个或多个自己的子列表，以此类推，以生成如下面的示例所示的**多层数据结构**。

给定链表的头节点 head ，将链表**扁平化** ，以便所有节点都出现在单层双链表中。让 `curr` 是一个带有子列表的节点。子列表中的节点应该出现在**扁平化列表**中的 `curr` *之后**和 `curr.next`**之前** 。

返回 *扁平列表的 `head` 。列表中的节点必须将其 **所有** 子指针设置为 `null` 。*

**示例 1：**
```
*
输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：
```
**示例 2：**
```
*
输入：head = [1,2,null,3]
输出：[1,3,2]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：
```
**示例 3：**
```
输入：head = []
输出：[]
说明：输入中可能存在空列表。
```
**提示：**

- 节点数目不超过 `1000`

- `1 5`

**如何表示测试用例中的多级链表？**

以 **示例 1** 为例：

1---2---3---4---5---6--NULL
|
7---8---9---10--NULL
|
11--12--NULL

序列化其中的每一级之后：

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

合并所有序列化结果，并去除末尾的 null 。

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
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
