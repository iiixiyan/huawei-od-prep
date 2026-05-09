# Day 07: Weekly Review（周复习）

## 📖 本周知识点总览

| 主题 | 核心技巧 | 典型题 |
|------|----------|--------|
| 字符串基础 | 双指针交替、GCD | Merge Alternately, GCD of Strings |
| 数组贪心 | 一次遍历、边界处理 | Can Place Flowers |
| 双指针原地操作 | 快慢指针、相向指针 | Move Zeroes, Container With Most Water |
| 前缀积 | 前缀积+后缀积空间优化 | Product Except Self |
| 滑动窗口（固定） | 窗口滑动公式 | Max Average, Max Vowels |
| 滑动窗口（可变） | 扩窗+缩窗模板 | Max Consecutive Ones III |
| 哈希表应用 | 集合、Counter、行列映射 | Find Difference, Unique Occurrences |
| 数学+字符串 | GCD 与整除性质 | GCD of Strings |

---

## 🧩 综合练习题

### 题目1：综合 — 合并 & 反转 & 子序列判断

**题目描述**：
给你一个字符串 `s` 和一个字符串数组 `words`，请你判断 `s` 是否能由 `words` 中的字符串**交替合并**而成。也就是说，存在一种方式将 `s` 分割成若干子串，这些子串按顺序分别来自 `words` 中的不同字符串（每个字符串使用一次）。

**思路分析**：
这题综合了交替合并和子序列思想。实际是问：能否用双指针从 `words` 中依次取字符构建 `s`？
简化版：检查 `s` 是否是 `words` 中字符串按某种顺序交替拼接的结果。

**参考代码**：
```python
def canFormString(s: str, words: List[str]) -> bool:
    """检查 s 是否可以由 words 交替组成（每个单词用一次）"""
    from itertools import permutations
    # 暴力解法：枚举所有排列（仅当 words 长度很小时）
    for perm in permutations(words):
        # 双指针交替合并所有单词
        res = []
        i = 0
        while any(i < len(w) for w in perm):
            for w in perm:
                if i < len(w):
                    res.append(w[i])
            i += 1
        if ''.join(res) == s:
            return True
    return False
```

---

### 题目2：综合 — 最大水量 + 滑动窗口

**题目描述**：
给你一个整数数组 `height`，表示一系列柱子的高度。你可以选择一个长度为 `k` 的连续子数组（滑动窗口），在这个子数组中找到能盛最多水的两根柱子。返回所有长度为 `k` 的窗口中，最大盛水量的最大值。

**思路分析**：
1. 用固定滑动窗口遍历数组
2. 在每个窗口内用双指针求最大盛水量
3. 取全局最大值

**参考代码**：
```python
def maxWaterInSlidingWindow(height: List[int], k: int) -> int:
    n = len(height)
    if k < 2:
        return 0
    
    max_water = 0
    for start in range(n - k + 1):
        window = height[start:start + k]
        # 在窗口内用双指针求最大水量
        l, r = 0, k - 1
        while l < r:
            w = r - l
            h = min(window[l], window[r])
            max_water = max(max_water, w * h)
            if window[l] < window[r]:
                l += 1
            else:
                r -= 1
    
    return max_water
```

---

### 题目3：综合 — 前缀积 + 哈希

**题目描述**：
给你一个整数数组 `nums`，请找出数组中所有长度为 `k` 的连续子数组中，乘积最大的那个子数组的乘积（不包含自身）。即：对每个子数组，计算除当前元素外其他元素的乘积，然后取这些乘积的最大值。

**思路分析**：
1. 滑动窗口获取每个长度为 k 的子数组
2. 在每个子数组内用"除自身以外数组的乘积"的方法
3. 取所有结果的最大值

---

## ⏱️ 限时小测（30分钟）

以下 5 题，每题 6 分钟，请计时完成：

**Q1**：交替合并字符串 `"abc"` 和 `"defgh"` 的结果是？

<details>
<summary>答案</summary>
`"adbecfgh"` — 先交替取 a d b e c f，剩余 gh 追加。
</details>

**Q2**：`canPlaceFlowers([1,0,0,0,1], 2)` 返回什么？

<details>
<summary>答案</summary>
`False` — 最多只能种 1 朵（位置 2）。
</details>

**Q3**：`productExceptSelf([1,2,3,4])` 的结果是？

<details>
<summary>答案</summary>
`[24, 12, 8, 6]` — 左前缀 [1,1,2,6] × 右后缀 [24,12,4,1]
</details>

**Q4**：滑动窗口求 `maxVowels("leetcode", 3)` 的结果是？

<details>
<summary>答案</summary>
`2` — 子串 `"lee"` 有 2 个元音（e, e），`"cod"` 有 1 个（o），`"code"` 的长度为 3 的子串最多 2 个元音。
</details>

**Q5**：`equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])` 的结果是？

<details>
<summary>答案</summary>
`3` — 第 0 行 [3,1,2,2] 没有匹配列；第 1 行 [1,4,4,5] 没有匹配列；第 2 行 [2,4,2,2] 匹配第 2,3 列（2次）；第 3 行 [2,4,2,2] 匹配第 2,3 列（2次...但注意不同行重复计数）。最终 3 对。
</details>

---

## 📊 自我评估表

| 题型 | 掌握程度（1-5） | 需要复习？ |
|------|:---:|:--------:|
| 字符串交替合并 | ___ / 5 | □ |
| GCD 求公因子字符串 | ___ / 5 | □ |
| 双指针反转/移动 | ___ / 5 | □ |
| 前缀积优化 | ___ / 5 | □ |
| 滑动窗口（固定） | ___ / 5 | □ |
| 滑动窗口（可变） | ___ / 5 | □ |
| 哈希表统计 | ___ / 5 | □ |
| 贪心思想 | ___ / 5 | □ |

**薄弱环节**：___________

## 🎯 下周预告

**Week 2 — 哈希表与栈**：
- 两数之和/三数之和
- 有效括号/最小栈
- 哈希表与栈综合应用
