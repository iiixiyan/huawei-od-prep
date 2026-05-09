# Day 04: Two Pointers（双指针）

## 📖 知识点讲解

### 快慢指针（同向双指针）

两个指针从同一方向出发，速度不同或启动时机不同。典型应用：数组去重、移动元素、原地修改。

```python
# 快慢指针模板：fast 遍历，slow 记录有效位置
slow = 0
for fast in range(len(nums)):
    if condition(nums[fast]):       # 满足条件
        nums[slow] = nums[fast]     # 保留
        slow += 1
return slow                         # 新长度
```

### 左右指针（相向双指针）

两个指针从两端向中间移动。典型应用：有序数组的两数之和、反转数组、容器盛水。

```python
# 左右指针模板
left, right = 0, len(arr) - 1
while left < right:
    if should_move_left(left):
        left += 1
    elif should_move_right(right):
        right -= 1
    else:
        # 处理当前 left, right 组合
        update_answer(left, right)
        left += 1   # 或 right -= 1
```

### 子序列双指针匹配

判断 `s` 是否为 `t` 的子序列：两个指针分别遍历 `s` 和 `t`，在 `t` 中按顺序找 `s` 的每个字符。

---

## 🧩 刷题任务

### 题目1：Move Zeroes（移动零）
**难度**：⭐
**题目描述**：
给定一个数组 `nums`，将所有 0 移动到数组末尾，同时保持非零元素的相对顺序。必须原地操作。

**思路分析**：
快慢指针法（同向双指针）：
- `slow` 指向当前可以放置非零元素的位置
- `fast` 遍历数组
- 遇到非零元素时，与 `nums[slow]` 交换，`slow++`
- 相当于把所有非零元素"挤"到前面

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        slow = 0  # 下一个非零元素应该放的位置
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

---

### 题目2：Is Subsequence（判断子序列）
**难度**：⭐
**题目描述**：
给定字符串 `s` 和 `t`，判断 `s` 是否为 `t` 的子序列。（子序列：不改变相对顺序，但可以不连续）

**思路分析**：
双指针在 `s` 和 `t` 上移动：
- 指针 `i` 指向 `s`，指针 `j` 指向 `t`
- 如果 `s[i] == t[j]`，`i` 和 `j` 都右移
- 否则只移动 `j`
- 最终如果 `i` 走到了 `s` 末尾，说明 `s` 是子序列

- 时间复杂度：O(n + m)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```

---

### 题目3：Container With Most Water（盛最多水的容器）
**难度**：⭐⭐
**题目描述**：
给定一个长度为 `n` 的整数数组 `height`，每根垂直线代表一个位置的高度。找两条线，使它们与 x 轴构成的容器能容纳最多的水（面积 = 宽度 × 高度）。返回最大水量。

**思路分析**：
左右指针法：
- 左指针 `l` 从 0 开始，右指针 `r` 从 n-1 开始
- 计算当前面积：`(r - l) * min(height[l], height[r])`
- 移动较矮的那一边（因为移动高的那边面积只会更小）
- 更新最大面积

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # 计算当前面积
            w = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, w * h)
            
            # 移动较矮的一边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
```

---

### 题目4：Max Number of K-Sum Pairs（K 和数对的最大数目）
**难度**：⭐⭐
**题目描述**：
给你一个整数数组 `nums` 和一个整数 `k`。每一步操作中，你需要从数组中选出和为 `k` 的两个整数，并将它们从数组中移除。返回最多可以执行的操作数。

**思路分析**：
排序 + 双指针法：
1. 对数组排序
2. 左右指针分别指向头和尾
3. 如果 `nums[l] + nums[r] == k`：计数 +1，左右同时移动
4. 如果和小于 k：左指针右移（增大和）
5. 如果和大于 k：右指针左移（减小和）

另一种方法：哈希表统计频次。

- 时间复杂度：O(n log n)（排序）
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                count += 1
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
        
        return count
```
