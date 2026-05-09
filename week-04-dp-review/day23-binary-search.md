# Day 23 — Binary Search（二分搜索）

## 📌 今日重点
- 二分搜索的三种模板（标准、左边界、右边界）
- 二分答案（在值域上二分）
- 峰值查找（局部有序）
- 排序 + 二分的组合技巧

---

## 1. 二分搜索三大模板

### 模板一：标准二分（找精确值）
```java
int binarySearch(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### 模板二：左边界（第一个 ≥ target）
```java
int leftBound(int[] nums, int target) {
    int left = 0, right = nums.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] >= target) right = mid;
        else left = mid + 1;
    }
    return left; // 返回索引；如果所有元素 < target，返回 nums.length
}
```

### 模板三：右边界（最后一个 ≤ target）
```java
int rightBound(int[] nums, int target) {
    int left = 0, right = nums.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return left - 1;
}
```

**记忆口诀**：
- 左闭右闭 `<=`：找精确值
- 左闭右开 `<`：找边界
- `>=` 左缩右 → 左边界
- `<=` 左移 → 右边界

---

## 2. 高频题型与题解

### 🔹 猜数字大小（374. Guess Number Higher or Lower）
**思路**：标准二分，guess API 返回 -1/0/1

```java
public int guessNumber(int n) {
    int left = 1, right = n;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int res = guess(mid);
        if (res == 0) return mid;
        else if (res == -1) right = mid - 1;
        else left = mid + 1;
    }
    return -1;
}
```

### 🔹 咒语与药水的对数（2300. Successful Pairs of Spells and Potions）
**思路**：排序 + 二分（典型组合）
- 将药水数组排序
- 对每个咒语，二分查找满足 `spell * potion >= success` 的最小药水强度
- 即找第一个 ≥ `ceil(success / spell)` 的位置

```java
public int[] successfulPairs(int[] spells, int[] potions, long success) {
    Arrays.sort(potions);
    int n = potions.length;
    int[] ans = new int[spells.length];
    for (int i = 0; i < spells.length; i++) {
        long need = (success + spells[i] - 1) / spells[i]; // 向上取整
        int idx = firstGreaterOrEqual(potions, need);
        ans[i] = n - idx;
    }
    return ans;
}

private int firstGreaterOrEqual(int[] arr, long target) {
    int left = 0, right = arr.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] >= target) right = mid;
        else left = mid + 1;
    }
    return left;
}
```

### 🔹 寻找峰值（162. Find Peak Element）
**思路**：二分 O(log n)，利用局部单调性
- 如果 `nums[mid] < nums[mid+1]`，峰值在右边
- 否则峰值在左边（或 mid 本身）

```java
public int findPeakElement(int[] nums) {
    int left = 0, right = nums.length - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1; // 上坡，峰值在右
        } else {
            right = mid;    // 下坡，峰值在左（含mid）
        }
    }
    return left;
}
```

### 🔹 爱吃香蕉的珂珂（875. Koko Eating Bananas）
**思路**：二分答案（经典）
- 速度 k 的范围是 [1, max(piles)]
- 对每个 k，计算总时间 `sum(ceil(pile / k))`
- 二分找满足总时间 ≤ h 的最小 k

```java
public int minEatingSpeed(int[] piles, int h) {
    int left = 1, right = 0;
    for (int p : piles) right = Math.max(right, p);

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (canEatAll(piles, h, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

private boolean canEatAll(int[] piles, int h, int k) {
    int hours = 0;
    for (int p : piles) {
        hours += (p + k - 1) / k; // 向上取整
        if (hours > h) return false;
    }
    return true;
}
```

---

## 3. 二分答案框架（值域二分）

当题目问「XXX 的最小最大值」或「在什么条件下可行」时，考虑二分答案：

```java
int left = minPossible, right = maxPossible;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (check(mid)) right = mid;  // 可行 → 尝试更小
    else left = mid + 1;          // 不可行 → 需要更大
}
return left;
```

**可二分的条件**：`check(x)` 关于 x 是单调的（可行域分界）

---

## 4. 华为 OD 常考二分变体

| 题型 | 特点 |
|------|------|
| **搜索旋转排序数组** | 先确定单调段再二分 |
| **寻找旋转排序数组最小值** | 与右端点比较 |
| **在排序数组中找元素范围** | 左边界 + 右边界 |
| **分割数组的最大值** | 二分答案 + 贪心 |
| **运货/包裹问题** | 二分答案，check 函数模拟 |

---

## 5. 课后练习（LeetCode）

| 题目 | 难度 | 说明 |
|------|------|------|
| 374. Guess Number | 🟢 简单 | 标准二分 |
| 2300. Successful Pairs | 🟡 中等 | 排序+二分 |
| 162. Find Peak Element | 🟡 中等 | 二分找峰值 |
| 875. Koko Eating Bananas | 🟡 中等 | 二分答案 |
| 33. Search in Rotated Array | 🟡 中等 | 旋转数组 |
| 34. Find First and Last | 🟡 中等 | 左右边界 |
| 410. Split Array Largest Sum | 🔴 困难 | 二分答案+贪心 |

---

## ⏱ 今日建议
- **模板不要混**：确定用「左闭右闭」还是「左闭右开」，全程保持一致
- **二分答案 check 函数**是核心，务必写对
- **ceil 计算**：`(a + b - 1) / b` 要熟练
- **峰值查找**用 while(left < right)，直觉上记住：nums[mid] 和 nums[mid+1] 比
