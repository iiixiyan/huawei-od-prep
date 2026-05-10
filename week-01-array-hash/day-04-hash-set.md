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
**题目**：给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值 ***`target`*  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

**提示：**

- `2 4`

- `-109 9`

- `-109 9`

- **只会存在一个有效答案**

**进阶：**你可以想出一个时间复杂度小于 `O(n2)` 的算法吗？
**难度**：简单
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
**题目**：编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」** 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。

- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。

- 如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**

```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**示例 2：**

```
输入：n = 2
输出：false
```

**提示：**

- `1 31 - 1`
**难度**：简单
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
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引*** *`i` 和* *`j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) 5`

- `-109 9`

- `0 5`
**难度**：简单
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
**题目**：给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)`* *的算法解决此问题。

**示例 1：**

```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**

```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

**示例 3：**

```
输入：nums = [1,0,1,2]
输出：3
```

**提示：**

- `0 5`

- `-109 9`
**难度**：中等
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
**题目**：对于字符串 `s` 和 `t`，只有在 `s = t + t + t + ... + t + t`（`t` 自身连接 1 次或多次）时，我们才认定 “`t` 能除尽 `s`”。

给定两个字符串 `str1` 和 `str2` 。返回 *最长字符串 `x`，要求满足 `x` 能除尽 `str1` 且 `x` 能除尽 `str2`* 。

**示例 1：**

**输入：**str1 = "ABCABC", str2 = "ABC"

**输出：**"ABC"

**示例 2：**

**输入：**str1 = "ABABAB", str2 = "ABAB"

**输出：**"AB"

**示例 3：**

**输入：**str1 = "LEET", str2 = "CODE"

**输出：**""

**示例 4：**

**输入：**str1 = "AAAAAB", str2 = "AAA"

**输出：**""

**提示：**

- `1 <= str1.length, str2.length <= 1000`

- `str1` 和 `str2` 由大写英文字母组成
**难度**：简单
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
**题目**：给你两个字符串：`ransomNote` 和 `magazine` ，判断 `ransomNote` 能不能由 `magazine` 里面的字符构成。

如果可以，返回 `true` ；否则返回 `false` 。

`magazine` 中的每个字符只能在 `ransomNote` 中使用一次。

**示例 1：**

```
输入：ransomNote = "a", magazine = "b"
输出：false
```

**示例 2：**

```
输入：ransomNote = "aa", magazine = "ab"
输出：false
```

**示例 3：**

```
输入：ransomNote = "aa", magazine = "aab"
输出：true
```

**提示：**

- `1 5`

- `ransomNote` 和 `magazine` 由小写英文字母组成
**难度**：简单
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
