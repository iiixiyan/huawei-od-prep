# Day 13: 字符串混合

## 📖 知识点

**混合题型覆盖：**
- **罗马数字转换**：映射 + 特殊规则（IV = 4, IX = 9 等）
- **单词模式匹配**：双向映射（字符→单词、单词→字符）
- **定长滑动窗口**：最大平均值、最多元音个数

**华为 OD 偏好：**
- 罗马数字转换（经典常考）
- 单词模式匹配（双映射哈希表）
- 滑动窗口极值（定长窗口）

---

## 🧩 刷题任务

### 1. 罗马数字转整数（⭐⭐） 来源：T150
**思路**：建立罗马字符到数值的映射。遍历字符串，如果当前值 < 下一个值，则减去当前值（如 IV 中的 I），否则加上当前值。

**代码**：
```python
def romanToInt(s: str) -> int:
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
         'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    n = len(s)
    for i, ch in enumerate(s):
        val = m[ch]
        if i + 1 < n and val < m[s[i + 1]]:
            ans -= val
        else:
            ans += val
    return ans
```

---

### 2. 整数转罗马数字（⭐⭐） 来源：T150
**思路**：从大到小列出所有罗马数字组合（含 4、9 等特殊值），贪心地每次减去最大的可表示值。

**代码**：
```python
def intToRoman(num: int) -> str:
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ans = ""
    for v, r in zip(vals, romans):
        while num >= v:
            ans += r
            num -= v
    return ans
```

---

### 3. 判断子序列（⭐） 来源：L75
**思路**：同 Day 09 题 2，双指针逐个匹配。

**代码**：
```python
def isSubsequence(s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```

---

### 4. 单词规律（⭐⭐） 来源：T150
**思路**：双向映射。拆分 pattern 和 str，确保 `char → word` 和 `word → char` 都是一对一。

**代码**：
```python
def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for ch, w in zip(pattern, words):
        if ch in char_to_word:
            if char_to_word[ch] != w:
                return False
        else:
            char_to_word[ch] = w
        if w in word_to_char:
            if word_to_char[w] != ch:
                return False
        else:
            word_to_char[w] = ch
    return True
```

---

### 5. 删掉一个元素以后全为 1 的最长子数组（⭐⭐） 来源：L75
**思路**：滑动窗口，允许窗口内有 1 个 0。等价于「最大连续 1 的个数 III」中 k=1 的情况，但题目要求必须删除一个元素，所以结果是 `窗口长度 - 1`（若窗口内有 0 则删除那个 0，若全 1 则删除一个 1）。

**代码**：
```python
def longestSubarray(nums: list[int]) -> int:
    l = 0
    zeros = 0
    ans = 0
    for r, val in enumerate(nums):
        if val == 0:
            zeros += 1
        while zeros > 1:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        ans = max(ans, r - l)  # 删除一个元素，所以长度是 r - l
    return ans
```

---

### 6. 定长子串中元音的最大数目（⭐⭐） 来源：L75
**思路**：固定窗口大小为 k。先统计第一个窗口的元音数，然后滑动：移除左边字符、加入右边字符，更新计数。

**代码**：
```python
def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    count = 0
    # 第一个窗口
    for i in range(k):
        if s[i] in vowels:
            count += 1
    ans = count
    # 滑动窗口
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        ans = max(ans, count)
    return ans
```

---

## 📌 总结
- **罗马数字转换**是常考题，掌握从大到小贪心和特殊规则
- **单词规律**考察双向映射，注意用两个哈希表确保一一对应
- **删除一个元素变全 1**和**最大元音数**是 L75 高频定长窗口题

