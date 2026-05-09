# Day 04: 哈希集合

## 📖 知识点
**哈希集合 (HashSet)**：
- 基于哈希表实现，存储不重复元素
- 查询/插入/删除平均时间复杂度 O(1)
- 常用于：去重、判断是否存在、记录访问状态、O(1) 查找
- Python 中的 set 和 frozenset

**连续序列问题** 的核心模式：用 set 存储所有元素，然后只从"序列起点"（即 `num-1` 不在 set 中）开始向后计数，避免重复计算。

## 🧩 刷题任务（6题）

### 1. 两数之和（⭐⭐）
**来源**：T150
**思路**：用哈希表（dict）存储已经遍历过的数字及其下标。遍历时，计算 `target - nums[i]` 是否已在哈希表中，如果是则返回两个下标。
**代码**：
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 2. 快乐数（⭐⭐）
**来源**：T150
**思路**：用 HashSet 记录已经出现过的数字，如果重复出现则进入循环，返回 False。或者用快慢指针检测循环（类似链表检测环）。
**代码**：
```python
def isHappy(n: int) -> bool:
    def get_next(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
```

### 3. 存在重复元素 II（⭐⭐）
**来源**：T150
**思路**：滑动窗口 + HashSet。维护一个大小为 k 的窗口，窗口内如有重复则返回 True。用 set 存储窗口内的元素，当窗口大小超过 k 时移除最左边的元素。
**代码**：
```python
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```

### 4. 最长连续序列（⭐⭐⭐）
**来源**：T150 / O
**思路**：用 set 存所有数字。遍历每个数字，只有当 `num - 1` 不在 set 中时（即它是连续序列的起点），才向后计数。这样每个数字最多被访问两次（一次在外层循环，一次在内层计数），时间复杂度 O(n)。
**代码**：
```python
def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0
    for num in num_set:
        # 只从序列起点开始计数
        if num - 1 not in num_set:
            cur = num
            length = 1
            while cur + 1 in num_set:
                cur += 1
                length += 1
            longest = max(longest, length)
    return longest
```

### 5. 字符串的最大公因子（⭐）
**来源**：L75
**思路**：如果 str1 + str2 == str2 + str1，则存在公因子字符串，其长度为 gcd(len(str1), len(str2))。用数学性质：两个字符串有公因子当且仅当它们拼接后相等。
**代码**：
```python
def gcdOfStrings(str1: str, str2: str) -> str:
    from math import gcd

    if str1 + str2 != str2 + str1:
        return ""
    g = gcd(len(str1), len(str2))
    return str1[:g]
```

### 6. 赎金信（⭐）
**来源**：T150
**思路**：用 Counter 统计 magazine 中每个字符的可用数量，遍历 ransomNote 中的字符，如果某个字符不够用则返回 False。
**代码**：
```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    counter = Counter(magazine)
    for ch in ransomNote:
        if counter[ch] == 0:
            return False
        counter[ch] -= 1
    return True
```

## 📝 总结
- **两数之和** 是哈希表应用的经典入门题，核心是"存已遍历 + 查补数"
- **最长连续序列** 的关键优化是"只从起点开始计数"，避免 O(n²)
- **快乐数** 的循环检测可以用 HashSet 或快慢指针两种思路
- **存在重复元素 II** 本质是固定大小的滑动窗口 + HashSet
- 字符串公因子利用了数学性质：如果 `s1 + s2 == s2 + s1`，则它们有公因子且长度为 gcd(len(s1), len(s2))
