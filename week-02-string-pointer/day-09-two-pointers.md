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

### 1. 移动零（⭐） 来源：L75
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

---

### 2. 判断子序列（⭐） 来源：L75 / T150
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

---

### 3. 盛最多水的容器（⭐⭐） 来源：L75 / T150
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

---

### 4. 两数之和 II - 输入有序数组（⭐⭐） 来源：T150 / O
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

---

### 5. 三数之和（⭐⭐⭐） 来源：T150 / O
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

---

### 6. K 和数对的最大数目（⭐⭐） 来源：L75
**思路**：
- 排序 + 双指针：排序后左右指针求和，等于 k 计数+1 并移动双指针，小于 k 左移，大于 k 右移
- 哈希表也可（计数配对）

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

---

## 📌 总结
- 双指针的核心在于**指针移动的决策依据**：移动哪一边能获得更优解？
- 华为 OD 高频：**盛水 + 三数之和 + 两数之和 II**，面试必须手撕
- 三数之和的**去重逻辑**是面试常考点，务必掌握

