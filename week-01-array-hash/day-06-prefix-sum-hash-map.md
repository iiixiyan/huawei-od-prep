# Day 06: Prefix Sum + Hash Map

## 📖 知识点讲解

### 前缀和（Prefix Sum）

前缀和是一种预处理技巧，用于快速计算子数组的和。

```python
# 一维前缀和
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

# 子数组 [l, r] 的和 = prefix[r + 1] - prefix[l]
```

### 前缀和 + 哈希映射

当需要判断某个目标值时，常用哈希表缓存前缀和：

```python
# 常见模式：两数之和的变体
seen = {}  # 值 -> 索引
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### 矩阵转置与行列映射

```python
# 方阵转置
n = len(grid)
transposed = [[grid[j][i] for j in range(n)] for i in range(n)]
```

---

## 🧩 刷题任务

### 题目1：Find Pivot Index（寻找数组的中心下标）
**难度**：⭐
**题目描述**：
给你一个整数数组 `nums`，请找到"中心下标"——该下标左侧所有元素之和等于右侧所有元素之和。如果不存在，返回 -1。如果有多个，返回最左边的一个。

**思路分析**：
前缀和思想：
1. 先计算数组总和 `total`
2. 遍历数组，维护左侧和 `left_sum`
3. 右侧和 = `total - left_sum - nums[i]`
4. 如果 `left_sum == total - left_sum - nums[i]`，返回 i
5. 更新 `left_sum += nums[i]`

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        
        return -1
```

---

### 题目2：Find the Difference of Two Arrays（数组差集）
**难度**：⭐
**题目描述**：
给你两个下标从 0 开始的整数数组 `nums1` 和 `nums2`，请返回一个长度为 2 的列表 `answer`，其中：
- `answer[0]` 是 `nums1` 中所有**不在** `nums2` 中的不同元素
- `answer[1]` 是 `nums2` 中所有**不在** `nums1` 中的不同元素

**思路分析**：
集合（哈希表）运算：
1. 将两个数组转为集合去重
2. 用集合差集运算即可

- 时间复杂度：O(n + m)
- 空间复杂度：O(n + m)

**参考代码**：
```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return [list(set1 - set2), list(set2 - set1)]
```

---

### 题目3：Unique Number of Occurrences（独一无二的出现次数）
**难度**：⭐
**题目描述**：
给你一个整数数组 `arr`，如果数组中每个元素的出现次数都是**独一无二**的，就返回 `true`；否则返回 `false`。

**思路分析**：
1. 用哈希表统计每个元素的出现频次（`Counter`）
2. 用集合检查频次值是否有重复

- 时间复杂度：O(n)
- 空间复杂度：O(n)

**参考代码**：
```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        freq = Counter(arr)
        # 频次值的数量 == 不同频次的集合大小 → 没有重复频次
        return len(freq.values()) == len(set(freq.values()))
```

---

### 题目4：Equal Row and Column Pairs（相等行列对）
**难度**：⭐⭐
**题目描述**：
给你一个下标从 0 开始的 `n x n` 整数矩阵 `grid`，请返回满足 `grid[i]` 行和 `grid[:][j]` 列相等的数对 `(i, j)` 的数量。

**思路分析**：
哈希映射法：
1. 将每一行转为元组（tuple），存入哈希表计数
2. 将每一列也转为元组，在哈希表中查找匹配的行
3. 累加每个列元组对应的行计数

- 时间复杂度：O(n²)
- 空间复杂度：O(n²)

**参考代码**：
```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # 统计每一行出现的次数
        row_count = {}
        for i in range(n):
            row = tuple(grid[i])
            row_count[row] = row_count.get(row, 0) + 1
        
        # 统计每一列
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            if col in row_count:
                count += row_count[col]
        
        return count
```
