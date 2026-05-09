# Day 38: 堆

## 📖 知识点
**堆模板**
```python
import heapq

# 最小堆（Python 默认）
heap = []
heapq.heappush(heap, val)
val = heapq.heappop(heap)

# 最大堆（取负数模拟）
heapq.heappush(heap, -val)
val = -heapq.heappop(heap)

# 前 K 个最小元素
heapq.nsmallest(k, iterable)
heapq.nlargest(k, iterable)
```

**堆的典型应用场景**：
1. **Top K 问题** → 维护大小为 K 的堆（求最大 K 个用最小堆，求最小 K 个用最大堆）
2. **数据流中位数** → 一个最大堆 + 一个最小堆，保持平衡
3. **合并 K 个有序链表** → 所有头节点入堆，每次弹出最小的
4. **多路归并** → 与合并 K 个有序链表类似
5. **贪心 + 堆** → 每次取最优解，然后加入新的候选

**技巧**：
- 需要自定义优先级时，存元组 `(priority, value)` 
- Python 的 heapq 不支持自定义比较器，可以用 `(priority, index, value)` 解决平局问题

## 🧩 刷题任务（6题）

### 1. 数组中的第K个最大元素（⭐⭐）来源：L75 / T150 / O
**思路**：维护大小为 K 的最小堆。遍历数组，当堆大小 < K 时直接入堆；否则若当前元素 > 堆顶，弹出堆顶并入堆新元素。最终堆顶就是第 K 大的元素。

**代码**：
```python
def findKthLargest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
```

### 2. 无限集中的最小数字（⭐⭐）来源：L75
**思路**：用一个最小堆存储当前集合中的数字，一个 visited 集合去重。初始化时把所有 1~1000 入堆。popSmallest 弹出堆顶；addBack 时如果数字不在 visited 中，入堆并标记。

**代码**：
```python
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)
        self.removed = set()

    def popSmallest(self):
        val = heapq.heappop(self.heap)
        self.removed.add(val)
        return val

    def addBack(self, num):
        if num in self.removed:
            self.removed.remove(num)
            heapq.heappush(self.heap, num)
```

### 3. 最大子序列的分数（⭐⭐⭐）来源：L75
**思路**：将两个数组按 nums2 降序配对。遍历时维持一个大小为 k 的最小堆存 nums1 的值，同时维护 sum1。对每个位置，堆满后计算分数 = sum1 * nums2[i]，取最大值。

**代码**：
```python
def maxScore(nums1, nums2, k):
    pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
    heap = []
    sum1 = 0
    res = 0
    for n1, n2 in pairs:
        heapq.heappush(heap, n1)
        sum1 += n1
        if len(heap) > k:
            sum1 -= heapq.heappop(heap)
        if len(heap) == k:
            res = max(res, sum1 * n2)
    return res
```

### 4. IPO（⭐⭐）来源：T150
**思路**：贪心 + 堆。先按 capital 排序项目。维护一个最大堆（存利润），把所有 capital ≤ w 的项目利润入堆。每次弹出最大利润的项目，w 增加。重复 k 次。

**代码**：
```python
def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    projects = sorted(zip(capital, profits))
    heap = []
    i = 0
    for _ in range(k):
        while i < n and projects[i][0] <= w:
            heapq.heappush(heap, -projects[i][1])
            i += 1
        if not heap:
            break
        w += -heapq.heappop(heap)
    return w
```

### 5. 查找和最小的K对数字（⭐⭐）来源：T150 / O
**思路**：多路归并。所有组合可以看作 nums1[i] + nums2[0] 的 i 条"链表"。每次取出最小的和，并将对应的 nums1[i] + nums2[j+1] 入堆。注意去重。

**代码**：
```python
def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []
    heap = []
    # 初始化：每个 nums1[i] + nums2[0]
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
    res = []
    while heap and len(res) < k:
        s, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return res
```

### 6. 数据流的中位数（⭐⭐⭐）来源：T150
**思路**：维护两个堆：最大堆（存左半部分）和最小堆（存右半部分）。保持两个堆的大小平衡（左堆比右堆多 0 或 1 个元素）。添加元素时先入左堆再调整到右堆，保持所有左堆元素 ≤ 右堆元素。

**代码**：
```python
class MedianFinder:
    def __init__(self):
        self.left = []   # 最大堆（存负数）
        self.right = []  # 最小堆

    def addNum(self, num):
        # 先入左堆（最大堆）
        heapq.heappush(self.left, -num)
        # 平衡：左堆最大 ≤ 右堆最小
        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        # 平衡大小：左堆最多比右堆多 1
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0
```

## 📝 总结
- **堆**擅长解决**动态 Top K** 和**流式数据**问题
- 求**最大** K 个元素 → 用**最小堆**（堆顶是门槛，只有比门槛大的才进来）
- 求**最小** K 个元素 → 用**最大堆**（Python 用负数模拟）
- **两个堆**模型可解决中位数、滑动窗口中间值等问题
- 贪心 + 堆的组合在面试中很常见（IPO、最大子序列分数）
