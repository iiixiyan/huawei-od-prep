# Day 05: Sliding Window（滑动窗口）

## 📖 知识点讲解

### 滑动窗口模板

滑动窗口是处理**子数组/子串**问题的经典方法，核心是维护一个窗口在数组/字符串上滑动。

#### 固定长度窗口模板

```python
# 固定长度 k 的滑动窗口
window_sum = sum(nums[:k])  # 初始化第一个窗口
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]  # 滑入新元素，滑出旧元素
    max_sum = max(max_sum, window_sum)
```

#### 可变长度窗口模板

```python
# 可变长度滑动窗口（解决"最长/最短满足条件子数组"）
left = 0
for right in range(len(nums)):
    # 扩窗：加入 nums[right]
    update_state(nums[right])
    
    # 缩窗：当窗口不满足条件时，移动 left
    while not is_valid():
        update_state(nums[left], remove=True)
        left += 1
    
    # 更新答案：此时窗口 [left, right] 是满足条件的
    update_answer(right - left + 1)
```

---

## 🧩 刷题任务

### 题目1：Maximum Average Subarray I（子数组最大平均数 I）
**难度**：⭐
**题目描述**：
给你一个由 `n` 个整数组成的数组 `nums` 和一个整数 `k`。找出长度为 `k` 的连续子数组的最大平均数。

**思路分析**：
固定长度滑动窗口：
1. 先计算前 k 个元素的和
2. 每次窗口右移一位：加新元素，减旧元素
3. 记录最大和，最后除以 k 得最大平均数

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
```

---

### 题目2：Maximum Number of Vowels in a Substring of Given Length（定长子串中元音的最大数目）
**难度**：⭐⭐
**题目描述**：
给你字符串 `s` 和整数 `k`，请返回长度为 `k` 的子串中元音字母的最大数目。

**思路分析**：
固定长度滑动窗口 + 元音判断：
1. 用集合存储元音字母以便 O(1) 判断
2. 先统计第一个窗口的元音数
3. 滑动窗口时，检查滑入字符是否是元音（+1），滑出字符是否是元音（-1）
4. 更新最大值

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        # 初始窗口
        count = sum(1 for c in s[:k] if c in vowels)
        max_count = count
        
        for i in range(k, len(s)):
            # 滑入新字符
            if s[i] in vowels:
                count += 1
            # 滑出旧字符
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        
        return max_count
```

---

### 题目3：Max Consecutive Ones III（最大连续1的个数 III）
**难度**：⭐⭐
**题目描述**：
给定一个由 `0` 和 `1` 组成的数组 `nums`，你可以将最多 `k` 个 `0` 翻转为 `1`。请返回仅包含 `1` 的最长（连续）子数组的长度。

**思路分析**：
可变长度滑动窗口：
- 窗口内最多允许有 `k` 个 0
- 右指针不断右移扩大窗口
- 当窗口中 0 的数量 > k 时，左指针右移缩小窗口
- 记录窗口的最大长度

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0  # 窗口中 0 的数量
        max_len = 0
        
        for right in range(len(nums)):
            # 扩大窗口
            if nums[right] == 0:
                zeros += 1
            
            # 缩窗条件：0 的数量超过 k
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # 更新答案
            max_len = max(max_len, right - left + 1)
        
        return max_len
```

---

### 题目4：Longest Subarray of 1's After Deleting One Element（删掉一个元素后全为1的最长子数组）
**难度**：⭐⭐
**题目描述**：
给你一个二进制数组 `nums`，你需要从中删掉一个元素。请返回删掉一个元素后，最长的只包含 `1` 的非空子数组的长度。如果不存在这样的子数组，返回 0。

**思路分析**：
可变长度滑动窗口的变体：
- 窗口内最多允许有 **1 个** 0（因为删掉一个元素）
- 相当于 k = 1 的 "Max Consecutive Ones" 问题
- 注意：必须删掉一个元素，所以结果是 `窗口长度 - 1`（如果窗口中有 0）或 `窗口长度 - 1`（如果全是 1，也得删一个）

简化：直接用滑动窗口，限制窗口内最多 1 个 0，返回 `max_len - 1`（因为必须删一个元素）。

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        # 必须删掉一个元素
        return max_len - 1
```
