# Day 42: 周复习

## 📖 本周知识点总览

| 主题 | 核心算法 | 关键模板 | 题量 |
|------|----------|----------|------|
| 二分搜索 | 标准二分、边界查找、旋转数组 | lower_bound / upper_bound | 6 |
| 二分+排序 | 按值二分、链表归并、计数排序 | 答案二分模板 | 6 |
| 堆 | Top K、两堆中位数、贪心+堆 | heapq 操作 | 6 |
| 位运算 | 异或消除、位掩码、状态机 | i&(i-1), x^x=0 | 6 |
| 数学综合 | 快速幂、开平方、回文、共线 | 快速幂迭代 | 6 |
| OD 100分 | 模拟、前缀和、DFS、Manacher | 螺旋矩阵、Kadane | 6 |

## 🧩 刷题任务（混合复习 — 6题）

### 1. 二分搜索：搜索旋转数组 II（⭐⭐⭐）来源：T150

**题目**：搜索旋转排序数组 II，数组中存在重复元素。判断 target 是否存在于 nums 中。

**思路**：相比 Day 36 的旋转数组搜索，有重复元素时可能出现 `nums[left] == nums[mid] == nums[right]` 无法判断有序段的情况。此时只能 left++、right-- 缩小区间。

**代码**：
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        # 无法判断有序段，缩小范围
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False
```

### 2. 堆：前 K 个高频元素（⭐⭐）来源：T150 / O

**题目**：给定非空整数数组，返回出现频率前 k 高的元素。

**思路**：先用 Counter 统计频率，再用大小为 k 的最小堆。堆中存 (频率, 元素)，按频率排序。

**代码**：
```python
def topKFrequent(nums, k):
    from collections import Counter
    freq = Counter(nums)
    heap = []
    for num, cnt in freq.items():
        heapq.heappush(heap, (cnt, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]
```

### 3. 位运算：子集（⭐⭐）来源：T150 / O

**题目**：给定整数数组 nums，返回所有可能的子集（幂集）。

**思路**：用位掩码枚举。从 0 到 2ⁿ - 1，每个数的二进制位表示对应元素是否选取。

**代码**：
```python
def subsets(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask >> i & 1:
                subset.append(nums[i])
        res.append(subset)
    return res
```

### 4. 数学：快乐数（⭐）来源：L75 / T150

**题目**：判断一个数是不是快乐数。每次将数字替换为各位数字的平方和，最终能变成 1 则是快乐数，否则会进入循环。

**思路**：快慢指针检测循环。或者用哈希集合记录已经出现的数字。平方和运算：`sum(int(d)**2 for d in str(n))`。

**代码**：
```python
def isHappy(n):
    def get_next(x):
        total = 0
        while x:
            total += (x % 10) ** 2
            x //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
```

### 5. OD 综合：任务调度（⭐⭐）来源：OD

**题目描述**：
有 N 个任务，每个任务有一个执行时间 t[i] 和一个优先级 p[i]。系统采用时间片轮转调度，时间片大小为 1。每次选择优先级最高的任务执行一个时间片，同优先级按序号从小到大。执行完一个时间片后，任务的优先级减 1。如果任务执行完毕（剩余时间为 0），则不再参与调度。输出所有任务执行完成的顺序（任务序号）。

**输入描述**：
第一行 N（任务数，≤ 1000）
接下来 N 行，每行两个整数 t[i] 和 p[i]（≤ 1000）

**输出描述**：
一行，N 个整数，表示调度完成的任务序号（从 1 开始）。

**示例输入**：
```
3
2 3
1 2
3 1
```

**示例输出**：
```
2 1 3
```

**思路**：用最大堆维护 (优先级, -序号, 剩余时间, 序号)。每次弹出优先级最高的任务执行一个时间片，更新优先级和剩余时间，如果还有剩余则重新入堆。

**代码**：
```python
def schedule_tasks(tasks):
    import heapq
    n = len(tasks)
    heap = []
    for i, (t, p) in enumerate(tasks):
        # 最大堆用负数优先级，序号小优先用 -i（序号越小越优先）
        heapq.heappush(heap, (-p, i, t))
    res = []
    while heap:
        neg_p, idx, remain = heapq.heappop(heap)
        p = -neg_p
        remain -= 1
        if remain == 0:
            res.append(idx + 1)  # 1-indexed
        else:
            # 优先级减1
            heapq.heappush(heap, (-(p - 1), idx, remain))
    return res

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    tasks = []
    idx = 1
    for _ in range(n):
        t = int(data[idx])
        p = int(data[idx + 1])
        tasks.append((t, p))
        idx += 2
    res = schedule_tasks(tasks)
    print(' '.join(map(str, res)))
```

### 6. 综合：寻找重复数（⭐⭐⭐⭐）来源：T150

**题目**：给定包含 n+1 个整数的数组，每个整数都在 [1, n] 范围内。只有一个数字重复出现（可能多次），找出这个重复的数字。不能修改原数组，只能使用 O(1) 额外空间。

**思路**：把数组看成链表，值映射为索引。因为有重复数字，所以有环，用 Floyd 判环法（快慢指针）找环入口。

**代码**：
```python
def findDuplicate(nums):
    # 快慢指针找相遇点
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # 找环入口
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```

## 🧪 小测验（10题）

1. 二分查找中，`while left < right` 和 `while left <= right` 有什么区别？
2. 旋转数组搜索时，如何判断 mid 在左段还是右段？
3. 堆排序的时间复杂度和空间复杂度分别是多少？
4. 什么情况下用最大堆模拟最小堆？Python 里如何实现？
5. 异或运算有哪些性质？举出两个应用场景。
6. `x & (x - 1)` 的作用是什么？`x & -x` 呢？
7. 求 x 的 n 次幂，时间复杂度能做到多少？如何实现？
8. 阶乘尾随零的个数如何计算？为什么只数因子 5 就够了？
9. 快慢指针可以解决哪些问题？列举至少 3 个。
10. 如何判断两个线段（或三个点）是否共线？

**答案**：
1. `left < right` 退出时 left==right，用于找边界；`left <= right` 退出时 left>right，用于精确查找
2. 比较 nums[mid] 和 nums[left]：若 nums[left] ≤ nums[mid] 则在左段，否则在右段
3. 时间 O(n log n)，空间 O(1)（原地建堆）或 O(n)（辅助数组）
4. 需要找第 K 个最小时用最大堆（因为堆顶是门槛）。Python 中存 `-val` 来模拟
5. a^a=0, a^0=a，a^b^a=b（交换律）。应用：找出现奇数次的数、简单加密
6. `x & (x-1)` 去掉最低位 1；`x & -x` 取最低位 1 的值
7. O(log n)，用快速幂（二进制分解）
8. 每 5 个数有一个因子 5，每 25 个数多一个… 因子 2 远多于 5，所以只数 5
9. 判环（链表环）、找中点、找重复数（Floyd）、快乐数检测
10. 计算斜率（最简分数）或叉积：(x2-x1)*(y3-y1) == (x3-x1)*(y2-y1)

## 📝 总结
- 本周覆盖了**二分搜索**、**堆**、**位运算**、**数学**和**OD 100分实战**五大模块
- 核心模板要背熟：lower_bound / upper_bound、快速幂、堆操作、位运算技巧
- OD 100分题注重**模拟能力**和**输入输出处理**，多练自然有感觉
- **快慢指针**和**Floyd 判环**是跨主题的通用技巧
- 每天 6 题，持之以恒，下周进入 Week 7！
