# Day 36: 二分搜索

## 📖 知识点
**二分搜索模板 (标准版)**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**二分搜索模板 (找边界)**
```python
# 第一个 >= target 的位置
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

# 第一个 > target 的位置
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left
```

**核心场景**：
1. 有序数组精确查找 → 标准二分
2. 有序数组找边界 → lower_bound / upper_bound
3. 旋转数组 → 画图找到有序区间，判断 target 是否在其中
4. 二维矩阵 → 把矩阵展开成一维或逐行二分
5. 峰值查找 → 比较 mid 和 mid+1 决定方向
6. 按值二分（答案二分）→ 在值域上二分判定可行性

## 🧩 刷题任务（6题）

### 1. 搜索插入位置（⭐⭐）来源：T150 / O
**思路**：经典 lower_bound。在有序数组中找到第一个 >= target 的位置。如果所有元素 < target，则返回 len(nums)。直接在模板上套用。

**代码**：
```python
def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left
```

### 2. 搜索二维矩阵（⭐⭐）来源：T150
**思路**：二维矩阵每一行递增，且每行第一个元素 > 上一行最后一个元素 → 拉直后是一个递增的一维数组。二分定位即可，mid // n 是行号，mid % n 是列号。

**代码**：
```python
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

### 3. 寻找峰值（⭐⭐）来源：L75 / T150
**思路**：nums[-1] = nums[n] = -∞，相邻元素不相等。二分法：如果 nums[mid] < nums[mid+1]，峰值在右侧；否则峰值在左侧（含 mid 自身）。不断缩小即可。

**代码**：
```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

### 4. 搜索旋转排序数组（⭐⭐⭐）来源：T150
**思路**：旋转数组的特点是分两段递增，且左段所有值 > 右段所有值。二分时先判断 mid 落在哪一段（对比 nums[mid] 和 nums[left]）。再判断 target 是否在该段的有序区间内，更新 left/right。

**代码**：
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # 左半段有序
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 右半段有序
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

### 5. 在排序数组中查找元素的第一个和最后一个位置（⭐⭐⭐）来源：T150
**思路**：两次二分。lower_bound 找第一个 >= target 的位置，检查是否等于 target。upper_bound 找第一个 > target 的位置，减 1 即为最后一个位置。

**代码**：
```python
def searchRange(nums, target):
    def lower_bound(arr, t):
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l) // 2
            if arr[m] >= t:
                r = m
            else:
                l = m + 1
        return l

    def upper_bound(arr, t):
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l) // 2
            if arr[m] > t:
                r = m
            else:
                l = m + 1
        return l

    first = lower_bound(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = upper_bound(nums, target) - 1
    return [first, last]
```

### 6. 寻找旋转排序数组中的最小值（⭐⭐）来源：T150
**思路**：旋转数组的最小值是唯一一个小于左边元素的值（或左边段与右边段的分界）。二分时比较 nums[mid] 和 nums[right]：如果 nums[mid] > nums[right]，最小值在右侧；否则在左侧（含 mid）。

**代码**：
```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
```

## 📝 总结
- **二分搜索**的核心是 **不断缩小搜索空间**，关键在于确定 mid 之后往哪边收缩
- 边界条件的统一写法：`while left < right` + `right = mid` / `left = mid + 1` 适用于大部分场景
- 旋转数组的关键动作：**先确定有序段，再判断 target 是否在其中**
- lower_bound / upper_bound 模板要背熟，能解决 "第一个/最后一个" 类问题
