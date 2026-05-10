# Day 14: 周复习 — 字符串 & 双指针综合

## 📖 知识点

**本周重点回顾：**

| 知识点 | 核心题型 | 难度 |
|--------|---------|------|
| 字符串基础 | 反转、前缀、子串匹配 | ⭐ |
| 双指针 | 两数/三数之和、盛水、移动零 | ⭐~⭐⭐⭐ |
| 回文 | 中心扩展、验证回文 II | ⭐~⭐⭐⭐ |
| 滑动窗口 | 可变/固定/计数窗口 | ⭐~⭐⭐⭐⭐ |
| 字符串综合 | 压缩、异位词、拓扑排序 | ⭐~⭐⭐⭐⭐ |

**华为 OD 本周必会 TOP 5：**
1. 无重复字符的最长子串（滑动窗口）
2. 三数之和（双指针 + 去重）
3. 盛最多水的容器（双指针）
4. 最长回文子串（中心扩展）
5. 最小覆盖子串（困难滑动窗口）

---

## 🧩 刷题任务 — 综合复习

### 阶段一：快速回顾（用手写思路代替代码）

1. **盛最多水的容器**：左右指针，移动较矮侧 O(n)
2. **无重复字符的最长子串**：滑动窗口，`seen` 记录最近位置
3. **三数之和**：排序 + 固定一个 + 双指针 + 去重
4. **最小覆盖子串**：Counter + 可变窗口，用 missing 计数
5. **和为 K 的子数组**：前缀和 + 哈希表

---

### 阶段二：Mini Test — 限时 45 分钟

#### 题目 1：三数之和（⭐⭐⭐）5 min

**代码**：
```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
```

#### 题目 2：无重复字符的最长子串（⭐⭐⭐）5 min

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

#### 题目 3：最长回文子串（⭐⭐⭐）8 min

**代码**：
```python
def longestPalindrome(s: str) -> str:
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
    ans = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        if len(odd) > len(ans):
            ans = odd
        if len(even) > len(ans):
            ans = even
    return ans
```

#### 题目 4：和为 K 的子数组（⭐⭐⭐）8 min

**代码**：
```python
def subarraySum(nums: list[int], k: int) -> int:
    from collections import defaultdict
    prefix = defaultdict(int)
    prefix[0] = 1
    s = ans = 0
    for x in nums:
        s += x
        ans += prefix[s - k]
        prefix[s] += 1
    return ans
```

#### 题目 5：最小覆盖子串（⭐⭐⭐⭐）12 min

**代码**：
```python
def minWindow(s: str, t: str) -> str:
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    l = 0
    start, min_len = 0, float('inf')
    for r, ch in enumerate(s):
        if ch in need:
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
        while missing == 0:
            if r - l + 1 < min_len:
                start = l
                min_len = r - l + 1
            left_ch = s[l]
            if left_ch in need:
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
            l += 1
    return "" if min_len == float('inf') else s[start:start + min_len]
```

---

### 阶段三：错误复盘模板

| 题目 | 是否独立 AC | 卡点 | 改进方向 |
|------|------------|------|---------|
| 三数之和 | □ 是 □ 否 | | |
| 无重复字符最长子串 | □ 是 □ 否 | | |
| 最长回文子串 | □ 是 □ 否 | | |
| 和为 K 子数组 | □ 是 □ 否 | | |
| 最小覆盖子串 | □ 是 □ 否 | | |

---

## 📌 本周总结

**Week 2 核心收获：**
1. **双指针**是 O(n) 降维利器，华为 OD 每题必想能不能用
2. **滑动窗口**三件套：可变、固定、计数刷熟
3. **回文问题**首选中心扩展，面试手写最稳
4. **前缀和 + 哈希表**是子数组求和的大杀器

**下周预告（Week 3 — 哈希表 & 数据结构）：**
- 哈希表基础（两数之和、最长连续序列）
- 栈（有效括号、逆波兰表达式）
- 队列（滑动窗口最大值）
- 堆（前 K 高频元素）
- 进阶数据结构（LRU、前缀树）

**继续加油！** 🔥
