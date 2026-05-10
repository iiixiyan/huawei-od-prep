# Day 11: 滑动窗口进阶

## 📖 知识点

**滑动窗口三大类：**
1. **可变窗口**：找最长/最短子数组/子串满足条件 → while 缩小窗口
2. **固定窗口**：固定大小滑窗，求最大/最小/平均值 → 加右减左
3. **计数窗口**：用 Counter 统计字符频次，比较窗口和目标是否匹配

**核心模板（可变窗口）：**
```python
l = 0
for r in range(n):
    加入 nums[r]
    while 窗口不满足条件:
        移除 nums[l]
        l += 1
    更新答案  # 通常是 r - l + 1
```

---

## 🧩 刷题任务

### 1. 无重复字符的最长子串（⭐⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
**难度**：中等
**题目**：给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串** 的长度。

**示例 1:**
```
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
```
**示例 2:**
```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
**示例 3:**
```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```
**提示：**

- `0 4`

- `s` 由英文字母、数字、符号和空格组成
**思路**：可变滑动窗口。`seen` 集合或字典记录字符最近位置。右指针扩展，若字符重复则左指针跳到重复位置+1，更新最大长度。
**代码**：
```python
def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    l = ans = 0
    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1
        seen[ch] = r
        ans = max(ans, r - l + 1)
    return ans
```
### 2. 最小覆盖子串（⭐⭐⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/minimum-window-substring/)
**难度**：困难
**题目**：给定两个字符串 `s` 和 `t`，长度分别是 `m` 和 `n`，返回 s 中的 **最短窗口 子串**，使得该子串包含 `t` 中的每一个字符（**包括重复字符**）。如果没有这样的子串，返回空字符串* *`""`。

测试用例保证答案唯一。

**示例 1：**
```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```
**示例 2：**
```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```
**示例 3:**
```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```
**提示：**

- `m == s.length`

- `n == t.length`

- `1 5`

- `s` 和 `t` 由英文字母组成

**进阶：**你能设计一个在 `O(m + n)` 时间内解决此问题的算法吗？
**思路**：可变窗口。用计数器记录 t 的需求。右指针扩展直到覆盖 t，然后收缩左指针找最短覆盖子串。
**代码**：
```python
def minWindow(s: str, t: str) -> str:
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    l = 0
    ans_start, ans_len = 0, float('inf')
    for r, ch in enumerate(s):
        if ch in need:
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
        while missing == 0:
            if r - l + 1 < ans_len:
                ans_start = l
                ans_len = r - l + 1
            left_ch = s[l]
            if left_ch in need:
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
            l += 1
    return "" if ans_len == float('inf') else s[ans_start:ans_start + ans_len]
