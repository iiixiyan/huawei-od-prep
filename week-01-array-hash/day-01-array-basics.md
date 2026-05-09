# Day 01: 数组基础操作

## 📖 知识点
**双指针原地操作**：在数组问题中，双指针技巧常用于原地修改数组，避免额外空间。两个指针从不同位置遍历，一个指向"当前写入位置"，另一个指向"当前读取位置"，在不使用额外数组的情况下完成元素删除、去重、合并等操作。

核心模式：
- **读写指针**：`slow` 指向已处理部分的末尾，`fast` 遍历整个数组
- **头尾指针**：左右夹逼，常用于有序数组的合并或交换
- **同向双指针**：两个指针同向移动，速度不同

## 🧩 刷题任务（6题）

### 1. 交替合并字符串（⭐）
**来源**：L75
**思路**：双指针分别遍历两个字符串，交替取字符拼接。当指针越界时，将剩余部分直接追加到结果末尾。
**代码**：
```python
def mergeAlternately(word1: str, word2: str) -> str:
    res = []
    i = j = 0
    m, n = len(word1), len(word2)
    while i < m or j < n:
        if i < m:
            res.append(word1[i])
            i += 1
        if j < n:
            res.append(word2[j])
            j += 1
    return "".join(res)

# 一行写法（Python trick，面试不推荐）
# def mergeAlternately(word1: str, word2: str) -> str:
#     from itertools import zip_longest
#     return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
```

### 2. 合并两个有序数组（⭐⭐）
**来源**：T150
**思路**：从后往前遍历，将较大的元素放到 nums1 末尾。三个指针：`p1=nums1有效末尾`、`p2=nums2末尾`、`p=合并后的末尾`。避免了从前往后需要移动大量元素的 O(n²) 问题。
**代码**：
```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead."""
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    # 如果 nums2 还有剩余，复制过去
    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]
```

### 3. 移除元素（⭐⭐）
**来源**：T150
**思路**：快慢指针。`slow` 指向下一个待写入位置，`fast` 遍历数组。当 `nums[fast] != val` 时，将 `nums[fast]` 复制到 `nums[slow]`，并 `slow += 1`。最终 `slow` 即为新数组长度。
**代码**：
```python
def removeElement(nums: list[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 4. 删除有序数组中的重复项（⭐⭐）
**来源**：T150
**思路**：快慢指针。`slow` 指向已去重部分的末尾，`fast` 遍历。当 `nums[fast] != nums[slow-1]` 时，说明遇到新元素，写入 `nums[slow]` 并移动 `slow`。因为数组已有序，相同元素必然相邻。
**代码**：
```python
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 1  # 第一个元素默认保留
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 5. 删除有序数组中的重复项 II（⭐⭐⭐）
**来源**：T150
**思路**：在 I 的基础上允许每个元素最多出现两次。用 `slow` 指向下一个写入位置，判断条件改为 `nums[fast] != nums[slow-2]`。因为如果 `nums[slow-2] == nums[fast]`，说明已经有至少两个相同元素了。
**代码**：
```python
def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 6. 多数元素（⭐⭐）
**来源**：T150
**思路**：**Boyer-Moore 投票算法**。核心思想：不同元素相互抵消。维护一个 `candidate` 和 `count`。遍历时如果 `count == 0`，选当前元素为 candidate；遇到相同元素 count+1，不同则 count-1。最终 candidate 即为多数元素（因为题目保证多数元素的出现次数 > n/2）。
**代码**：
```python
def majorityElement(nums: list[int]) -> int:
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```

## 📝 总结
- **双指针是数组原地操作的核心技巧**，6道题中有5道使用了快慢/头尾指针
- 快慢指针的通用模板：`slow` 指向已处理部分的末尾，`fast` 遍历未处理部分
- 删除重复元素时，关键是确定"保留条件"——比较 `nums[fast]` 和 `nums[slow - k]`，其中 k 是允许的最大重复次数
- Boyer-Moore 投票算法是求多数元素的线性时间、常数空间最优解，理解"抵消"的思想很重要
