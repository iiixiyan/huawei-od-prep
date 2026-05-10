# Day 09: 双指针

## 📖 知识点

**双指针核心模式：**
- **左右指针**（相向而行）：有序数组两数之和、盛水、回文
- **快慢指针**（同向而行）：移除零、子序列
- **滑动窗口**（同向，窗口可变/固定）：子数组/子串问题

**双指针优势：** 将 O(n²) 暴力降为 O(n)，空间 O(1)

**华为 OD 常考类型：**
- 两数/三数之和 → 排序 + 左右指针
- 容器盛水 → 左右指针移动短板
- 移除零 → 快慢指针原地交换

---

## 🧩 刷题任务

### 1. 移动零（⭐）
**来源**：[L75](https://leetcode.cn/problems/move-zeroes/)
**难度**：简单
**题目**：给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意** ，必须在不复制数组的情况下原地对数组进行操作。

**示例 1:**
```
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
```
**示例 2:**
```
输入: nums = [0]
输出: [0]
```
**提示**:

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

**进阶：**你能尽量减少完成的操作次数吗？
**思路**：快慢指针。slow 指向待填充位置，fast 遍历数组。fast 遇到非零则写入 slow 并移动 slow。遍历完后 slow 之后补零。
**代码**：
```python
def moveZeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    # 后续补零（其实交换时已经处理了，无需单独写）
```
### 2. 判断子序列（⭐） / T150
**来源**：[L75](https://leetcode.cn/problems/is-subsequence/)
**难度**：简单
**题目**：给定字符串 **s**和**t**，判断**s**是否为**t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

**致谢：**

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

**示例 1：**
```
输入：s = "abc", t = "ahbgdc"
输出：true
```
**示例 2：**
```
输入：s = "axc", t = "ahbgdc"
输出：false
```
**提示：**

- `0 <= s.length <= 100`
- `0 <= t.length <= 5 * 10^4`
**思路**：双指针 i 遍历 s，j 遍历 t。t 中匹配到 s[i] 则 i 前进。最终判断 i 是否走完 s。
**代码**：
```python
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```
### 3. 盛最多水的容器（⭐⭐） / T150
**来源**：[L75](https://leetcode.cn/problems/container-with-most-water/)
**难度**：中等
**题目**：给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

**示例 1：**
```
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```
**示例 2：**
```
输入：height = [1,1]
输出：1
```
**提示：**

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`
**思路**：左右指针初始在两端。面积 = min(height[l], height[r]) * (r - l)。每次移动较矮的那一侧（因为移动高的一侧面积不可能更大），记录最大面积。
**代码**：
```python
def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        ans = max(ans, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans
```
### 4. 两数之和 II - 输入有序数组（⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)
**难度**：中等
**题目**：给你一个下标从 **1** 开始的整数数组 `numbers`，该数组已按 **非递减顺序排列**。请你从数组中找出满足相加之和等于目标数 `target` 的两个数。

如果设这两个数分别是 `numbers[index1]` 和 `numbers[index2]`，则 `1 <= index1 < index2 <= numbers.length`。

以长度为 2 的整数数组 `[index1, index2]` 的形式返回这两个整数的下标。

你可以假设每个输入 **只对应唯一的答案**，而且你 **不可以** 重复使用相同的元素。

**示例 1：**
```
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2。返回 [1, 2] 。
```
**示例 2：**
```
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3。返回 [1, 3] 。
```
**示例 3：**
```
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2。返回 [1, 2] 。
```
**提示：**

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `-1000 <= target <= 1000`
- **只会存在一个有效答案**
**思路**：有序数组，左右指针。和 < target 则左指针右移，> target 则右指针左移，等于则返回。
**代码**：
```python
def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []
```
### 5. 三数之和（⭐⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/3sum/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

**示例 1：**
```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```
**示例 2：**
```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```
**示例 3：**
```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```
**提示：**

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
**思路**：排序后固定第一个数（去重），内层双指针找后两个数。注意跳过重复元素。
**代码**：
```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # 去重
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1  # 去重
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1  # 去重
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
```
### 6. K 和数对的最大数目（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/max-number-of-k-sum-pairs/)
**难度**：中等
**题目**：给你一个整数数组 `nums` 和一个整数 `k` 。

每一步操作中，你需要从数组中选出和为 `k` 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。

**示例 1：**
```
输入：nums = [1,2,3,4], k = 5
输出：2
解释：开始时 nums = [1,2,3,4]：
- 移出 1 和 4 ，之后 nums = [2,3]
- 移出 2 和 3 ，之后 nums = []
不再有和为 5 的数对，因此最多执行 2 次操作。
```
**示例 2：**
```
输入：nums = [3,1,3,4,3], k = 6
输出：1
解释：开始时 nums = [3,1,3,4,3]：
- 移出前两个 3 ，之后nums = [1,4,3]
不再有和为 6 的数对，因此最多执行 1 次操作。
```
**提示：**

- `1 <= nums.length <= 10^5`
- `1 <= k <= 10^9`
- `1 <= nums[i] <= 10^9`
**思路**：- 排序 + 双指针：排序后左右指针求和，等于 k 计数+1 并移动双指针，小于 k 左移，大于 k 右移 - 哈希表也可（计数配对）
**代码**：
```python
def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    l, r = 0, len(nums) - 1
    ans = 0
    while l < r:
        s = nums[l] + nums[r]
        if s == k:
            ans += 1
            l += 1
            r -= 1
        elif s < k:
            l += 1
        else:
            r -= 1
    return ans
```
## 📌 总结
- 双指针的核心在于**指针移动的决策依据**：移动哪一边能获得更优解？
- 华为 OD 高频：**盛水 + 三数之和 + 两数之和 II**，面试必须手撕
- 三数之和的**去重逻辑**是面试常考点，务必掌握