```
### 3. 长度最小的子数组（⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/minimum-size-subarray-sum/)
**难度**：中等
**题目**：给定一个含有 `n` 个正整数的数组和一个正整数 `target` * 。**

找出该数组中满足其总和大于等于 `target` 的长度最小的 **子数组** `[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度**。**如果不存在符合条件的子数组，返回 `0` 。

**示例 1：**
```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```
**示例 2：**
```
输入：target = 4, nums = [1,4,4]
输出：1
```
**示例 3：**
```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```
**提示：**

- `1 9`

- `1 5`

- `1 4`

**进阶：**

- 如果你已经实现* *`O(n)` 时间复杂度的解法, 请尝试设计一个 `O(n log(n))` 时间复杂度的解法。
**思路**：可变窗口。右指针扩展求和，当和 >= target 时收缩左指针找最小长度。
**代码**：
```python
def minSubArrayLen(target: int, nums: list[int]) -> int:
    l = total = 0
    ans = float('inf')
    for r, val in enumerate(nums):
        total += val
        while total >= target:
            ans = min(ans, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if ans == float('inf') else ans
```
### 4. 乘积小于 K 的子数组（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/subarray-product-less-than-k/)
**难度**：中等
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，请你返回子数组内所有元素的乘积严格小于* *`k` 的连续子数组的数目。

**示例 1：**
```
输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
```
**示例 2：**
```
输入：nums = [1,2,3], k = 0
输出：0
**提示: **
- `1 4`
- `1 6`
```
**思路**：滑动窗口。右指针扩展，乘积 *= nums[r]。乘积 >= k 时收缩左指针。每次符合条件时，以 r 结尾的合法子数组有 `r - l + 1` 个。
**代码**：
```python
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    l = 0
    prod = 1
    ans = 0
    for r, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod //= nums[l]
            l += 1
        ans += r - l + 1
    return ans
```
### 5. 和为 K 的子数组（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/subarray-sum-equals-k/)
**难度**：中等
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 *该数组中和为 `k` 的子数组的个数 *。

子数组是数组中元素的连续非空序列。

**示例 1：**
```
输入：nums = [1,1,1], k = 2
输出：2
```
**示例 2：**
```
输入：nums = [1,2,3], k = 3
输出：2
```
**提示：**

- `1 4`

- `-1000 7 7`
**思路**：前缀和 + 哈希表。遍历数组，计算前缀和。用哈希表记录每个前缀和出现的次数，当前缀和 - k 在表中时，累计次数到结果。
**代码**：
```python
def subarraySum(nums: list[int], k: int) -> int:
    from collections import defaultdict
    prefix = defaultdict(int)
    prefix[0] = 1  # 前缀和为0出现1次
    s = ans = 0
    for val in nums:
        s += val
        ans += prefix[s - k]
        prefix[s] += 1
    return ans
```
### 6. 连续数组（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/contiguous-array/)
**难度**：中等
**题目**：给定一个二进制数组 `nums` , 找到含有相同数量的 `0` 和 `1` 的最长连续子数组，并返回该子数组的长度。

**示例 1：**
```
输入：nums = [0,1]
输出：2
说明：[0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
```
**示例 2：**
```
输入：nums = [0,1,0]
输出：2
说明：[0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
```
**示例 3：**
```
输入：nums = [0,1,1,1,1,1,0,0,0]
输出：6
解释：[1,1,1,0,0,0] 是具有相同数量 0 和 1 的最长连续子数组。
```
**提示：**

- `1 5`

- `nums[i]` 不是 `0` 就是 `1` *思路**：把 0 视为 -1，问题转化为和为 0 的最长子数组。前缀和 + 哈希表记录首次出现的位置。
**代码**：
```python
def findMaxLength(nums: list[int]) -> int:
    # 0 -> -1, 找和为0的最长子数组
    first = {0: -1}
    s = ans = 0
    for i, val in enumerate(nums):
        s += 1 if val == 1 else -1
        if s in first:
            ans = max(ans, i - first[s])
        else:
            first[s] = i
    return ans
```
### 7. 最大连续 1 的个数 III（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/max-consecutive-ones-iii/)
**难度**：中等
**题目**：给定一个二进制数组 `nums` 和一个整数 `k`，假设最多可以翻转 `k` 个 `0` ，则返回执行操作后 *数组中连续 `1` 的最大个数* 。

**示例 1：**
```
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```
**示例 2：**
```
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```
**提示：**

- `1 5`

- `nums[i]` 不是 `0` 就是 `1`

- `0
**思路**：滑动窗口。允许翻转 k 个 0（即窗口内最多 k 个 0）。右指针扩展，0 的计数超过 k 时收缩左指针。
**代码**：
```python
def longestOnes(nums: list[int], k: int) -> int:
    l = 0
    zeros = 0
    ans = 0
    for r, val in enumerate(nums):
        if val == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans
```
## 📌 总结
- Day 11 是滑动窗口最密集的一天，7 道题覆盖了所有窗口题型
- **华为 OD 必考**：无重复字符最长子串、和为 K 的子数组、最小覆盖子串
- 前缀和 + 哈希表是解决子数组求和问题的**万能套路**
