# Day 22 — Heap / Priority Queue（堆 / 优先队列）

## 📌 今日重点
- 堆（小顶堆 / 大顶堆）的模板与 API 使用
- 多路归并思想
- Top-K 问题：堆排 vs 快速选择
- 贪心 + 堆的复合题型

---

## 1. 堆的核心模板（Java）

```java
// 小顶堆（默认）
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// 大顶堆
PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

// 自定义对象
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]); // 按第一个元素小顶堆

// 常用操作
pq.offer(val);    // 入堆 O(logk)
pq.poll();        // 出堆 O(logk)
pq.peek();        // 查看堆顶 O(1)
pq.size();
```

### 多路归并框架
```java
// 多个有序数组合并成一个大顶堆/小顶堆
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
for (int i = 0; i < lists.length; i++) {
    if (lists[i] != null) pq.offer(new int[]{lists[i].val, i});
}
while (!pq.isEmpty()) {
    int[] cur = pq.poll();
    // 处理 cur[0]
    if (next != null) pq.offer(new int[]{next.val, idx});
}
```

---

## 2. 高频题型与题解

### 🔹 数组中的第 K 个最大元素（215. Kth Largest Element）
| 方法 | 时间复杂度 | 空间 |
|------|-----------|------|
| 堆排（大小为k的小顶堆） | O(n log k) | O(k) |
| 快速选择（Quick Select） | O(n) avg / O(n²) worst | O(1) |

**堆解法思路**：维护大小为 k 的小顶堆，遍历数组时入堆；堆大小超过 k 就 poll。最后堆顶就是第 k 大的元素。

```java
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    for (int num : nums) {
        minHeap.offer(num);
        if (minHeap.size() > k) minHeap.poll();
    }
    return minHeap.peek();
}
```

**快速选择（笔试更优）**：
```java
public int findKthLargest(int[] nums, int k) {
    int n = nums.length;
    int left = 0, right = n - 1;
    while (left <= right) {
        int pivot = partition(nums, left, right);
        if (pivot == n - k) return nums[pivot];
        else if (pivot < n - k) left = pivot + 1;
        else right = pivot - 1;
    }
    return -1;
}

private int partition(int[] nums, int left, int right) {
    int pivot = nums[right];
    int i = left;
    for (int j = left; j < right; j++) {
        if (nums[j] <= pivot) swap(nums, i++, j);
    }
    swap(nums, i, right);
    return i;
}
```

### 🔹 无限集中的最小数字（2336. Smallest Number in Infinite Set）
**思路**：小顶堆 + 哈希集合（记录已加入的元素）
- 用一个变量 `current` 指向当前最小的未被取出的正整数
- 被 pop 后，current++；被 addBack 时，如果元素小于 current 且不在堆中，入堆

```java
class SmallestInfiniteSet {
    PriorityQueue<Integer> heap;
    Set<Integer> set;
    int current = 1;

    public SmallestInfiniteSet() {
        heap = new PriorityQueue<>();
        set = new HashSet<>();
    }

    public int popSmallest() {
        if (!heap.isEmpty()) {
            int val = heap.poll();
            set.remove(val);
            return val;
        }
        return current++;
    }

    public void addBack(int num) {
        if (num < current && !set.contains(num)) {
            heap.offer(num);
            set.add(num);
        }
    }
}
```

### 🔹 最大子序列的分数（2542. Maximum Subsequence Score）
**思路**：排序 + 小顶堆（经典贪心 + 堆组合）
- 将两个数组绑定，按 nums2 降序排列
- 遍历时维护大小为 k 的小顶堆（存 nums1 值），同时维护 sum
- 每次当堆满 k 个时，用 `sum * nums2[i]` 更新答案

```java
public long maxScore(int[] nums1, int[] nums2, int k) {
    int n = nums1.length;
    int[][] pairs = new int[n][2];
    for (int i = 0; i < n; i++) {
        pairs[i] = new int[]{nums1[i], nums2[i]};
    }
    Arrays.sort(pairs, (a, b) -> b[1] - a[1]); // 按 nums2 降序

    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    long sum = 0, ans = 0;
    for (int[] p : pairs) {
        minHeap.offer(p[0]);
        sum += p[0];
        if (minHeap.size() > k) sum -= minHeap.poll();
        if (minHeap.size() == k) ans = Math.max(ans, sum * p[1]);
    }
    return ans;
}
```

### 🔹 K 名工人最低成本（857. Minimum Cost to Hire K Workers）
**思路**：按 wage/quality 比例排序 + 大顶堆（存 quality）
- 每个工人有 "单位质量工资比" = wage[i] / quality[i]
- 按比例升序排序
- 遍历时取 quality 最大的 k 个（用大顶堆），保证总 quality 最小，再用当前比例计算总工资

```java
public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
    int n = quality.length;
    double[][] workers = new double[n][2];
    for (int i = 0; i < n; i++) {
        workers[i] = new double[]{(double) wage[i] / quality[i], (double) quality[i]};
    }
    Arrays.sort(workers, (a, b) -> Double.compare(a[0], b[0]));

    PriorityQueue<Double> maxHeap = new PriorityQueue<>((a, b) -> Double.compare(b, a));
    double sumQ = 0, ans = Double.MAX_VALUE;
    for (double[] w : workers) {
        sumQ += w[1];
        maxHeap.offer(w[1]);
        if (maxHeap.size() > k) sumQ -= maxHeap.poll();
        if (maxHeap.size() == k) ans = Math.min(ans, sumQ * w[0]);
    }
    return ans;
}
```

---

## 3. 华为 OD 常考堆的变形

| 题型 | 特点 |
|------|------|
| **Top-K 频率** | HashMap 统计频率 + 堆取 Top-K |
| **合并 K 个有序链表** | 多路归并，经典面试题 |
| **数据流的中位数** | 大顶堆 + 小顶堆（双堆） |
| **会议室 II** | 最小会议室数，按结束时间用小顶堆 |
| **K 个最接近的元素** | 堆 / 双指针 / 二分 |

---

## 4. 课后练习（LeetCode）

| 题目 | 难度 | 说明 |
|------|------|------|
| 215. Kth Largest Element | 🟡 中等 | 堆 / 快选 |
| 2336. Smallest Infinite Set | 🟡 中等 | 堆 + Set |
| 2542. Max Subsequence Score | 🟡 中等 | 排序 + 堆 |
| 857. Min Cost to Hire K Workers | 🔴 困难 | 比例排序 + 堆 |
| 347. Top K Frequent Elements | 🟡 中等 | 频率 + 堆 |
| 295. Find Median from Data Stream | 🔴 困难 | 双堆 |
| 253. Meeting Rooms II | 🟡 中等 | 区间 + 堆 |

---

## ⏱ 今日建议
- **先掌握模板**：PriorityQueue 的 4 种构造方式
- **Top-K 首选堆**：n log k 足够应对笔试
- **贪心 + 堆 = 高频**：先排序再堆（Day22 的 2542/857 都是这个套路）
- **双堆技巧**：295 数据流中位数必考
