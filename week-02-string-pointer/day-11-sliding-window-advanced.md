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

### 1. 无重复字符的最长子串（⭐⭐⭐） 来源：T150 / O
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

---

### 2. 最小覆盖子串（⭐⭐⭐⭐） 来源：T150 / O
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

---

### 3. 长度最小的子数组（⭐⭐） 来源：T150 / O
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

---

### 4. 乘积小于 K 的子数组（⭐⭐） 来源：O
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

---

### 5. 和为 K 的子数组（⭐⭐⭐） 来源：O
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

---

### 6. 连续数组（⭐⭐⭐） 来源：O
**思路**：把 0 视为 -1，问题转化为和为 0 的最长子数组。前缀和 + 哈希表记录首次出现的位置。

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

---

### 7. 最大连续 1 的个数 III（⭐⭐） 来源：L75
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

---

## 📌 总结
- Day 11 是滑动窗口最密集的一天，7 道题覆盖了所有窗口题型
- **华为 OD 必考**：无重复字符最长子串、和为 K 的子数组、最小覆盖子串
- 前缀和 + 哈希表是解决子数组求和问题的**万能套路**

