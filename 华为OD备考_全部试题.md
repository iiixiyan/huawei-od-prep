
### .git

### 第1周·数组与哈希表
- [day-01-array-basics](#day-01-array-basics)
- [day-02-array-advanced](#day-02-array-advanced)
- [day-03-array-math](#day-03-array-math)
- [day-04-hash-set](#day-04-hash-set)
- [day-05-hash-map](#day-05-hash-map)
- [day-06-prefix-sum-intervals](#day-06-prefix-sum-intervals)
- [day-07-week-review](#day-07-week-review)

### 第2周·字符串与双指针
- [day-08-strings-basics](#day-08-strings-basics)
- [day-09-two-pointers](#day-09-two-pointers)
- [day-10-palindrome-sliding-window](#day-10-palindrome-sliding-window)
- [day-11-sliding-window-advanced](#day-11-sliding-window-advanced)
- [day-12-string-comprehensive](#day-12-string-comprehensive)
- [day-13-string-mixed](#day-13-string-mixed)
- [day-14-weekly-review](#day-14-weekly-review)

### 第3周·链表与栈队列
- [D15-栈基础](#d15-栈基础)
- [D16-栈进阶](#d16-栈进阶)
- [D17-队列+设计](#d17-队列+设计)
- [D18-链表基础](#d18-链表基础)
- [D19-链表进阶](#d19-链表进阶)
- [day-20-linked-list-advanced-2](#day-20-linked-list-advanced-2)
- [day-21-weekly-review](#day-21-weekly-review)

### 第4周·树与图(复习)
- [D22-二叉树遍历](#d22-二叉树遍历)
- [D23-树的构建](#d23-树的构建)
- [D24-树的路径](#d24-树的路径)
- [D25-BFS-层序遍历](#d25-bfs-层序遍历)
- [D26-二叉搜索树BST](#d26-二叉搜索树bst)
- [D27-树的综合](#d27-树的综合)
- [D28-周复习](#d28-周复习)

### 第5周·OD100题(上)
- [day29-graph-dfs](#day29-graph-dfs)
- [day30-graph-bfs](#day30-graph-bfs)
- [day31-graph-advanced](#day31-graph-advanced)
- [day32-backtracking-basics](#day32-backtracking-basics)
- [day33-backtracking-advanced](#day33-backtracking-advanced)
- [day34-trie](#day34-trie)
- [day35-weekly-review](#day35-weekly-review)

### 第6周·OD100题(下)
- [D36-Binary-Search](#d36-binary-search)
- [D37-Binary-Search-Sorting](#d37-binary-search-sorting)
- [D38-Heap](#d38-heap)
- [D39-Bit-Manipulation](#d39-bit-manipulation)
- [D40-Math](#d40-math)
- [D41-OD-100](#d41-od-100)
- [D42-Review](#d42-review)

### 第7周·OD200题
- [D43_DP_一维入门](#d43dp一维入门)
- [D44_DP_一维进阶](#d44dp一维进阶)
- [D45_DP_二维](#d45dp二维)
- [D46_DP_高级](#d46dp高级)
- [D47_DP_字符串](#d47dp字符串)
- [D48_图_并查集_DP综合](#d48图并查集dp综合)
- [D49_周复习](#d49周复习)

### 第8周·模拟与冲刺
- [day-50-od-100-six](#day-50-od-100-six)
- [day-51-od-100-six-2](#day-51-od-100-six-2)
- [day-52-od-200-three](#day-52-od-200-three)
- [day-53-od-200-three-2](#day-53-od-200-three-2)
- [day-54-mock-test-1](#day-54-mock-test-1)
- [day-55-mock-test-2](#day-55-mock-test-2)
- [day-56-final-sprint](#day-56-final-sprint)

---

---
# .git
> 共计 0 天


---
# 第1周·数组与哈希表
> 共计 7 天

# Day 01: 数组基础操作

## 📖 知识点
**双指针原地操作**：在数组问题中，双指针技巧常用于原地修改数组，避免额外空间。两个指针从不同位置遍历，一个指向"当前写入位置"，另一个指向"当前读取位置"，在不使用额外数组的情况下完成元素删除、去重、合并等操作。

核心模式：
- **读写指针**：`slow` 指向已处理部分的末尾，`fast` 遍历整个数组
- **头尾指针**：左右夹逼，常用于有序数组的合并或交换
- **同向双指针**：两个指针同向移动，速度不同

## 🧩 刷题任务（6题）

### 1. 交替合并字符串（⭐）
**来源**：[L75](https://leetcode.cn/problems/merge-strings-alternately/)
**难度**：简单
**题目**：给你两个字符串 `word1` 和 `word2` 。请你从 `word1` 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。返回 **合并后的字符串** 。
**示例 1：**
```
输入：word1 = "abc", word2 = "pqr"
输出："apbqcr"
解释：字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r
```
**示例 2：**
```
输入：word1 = "ab", word2 = "pqrs"
输出："apbqrs"
解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
word1：  a   b
word2：    p   q   r   s
合并后：  a p b q   r   s
```
**示例 3：**
```
输入：word1 = "abcd", word2 = "pq"
输出："apbqcd"
解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
word1：  a   b   c   d
word2：    p   q
合并后：  a p b q c   d
```
**提示：**
- `1 <= word1.length, word2.length <= 100`
- `word1` 和 `word2` 由小写英文字母组成
**思路**：双指针分别遍历两个字符串，交替取字符拼接。当指针越界时，将剩余部分直接追加到结果末尾。
**代码**：
```python
def mergeAlternately(word1: str, word2: str) -> str:
    res = []
    i = j = 0
    m, n = len(word1), len(word2)
    while i < m or j < n:
        if i < m:
            res.append(word1[i])
            i += 1
        if j < n:
            res.append(word2[j])
            j += 1
    return "".join(res)

# 一行写法（Python trick，面试不推荐）
# def mergeAlternately(word1: str, word2: str) -> str:
#     from itertools import zip_longest
#     return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
```

### 2. 合并两个有序数组（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/merge-sorted-array/)
**难度**：简单
**题目**：给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。
**示例 1：**
```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。合并结果是 [1,2,2,3,5,6] 。
```
**示例 2：**
```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
```
**示例 3：**
```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。注意，因为 m = 0 ，所以 nums1 中没有元素。
```
**提示：**
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
**进阶：**你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？
**思路**：从后往前遍历，将较大的元素放到 nums1 末尾。三个指针：`p1=nums1有效末尾`、`p2=nums2末尾`、`p=合并后的末尾`。避免了从前往后需要移动大量元素的 O(n²) 问题。
**代码**：
```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead."""
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]
```

### 3. 移除元素（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/remove-element/)
**难度**：简单
**题目**：给你一个数组 `nums` 和一个值 `val`，你需要 **原地** 移除所有数值等于 `val` 的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。假设 `nums` 中不等于 `val` 的元素数量为 `k`，你需要将 `nums` 的前 `k` 个元素设为不等于 `val` 的值，并返回 `k`。
**示例 1：**
```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数应该返回 k = 2，且 nums 的前两个元素均为 2。
```
**示例 2：**
```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，且 nums 的前五个元素为 0,1,3,0,4。
```
**思路**：快慢指针。`slow` 指向下一个待写入位置，`fast` 遍历数组。当 `nums[fast] != val` 时，将 `nums[fast]` 复制到 `nums[slow]`，并 `slow += 1`。最终 `slow` 即为新数组长度。
**代码**：
```python
def removeElement(nums: list[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 4. 删除有序数组中的重复项（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)
**难度**：简单
**题目**：给你一个 **非严格递增排列** 的数组 `nums` ，请你 **原地** 删除重复出现的元素，使每个元素 **只出现一次**，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致**。`nums` 的前 `k` 个元素应包含排序后的唯一数字。
**示例 1：**
```
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回 k = 2，且 nums 的前两个元素为 1 和 2。
```
**示例 2：**
```
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
解释：函数应该返回 k = 5，且 nums 的前五个元素为 0,1,2,3,4。
```
**思路**：快慢指针。`slow` 指向已去重部分的末尾，`fast` 遍历。当 `nums[fast] != nums[slow-1]` 时，说明遇到新元素，写入 `nums[slow]` 并移动 `slow`。因为数组已有序，相同元素必然相邻。
**代码**：
```python
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 5. 删除有序数组中的重复项 II（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)
**难度**：中等
**题目**：给你一个有序数组 `nums` ，请你 **原地** 删除重复出现的元素，使得出现次数超过两次的元素 **只出现两次**，返回删除后数组的新长度。不要使用额外的数组空间，你必须在 **原地** 修改输入数组并在使用 O(1) 额外空间的条件下完成。
**示例 1：**
```
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3,_]
解释：函数应返回 k = 5，且 nums 的前五个元素为 1,1,2,2,3。
```
**示例 2：**
```
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3,_,_]
解释：函数应返回 k = 7，且 nums 的前七个元素为 0,0,1,1,2,3,3。
```
**思路**：在 I 的基础上允许每个元素最多出现两次。用 `slow` 指向下一个写入位置，判断条件改为 `nums[fast] != nums[slow-2]`。因为如果 `nums[slow-2] == nums[fast]`，说明已经有至少两个相同元素了。
**代码**：
```python
def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 6. 多数元素（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/majority-element/)
**难度**：简单
**题目**：给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。你可以假设数组是非空的，并且给定的数组总是存在多数元素。
**示例 1：**
```
输入：nums = [3,2,3]
输出：3
```
**示例 2：**
```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```
**思路**：**Boyer-Moore 投票算法**。核心思想：不同元素相互抵消。维护一个 `candidate` 和 `count`。遍历时如果 `count == 0`，选当前元素为 candidate；遇到相同元素 count+1，不同则 count-1。最终 candidate 即为多数元素（因为题目保证多数元素的出现次数 > n/2）。
**代码**：
```python
def majorityElement(nums: list[int]) -> int:
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```

## 📝 总结
- **双指针是数组原地操作的核心技巧**，6道题中有5道使用了快慢/头尾指针
- 快慢指针的通用模板：`slow` 指向已处理部分的末尾，`fast` 遍历未处理部分
- 删除重复元素时，关键是确定"保留条件"——比较 `nums[fast]` 和 `nums[slow - k]`，其中 k 是允许的最大重复次数
- Boyer-Moore 投票算法是求多数元素的线性时间、常数空间最优解，理解"抵消"的思想很重要


---

# Day 02: 数组进阶操作

## 📖 知识点
**状态机与贪心策略**：
- **状态机**：在股票问题中，用状态变量（持有/不持有）代表不同阶段的决策，通过状态转移方程更新最优解
- **贪心算法**：每一步都做出当前最优选择，从而得到全局最优。适用于具有"最优子结构"的问题
- **跳跃游戏**：维护当前能到达的最远位置，贪心地选择跳跃范围

## 🧩 刷题任务（6题）

### 1. 轮转数组（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/rotate-array/)
**难度**：中等
**题目**：给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

**示例 1:**
```
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
```
**示例 2:**
```
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
```
**提示：**

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

**进阶：**

- 尽可能想出更多的解决方案，至少有 **三种**不同的方法可以解决这个问题。
- 你可以使用空间复杂度为 `O(1)` 的**原地**算法解决这个问题吗？
**思路**：三次翻转法。先将整体翻转，再翻转前 k 个，再翻转后 n-k 个。注意 k 可能大于 n，先取模 `k %= n`。空间 O(1)。
**代码**：
```python
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    if k == 0:
        return

    def reverse(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
```
### 2. 买卖股票的最佳时机（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
**难度**：简单
**题目**：给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天**买入这只股票，并选择在**未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```
**示例 2：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```
**提示：**

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
**思路**：一次遍历，维护历史最低价 `min_price`，不断计算当前卖出能获得的最大利润 `price - min_price`，更新全局最大利润。
**代码**：
```python
def maxProfit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
```
### 3. 买卖股票的最佳时机 II（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)
**难度**：简单
**题目**：给你一个整数数组 `prices` ，其中 `prices[i]` 表示某支股票第 `i` 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 **最多**只能持有 **一股**股票。你也可以先购买，然后在 **同一天**出售。

返回你能获得的 **最大**利润。

**示例 1：**
```
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 利润 = 5-1 = 4 。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 利润 = 6-3 = 3 。
总利润 = 4 + 3 = 7 。
```
**示例 2：**
```
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 利润 = 5-1 = 4 。
总利润 = 4 。
```
**示例 3：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。
```
**提示：**

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
**思路**：**贪心**。可以无限次交易，只要今天比昨天价格高，就在昨天买今天卖。累加所有正收益。相当于把所有上涨的波段的差值和相加。
**代码**：
```python
def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```
### 4. 跳跃游戏（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/jump-game/)
**难度**：中等
**题目**：给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
```
**示例 2：**
```
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
```
**提示：**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`
**思路**：**贪心**。维护当前能到达的最远位置 `max_reach`。遍历每个位置，如果当前位置已经超过 `max_reach` 则无法到达。否则用 `i + nums[i]` 更新 `max_reach`。最后检查 `max_reach >= n-1`。
**代码**：
```python
def canJump(nums: list[int]) -> bool:
    max_reach = 0
    for i, step in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + step)
    return True
```
### 5. 跳跃游戏 II（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/jump-game-ii/)
**难度**：中等
**题目**：给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置为 `nums[0]`。

每个元素 `nums[i]` 表示从索引 `i` 向前跳转的最大长度。换句话说，如果你在 `nums[i]` 处，你可以跳转到任意 `nums[i + j]` 处：

- `0 <= j <= nums[i]`
- `i + j < n`

返回到达 `nums[n - 1]` 的最小跳跃次数。生成的测试用例可以到达 `nums[n - 1]`。

**示例 1：**
```
输入：nums = [2,3,1,1,4]
输出：2
解释：跳到最后一个位置的最小跳跃数是 2。
从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达最后一个位置。
```
**示例 2：**
```
输入：nums = [2,3,0,1,4]
输出：2
```
**提示：**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`
**思路**：**贪心 + BFS 思想**。用 `cur_end` 表示当前跳跃能到达的边界，`farthest` 表示在当前步数范围内能到达的最远位置。当遍历到 `cur_end` 时，步数 +1，并将 `cur_end` 更新为 `farthest`。
**代码**：
```python
def jump(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(n - 1):  # 不需要遍历最后一个位置
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```
### 6. H 指数（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/h-index/)
**难度**：中等
**题目**：给你一个整数数组 `citations` ，其中 `citations[i]` 表示研究者的第 `i` 篇论文被引用的次数。计算并返回该研究者的 **`h` 指数**。

根据维基百科上 h 指数的定义：`h` 代表"高引用次数" ，一名科研人员的 `h` 指数是指他（她）至少发表了 `h` 篇论文，并且**至少**有 `h` 篇论文被引用次数大于等于 `h` 。如果 `h` 有多种可能的值，**`h` 指数**是其中最大的那个。

**示例 1：**
```
输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
```
**示例 2：**
```
输入：citations = [1,3,1]
输出：1
```
**提示：**

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`
**思路**：**排序法**。先将引用次数降序排列。从前往后找最大的 h 使得 `citations[h-1] >= h`。也可以使用计数排序（因为引用次数最多为 n）来达到 O(n) 时间复杂度。
**代码**：
```python
def hIndex(citations: list[int]) -> int:
    n = len(citations)
    # 计数排序思想：引用数 > n 的记为 n
    count = [0] * (n + 1)
    for c in citations:
        count[min(c, n)] += 1

    total = 0
    for h in range(n, -1, -1):
        total += count[h]
        if total >= h:
            return h
    return 0
```
## 📝 总结
- **股票问题的核心是状态定义**：`dp[i][持有/不持有]` 或贪心累积正波动
- **贪心的关键是证明最优子结构**：局部最优选择不影响后续全局最优
- 跳跃游戏 II 中，边界更新的方式类似于 BFS 的层序遍历，需要理解「步数」和「可达范围」的关系
- H 指数的计数排序是利用了题目中引用次数的上限为 n 这一约束


---

# Day 03: 数组 + 数学

## 📖 知识点
**左右遍历 / 前缀积 / 双指针**：
- **前缀积+后缀积**：将问题分解为"左边所有元素的积 × 右边所有元素的积"，用两次遍历分别计算
- **左右遍历**：在处理接雨水、分糖果等问题时，从左到右和从右到左两次遍历可以分别处理不同方向的约束
- **接雨水双指针**：左右指针向中间移动，记录左右两侧的最大高度，用较矮的一侧决定当前位置的储水量

## 🧩 刷题任务（6题）

### 1. 除自身以外数组的乘积（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/product-of-array-except-self/)
**难度**：中等
**题目**：给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除了 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证**数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在**32 位**整数范围内。

请**不要使用除法，**且在 `O(n)` 时间复杂度内完成此题。

**示例 1:**
```
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
```
**示例 2:**
```
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
```
**提示：**

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`

**进阶：**你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为**额外空间。）
**思路**：前缀积 × 后缀积。第一遍从左到右，`answer[i]` 存 `nums[i]` 左边所有数的乘积。第二遍从右到左，用一个变量 `suffix` 记录右边所有数的乘积，乘到 `answer[i]` 上。空间 O(1) 除输出数组外。
**代码**：
```python
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # 前缀积
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # 后缀积
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```
### 2. 加油站（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/gas-station/)
**难度**：中等
**题目**：在一条环路上有 `n` 个加油站，其中第 `i` 个加油站有汽油 `gas[i]` 升。

你有一辆油箱容量无限的的汽车，从第 `i` 个加油站开往第 `i+1` 个加油站需要消耗汽油 `cost[i]` 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 `gas` 和 `cost` ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 `-1` 。如果存在解，则 **保证**它是**唯一** 的。

**示例 1:**
```
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
```
**示例 2:**
```
输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
```
**提示:**

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i] <= 10^4`
- `0 <= cost[i] <= 10^4`

- 输入保证答案唯一。
**思路**：**贪心**。从 `start` 出发，`total_gas` 记录总剩余油量，`cur_gas` 记录从当前起点出发的累计剩余。如果 `cur_gas < 0`，说明从 `start` 到当前位置之间任何点都无法到达终点，将起点设为 `i+1` 并重置 `cur_gas`。如果 `total_gas < 0` 则无解。
**代码**：
```python
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    start = total_gas = cur_gas = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_gas += diff
        cur_gas += diff
        if cur_gas < 0:
            start = i + 1
            cur_gas = 0
    return start if total_gas >= 0 else -1
```
### 3. 分发糖果（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/candy/)
**难度**：困难
**题目**：`n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

- 每个孩子至少分配到 `1` 个糖果。

- 相邻两个孩子中，评分更高的那个会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。

**示例 1：**
```
输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
```
**示例 2：**
```
输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
```
**提示：**

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`
**思路**：**左右两次遍历**。先从左到右：如果 `ratings[i] > ratings[i-1]`，则 `candies[i] = candies[i-1] + 1`，否则为 1。再从右到左：如果 `ratings[i] > ratings[i+1]`，则 `candies[i] = max(candies[i], candies[i+1] + 1)`。两次遍历结果取最大值。
**代码**：
```python
def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    # 从左到右
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # 从右到左
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
```
### 4. 接雨水（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/trapping-rain-water/)
**难度**：困难
**题目**：给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例 1：**
```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
```
**示例 2：**
```
输入：height = [4,2,0,3,2,5]
输出：9
```
**提示：**

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`
**思路**：**双指针**。左右指针向中间移动，维护 `left_max` 和 `right_max`。当 `height[left] < height[right]` 时，左边是短板，当前位置能接的水 = `left_max - height[left]`（如果左指针处高度小于左最大高度）。对称处理右边。不需要额外数组。
**代码**：
```python
def trap(height: list[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```
### 5. 种花问题（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/can-place-flowers/)
**难度**：简单
**题目**：假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 `flowerbed` 表示花坛，由若干 `0` 和 `1` 组成，其中 `0` 表示没种植花，`1` 表示种植了花。另有一个数 `n` ，能否在不打破种植规则的情况下种入 `n` 朵花？能则返回 `true` ，不能则返回 `false` 。

**示例 1：**
```
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
```
**示例 2：**
```
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
```
**提示：**

- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` 为 `0` 或 `1`
- `flowerbed` 中不存在相邻的两朵花
- `0 <= n <= flowerbed.length`
**思路**：**贪心**。遍历花坛，如果当前位置能种花（`flowerbed[i] == 0` 且左右邻居都没有花），就种下并减少待种数量。注意边界处理：首尾只需要检查一侧。
**代码**：
```python
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
```
### 6. 拥有最多糖果的孩子（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/)
**难度**：简单
**题目**：有 `n` 个有糖果的孩子。给你一个数组 `candies`，其中 `candies[i]` 代表第 `i` 个孩子拥有的糖果数目，和一个整数 `extraCandies` 表示你所有的额外糖果的数量。

返回一个长度为 `n` 的布尔数组 `result`，如果把所有的 `extraCandies` 给第 `i` 个孩子之后，他会拥有所有孩子中 **最多**的糖果，那么 `result[i]` 为 `true`，否则为 `false`。

注意，允许有多个孩子同时拥有 **最多** 的糖果数目。

**示例 1：**
```
输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true]
解释：如果你把额外的糖果全部给：
孩子 1，将有 2 + 3 = 5 个糖果，是孩子中最多的。
孩子 2，将有 3 + 3 = 6 个糖果，是孩子中最多的。
孩子 3，将有 5 + 3 = 8 个糖果，是孩子中最多的。
孩子 4，将有 1 + 3 = 4 个糖果，不是孩子中最多的。
孩子 5，将有 3 + 3 = 6 个糖果，是孩子中最多的。
```
**示例 2：**
```
输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false]
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。
```
**示例 3：**
```
输入：candies = [12,1,12], extraCandies = 10
输出：[true,false,true]
```
**提示：**

- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`
**思路**：先找到当前最大值，然后对每个孩子判断 `candies[i] + extraCandies >= max_candies`。
**代码**：
```python
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    return [c + extraCandies >= max_candies for c in candies]
```
## 📝 总结
- **前缀积**是"除自身以外乘积"问题的标准解法，本质是分解成两个独立子问题
-**左右两次遍历**适用于同时受左右两侧约束的问题（分糖果、接雨水的单调栈解法也是类似思路）
-**接雨水的双指针法**是 O(1) 空间的最优解，关键在于理解"短板效应"——由较矮的一侧决定水位
-**加油站问题** 的核心结论是：如果从 A 到 B 无法到达，则 A 到 B 之间任意一点也无法到达终点


---

# Day 04: 哈希集合

## 📖 知识点
**哈希集合 (HashSet)**：
- 基于哈希表实现，存储不重复元素
- 查询/插入/删除平均时间复杂度 O(1)
- 常用于：去重、判断是否存在、记录访问状态、O(1) 查找
- Python 中的 set 和 frozenset

**连续序列问题** 的核心模式：用 set 存储所有元素，然后只从"序列起点"（即 `num-1` 不在 set 中）开始向后计数，避免重复计算。

## 🧩 刷题任务（6题）

### 1. 两数之和（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/two-sum/)
**难度**：简单
**题目**：给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target` 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

**示例 1：**
```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```
**示例 2：**
```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```
**示例 3：**
```
输入：nums = [3,3], target = 6
输出：[0,1]
```
**提示：**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **只会存在一个有效答案**

**进阶：**你可以想出一个时间复杂度小于 `O(n²)` 的算法吗？
**思路**：用哈希表（dict）存储已经遍历过的数字及其下标。遍历时，计算 `target - nums[i]` 是否已在哈希表中，如果是则返回两个下标。
**代码**：
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
### 2. 快乐数（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/happy-number/)
**难度**：简单
**题目**：编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」**定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。

- 然后重复这个过程直到这个数变为 1，也可能是**无限循环**但始终变不到 1。

- 如果这个过程**结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**
```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
**示例 2：**
```
输入：n = 2
输出：false
```
**提示：**

- `1 <= n <= 2^31 - 1`
**思路**：用 HashSet 记录已经出现过的数字，如果重复出现则进入循环，返回 False。或者用快慢指针检测循环（类似链表检测环）。
**代码**：
```python
def isHappy(n: int) -> bool:
    def get_next(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
```
### 3. 存在重复元素 II（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/contains-duplicate-ii/)
**难度**：简单
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true`；否则，返回 `false` 。

**示例 1：**
```
输入：nums = [1,2,3,1], k = 3
输出：true
```
**示例 2：**
```
输入：nums = [1,0,1,1], k = 1
输出：true
```
**示例 3：**
```
输入：nums = [1,2,3,1,2,3], k = 2
输出：false
```
**提示：**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`
**思路**：滑动窗口 + HashSet。维护一个大小为 k 的窗口，窗口内如有重复则返回 True。用 set 存储窗口内的元素，当窗口大小超过 k 时移除最左边的元素。
**代码**：
```python
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```
### 4. 最长连续序列（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/longest-consecutive-sequence/)
**难度**：中等
**题目**：给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

**示例 1：**
```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```
**示例 2：**
```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```
**示例 3：**
```
输入：nums = [1,0,1,2]
输出：3
```
**提示：**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
**思路**：用 set 存所有数字。遍历每个数字，只有当 `num - 1` 不在 set 中时（即它是连续序列的起点），才向后计数。这样每个数字最多被访问两次（一次在外层循环，一次在内层计数），时间复杂度 O(n)。
**代码**：
```python
def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0
    for num in num_set:
        # 只从序列起点开始计数
        if num - 1 not in num_set:
            cur = num
            length = 1
            while cur + 1 in num_set:
                cur += 1
                length += 1
            longest = max(longest, length)
    return longest
```
### 5. 字符串的最大公因子（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/greatest-common-divisor-of-strings/)
**难度**：简单
**题目**：对于字符串 `s` 和 `t`，只有在 `s = t + t + t + ... + t + t`（`t` 自身连接 1 次或多次）时，我们才认定 “`t` 能除尽 `s`”。

给定两个字符串 `str1` 和 `str2` 。返回 *最长字符串 `x`，要求满足 `x` 能除尽 `str1` 且 `x` 能除尽 `str2`  。

**示例 1：**
```
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
```
**示例 2：**
```
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
```
**示例 3：**
```
输入：str1 = "LEET", str2 = "CODE"
输出：""
```
**示例 4：**
```
输入：str1 = "AAAAAB", str2 = "AAA"
输出：""
```
**提示：**

- `1 <= str1.length, str2.length <= 1000`
**思路**：如果 str1 + str2 == str2 + str1，则存在公因子字符串，其长度为 gcd(len(str1), len(str2))。用数学性质：两个字符串有公因子当且仅当它们拼接后相等。
**代码**：
```python
def gcdOfStrings(str1: str, str2: str) -> str:
    from math import gcd

    if str1 + str2 != str2 + str1:
        return ""
    g = gcd(len(str1), len(str2))
    return str1[:g]
```
### 6. 赎金信（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/ransom-note/)
**难度**：简单
**题目**：给你两个字符串：`ransomNote` 和 `magazine` ，判断 `ransomNote` 能不能由 `magazine` 里面的字符构成。

如果可以，返回 `true` ；否则返回 `false` 。

`magazine` 中的每个字符只能在 `ransomNote` 中使用一次。

**示例 1：**
```
输入：ransomNote = "a", magazine = "b"
输出：false
```
**示例 2：**
```
输入：ransomNote = "aa", magazine = "ab"
输出：false
```
**示例 3：**
```
输入：ransomNote = "aa", magazine = "aab"
输出：true
```
**提示：**

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` 和 `magazine` 由小写英文字母组成
**思路**：用 Counter 统计 magazine 中每个字符的可用数量，遍历 ransomNote 中的字符，如果某个字符不够用则返回 False。
**代码**：
```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    counter = Counter(magazine)
    for ch in ransomNote:
        if counter[ch] == 0:
            return False
        counter[ch] -= 1
    return True
```
## 📝 总结
- **两数之和**是哈希表应用的经典入门题，核心是"存已遍历 + 查补数"
- **最长连续序列**的关键优化是"只从起点开始计数"，避免 O(n²)
-**快乐数**的循环检测可以用 HashSet 或快慢指针两种思路
-**存在重复元素 II** 本质是固定大小的滑动窗口 + HashSet
- 字符串公因子利用了数学性质：如果 `s1 + s2 == s2 + s1`，则它们有公因子且长度为 gcd(len(s1), len(s2))


---

# Day 05: 哈希映射

## 📖 知识点
**哈希映射 (HashMap) / Counter**：
- 键值对存储，O(1) 平均时间复杂度的增删改查
- Python 中的 dict、collections.Counter、defaultdict
- 常见应用模式：
  - **字符映射**：建立两个字符之间的一对一映射关系（双射）
  - **分组**：用排序后的字符串作为 key 分组字母异位词
  - **计数**：统计出现次数，验证频率关系

## 🧩 刷题任务（6题）

### 1. 字母异位词分组（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/group-anagrams/)
**难度**：中等
**题目**：给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

**示例 1:**
```
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
- 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
- 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
- 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
```
**示例 2:**
```
输入: strs = [""]
输出: [[""]]
```
**示例 3:**
```
输入: strs = ["a"]
输出: [["a"]]
```
**提示：**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
**思路**：将每个字符串排序后的结果作为 key，原字符串加入对应 value 列表。或者用字符计数元组作为 key（长度为 26 的 tuple），避免排序的 O(k log k)。
**代码**：
```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        # 排序法
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# 计数法（避免排序，用元组作为 key）
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     from collections import defaultdict
#     groups = defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for ch in s:
#             count[ord(ch) - ord("a")] += 1
#         groups[tuple(count)].append(s)
#     return list(groups.values())
```
### 2. 有效的字母异位词（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/valid-anagram/)
**难度**：简单
**题目**：给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。

**示例 1:**
```
输入: s = "anagram", t = "nagaram"
输出: true
```
**示例 2:**
```
输入: s = "rat", t = "car"
输出: false
```
**提示:**

- `1 <= s.length <= 5 * 10^4`
- `s` 和 `t` 仅包含小写字母

**进阶: **如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
**思路**：用长度为 26 的数组计数 s 和 t 中字符出现的次数。如果两个字符串长度不同直接返回 False。最后检查计数数组是否全为零。
**代码**：
```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord("a")] += 1
    for ch in t:
        idx = ord(ch) - ord("a")
        count[idx] -= 1
        if count[idx] < 0:
            return False
    return True
```
### 3. 同构字符串（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/isomorphic-strings/)
**难度**：简单
**题目**：给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

**示例 1：**
```
输入：s = "egg", t = "add"
输出：true
解释：
字符串 `s` 和 `t` 可以通过以下方式变得相同：
- 将 `'e'` 映射为 `'a'`。
- 将 `'g'` 映射为 `'d'`。
```
**示例 2：**
```
输入：s = "f11", t = "b23"
输出：false
解释：
字符串 `s` 和 `t` 无法变得相同，因为 `'1'` 需要同时映射到 `'2'` 和 `'3'`。
```
**示例 3：**
```
输入：s = "paper", t = "title"
输出：true
```
**提示：**

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` 和 `t` 由任意有效的 ASCII 字符组成
**思路**：双射（双向映射）。用两个字典分别存储 s→t 和 t→s 的映射关系。遍历时检查两个方向的映射是否一致：如果 s[i] 已映射到别的字符，或 t[i] 已被别的字符映射，则返回 False。
**代码**：
```python
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for ch_s, ch_t in zip(s, t):
        if (ch_s in map_s_to_t and map_s_to_t[ch_s] != ch_t) or \
           (ch_t in map_t_to_s and map_t_to_s[ch_t] != ch_s):
            return False
        map_s_to_t[ch_s] = ch_t
        map_t_to_s[ch_t] = ch_s
    return True
```
### 4. 单词规律（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/word-pattern/)
**难度**：简单
**题目**：给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循**指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。具体来说：

- `pattern` 中的每个字母都 **恰好**映射到 `s` 中的一个唯一单词。

- `s` 中的每个唯一单词都**恰好** 映射到 `pattern` 中的一个字母。

- 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

**示例1:**
```
输入: pattern = "abba", s = "dog cat cat dog"
输出: true
```
**示例 2:**
```
输入:pattern = "abba", s = "dog cat cat fish"
输出: false
```
**示例 3:**
```
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
```
**提示:**

- `1 <= pattern.length <= 300`
**思路**：与同构字符串类似，将 pattern 中的每个字母和 words 中的每个单词建立双射关系。先按空格分割字符串得到单词列表，然后使用两个字典建立双向映射。
**代码**：
```python
def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for ch, word in zip(pattern, words):
        if ch in char_to_word and char_to_word[ch] != word:
            return False
        if word in word_to_char and word_to_char[word] != ch:
            return False
        char_to_word[ch] = word
        word_to_char[word] = ch
    return True
```
### 5. 两个数组的交集（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/find-the-difference-of-two-arrays/)
**难度**：简单
**题目**：给你两个下标从 `0` 开始的整数数组 `nums1` 和 `nums2` ，请你返回一个长度为 `2` 的列表 `answer` ，其中：

- `answer[0]` 是 `nums1` 中所有**不**存在于 `nums2` 中的 **不同** 整数组成的列表。

- `answer[1]` 是 `nums2` 中所有**不**存在于 `nums1` 中的 **不同** 整数组成的列表。

**注意：**列表中的整数可以按 **任意** 顺序返回。

**示例 1：**
```
输入：nums1 = [1,2,3], nums2 = [2,4,6]
输出：[[1,3],[4,6]]
解释：
对于 nums1 ，nums1[1] = 2 出现在 nums2 中下标 0 处，然而 nums1[0] = 1 和 nums1[2] = 3 没有出现在 nums2 中。因此，answer[0] = [1,3]。
对于 nums2 ，nums2[0] = 2 出现在 nums1 中下标 1 处，然而 nums2[1] = 4 和 nums2[2] = 6 没有出现在 nums1 中。因此，answer[1] = [4,6]。
```
**示例 2：**
```
输入：nums1 = [1,2,3,3], nums2 = [1,1,2,2]
输出：[[3],[]]
解释：
对于 nums1 ，nums1[2] 和 nums1[3] 没有出现在 nums2 中。由于 nums1[2] == nums1[3] ，二者的值只需要在 answer[0] 中出现一次，故 answer[0] = [3]。
nums2 中的每个整数都在 nums1 中出现，因此，answer[1] = [] 。
```
**提示：**

- `1 <= nums1.length, nums2.length <= 1000`
**思路**：将 nums1 转为 set，遍历 nums2，如果元素在 set 中则加入结果集并从 set 移除（避免重复）。或者用两个 set 求交集运算。
**代码**：
```python
def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]
```
### 6. 独一无二的出现次数（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/unique-number-of-occurrences/)
**难度**：简单
**题目**：给你一个整数数组 `arr`，如果每个数的出现次数都是独一无二的，就返回 `true`；否则返回 `false`。

**示例 1：**
```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
```
**示例 2：**
```
输入：arr = [1,2]
输出：false
```
**示例 3：**
```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
```
**提示：**

- `1 <= arr.length <= 1000`
**思路**：用 Counter 统计每个数字的出现次数，然后检查这些次数是否互不相同。用 set 去重，比较 set 大小和 Counter 大小是否相等。
**代码**：
```python
def uniqueOccurrences(arr: list[int]) -> bool:
    from collections import Counter
    count = Counter(arr)
    return len(set(count.values())) == len(count)
```
## 📝 总结
- **字母异位词分组**的核心是找到一种标准化表示（sorted string 或 count tuple）作为哈希表的 key
- **同构字符串 / 单词规律**都涉及双射（双向映射），必须用两个哈希表保证一一对应
- **Counter**是 Python 中非常实用的计数工具，配合 set 可以快速判断频率的独特性
- **Python set 的集合运算**（差集、交集、并集）在处理数组比较时很便捷


---

# Day 06: 前缀和 + 区间

## 📖 知识点
**前缀和与区间合并**：
- **前缀和模板**：构建数组 `prefix[i]` 表示前 i 个元素的和（或 `prefix[i] = sum(nums[0:i])`）。区间 `[l, r]` 的和 = `prefix[r+1] - prefix[l]`
- **二维前缀和**：`prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + matrix[i][j]`，子矩阵和 = `prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1]`
- **区间合并**：按起点排序，遍历时维护当前合并区间的末尾，判断是否有重叠
- **贪心射气球**：按区间终点排序，每次射中最早结束的区间

## 🧩 刷题任务（6题）

### 1. 寻找最高海拔（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/find-the-highest-altitude/)
**难度**：简单
**题目**：有一个自行车手打算进行一场公路骑行，这条路线总共由 `n + 1` 个不同海拔的点组成。自行车手从海拔为 `0` 的点 `0` 开始骑行。

给你一个长度为 `n` 的整数数组 `gain` ，其中 `gain[i]` 是点 `i` 和点 `i + 1` 的 **净海拔高度差**（`0 <= gain[i] <= 100`）。
- `n == gain.length`
- `1 <= n <= 100`
**思路**：简单前缀和问题。从海拔 0 开始，遍历 gain 数组累加海拔变化，记录过程中的最大值。
**代码**：
```python
def largestAltitude(gain: list[int]) -> int:
    current = 0
    max_alt = 0
    for g in gain:
        current += g
        max_alt = max(max_alt, current)
    return max_alt
```
### 2. 寻找数组的中心下标（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/find-pivot-index/)
**难度**：简单
**题目**：给你一个整数数组 `nums` ，请计算数组的 **中心下标**。

数组**中心下标**是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 `0` ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回**最靠近左边** 的那一个。如果数组不存在中心下标，返回 `-1` 。

**示例 1：**
```
输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
```
**示例 2：**
```
输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
```
**示例 3：**
```
输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
```
**提示：**

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

**注意：**本题与主站 1991 题相同：https://leetcode.cn/problems/find-the-middle-index-in-array/
**思路**：先计算总和 total，再从左到右遍历。维护 `left_sum`，当前索引右边的和为 `total - left_sum - nums[i]`。当 `left_sum == total - left_sum - nums[i]` 时返回。注意左右边界的情况。
**代码**：
```python
def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1
```
### 3. 二维区域和检索 - 矩阵不可变（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/range-sum-query-2d-immutable/)
**难度**：中等
**题目**：给定一个二维矩阵 `matrix`，以下类型的多个请求：

- **计算其子矩形范围内元素的总和，该子矩阵的 **左上角** 为 `(row1, col1)` ，**右下角** 为 `(row2, col2)` 。

实现 `NumMatrix` 类：

- `NumMatrix(int[][] matrix)` 给定整数矩阵 `matrix` 进行初始化

- `int sumRegion(int row1, int col1, int row2, int col2)` 返回 **左上角** `(row1, col1)` 、**右下角** `(row2, col2)` 所描述的子矩阵的元素**总和** 。

**示例 1：**
```
输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]
解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
```
**提示：**

- `m == matrix.length`

- `n == matrix[i].length`

- `1 <= m, n <= 200`
- `-10^5 <= matrix[i][j] <= 10^5`
- 最多调用 `10^4` 次 `sumRegion` 方法
**思路**：预处理二维前缀和数组 `prefix`，其中 `prefix[i+1][j+1]` 表示从 (0,0) 到 (i,j) 的子矩阵和。查询时用容斥原理计算任意子矩阵的和。
**代码**：
```python
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.prefix[i + 1][j + 1] = self.prefix[i][j + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefix
        return (p[row2 + 1][col2 + 1]
                - p[row1][col2 + 1]
                - p[row2 + 1][col1]
                + p[row1][col1])
```
### 4. 合并区间（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/merge-intervals/)
**难度**：中等
**题目**：以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

**示例 1：**
```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```
**示例 2：**
```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```
**示例 3：**
```
输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
```
**提示：**

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`
**思路**：先将区间按左端点排序。遍历区间，如果当前区间的左端点大于 merged 中最后一个区间的右端点，则不重叠，直接加入；否则重叠，更新最后一个区间的右端点为两者最大值。
**代码**：
```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```
### 5. 插入区间（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/insert-interval/)
**难度**：中等
**题目**：给你一个**无重叠的**，按照区间起始端点排序的区间列表 `intervals`，其中 `intervals[i] = [starti, endi]` 表示第 `i` 个区间的开始和结束，并且 `intervals` 按照 `starti` 升序排列。同样给定一个区间 `newInterval = [start, end]` 表示另一个区间的开始和结束。

在 `intervals` 中插入区间 `newInterval`，使得 `intervals` 依然按照 `starti` 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 `intervals`。

**注意** 你不需要原地修改 `intervals`。你可以创建一个新数组然后返回它。

**示例 1：**
```
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
```
**示例 2：**
```
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
```
**提示：**

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^5`
- `intervals` 根据 `starti` 按 **升序** 排列
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`
**思路**：分三个阶段处理：先加入所有不与 newInterval 重叠且在其左侧的区间；然后合并所有与 newInterval 重叠的区间（更新 newInterval 的左右端点）；最后加入所有在其右侧的区间。
**代码**：
```python
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    i, n = 0, len(intervals)
    # 第一阶段：不重叠且在左侧
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    # 第二阶段：合并重叠区间
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    # 第三阶段：剩余区间
    while i < n:
        result.append(intervals[i])
        i += 1
    return result
```
### 6. 用最少数量的箭引爆气球（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)
**难度**：中等
**题目**：有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 `points` ，其中`points[i] = [xstart, xend]` 表示水平直径在 `xstart` 和 `xend`之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 **完全垂直**地射出。在坐标 `x` 处射出一支箭，若有一个气球的直径的开始和结束坐标为 `xstart`，`xend`， 且满足  `xstart ≤ x ≤ xend`，则该气球会被**引爆**。可以射出的弓箭的数量**没有限制** 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 `points` ，返回引爆所有气球所必须射出的 **最小** 弓箭数。

**示例 1：**
```
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。
```
**示例 2：**
```
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。
```
**示例 3：**
```
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
```
**提示:**

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= xstart < xend <= 2^31 - 1`
**思路**：**贪心**。按区间右端点排序，第一支箭射在第一个区间的右端点，然后遍历剩余区间，如果当前区间的左端点 > 箭的位置（即上一箭射不中），则需要新箭并更新箭的位置。
**代码**：
```python
def findMinArrowShots(points: list[list[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    arrow_pos = points[0][1]
    for start, end in points[1:]:
        if start > arrow_pos:
            arrows += 1
            arrow_pos = end
    return arrows
```
## 📝 总结
- **前缀和**的核心是空间换时间，预处理 O(n)，查询 O(1)
- **二维前缀和**的容斥原理公式需要记牢：`sum = prefix[i2+1][j2+1] - prefix[i1][j2+1] - prefix[i2+1][j1] + prefix[i1][j1]`
- **区间合并**三步法：排序 → 判断重叠（`interval[0] > merged[-1][1]`）→ 合并或追加
- **插入区间**是区间合并的变体，关键在于分三段处理
- **射气球**的贪心策略是"每次射尽量多的气球"，按右端点排序是最优的（类似活动选择问题）


---

# Day 07: 周复习

## 📖 知识点
本周覆盖的核心知识点总览：

| 类别 | 知识点 | 代表题型 |
|------|--------|----------|
| 双指针 | 快慢指针、头尾指针、读写指针 | 移除元素、去重、合并有序数组 |
| 贪心 | 局部最优 → 全局最优 | 股票 II、跳跃游戏、加油站、射气球 |
| 左右遍历 | 前缀+后缀 | 除自身以外数组乘积、分糖果 |
| 哈希集合 | O(1) 查找、去重 | 两数之和、最长连续序列 |
| 哈希映射 | 双射、分组、计数 | 同构字符串、字母异位词分组 |
| 前缀和 | 一维/二维、区间和快速查询 | 中心下标、二维区域和检索 |
| 区间合并 | 排序+合并 | 合并区间、插入区间 |

## 🧩 刷题任务（6题 - 混合复习）

### 1. 移动零（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/move-zeroes/)
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
**思路**：快慢指针，类似移除元素。slow 指向下一个非零元素应该放置的位置，fast 遍历数组。遇到非零元素就交换到 slow 位置。
**代码**：
```python
def moveZeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```
### 2. 有效的数独（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/valid-sudoku/)
**难度**：中等
**题目**：请你判断一个 `9 x 9` 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

- 数字 `1-9` 在每一行只能出现一次。
- 数字 `1-9` 在每一列只能出现一次。
- 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。

**思路**：用三个集合数组分别记录每行、每列、每个 3×3 子数独中出现的数字。遍历时检查当前数字是否已在对应行/列/子数独中出现过。子数独索引 = (row // 3) * 3 + (col // 3)。
**代码**：
```python
def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            box_idx = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    return True
```
### 3. 盛最多水的容器（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/container-with-most-water/)
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
**思路**：双指针从两端向中间移动，计算当前面积 = 较矮高度 × 宽度。每次移动较矮的那一侧指针，因为宽度减小，只有高度可能变大才有可能得到更大面积。
**代码**：
```python
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
```
### 4. O(1) 时间插入、删除和获取随机元素（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/insert-delete-getrandom-o1/)
**难度**：中等
**题目**：实现 `RandomizedSet` 类，支持在平均时间复杂度 O(1) 内完成插入、删除和获取随机元素操作。
**思路**：组合使用哈希表（值→索引）和动态数组。插入时在数组末尾追加并记录索引；删除时将待删元素与末尾元素交换再删除（O(1)），更新哈希表；随机取用 random.choice。
**代码**：
```python
import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last_val = self.nums[-1]
        # 将最后一个元素移到被删除的位置
        self.nums[idx] = last_val
        self.val_to_idx[last_val] = idx
        # 删除最后一个元素
        self.nums.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```
### 5. 缺失的第一个正数（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/first-missing-positive/)
**难度**：困难
**题目**：给你一个未排序的整数数组 `nums` ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 `O(n)` 并且只使用常数级别额外空间的解决方案。

**思路**：**原地哈希**。将数组视为哈希表：把数字 x 放到下标 x-1 的位置。遍历数组，如果 `1 <= nums[i] <= n` 且 `nums[i] != nums[nums[i]-1]`，则交换。最后遍历，第一个 `nums[i] != i+1` 的位置即为答案。
**代码**：
```python
def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        correct_idx = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```
### 6. 生命游戏（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/game-of-life/)
**难度**：中等
**题目**：根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 `m × n` 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：`1` 即为活细胞，或 `0` 即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 `m x n` 网格面板 `board` 的当前状态，返回下一个状态。

**思路**：**原地标记法**。用特殊状态表示变化：2 表示从活→死，-1 表示从死→活。统计每个细胞周围 8 个方向的活细胞数，根据规则更新。第二次遍历将特殊状态转换回 0/1。
**代码**：
```python
def gameOfLife(board: list[list[int]]) -> None:
    m, n = len(board), len(board[0])
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1),
                  (0,1), (1,-1), (1,0), (1,1)]

    def count_live(r: int, c: int) -> int:
        cnt = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                cnt += 1
        return cnt

    for r in range(m):
        for c in range(n):
            live = count_live(r, c)
            if board[r][c] == 1 and (live < 2 or live > 3):
                board[r][c] = 2  # 活→死
            if board[r][c] == 0 and live == 3:
                board[r][c] = -1  # 死→活

    for r in range(m):
        for c in range(n):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == -1:
                board[r][c] = 1
```
## 📝 小测验

每题快速自测，检查能否在 30 秒内说出答案：

1. 合并两个有序数组（从后往前）的时间复杂度？空间复杂度？
2. 快慢指针删除重复元素时，slow 和 fast 分别代表什么？
3. Boyer-Moore 投票算法的前提条件是什么？
4. 接雨水的双指针法中，哪一侧决定当前水位？
5. 最长连续序列的优化关键是什么？
6. 字母异位词分组有哪两种常见的 key 设计？
7. 二维前缀和的容斥原理公式是什么？
8. 区间合并的第一步是什么？
9. 原地哈希的核心思想是什么？（缺失的第一个正数）
10. 随机集合删除元素时如何保证 O(1)？

**答案**：
1. O(m+n), O(1)
2. slow 指向已处理（写入）位置末尾，fast 遍历未处理部分
3. 多数元素出现次数 > n/2
4. 较矮的一侧
5. 只从序列起点（num-1 不在 set 中）开始计数
6. 排序后的字符串、长度为 26 的计数元组
7. `sum = p[i2+1][j2+1] - p[i1][j2+1] - p[i2+1][j1] + p[i1][j1]`
8. 按区间左端点排序
9. 将数组本身当作哈希表，把数字 x 放到下标 x-1 的位置
10. 将待删元素与末尾元素交换，再删除末尾元素并更新哈希表

## 📝 本周总结

Week 1 覆盖了数组和哈希表最核心的面试题型，主要收获：

1. **双指针**是数组原地操作的最重要技巧，贯穿整个数组章节
2. **哈希表**提供了 O(1) 的查找能力，是时间换空间的最佳体现
3. **贪心 + 排序**在区间问题和跳跃游戏中非常高效
4. **前缀和**将区间和查询从 O(n) 优化到 O(1)
5. **原地哈希**利用数组本身作为哈希表，空间 O(1)

建议掌握程度：D01-D03 需要达到 bug-free 手写，D04-D06 需要理解核心思路并能 10 分钟内写出代码，D07 为综合能力测试。


---


---
# 第2周·字符串与双指针
> 共计 7 天

# Day 08: 字符串基础

## 📖 知识点

**字符串常见操作：**
- 双指针（头尾指针、快慢指针）
- 字符串不可变 → 转 list 操作再 join
- 原地反转、单词反转
- 前缀匹配、Z 字形变换坐标映射
- 滑动窗口/KMP 子串匹配

**核心套路：**
1. **反转类**：左右指针交换 or 切片逆序
2. **前缀类**：逐个字符比对，不同时截断
3. **坐标变换类**：找规律映射行/列索引
4. **子串匹配**：暴力滑窗 O(n*m) 或 KMP O(n+m)

---

## 🧩 刷题任务

### 1. 反转字符串中的元音字母（⭐）
**来源**：[L75](https://leetcode.cn/problems/reverse-vowels-of-a-string/)
**难度**：简单
**题目**：给你一个字符串 `s` ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，且可能以大小写两种形式出现不止一次。

**示例 1：**
```
输入：s = "IceCreAm"
输出："AceCreIm"
解释：
`s` 中的元音是 `['I', 'e', 'e', 'A']`。反转这些元音，`s` 变为 `"AceCreIm"`.
```
**示例 2：**
```
输入：s = "leetcode"
输出："leotcede"
```
**提示：**

- `1 <= s.length <= 3 * 10^5`
- `s` 由 **可打印的 ASCII** 字符组成
**思路**：左右双指针，分别向中间移动。左指针找元音，右指针找元音，找到后交换。注意大小写都算元音。
**代码**：
```python
def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    cs = list(s)
    l, r = 0, len(cs) - 1
    while l < r:
        while l < r and cs[l] not in vowels:
            l += 1
        while l < r and cs[r] not in vowels:
            r -= 1
        cs[l], cs[r] = cs[r], cs[l]
        l += 1
        r -= 1
    return "".join(cs)
```
### 2. 反转字符串中的单词（⭐⭐） / T150
**来源**：[L75](https://leetcode.cn/problems/reverse-words-in-a-string/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。

**单词**是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的**单词**分隔开。

返回**单词**顺序颠倒且**单词** 之间用单个空格连接的结果字符串。

**注意：**输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

**示例 1：**
```
输入：s = "the sky is blue"
输出："blue is sky the"
```
**示例 2：**
```
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
```
**示例 3：**
```
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
```
**提示：**

- `1 <= s.length <= 10^4`
- `s` 包含英文大小写字母、数字和空格 `' '`
- `s` 中 **至少存在一个** 单词

**进阶：**如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 `O(1)` 额外空间复杂度的 **原地** 解法。
**思路**：先整体反转（逆序），再逐个单词反转回来；或者直接用 split 分割后逆序拼接。注意处理多余空格。
**代码**：
```python
def reverseWords(s: str) -> str:
    # 方法1：split + 逆序
    return " ".join(reversed(s.split()))

    # 方法2：双指针原地翻转（适合面试）
    # cs = list(s.strip())
    # # 先整体翻转
    # cs.reverse()
    # # 再逐个单词翻转
    # n = len(cs)
    # i = 0
    # while i < n:
    #     if cs[i] == ' ':
    #         i += 1
    #         continue
    #     j = i
    #     while j < n and cs[j] != ' ':
    #         j += 1
    #     # 翻转单词 cs[i:j]
    #     l, r = i, j - 1
    #     while l < r:
    #         cs[l], cs[r] = cs[r], cs[l]
    #         l += 1
    #         r -= 1
    #     i = j
    # # 清理多余空格
    # return " ".join("".join(cs).split())
```
### 3. 最长公共前缀（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/longest-common-prefix/)
**难度**：简单
**题目**：编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

**示例 1：**
```
输入：strs = ["flower","flow","flight"]
输出："fl"
```
**示例 2：**
```
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```
**提示：**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
**思路**：取第一个字符串作为初始前缀，遍历后续字符串，逐一比对缩短前缀。遇到空串或前缀为空时提前返回。
**代码**：
```python
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```
### 4. Z 字形变换（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/zigzag-conversion/)
**难度**：中等
**题目**：将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

**示例 1：**
```
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
```
**示例 2：**
```
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
```
**示例 3：**
```
输入：s = "A", numRows = 1
输出："A"
```
**提示：**

- `1 <= s.length <= 1000`
- `1 <= numRows <= 1000`
**思路**：模拟 Z 字形。用 `numRows` 个 `StringBuilder`，指针 curRow 上下摆动 (down/up)，把字符添加到对应行。最后拼接所有行。
**代码**：
```python
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * numRows
    cur, direction = 0, 1  # 1 = down, -1 = up
    for ch in s:
        rows[cur] += ch
        cur += direction
        if cur == 0 or cur == numRows - 1:
            direction *= -1
    return "".join(rows)
```
### 5. 最后一个单词的长度（⭐）
**来源**：[T150](https://leetcode.cn/problems/length-of-last-word/)
**难度**：简单
**题目**：给你一个字符串 `s`，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 **最后一个** 单词的长度。

**单词** 是指仅由字母组成、不包含任何空格字符的最大子字符串。

**示例 1：**
```
输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为 5。
```
**示例 2：**
```
输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为 4。
```
**示例 3：**
```
输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为 6 的"joyboy"。
```
**提示：**

- `1 <= s.length <= 10^4`
- `s` 仅有英文字母和空格 `' '` 组成
- `s` 中至少存在一个单词
**思路**：从末尾向前遍历，跳过末尾空格，计数非空格字符，遇到空格则停止。
**代码**：
```python
def lengthOfLastWord(s: str) -> int:
    count = 0
    i = len(s) - 1
    # 跳过末尾空格
    while i >= 0 and s[i] == ' ':
        i -= 1
    # 统计单词长度
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1
    return count
```
### 6. 找出字符串中第一个匹配项的下标（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)
**难度**：简单
**题目**：给你两个字符串 `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串的第一个匹配项的下标（下标从 0 开始）。如果 `needle` 不是 `haystack` 的一部分，则返回  `-1` 。

**示例 1：**
```
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
```
**示例 2：**
```
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
```
**提示：**

- `1 <= haystack.length <= 10^4`
- `1 <= needle.length <= 10^4`
- `haystack` 和 `needle` 仅由小写英文字符组成
**思路**：- 暴力：滑窗逐一比较（O(n*m)） - KMP：O(n+m) 预处理 next 数组，利用已匹配信息避免回溯
**代码**：
```python
def strStr(haystack: str, needle: str) -> int:
    # 暴力解法（面试够用）
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1

    # KMP（进阶）
    # if not needle:
    #     return 0
    # n, m = len(haystack), len(needle)
    # # 构建 next 数组
    # next_arr = [0] * m
    # j = 0
    # for i in range(1, m):
    #     while j > 0 and needle[i] != needle[j]:
    #         j = next_arr[j - 1]
    #     if needle[i] == needle[j]:
    #         j += 1
    #     next_arr[i] = j
    # # 匹配
    # j = 0
    # for i in range(n):
    #     while j > 0 and haystack[i] != needle[j]:
    #         j = next_arr[j - 1]
    #     if haystack[i] == needle[j]:
    #         j += 1
    #     if j == m:
    #         return i - m + 1
    # return -1
```
## 📌 总结
- Day 08 覆盖了字符串最基础的 6 种题型：双指针交换、单词反转、前缀匹配、坐标变换、逆序遍历、子串匹配
- 华为 OD 机考中**字符串反转、最长公共前缀、子串匹配**出现频率很高，务必熟练


---

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


---

# Day 10: 回文 / 滑动窗口

## 📖 知识点

**回文串核心套路：**
- **中心扩展法**：每个字符/两个字符为中心向外扩展 O(n²)
- **动态规划**：`dp[i][j] = s[i]==s[j] and dp[i+1][j-1]`
- **Manacher 算法**：O(n) 求最长回文子串（进阶）

**滑动窗口模板：**
```python
while right < n:
    扩展窗口
    while 窗口不满足条件:
        缩小窗口
    更新答案
```

---

## 🧩 刷题任务

### 1. 验证回文串（⭐） / O
**来源**：[T150](https://leetcode.cn/problems/valid-palindrome/)
**难度**：简单
**题目**：如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串**。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是**回文串** ，返回 `true`；否则，返回 `false`。

**示例 1：**
```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```
**示例 2：**
```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```
**示例 3：**
```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```
**提示：**

- `1 <= s.length <= 2 * 10^5`
- `s` 仅由可打印的 ASCII 字符组成
**思路**：双指针左右逼近。忽略非字母数字字符，忽略大小写。遇到非字母数字跳过。
**代码**：
```python
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
```
### 2. 验证回文串 II（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/valid-palindrome/)
**难度**：简单
**题目**：如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串**。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是**回文串** ，返回 `true`；否则，返回 `false`。

**示例 1：**
```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```
**示例 2：**
```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```
**示例 3：**
```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```
**提示：**

- `1 <= s.length <= 10^5`
- `s` 仅由可打印的 ASCII 字符组成
**思路**：最多删除一个字符。双指针遇到不匹配时，尝试删除左指针或右指针位置的字符，分别检查剩余子串是否为回文。
**代码**：
```python
def validPalindrome(s: str) -> bool:
    def check(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return check(l + 1, r) or check(l, r - 1)
        l += 1
        r -= 1
    return True
```
### 3. 回文子串（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/palindromic-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

**回文字符串** 是正着读和倒过来读一样的字符串。

**子字符串** 是字符串中的由连续字符组成的一个序列。

**示例 1：**
```
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
```
**示例 2：**
```
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```
**提示：**

- `1 <= s.length <= 1000`
**思路**：中心扩展法。每个字符（奇数长度）和每两个字符之间（偶数长度）作为中心向外扩展，统计回文个数。
**代码**：
```python
def countSubstrings(s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        # 奇数长度回文
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        # 偶数长度回文
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans
```
### 4. 最长回文子串（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/palindromic-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

**回文字符串** 是正着读和倒过来读一样的字符串。

**子字符串** 是字符串中的由连续字符组成的一个序列。

**示例 1：**
```
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
```
**示例 2：**
```
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```
**提示：**

- `1 <= s.length <= 1000`
**思路**：中心扩展法，维护最长回文的起止位置。遍历每个中心，扩展获取回文长度。
**代码**：
```python
def longestPalindrome(s: str) -> str:
    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    longest = ""
    for i in range(len(s)):
        # 奇数长度
        odd = expand(i, i)
        # 偶数长度
        even = expand(i, i + 1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest
```
### 5. 字符串的排列（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/permutation-in-string/)
**难度**：中等
**题目**：给你两个字符串 `s1` 和 `s2` ，写一个函数来判断 `s2` 是否包含 `s1` 的 排列。如果是，返回 `true` ；否则，返回 `false` 。

换句话说，`s1` 的排列之一是 `s2` 的 **子串** 。

**示例 1：**
```
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```
**示例 2：**
```
输入：s1= "ab" s2 = "eidboaoo"
输出：false
```
**提示：**

- `1 <= s1.length <= 10^4`
- `1 <= s2.length <= 10^4`
- `s1` 和 `s2` 仅包含小写字母
**思路**：滑动窗口 + 计数。固定窗口大小为 len(s1)，统计 s1 字符计数，在 s2 上滑动窗口，每次加入新字符、移除旧字符，比较计数是否一致。
**代码**：
```python
def checkInclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False
    cnt1 = [0] * 26
    cnt2 = [0] * 26
    a_ord = ord('a')
    for ch in s1:
        cnt1[ord(ch) - a_ord] += 1
    for i, ch in enumerate(s2):
        cnt2[ord(ch) - a_ord] += 1
        if i >= n1:
            cnt2[ord(s2[i - n1]) - a_ord] -= 1
        if cnt1 == cnt2:
            return True
    return False
```
### 6. 反转字符串（⭐）
**来源**：[O](https://leetcode.cn/problems/reverse-string/)
**难度**：简单
**题目**：编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `s` 的形式给出。

不要给另外的数组分配额外的空间，你必须**原地修改输入数组**、使用 O(1) 的额外空间解决这一问题。

**示例 1：**
```
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```
**示例 2：**
```
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```
**提示：**

- `1 <= s.length <= 10^5`
- `s[i]` 都是 ASCII 码表中的可打印字符
**思路**：左右指针交换字符。原地修改。
**代码**：
```python
def reverseString(s: list[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```
## 📌 总结
- 回文问题首选**中心扩展法**，比 DP 更直观且空间 O(1)
- **滑动窗口**的核心是窗口收缩和扩展的条件
- 华为 OD 回问题型常考：**验证回文串 II**（允许删一个字符）、**最长回文子串**


---

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

### 1. 无重复字符的最长子串（⭐⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
**难度**：中等
**题目**：给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串** 的长度。

**示例 1:**
```
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
```
**示例 2:**
```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
**示例 3:**
```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```
**提示：**

- `0 <= s.length <= 5 * 10^4`
- `s` 由英文字母、数字、符号和空格组成
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
### 2. 最小覆盖子串（⭐⭐⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/minimum-window-substring/)
**难度**：困难
**题目**：给定两个字符串 `s` 和 `t`，长度分别是 `m` 和 `n`，返回 s 中的 **最短窗口 子串**，使得该子串包含 `t` 中的每一个字符（**包括重复字符**）。如果没有这样的子串，返回空字符串 `""`。

测试用例保证答案唯一。

**示例 1：**
```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```
**示例 2：**
```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```
**示例 3:**
```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```
**提示：**

- `m == s.length`

- `n == t.length`

- `1 <= m, n <= 10^5`
- `s` 和 `t` 由英文字母组成

**进阶：**你能设计一个在 `O(m + n)` 时间内解决此问题的算法吗？
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
### 3. 长度最小的子数组（⭐⭐） / O
**来源**：[T150](https://leetcode.cn/problems/minimum-size-subarray-sum/)
**难度**：中等
**题目**：给定一个含有 `n` 个正整数的数组和一个正整数 `target`。

找出该数组中满足其总和大于等于 `target` 的长度最小的 **子数组** `[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度。如果不存在符合条件的子数组，返回 `0` 。

**示例 1：**
```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```
**示例 2：**
```
输入：target = 4, nums = [1,4,4]
输出：1
```
**示例 3：**
```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```
**提示：**

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

**进阶：**

- 如果你已经实现 `O(n)` 时间复杂度的解法, 请尝试设计一个 `O(n log(n))` 时间复杂度的解法。
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
### 4. 乘积小于 K 的子数组（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/subarray-product-less-than-k/)
**难度**：中等
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，请你返回子数组内所有元素的乘积严格小于 `k` 的连续子数组的数目。

**示例 1：**
```
输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
```
**示例 2：**
```
输入：nums = [1,2,3], k = 0
输出：0
```
**提示：**

- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`
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
### 5. 和为 K 的子数组（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/subarray-sum-equals-k/)
**难度**：中等
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回该数组中和为 `k` 的子数组的个数。

子数组是数组中元素的连续非空序列。

**示例 1：**
```
输入：nums = [1,1,1], k = 2
输出：2
```
**示例 2：**
```
输入：nums = [1,2,3], k = 3
输出：2
```
**提示：**

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`
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
### 6. 连续数组（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/contiguous-array/)
**难度**：中等
**题目**：给定一个二进制数组 `nums` , 找到含有相同数量的 `0` 和 `1` 的最长连续子数组，并返回该子数组的长度。

**示例 1：**
```
输入：nums = [0,1]
输出：2
说明：[0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
```
**示例 2：**
```
输入：nums = [0,1,0]
输出：2
说明：[0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
```
**示例 3：**
```
输入：nums = [0,1,1,1,1,1,0,0,0]
输出：6
解释：[1,1,1,0,0,0] 是具有相同数量 0 和 1 的最长连续子数组。
```
**提示：**

- `1 <= nums.length <= 10^5`
- `nums[i]` 不是 `0` 就是 `1`
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
### 7. 最大连续 1 的个数 III（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/max-consecutive-ones-iii/)
**难度**：中等
**题目**：给定一个二进制数组 `nums` 和一个整数 `k`，假设最多可以翻转 `k` 个 `0` ，则返回执行操作后 *数组中连续 `1` 的最大个数* 。

**示例 1：**
```
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```
**示例 2：**
```
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```
**提示：**

- `1 <= nums.length <= 10^5`
- `nums[i]` 不是 `0` 就是 `1`
- `0 <= k <= nums.length`
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
## 📌 总结
- Day 11 是滑动窗口最密集的一天，7 道题覆盖了所有窗口题型
- **华为 OD 必考**：无重复字符最长子串、和为 K 的子数组、最小覆盖子串
- 前缀和 + 哈希表是解决子数组求和问题的**万能套路**


---

# Day 12: 字符串综合

## 📖 知识点

**字符串进阶题型：**
- **异位词匹配**：滑动窗口 + 计数数组
- **原地压缩**：双指针读写
- **递增三元组**：贪心维护最小值和中间值
- **文本对齐**：模拟 + 空格均匀分配
- **拓扑排序**：外星词典（图论 + 字符串比较）
- **时间处理**：分钟统一 + 环状最小差值

---

## 🧩 刷题任务

### 1. 找到字符串中所有字母异位词（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
**难度**：中等
**题目**：给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 **异位词 **的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**示例 1:**
```
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```
**示例 2:**
```
输入: s = "abab", p = "ab"
输出：[0,1,2]
解释：
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```
**提示：**

- `1 <= s.length <= 3 * 10^4`
- `s` 和 `p` 仅包含小写字母
**思路**：固定窗口大小 = len(p)。计数数组统计字符频次。滑动窗口时加入新字符、移除旧字符，比较计数是否一致。
**代码**：
```python
def findAnagrams(s: str, p: str) -> list[int]:
    n, m = len(s), len(p)
    if n < m:
        return []
    cnt_p = [0] * 26
    cnt_w = [0] * 26
    a_ord = ord('a')
    for ch in p:
        cnt_p[ord(ch) - a_ord] += 1
    res = []
    for i, ch in enumerate(s):
        cnt_w[ord(ch) - a_ord] += 1
        if i >= m:
            cnt_w[ord(s[i - m]) - a_ord] -= 1
        if cnt_w == cnt_p:
            res.append(i - m + 1)
    return res
```
### 2. 字符串压缩（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/string-compression/)
**难度**：中等
**题目**：给你一个字符数组 `chars` ，请使用下述算法压缩：

从一个空字符串 `s` 开始。对于 `chars` 中的每组 **连续重复字符** ：

- 如果这一组长度为 `1` ，则将字符追加到 `s` 中。

- 否则，需要向 `s` 追加字符，后跟这一组的长度。

压缩后得到的字符串 `s` 不应该直接返回，需要转储到字符数组 `chars` 中。需要注意的是，如果组长度为 `10` 或 `10` 以上，则在 `chars` 数组中会被拆分为多个字符。

请在**修改完输入数组后** ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

**注意：**数组中超出返回长度的字符无关紧要，应予忽略。

**示例 1：**
```
输入：chars = ["a","a","b","b","c","c","c"]
输出：6
解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
```
**示例 2：**
```
输入：chars = ["a"]
输出：1
解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。
```
**示例 3：**
```
输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：4
解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
```
**提示：**

- `1 <= chars.length <= 2000`
**思路**：双指针原地压缩。读指针遍历，写指针写入。统计连续相同字符的个数，个数 > 1 时写入数字（可能多位数）。
**代码**：
```python
def compress(chars: list[str]) -> int:
    write = 0
    i = 0
    n = len(chars)
    while i < n:
        ch = chars[i]
        cnt = 1
        while i + cnt < n and chars[i + cnt] == ch:
            cnt += 1
        chars[write] = ch
        write += 1
        if cnt > 1:
            for c in str(cnt):
                chars[write] = c
                write += 1
        i += cnt
    return write
```
### 3. 递增的三元子序列（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/increasing-triplet-subsequence/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，判断这个数组中是否存在长度为 `3` 的递增子序列。

如果存在这样的三元组下标 `(i, j, k)` 且满足 `i < j < k` ，使得 `nums[i] < nums[j] < nums[k]` ，返回 `true` ；否则，返回 `false` 。

**提示：**

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

**进阶：**你能实现时间复杂度为 `O(n)` ，空间复杂度为 `O(1)` 的解决方案吗？
**思路**：贪心。维护两个变量 `first` 和 `second`（分别表示最小值、第二小的值）。遍历数组，遇到比 first 小的更新 first，比 first 大且比 second 小更新 second，比 second 大则找到。
**代码**：
```python
def increasingTriplet(nums: list[int]) -> bool:
    first = second = float('inf')
    for x in nums:
        if x <= first:
            first = x
        elif x <= second:
            second = x
        else:
            return True
    return False
```
### 4. 文本左右对齐（⭐⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/text-justification/)
**难度**：困难
**题目**：给定一个单词数组 `words` 和一个长度 `maxWidth` ，重新排版单词，使其成为每行恰好有 `maxWidth` 个字符，且左右两端对齐的文本。

你应该使用 “**贪心算法**” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 `' '` 填充，使得每行恰好有 *maxWidth* 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入**额外的**空格。

**注意:**

- 单词是指由非空格字符组成的字符序列。

- 每个单词的长度大于 0，小于等于 *maxWidth*。

- 输入单词数组 `words` 至少包含一个单词。

**示例 1:**
```
输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
"This    is    an",
"example  of text",
"justification.  "
]
```
**示例 2:**
```
输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
"What   must   be",
"acknowledgment  ",
"shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
因为最后一行应为左对齐，而不是左右两端对齐。
第二行同样为左对齐，这是因为这行只包含一个单词。
```
**示例 3:**
```
输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
"Science  is  what we",
"understand      well",
"enough to explain to",
"a  computer.  Art is",
"everything  else  we",
"do                  "
]
```
**提示：**

- `1 <= words.length <= 300`
**思路**：贪心分组，每行尽量多放单词。当前行长度 + 下一个单词长度 + 1 <= maxWidth 则加入。最后一行左对齐，其他行均匀分配空格。
**代码**：
```python
def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    res = []
    i = 0
    n = len(words)
    while i < n:
        # 确定当前行能放哪些单词
        j = i
        cur_len = 0
        while j < n and cur_len + len(words[j]) + (j - i) <= maxWidth:
            cur_len += len(words[j])
            j += 1
        # 当前行单词索引 [i, j)
        words_cnt = j - i
        spaces = maxWidth - cur_len
        # 最后一行或只有一个单词 → 左对齐
        if j == n or words_cnt == 1:
            line = " ".join(words[i:j])
            line += " " * (maxWidth - len(line))
        else:
            # 均匀分配空格
            each = spaces // (words_cnt - 1)
            extra = spaces % (words_cnt - 1)
            line = ""
            for k in range(words_cnt - 1):
                line += words[i + k] + " " * (each + (1 if k < extra else 0))
            line += words[j - 1]
        res.append(line)
        i = j
    return res
```
### 5. 火星词典 / 外星词典（⭐⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/alien-dictionary/)
**难度**：困难
**思路**：拓扑排序。比较相邻单词找到第一个不同字符，构建有向边。对所有字母进行拓扑排序（BFS / DFS）。
**代码**：
```python
def alienOrder(words: list[str]) -> str:
    from collections import defaultdict, deque
    # 建图
    g = defaultdict(set)
    indeg = defaultdict(int)
    for w in words:
        for ch in w:
            indeg.setdefault(ch, 0)
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # 检查非法情况：w1 是 w2 的前缀但更长
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in g[c1]:
                    g[c1].add(c2)
                    indeg[c2] += 1
                break
    # 拓扑排序
    q = deque([c for c, d in indeg.items() if d == 0])
    res = ""
    while q:
        c = q.popleft()
        res += c
        for nxt in g[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return res if len(res) == len(indeg) else ""
```
### 6. 最小时间差（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/minimum-time-difference/)
**难度**：中等
**题目**：给定一个 24 小时制（小时:分钟 **"HH:MM"**）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

**示例 1：**
```
输入：timePoints = ["23:59","00:00"]
输出：1
```
**示例 2：**
```
输入：timePoints = ["00:00","23:59","00:00"]
输出：0
```
**提示：**

- `2 <= timePoints.length <= 2 * 10^4`
- `timePoints[i]` 格式为 **"HH:MM"**
**思路**：将时间转换为分钟（0~1439）。排序后计算相邻差值，并处理首尾差值（环状）。
**代码**：
```python
def findMinDifference(timePoints: list[str]) -> int:
    minutes = []
    for t in timePoints:
        h, m = map(int, t.split(":"))
        minutes.append(h * 60 + m)
    minutes.sort()
    n = len(minutes)
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, minutes[i + 1] - minutes[i])
    # 首位环状差值
    ans = min(ans, 1440 - minutes[-1] + minutes[0])
    return ans
```
## 📌 总结
- Day 12 综合度较高，涵盖异位词、压缩、贪心、模拟、图论、时间处理
- **华为 OD 高频**：字符串压缩、递增三元组、异位词
- **文本对齐**和**外星词典**虽难，但出现频率不高，适合学有余力时攻破


---

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

### 1. 罗马数字转整数（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/roman-to-integer/)
**难度**：简单
**题目**：罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 `2` 写做 `II` ，即为两个并列的 1 。`12` 写做 `XII` ，即为 `X` + `II` 。 `27` 写做  `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。

**示例 1:**
```
输入: s = "III"
输出: 3
```
**示例 2:**
```
输入: s = "IV"
输出: 4
```
**示例 3:**
```
输入: s = "IX"
输出: 9
```
**示例 4:**
```
输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```
**示例 5:**
```
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```
**提示：**

- `1 <= s.length <= 15`
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
### 2. 整数转罗马数字（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/integer-to-roman/)
**难度**：中等
**题目**：七个不同的符号代表罗马数字，其值如下：

符号 值
I    1
V    5
X    10
L    50
C    100
D    500
M    1000

罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：

- 如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
- 如果该值以 4 或 9 开头，使用 **减法形式**，表示从以下符号中减去一个符号，例如 4 是 5 (`V`) 减 1 (`I`): `IV` ，9 是 10 (`X`) 减 1 (`I`)：`IX`。仅使用以下减法形式：4 (`IV`)，9 (`IX`)，40 (`XL`)，90 (`XC`)，400 (`CD`) 和 900 (`CM`)。
- 只有 10 的次方（`I`, `X`, `C`, `M`）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (`V`)，50 (`L`) 或 500 (`D`)。如果需要将符号附加4次，请使用 **减法形式**。

给定一个整数，将其转换为罗马数字。

**示例 1：**
```
输入：num = 3749
输出："MMMDCCXLIX"
解释：
3000 = MMM 由于 1000 (M) + 1000 (M) + 1000 (M)
700 = DCC 由于 500 (D) + 100 (C) + 100 (C)
40 = XL 由于 50 (L) 减 10 (X)
9 = IX 由于 10 (X) 减 1 (I)
注意：49 不是 50 (L) 减 1 (I) 因为转换是基于小数位
```
**示例 2：**
```
输入：num = 58
输出："LVIII"
解释：
50 = L
8 = VIII
```
**示例 3：**
```
输入：num = 1994
输出："MCMXCIV"
解释：
1000 = M
900 = CM
90 = XC
4 = IV
```
**提示：**

- `1 <= num <= 3999`
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
### 3. 判断子序列（⭐）
**来源**：[L75](https://leetcode.cn/problems/is-subsequence/)
**难度**：简单
**题目**：给定字符串 **s**和**t**，判断**s**是否为**t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

**致谢：**

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

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
### 4. 单词规律（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/word-pattern/)
**难度**：简单
**题目**：给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循**指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。具体来说：

- `pattern` 中的每个字母都 **恰好**映射到 `s` 中的一个唯一单词。
- `s` 中的每个唯一单词都**恰好** 映射到 `pattern` 中的一个字母。
- 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

**示例1:**
```
输入: pattern = "abba", s = "dog cat cat dog"
输出: true
```
**示例 2:**
```
输入:pattern = "abba", s = "dog cat cat fish"
输出: false
```
**示例 3:**
```
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
```
**提示:**

- `1 <= pattern.length <= 300`
- `1 <= s.length <= 300`
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
### 5. 删掉一个元素以后全为 1 的最长子数组（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/)
**难度**：中等
**题目**：给你一个二进制数组 `nums` ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

**示例 1：**
```
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
```
**示例 2：**
```
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
```
**示例 3：**
```
输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
```
**提示：**

- `1 <= nums.length <= 10^5`
- `nums[i]` 要么是 `0` 要么是 `1` 。
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
### 6. 定长子串中元音的最大数目（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
**难度**：中等
**题目**：给你字符串 `s` 和整数 `k` 。

请返回字符串 `s` 中长度为 `k` 的单个子字符串中可能包含的最大元音字母数。

英文中的 **元音字母 **为（`a`, `e`, `i`, `o`, `u`）。

**示例 1：**
```
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
```
**示例 2：**
```
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
```
**示例 3：**
```
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
```
**示例 4：**
```
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
```
**示例 5：**
```
输入：s = "tryhard", k = 4
输出：1
```
**提示：**

- `1 <= s.length <= 10^5`
- `1 <= k <= s.length`
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
## 📌 总结
- **罗马数字转换**是常考题，掌握从大到小贪心和特殊规则
- **单词规律**考察双向映射，注意用两个哈希表确保一一对应
- **删除一个元素变全 1**和**最大元音数**是 L75 高频定长窗口题


---

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


---


---
# 第3周·链表与栈队列
> 共计 7 天

# D15 栈基础 — 6题

> 掌握栈的 LIFO 特性，解决括号匹配、路径简化、表达式求值、相邻消除等经典问题。

---

## 1. 有效的括号
**来源**：[L20](https://leetcode.cn/problems/?search=20)
**难度**：简单
**题目**：给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

- 左括号必须用相同类型的右括号闭合。

- 左括号必须以正确的顺序闭合。

- 每个右括号都有一个对应的相同类型的左括号。

**示例 1：**
```
**输入：**s = "()"
**输出：**true
```
**示例 2：**
```
**输入：**s = "()[]{}"
**输出：**true
```
**示例 3：**
```
**输入：**s = "(]"
**输出：**false
```
**示例 4：**
```
**输入：**s = "([])"
**输出：**true
```
**示例 5：**
```
**输入：**s = "([)]"
**输出：**false
```
**提示：**

- `1 4`

- `s` 仅由括号 `'()[]{}'` 组成
**思路**：遇到左括号入栈，遇到右括号检查栈顶是否匹配，匹配则出栈，不匹配直接返回 false。最后栈为空才合法。
**代码**：
```python
def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:          # 右括号
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:                    # 左括号
            stack.append(ch)
    return not stack
```
## 2. 简化路径
**来源**：[L71](https://leetcode.cn/problems/?search=71)
**难度**：中等
**题目**：给你一个字符串 `path` ，表示指向某一文件或目录的 Unix 风格 **绝对路径 **（以 `'/'` 开头），请你将其转化为 **更加简洁的规范路径**。

在 Unix 风格的文件系统中规则如下：

- 一个点 `'.'` 表示当前目录本身。

- 此外，两个点 `'..'` 表示将目录切换到上一级（指向父目录）。

- 任意多个连续的斜杠（即，`'//'` 或 `'///'`）都被视为单个斜杠 `'/'`。

- 任何其他格式的点（例如，`'...'` 或 `'....'`）均被视为有效的文件/目录名称。

返回的 **简化路径** 必须遵循下述格式：

- 始终以斜杠 `'/'` 开头。

- 两个目录名之间必须只有一个斜杠 `'/'` 。

- 最后一个目录名（如果存在）**不能 **以 `'/'` 结尾。

- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 `'.'` 或 `'..'`）。

返回简化后得到的 **规范路径** 。

**示例 1：**
```
**输入：**path = "/home/"
**输出：**"/home"
**解释：**
应删除尾随斜杠。
```
**示例 2：**
```
**输入：**path = "/home//foo/"
**输出：**"/home/foo"
**解释：**
多个连续的斜杠被单个斜杠替换。
```
**示例 3：**
```
**输入：**path = "/home/user/Documents/../Pictures"
**输出：**"/home/user/Pictures"
**解释：**
两个点 `".."` 表示上一级目录（父目录）。
```
**示例 4：**
```
**输入：**path = "/../"
**输出：**"/"
**解释：**
不可能从根目录上升一级目录。
```
**示例 5：**
```
**输入：**path = "/.../a/../b/c/../d/./"
**输出：**"/.../b/d"
**解释：**
`"..."` 在这个问题中是一个合法的目录名。
```
**提示：**

- `1
**思路**：按 `/` 分割，遍历各部分：空串和 `.` 忽略；`..` 弹出栈顶；其他入栈。最后拼接 `'/' + '/'.join(stack)`。
**代码**：
```python
def simplifyPath(path: str) -> str:
    stack = []
    for part in path.split('/'):
        if part in ('', '.'):
            continue
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)
```
## 3. 最小栈
**来源**：[L155](https://leetcode.cn/problems/?search=155)
**难度**：中等
**题目**：设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。

- `void push(int val)` 将元素val推入堆栈。

- `void pop()` 删除堆栈顶部的元素。

- `int top()` 获取堆栈顶部的元素。

- `int getMin()` 获取堆栈中的最小元素。

**示例 1:**
```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]
解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```
**提示：**

- `-231 31 - 1`

- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用

- `push`, `pop`, `top`, and `getMin`最多被调用 `3 * 104` 次
**思路**：辅助栈同步保存当前最小值。push 时如果新值 ≤ 当前最小则入辅助栈；pop 时如果弹出值等于辅助栈顶则弹出辅助栈。
**代码**：
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```
## 4. 逆波兰表达式求值
**来源**：[L150](https://leetcode.cn/problems/?search=150)
**难度**：中等
**题目**：给你一个字符串数组 `tokens` ，表示一个根据 逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

**注意：**

- 有效的算符为 `'+'`、`'-'`、`'*'` 和 `'/'` 。

- 每个操作数（运算对象）都可以是一个整数或者另一个表达式。

- 两个整数之间的除法总是 **向零截断**。

- 表达式中不含除零运算。

- 输入是一个根据逆波兰表示法表示的算术表达式。

- 答案及所有中间计算结果可以用**32 位** 整数表示。

**示例 1：**
```
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
```
**示例 2：**
```
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
```
**示例 3：**
```
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```
**提示：**

- `1 4`

- `tokens[i]` 是一个算符（`"+"`、`"-"`、`"*"` 或 `"/"`），或是在范围 `[-200, 200]` 内的一个整数

**逆波兰表达式：**

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

- 平常使用的算式则是一种中缀表达式，如 `( 1 + 2 ) * ( 3 + 4 )` 。

- 该算式的逆波兰表达式写法为 `( ( 1 2 + ) ( 3 4 + ) * )` 。

逆波兰表达式主要有以下两个优点：

- 去掉括号后表达式无歧义，上式即便写成 `1 2 + 3 4 + * `也可以依据次序计算出正确结果。

- 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
**思路**：遍历 tokens，数字入栈；遇到运算符弹出两个数字运算后结果入栈。注意 `-` 和 `/` 的顺序（`b-a` 而非 `a-b`）。
**代码**：
```python
def evalRPN(tokens: list[str]) -> int:
    stack = []
    ops = {'+', '-', '*', '/'}
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            else: stack.append(int(a / b))  # 向零取整
        else:
            stack.append(int(t))
    return stack[0]
```
## 5. 移除星号
**来源**：[L2390](https://leetcode.cn/problems/?search=2390)
**难度**：中等
**题目**：给你一个包含若干星号 `*` 的字符串 `s` 。

在一步操作中，你可以：

- 选中 `s` 中的一个星号。

- 移除星号 **左侧**最近的那个**非星号**字符，并移除该星号自身。

返回移除**所有** 星号之后的字符串**。**

**注意：**

- 生成的输入保证总是可以执行题面中描述的操作。

- 可以证明结果字符串是唯一的。

**示例 1：**
```
输入：s = "leet**cod*e"
输出："lecoe"
解释：从左到右执行移除操作：
- 距离第 1 个星号最近的字符是 "leet**cod*e" 中的 't' ，s 变为 "lee*cod*e" 。
- 距离第 2 个星号最近的字符是 "lee*cod*e" 中的 'e' ，s 变为 "lecod*e" 。
- 距离第 3 个星号最近的字符是 "lecod*e" 中的 'd' ，s 变为 "lecoe" 。
不存在其他星号，返回 "lecoe" 。
```
**示例 2：**
```
输入：s = "erase*****"
输出：""
解释：整个字符串都会被移除，所以返回空字符串。
```
**提示：**

- `1 5`

- `s` 由小写英文字母和星号 `*` 组成

- `s` 可以执行上述操作
**思路**：栈模拟即可，遇到 `*` 出栈（栈非空），否则入栈。
**代码**：
```python
def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == '*':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)
```
## 6. 小行星碰撞
**来源**：[L735](https://leetcode.cn/problems/?search=735)
**难度**：中等
**题目**：给定一个整数数组 `asteroids`，表示在同一行的小行星。数组中小行星的索引表示它们在空间中的相对位置。

对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。

找出碰撞后剩下的所有小行星。碰撞规则：两个小行星相互碰撞，较小的小行星会爆炸。如果两颗小行星大小相同，则两颗小行星都会爆炸。两颗移动方向相同的小行星，永远不会发生碰撞。

**示例 1：**
```
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
```
**示例 2：**
```
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。
```
**示例 3：**
```
输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
```
**示例 4：**
```
输入：asteroids = [3,5,-6,2,-1,4]
输出：[-6,2,4]
解释：小行星 -6 使小行星 3 和 5 爆炸，然后继续向左移动。在另一边，小行星 2 使小行星 -1 爆炸，然后继续向右移动，没有碰撞小行星 4。
```
**提示：**

- `2 4`

- `-1000
**思路**：栈模拟。遍历行星，当前行星 `x` 向左（负）且栈顶向右（正）时碰撞。栈顶绝对值小则弹出，相等则弹出且当前行星消失，当前行星小则直接消失。否则入栈。
**代码**：
```python
def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for x in asteroids:
        while stack and x < 0 < stack[-1]:   # 只有 右→左 才碰撞
            if stack[-1] < -x:
                stack.pop()
                continue
            elif stack[-1] == -x:
                stack.pop()
            break   # 当前行星被摧毁，跳出 while
        else:       # while 未执行或正常结束 → 无碰撞
            stack.append(x)
    return stack
```
## 📦 今日总结

| 题型 | 核心技巧 | 标志 |
|------|---------|------|
| 括号匹配 | 左入右出，查配匹 | 成对出现 |
| 路径简化 | 按分隔符拆分，栈模拟 | `..` 弹出，`.` 忽略 |
| 最小栈 | 辅助栈同步最小值 | O(1) getMin |
| 表达式求值 | 数字入栈，遇符号弹出两个运算 | 后缀表达式 |
| 相邻消除 | 栈顶匹配则出栈 | 星号/退格/相邻重复 |
| 带条件碰撞 | 只有特定方向组合才触发 | 右→左碰撞 |

> 💡 **栈题心法**：遇到"最近关联""成对消除""路径回溯"类问题时，优先考虑栈。写代码时注意边界（空栈、遍历结束后的栈状态）。


---

# D16 栈进阶 — 6题

> 单调栈、递归解码、表达式计算等进阶栈应用。

---

## 1. 解码字符串
**来源**：[L394](https://leetcode.cn/problems/?search=394)
**难度**：中等
**题目**：给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。

测试用例保证输出的长度不会超过 `105`。

**示例 1：**
```
输入：s = "3[a]2[bc]"
输出："aaabcbc"
```
**示例 2：**
```
输入：s = "3[a2[c]]"
输出："accaccacc"
```
**示例 3：**
```
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
```
**示例 4：**
```
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
```
**提示：**

- `1 `s` 由小写英文字母、数字和方括号 `'[]'` 组成

- `s` 保证是一个 **有效** 的输入。

- `s` 中所有整数的取值范围为 `[1, 300]`
**思路**：两个栈分别存数字和前面的字符串。遍历时：数字入数字栈；字母累加；`[` 把当前数字和已拼字符串入栈（作为上下文保存）；`]` 弹出数字和前面的字符串拼在一起。
**代码**：
```python
def decodeString(s: str) -> str:
    num_stack = []
    str_stack = []
    cur_num = 0
    cur_str = ''
    for ch in s:
        if ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == '[':
            num_stack.append(cur_num)
            str_stack.append(cur_str)
            cur_num, cur_str = 0, ''
        elif ch == ']':
            cur_str = str_stack.pop() + cur_str * num_stack.pop()
        else:
            cur_str += ch
    return cur_str
```
## 2. 每日温度
**来源**：[L739](https://leetcode.cn/problems/?search=739)
**难度**：中等
**题目**：给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

**示例 1:**
```
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
```
**示例 2:**
```
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
```
**示例 3:**
```
输入: temperatures = [30,60,90]
输出: [1,1,0]
```
**提示：**

- `1 5`

- `30
**思路**：单调递减栈。栈存下标，遇到比栈顶大的温度时出栈并计算结果。
**代码**：
```python
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    res = [0] * n
    stack = []   # 存下标，栈顶到栈底递增（严格说栈内温度单调递减）
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res
```
## 3. 柱状图中最大的矩形
**来源**：[L84](https://leetcode.cn/problems/?search=84)
**难度**：困难
**题目**：给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

**示例 1:**
```
*
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```
**示例 2：**
```
*
输入： heights = [2,4]
输出： 4
```
**提示：**

- `1 5`

- `0 4`
**思路**：单调递增栈（存下标）。遍历时遇到更矮的柱子则弹出栈顶，以弹出高度为高，左右边界为当前下标和栈顶下标计算面积。最后清空栈。
**代码**：
```python
def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    # 末尾加 0 保证最后清空栈
    heights = heights + [0]
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
```
## 4. 最大矩形
**来源**：[L85](https://leetcode.cn/problems/?search=85)
**难度**：困难
**题目**：给定一个仅包含 `0` 和 `1` 、大小为 `rows x cols` 的二维二进制矩阵，找出只包含 `1` 的最大矩形，并返回其面积。

**示例 1：**
```
*
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
```
**示例 2：**
```
输入：matrix = [["0"]]
输出：0
```
**示例 3：**
```
输入：matrix = [["1"]]
输出：1
```
**提示：**

- `rows == matrix.length`

- `cols == matrix[0].length`

- `1
**思路**：逐行处理，将每一行看作柱状图（当前行及以上连续的 '1' 视为高度），调用 84 题的最大矩形函数求解。
**代码**：
```python
def maximalRectangle(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]: return 0
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area
```
## 5. 基本计算器
**来源**：[L224](https://leetcode.cn/problems/?search=224)
**难度**：困难
**题目**：给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 `eval()` 。

**示例 1：**
```
输入：s = "1 + 1"
输出：2
```
**示例 2：**
```
输入：s = " 2-1 + 2 "
输出：3
```
**示例 3：**
```
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
```
**提示：**

- `1 5`

- `s` 由数字、`'+'`、`'-'`、`'('`、`')'`、和 `' '` 组成

- `s` 表示一个有效的表达式

- `'+'` 不能用作一元运算(例如， `"+1"` 和 `"+(2 + 3)"` 无效)

- `'-'` 可以用作一元运算(即 `"-1"` 和 `"-(2 + 3)"` 是有效的)

- 输入中不存在两个连续的操作符

- 每个数字和运行的计算将适合于一个有符号的 32位 整数
**思路**：栈存符号和结果。当前符号 `sign`（±1），遇到数字累加，遇到 `+/-` 更新 sign，遇到 `(` 把当前结果和符号入栈然后重置，遇到 `)` 弹出之前的结果和符号进行计算。
**代码**：
```python
def calculate(s: str) -> int:
    stack = []
    res, sign, i = 0, 1, 0
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            res += sign * num
            continue
        elif ch == '+': sign = 1
        elif ch == '-': sign = -1
        elif ch == '(':
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif ch == ')':
            res = stack.pop() * res + stack.pop()
        i += 1
    return res
```
## 6. 基本计算器 II
**来源**：[L227](https://leetcode.cn/problems/?search=227)
**难度**：困难
**题目**：给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 `eval()` 。

**示例 1：**
```
输入：s = "1 + 1"
输出：2
```
**示例 2：**
```
输入：s = " 2-1 + 2 "
输出：3
```
**示例 3：**
```
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
```
**提示：**

- `1 5`

- `s` 由数字、`'+'`、`'-'`、`'('`、`')'`、和 `' '` 组成

- `s` 表示一个有效的表达式

- `'+'` 不能用作一元运算(例如， `"+1"` 和 `"+(2 + 3)"` 无效)

- `'-'` 可以用作一元运算(即 `"-1"` 和 `"-(2 + 3)"` 是有效的)

- 输入中不存在两个连续的操作符

- 每个数字和运行的计算将适合于一个有符号的 32位 整数
**思路**：一次遍历，当前数字和运算符。遇到 `+` 把数字压栈（正数），`-` 压负数，`*` 和 `/` 将栈顶出栈与当前数字运算后重新入栈。最后求和。
**代码**：
```python
def calculate(s: str) -> int:
    stack = []
    num, op = 0, '+'
    s = s.replace(' ', '')
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in '+-*/' or i == len(s) - 1:
            if op == '+': stack.append(num)
            elif op == '-': stack.append(-num)
            elif op == '*': stack.append(stack.pop() * num)
            elif op == '/': stack.append(int(stack.pop() / num))
            op = ch
            num = 0
    return sum(stack)
```
## 📦 今日总结

| 题型 | 核心思路 | 栈类型 |
|------|---------|--------|
| 解码字符串 | 双栈（数字+字符串），遇到 `[` 保存上下文 | 辅助栈 |
| 每日温度 | 单调递减栈，存下标 | 单调栈 |
| 柱状最大矩形 | 单调递增栈，遇到更矮时计算弹出高度的面积 | 单调栈 |
| 最大矩形 | 逐行转柱状图，复用 84 | 单调栈+DP |
| 基本计算器 I | 栈存括号后的结果和符号 | 辅助栈 |
| 基本计算器 II | 直接压栈，`*/` 先算 | 辅助栈 |

> 💡 **单调栈记忆**：求"下一个更大/更小"用单调栈。栈内数据保持单调（递增/递减），遇到破坏单调性的元素就出栈计算答案。


---

# D17 队列+设计 — 6题

> 队列（FIFO）、双端队列、循环队列、以及基于队列的二叉树设计题。

---

## 1. 最近的请求次数
**来源**：[L933](https://leetcode.cn/problems/?search=933)
**难度**：简单
**题目**：写一个 `RecentCounter` 类来计算特定时间范围内最近的请求。

请你实现 `RecentCounter` 类：

- `RecentCounter()` 初始化计数器，请求数为 0 。

- `int ping(int t)` 在时间 `t` 添加一个新请求，其中 `t` 表示以毫秒为单位的某个时间，并返回过去 `3000` 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 `[t-3000, t]` 内发生的请求数。

**保证** 每次对 `ping` 的调用都使用比之前更大的 `t` 值。

**示例 1：**
```
输入：
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
输出：
[null, 1, 2, 3, 3]
解释：
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
```
**提示：**

- `1 9`

- 保证每次对 `ping` 调用所使用的 `t` 值都 **严格递增**

- 至多调用 `ping` 方法 `104` 次
**思路**：队列存储所有 ping 的时间戳。每次 ping 时，将队首 `< t - 3000` 的时间弹出，返回队列长度。
**代码**：
```python
class RecentCounter:
    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.pop(0)
        return len(self.q)
```
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```
## 2. Dota2 参议院
**来源**：[L649](https://leetcode.cn/problems/?search=649)
**难度**：中等
**题目**：Dota2 的世界里有两个阵营：`Radiant`（天辉）和 `Dire`（夜魇）


Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的 **一 **项：

- **剥夺一名参议员的权利**：一名参议员可以使另一名参议员在本轮及所有后续轮次中失去所有权利。

- **宣布胜利**：如果参议员发现有权利投票的参议员都是 **同一个阵营的** ，他可以宣布胜利并决定在游戏中的有关变化。

给你一个字符串 `senate` 代表每个参议员的阵营。字母 `'R'` 和 `'D'`分别代表了 `Radiant`（天辉）和 `Dire`（夜魇）。然后，如果有 `n` 个参议员，给定字符串的大小将是 `n`。


以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。


假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 `"Radiant"` 或 `"Dire"` 。

**示例 1：**
```
输入：senate = "RD"
输出："Radiant"
解释：
第 1 轮时，第一个参议员来自 Radiant 阵营，他可以使用第一项权利让第二个参议员失去所有权利。
这一轮中，第二个参议员将会被跳过，因为他的权利被禁止了。
第 2 轮时，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人。
```
**示例 2：**
```
输入：senate = "RDD"
输出："Dire"
解释：
第 1 轮时，第一个来自 Radiant 阵营的参议员可以使用第一项权利禁止第二个参议员的权利。
这一轮中，第二个来自 Dire 阵营的参议员会将被跳过，因为他的权利被禁止了。
这一轮中，第三个来自 Dire 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利。
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
```
**提示：**

- `n == senate.length`

- `1 4`

- `senate[i]` 为 `'R'` 或 `'D'`
**思路**：两个队列分别存 R 和 D 的下标。模拟每一轮：取队首比较，小的（先投票的）可以淘汰另一个，该议员进入下一轮（下标 + n 重新入队）。直到某一方队列为空。
**代码**：
```python
from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    q_r = deque()
    q_d = deque()
    for i, ch in enumerate(senate):
        if ch == 'R': q_r.append(i)
        else: q_d.append(i)
    while q_r and q_d:
        r = q_r.popleft()
        d = q_d.popleft()
        if r < d:       # R 先投票，淘汰 D
            q_r.append(r + n)
        else:           # D 先投票，淘汰 R
            q_d.append(d + n)
    return "Radiant" if q_r else "Dire"
```
## 3. 数据流中的移动平均值
**来源**：[L346](https://leetcode.cn/problems/?search=346)
**难度**：简单
**思路**：队列维护窗口内的值，窗口溢出时弹出队首。维护 sum 避免每次都求和。
**代码**：
```python
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        return self.sum / len(self.q)
```
## 4. 完全二叉树插入器
**来源**：[L919](https://leetcode.cn/problems/?search=919)
**难度**：中等
**题目**：**完全二叉树** 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。


设计一种算法，将一个新节点插入到一棵完全二叉树中，并在插入后保持其完整。


实现 `CBTInserter` 类:

- `CBTInserter(TreeNode root)` 使用头节点为 `root` 的给定树初始化该数据结构；

- `CBTInserter.insert(int v)`  向树中插入一个值为 `Node.val == val`的新节点 `TreeNode`。使树保持完全二叉树的状态，**并返回插入节点** `TreeNode` *的父节点的值**；

- `CBTInserter.get_root()` 将返回树的头节点。

**示例 1：**
```
*
输入
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
输出
[null, 1, 2, [1, 2, 3, 4]]
解释
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
```
**提示：**

- 树中节点数量范围为 `[1, 1000]`

- `0 4` 次
**思路**：BFS 层序遍历，将所有子节点不完整的节点（缺左或缺右）加入候选队列。插入时取候选队列首个节点插入，如果插入后该节点子节点变完整了则移出候选队列，新节点加入候选队列（因为新节点左右为空）。
**代码**：
```python
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.candidates = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.candidates.append(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    def insert(self, val: int) -> int:
        node = self.candidates[0]
        new_node = TreeNode(val)
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.candidates.popleft()   # 左右都满了，移出
        self.candidates.append(new_node)
        return node.val

    def get_root(self) -> TreeNode:
        return self.root
```
## 5. 在每个树行中找最大值
**来源**：[L515](https://leetcode.cn/problems/?search=515)
**难度**：中等
**题目**：给定一棵二叉树的根节点 `root` ，请找出该二叉树中每一层的最大值。

**示例1：**
```
*
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
```
**示例2：**
```
输入: root = [1,2,3]
输出: [1,3]
```
**提示：**

- 二叉树的节点个数的范围是 `[0,104]`

- `-231 31 - 1`
**思路**：BFS 层序遍历，每层记录最大值。
**代码**：
```python
from collections import deque

def largestValues(root: TreeNode) -> list[int]:
    if not root: return []
    q = deque([root])
    res = []
    while q:
        level_max = float('-inf')
        for _ in range(len(q)):
            node = q.popleft()
            level_max = max(level_max, node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level_max)
    return res
```
## 6. 找树左下角的值
**来源**：[L513](https://leetcode.cn/problems/?search=513)
**难度**：中等
**题目**：给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边 **节点的值。


假设二叉树中至少有一个节点。


 


**示例 1:**
```
*
输入: root = [2,1,3]
输出: 1
```
**示例 2:**
```
*
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
```
**提示:**

- 二叉树的节点个数的范围是 `[1,104]`

- `-231 31 - 1`
**思路**：BFS 从右向左遍历（每层先右后左），最后一个访问的节点即最底层最左节点。或者 BFS 从左到右，每层更新第一个节点。
**代码**：
```python
from collections import deque

def findBottomLeftValue(root: TreeNode) -> int:
    q = deque([root])
    # 方法1：从右向左层序，最后一个节点即答案
    while q:
        node = q.popleft()
        if node.right: q.append(node.right)   # 先右后左
        if node.left: q.append(node.left)
    return node.val
```
def findBottomLeftValue(root: TreeNode) -> int:
    q = deque([root])
    res = root.val
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0: res = node.val   # 每层第一个
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res
```
## 📦 今日总结

| 题型 | 核心技巧 | 数据结构 |
|------|---------|---------|
| 最近请求次数 | 滑动窗口 + 队首过期 | deque |
| Dota2 参议院 | 双队列 + 轮次标记 | deque |
| 移动平均值 | 窗口队列 + 累计和 | deque |
| 完全二叉树插入器 | BFS 预筛选候选节点 | deque |
| 每行最大值 | BFS 逐层遍历 | deque |
| 左下角值 | 从右向左 BFS | deque |

> 💡 **队列心法**：BFS 层序遍历是二叉树问题的核心模板。队列本身常用于滑动窗口、轮询调度、拓扑排序等场景。Python 高频面试用 `collections.deque` 替代 `list` 做队列。


---

# D18 链表基础 — 6题

> 链表的核心操作：遍历、判环、反转、合并、相加。掌握快慢指针和 dummy 节点技巧。

---

## 1. 环形链表
**来源**：[L141](https://leetcode.cn/problems/?search=141)
**难度**：简单
**题目**：给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递 **。仅仅是为了标识链表的实际情况。

*如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

**示例 1：**
```
*
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```
**示例 2：**
```
*
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```
**示例 3：**
```
*
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```
**提示：**

- 链表中节点的数目范围是 `[0, 104]`

- `-105 5`

- `pos` 为 `-1` 或者链表中的一个 **有效索引** 。

**进阶：**你能用 `O(1)`（即，常量）内存解决此问题吗？
**思路**：快慢指针。快指针每次走两步，慢指针每次走一步，如果相遇则有环。
**代码**：
```python
def hasCycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
## 2. 环形链表 II
**来源**：[L142](https://leetcode.cn/problems/?search=142)
**难度**：简单
**题目**：给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递 **。仅仅是为了标识链表的实际情况。

*如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

**示例 1：**
```
*
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```
**示例 2：**
```
*
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```
**示例 3：**
```
*
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```
**提示：**

- 链表中节点的数目范围是 `[0, 104]`

- `-105 5`

- `pos` 为 `-1` 或者链表中的一个 **有效索引** 。

**进阶：**你能用 `O(1)`（即，常量）内存解决此问题吗？
**思路**：第一阶段快慢指针相遇（同 141）；第二阶段从 head 和相遇点同步前进，相遇处即环入口。 O ← ← ← ← ← ← ← ← ← D ↓                   ↑ A → ... → B → ... → C ↑相遇点 数学推导：快慢指针相遇后，head 到入口距离 = 相遇点到入口距离
**代码**：
```python
def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:          # 相遇
            slow = head
            while slow != fast:   # 找入口
                slow = slow.next
                fast = fast.next
            return slow
    return None
```
## 3. 相交链表
**来源**：[L160](https://leetcode.cn/problems/?search=160)
**难度**：简单
**题目**：给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交**：**

*

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

**自定义评测：**

**评测系统**的输入如下（你设计的程序**不适用**此输入）：

- `intersectVal` - 相交的起始节点的值。如果不存在相交节点，这一值为 `0`

- `listA` - 第一个链表

- `listB` - 第二个链表

- `skipA` - 在 `listA` 中（从头节点开始）跳到交叉节点的节点数

- `skipB` - 在 `listB` 中（从头节点开始）跳到交叉节点的节点数

评测系统将根据这些输入创建链式数据结构，并将两个头节点 `headA` 和 `headB` 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被**视作正确答案** 。

**示例 1：**
```
*
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```
**示例 2：**
```
*
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```
**示例 3：**
```
*
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：No intersection
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
```
**提示：**

- `listA` 中节点数目为 `m`

- `listB` 中节点数目为 `n`

- `1 4`

- `1 5`

- `0

**进阶：**你能否设计一个时间复杂度 `O(m + n)` 、仅用 `O(1)` 内存的解决方案？
**思路**：双指针。分别从 A 和 B 出发，走到末尾后转到另一个链表的头继续走，相遇点即交点。原理：两指针走过的路程相同（A+B 长度之和）。
**代码**：
```python
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB: return None
    pa, pb = headA, headB
    while pa != pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa
```
## 4. 反转链表
**来源**：[L206](https://leetcode.cn/problems/?search=206)
**难度**：简单
**题目**：给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

**示例 1：**
```
*
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```
**示例 2：**
```
*
输入：head = [1,2]
输出：[2,1]
```
**示例 3：**
```
输入：head = []
输出：[]
```
**提示：**

- 链表中节点的数目范围是 `[0, 5000]`

- `-5000

**进阶：**链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
**思路**：迭代法（前驱 prev，当前 cur，临时 next）或递归法。
**代码**：
```python
# 迭代法
def reverseList(head: ListNode) -> ListNode:
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

# 递归法
def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverseList(head.next)   # 反转后续
    head.next.next = head               # 反转当前
    head.next = None
    return new_head
```
## 5. 合并两个有序链表
**来源**：[L21](https://leetcode.cn/problems/?search=21)
**难度**：简单
**题目**：将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例 1：**
```
*
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```
**示例 2：**
```
输入：l1 = [], l2 = []
输出：[]
```
**示例 3：**
```
输入：l1 = [], l2 = [0]
输出：[0]
```
**提示：**

- 两个链表的节点数目范围是 `[0, 50]`

- `-100
**思路**：dummy 节点 + 双指针遍历比较。
**代码**：
```python
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = cur = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 if list1 else list2
    return dummy.next
```
## 6. 两数相加
**来源**：[L2](https://leetcode.cn/problems/?search=2)
**难度**：中等
**题目**：给你两个 **非空**的链表，表示两个非负的整数。它们每位数字都是按照**逆序**的方式存储的，并且每个节点只能存储**一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**
```
*
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```
**示例 2：**
```
输入：l1 = [0], l2 = [0]
输出：[0]
```
**示例 3：**
```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```
**提示：**

- 每个链表中的节点数在范围 `[1, 100]` 内

- `0
**思路**：链表遍历 + 进位。每次取两个节点和进位值相加，生成新节点。
**代码**：
```python
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        carry = sum_val // 10
        cur.next = ListNode(sum_val % 10)
        cur = cur.next
    return dummy.next
```
## 📦 今日总结

| 题型 | 核心技巧 | 时间复杂度 |
|------|---------|-----------|
| 环检测 | 快慢指针 | O(n) |
| 环入口 | 快慢指针 + 同步走 | O(n) |
| 相交链表 | 双指针走等长路径 | O(m+n) |
| 反转链表 | 三指针迭代 / 递归 | O(n) |
| 合并有序链表 | dummy + 双指针 | O(m+n) |
| 两数相加 | 遍历 + 进位处理 | O(max(m,n)) |

> 💡 **链表心法**：
> 1. **dummy 节点**：头节点可能被修改时，用 `dummy = ListNode(0); dummy.next = head` 简化逻辑
> 2. **快慢指针**：判环、找中点、找倒数第 k 个节点
> 3. **画图**：链表操作一定要画图理解指针指向


---

# D19 链表进阶 — 6题

> 链表进阶操作：删除、重排、回文、深拷贝。

---

## 1. 删除链表的倒数第 N 个节点
**来源**：[L19](https://leetcode.cn/problems/?search=19)
**难度**：中等
**题目**：给你一个链表，删除链表的倒数第 `n`  *个结点，并且返回链表的头结点。

**示例 1：**
```
*
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```
**示例 2：**
```
输入：head = [1], n = 1
输出：[]
```
**示例 3：**
```
输入：head = [1,2], n = 1
输出：[1]
```
**提示：**

- 链表中结点的数目为 `sz`

- `1

**进阶：**你能尝试使用一趟扫描实现吗？
**思路**：快慢指针。快指针先走 n 步，然后快慢指针同步走，快指针到末尾时慢指针指向待删除节点的前驱。
**代码**：
```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```
## 2. 删除链表中间节点
**来源**：[L2095](https://leetcode.cn/problems/?search=2095)
**难度**：中等
**题目**：给你一个链表的头节点 `head` 。**删除**链表的**中间节点**，并返回修改后的链表的头节点 `head` 。

长度为 `n` 链表的中间节点是从头数起第 `⌊n / 2⌋` 个节点（下标从**0** 开始），其中 `⌊x⌋` 表示小于或等于 `x` 的最大整数。

- 对于 `n` = `1`、`2`、`3`、`4` 和 `5` 的情况，中间节点的下标分别是 `0`、`1`、`1`、`2` 和 `2` 。

**示例 1：**
```
*
输入：head = [1,3,4,7,1,2,6]
输出：[1,3,4,1,2,6]
解释：
上图表示给出的链表。节点的下标分别标注在每个节点的下方。
由于 n = 7 ，值为 7 的节点 3 是中间节点，用红色标注。
返回结果为移除节点后的新链表。
```
**示例 2：**
```
*
输入：head = [1,2,3,4]
输出：[1,2,4]
解释：
上图表示给出的链表。
对于 n = 4 ，值为 3 的节点 2 是中间节点，用红色标注。
```
**示例 3：**
```
*
输入：head = [2,1]
输出：[2]
解释：
上图表示给出的链表。
对于 n = 2 ，值为 1 的节点 1 是中间节点，用红色标注。
值为 2 的节点 0 是移除节点 1 后剩下的唯一一个节点。
```
**提示：**

- 链表中节点的数目在范围 `[1, 105]` 内

- `1 5`
**思路**：快慢指针找中间节点的前驱。快指针走两步，慢指针走一步。快指针结束时慢指针停在中间节点前。
**代码**：
```python
def deleteMiddle(head: ListNode) -> ListNode:
    if not head.next: return None   # 只有一个节点
    dummy = ListNode(0, head)
    slow, fast = dummy, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head
```
def deleteMiddle(head: ListNode) -> ListNode:
    if not head.next: return None
    prev = ListNode(0, head)
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head
```
## 3. 奇偶链表
**来源**：[L328](https://leetcode.cn/problems/?search=328)
**难度**：中等
**题目**：给定单链表的头节点 `head` ，将所有索引为奇数的节点和索引为偶数的节点分别分组，保持它们原有的相对顺序，然后把偶数索引节点分组连接到奇数索引节点分组之后，返回重新排序的链表。


**第一个**节点的索引被认为是 **奇数**，**第二个**节点的索引为 **偶数** ，以此类推。


请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。


你必须在 `O(1)` 的额外空间复杂度和 `O(n)` 的时间复杂度下解决这个问题。

**示例 1:**
```
*
输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]
```
**示例 2:**
```
*
输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]
```
**提示:**

- `n == ` 链表中的节点数

- `0 4`

- `-106 6`
**思路**：分离为奇数链表和偶数链表，最后将偶数链表接到奇数链表末尾。
**代码**：
```python
def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next: return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
```
## 4. 重排链表
**来源**：[L143](https://leetcode.cn/problems/?search=143)
**难度**：中等
**题目**：给定一个单链表 `L`  *的头节点 `head` ，单链表 `L` 表示为：


L0 → L1 → … → Ln - 1 → Ln

请将其重新排列后变为：


L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

**示例 1：**
```
*
输入：head = [1,2,3,4]
输出：[1,4,2,3]
```
**示例 2：**
```
*
输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]
```
**提示：**

- 链表的长度范围为 `[1, 5 * 104]`

- `1
**思路**：三步法：① 快慢指针找中点（拆分前后半段）② 反转后半段 ③ 合并前后半段。
**代码**：
```python
def reorderList(head: ListNode) -> None:
    if not head or not head.next: return
    # 1. 找中点
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 2. 反转后半段
    prev, cur = None, slow.next
    slow.next = None          # 断开前后
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # 3. 合并
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
```
## 5. 回文链表
**来源**：[L234](https://leetcode.cn/problems/?search=234)
**难度**：简单
**题目**：给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
*
输入：head = [1,2,2,1]
输出：true
```
**示例 2：**
```
*
输入：head = [1,2]
输出：false
```
**提示：**

- 链表中节点数目在范围`[1, 105]` 内

- `0

**进阶：**你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？
**思路**：找中点 → 反转后半段 → 比较前后半段 → 可选恢复链表。
**代码**：
```python
def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next: return True
    # 1. 找中点
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 2. 反转后半段
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    # 3. 比较
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True
```
## 6. 复制带随机指针的链表
**来源**：[L138](https://leetcode.cn/problems/?search=138)
**难度**：中等
**题目**：给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。


构造这个链表的 **深拷贝**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点 **。


例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。


返回复制链表的头节点。


用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

- `val`：一个表示 `Node.val` 的整数。

- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为  `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

**示例 1：**
```
*
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```
**示例 2：**
```
*
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```
**示例 3：**
```
*****
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```
**提示：**

- `0

- `-104 4`

- `Node.random` 为 `null` 或指向链表中的节点。
**思路**：三步法 O(1) 空间：① 每个原节点后复制一个新节点 ② 设置新节点的 random 指针 ③ 拆分新旧链表。
**代码**：
```python
def copyRandomList(head: 'Node') -> 'Node':
    if not head: return None
    # 1. 复制节点 A → A' → B → B' → ...
    cur = head
    while cur:
        new_node = Node(cur.val, cur.next, None)
        cur.next = new_node
        cur = new_node.next
    # 2. 设置 random
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    # 3. 拆分
    cur = head
    new_head = head.next
    while cur:
        new_node = cur.next
        cur.next = new_node.next
        new_node.next = new_node.next.next if new_node.next else None
        cur = cur.next
    return new_head
```
def copyRandomList(head: 'Node') -> 'Node':
    if not head: return None
    old_to_new = {}
    cur = head
    while cur:
        old_to_new[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        old_to_new[cur].next = old_to_new.get(cur.next)
        old_to_new[cur].random = old_to_new.get(cur.random)
        cur = cur.next
    return old_to_new[head]
```
## 📦 今日总结

| 题型 | 核心技巧 | 空间 |
|------|---------|------|
| 删倒数 N 点 | 快慢指针 + dummy | O(1) |
| 删中间节点 | 快慢指针找前驱 | O(1) |
| 奇偶链表 | 分离 + 拼接 | O(1) |
| 重排链表 | 找中点 → 反转 → 合并 | O(1) |
| 回文链表 | 找中点 → 反转 → 比较 | O(1) |
| 深拷贝 | 原链表插入副本 / 哈希表 | O(1) / O(n) |

> 💡 **链表进阶心法**：大多数链表难题可分解为"找中点""反转""合并"三个子操作的组合。建议背诵这三段代码（快慢指针、反转链表、合并链表），它们是链表操作的基本积木。


---

# D20 链表高阶 — 6题

> 链表进阶操作：区间反转、K 组反转、去重、旋转、划分、多级链表展开。

---

## 1. 反转链表 II ✅
**来源**：[LeetCode](https://leetcode.cn/problems/reverse-linked-list-ii/)
**难度**：中等
**题目**：给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left
- 链表中节点数目为 `n`

- `1

**进阶：** 你可以使用一趟扫描完成反转吗？
**Leetcode 92 · T150**

**问题**：反转链表中第 left 到第 right 个节点之间的部分。

**思路**：穿针引线法。找到 left 的前驱节点（prev），然后对区间内的节点执行头插法反转。先定位到 left 位置，然后逐个将后面的节点插入到 prev 之后。

```python
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    # 1. 走到 left 前一个节点
    for _ in range(left - 1):
        prev = prev.next
    # 2. 头插法反转 [left, right]
    cur = prev.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：头插法时 `cur.next` 指向 nxt 的下一个；`nxt.next = prev.next` 而不是 `cur`；使用 dummy 处理 left=1 的情况。

---

## 2. K 个一组反转链表 ✅
**来源**：[LeetCode](https://leetcode.cn/problems/reverse-nodes-in-k-group/)
**难度**：困难
**题目**：给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1：**
```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```
**示例 2：**
```
*
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```
**提示：**

- 链表中的节点数目为 `n`

- `1

**进阶：**你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？
**Leetcode 25 · T150**

**问题**：每 k 个节点一组反转链表，不足 k 个不反转。

**思路**：先计算链表长度，分组反转。每组内用 prev/cur/nxt 三指针反转，组间用 tail 衔接。

```python
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # 计算长度
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(n // k):
        # 反转当前组 k 个节点
        cur = prev.next
        for _ in range(k - 1):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        # 移动 prev 到组尾（即反转后的最后一个节点）
        prev = cur

    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：每组反转后 prev 定位到 cur（反转前的第一个节点，反转后是最后一个）；头插法逻辑同反转链表 II；提前算长度避免额外遍历判断。

---

## 3. 删除排序链表中的重复元素 II ✅
**来源**：[LeetCode](https://leetcode.cn/problems/sort-list/)
**难度**：中等
**题目**：给你链表的头结点 `head` ，请将其按 **升序**排列并返回**排序后的链表** 。

**示例 1：**
```
*
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```
**示例 2：**
```
*
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```
**示例 3：**
```
输入：head = []
输出：[]
```
**提示：**

- 链表中节点的数目在范围 `[0, 5 * 104]` 内

- `-105 5`

**进阶：**你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
**思路**：dummy + 双指针。prev 指向确定不重复的节点，cur 遍历检测重复。
**代码**：
```python
def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    cur = head
    while cur:
        # 跳过重复节点
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        # 判断是否有重复
        if prev.next == cur:       # 无重复
            prev = prev.next
        else:                      # 有重复，跳过所有
            prev.next = cur.next
        cur = cur.next
    return dummy.next
```
## 4. 旋转链表 ✅
**来源**：[LeetCode](https://leetcode.cn/problems/rotate-list/)
**难度**：中等
**题目**：给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动 `k`  *个位置。

**示例 1：**
```
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
```
**示例 2：**
```
*
输入：head = [0,1,2], k = 4
输出：[2,0,1]
```
**提示：**

- 链表中节点的数目在范围 `[0, 500]` 内

- `-100 9`
**Leetcode 61 · T150**

**问题**：将链表每个节点向右移动 k 个位置。

**思路**：闭合成环再断开。先遍历求长度，将 k 取模。找到新头的前驱（第 n - k%n - 1 个节点），断开得到新头。

```python
def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    # 1. 求长度并找到尾节点
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1

    # 2. 连成环
    tail.next = head

    # 3. 找到新头的前驱 (n - k%n) 步
    k %= n
    steps = n - k
    prev = head
    for _ in range(steps - 1):
        prev = prev.next

    # 4. 断开
    new_head = prev.next
    prev.next = None
    return new_head
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：k 可能很大，需要对 n 取模；断开位置是第 n - k%n 个节点（从 0 开始计数）；空链表或单节点直接返回。

---

## 5. 分隔链表 ✅
**来源**：[LeetCode](https://leetcode.cn/problems/partition-list/)
**难度**：中等
**题目**：给你一个链表的头节点 `head` 和一个特定值* *`x` ，请你对链表进行分隔，使得所有 **小于**`x` 的节点都出现在**大于或等于**`x` 的节点之前。

你应当**保留** 两个分区中每个节点的初始相对位置。

**示例 1：**
```
*
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```
**示例 2：**
```
输入：head = [2,1], x = 2
输出：[1,2]
```
**提示：**

- 链表中节点的数目在范围 `[0, 200]` 内

- `-100
**Leetcode 86 · T150**

**问题**：给定一个值 x，将链表划分，所有小于 x 的节点排在大于等于 x 的节点之前，保持原有相对顺序。

**思路**：双链表法。维护 small 链表和 large 链表，遍历原链表分别拼接，最后 small 尾接 large 头。

```python
def partition(head: ListNode, x: int) -> ListNode:
    small = ListNode(0)
    large = ListNode(0)
    p1, p2 = small, large

    while head:
        if head.val < x:
            p1.next = head
            p1 = p1.next
        else:
            p2.next = head
            p2 = p2.next
        head = head.next

    p2.next = None          # 防止大链表尾还指向原链表
    p1.next = large.next    # 小链表尾接大链表头
    return small.next
```

**复杂度**：时间 O(n)，空间 O(1)

**易错点**：`p2.next = None` 防止成环（大链表最后一个节点可能还指向小链表节点）；small 和 large 都使用 dummy 节点；保持相对顺序（稳定划分）。

---

## 6. 扁平化多级双向链表 ✅
**来源**：[LeetCode](https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/)
**难度**：中等
**题目**：你会得到一个双链表，其中包含的节点有一个下一个指针、一个前一个指针和一个额外的 **子指针**。这个子指针可能指向一个单独的双向链表，也包含这些特殊的节点。这些子列表可以有一个或多个自己的子列表，以此类推，以生成如下面的示例所示的**多层数据结构**。

给定链表的头节点 head ，将链表**扁平化** ，以便所有节点都出现在单层双链表中。让 `curr` 是一个带有子列表的节点。子列表中的节点应该出现在**扁平化列表**中的 `curr` *之后**和 `curr.next`**之前** 。

返回 *扁平列表的 `head` 。列表中的节点必须将其 **所有** 子指针设置为 `null` 。*

**示例 1：**
```
*
输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：
```
**示例 2：**
```
*
输入：head = [1,2,null,3]
输出：[1,3,2]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：
```
**示例 3：**
```
输入：head = []
输出：[]
说明：输入中可能存在空列表。
```
**提示：**

- 节点数目不超过 `1000`

- `1 5`

**如何表示测试用例中的多级链表？**

以 **示例 1** 为例：

1---2---3---4---5---6--NULL
|
7---8---9---10--NULL
|
11--12--NULL

序列化其中的每一级之后：

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

合并所有序列化结果，并去除末尾的 null 。

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
**Leetcode 430 · O**

**问题**：多级双向链表中，节点除了 next/prev 还有 child 指针。将链表扁平化，使所有节点出现在单一级别（child 变为 next）。

**思路**：DFS / 迭代。遇到有 child 的节点，将 child 链展平插入到当前节点和 next 之间。递归处理 child 子链表。

```python
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Node') -> 'Node':
    if not head:
        return head

    dummy = Node(0, None, head, None)
    stack = [head]
    prev = dummy

    while stack:
        cur = stack.pop()
        # 连接 prev <-> cur
        cur.prev = prev
        prev.next = cur

        # 先压 next（后出），再压 child（先出）
        if cur.next:
            stack.append(cur.next)
            cur.next = None        # 断开原 next
        if cur.child:
            stack.append(cur.child)
            cur.child = None       # 清空 child

        prev = cur

    dummy.next.prev = None
    return dummy.next
```

**复杂度**：时间 O(n)，空间 O(n)（栈递归深度）

**易错点**：用栈时要先推 next 再推 child（child 需要先展开）；每个节点处理完要清空 child 指针；双向链表的 prev 指针也要正确连接。

---

## 📦 今日总结

| 题型 | 核心技巧 | 复杂度 |
|------|---------|--------|
| 反转链表 II | 头插法 / 穿针引线 | O(n) O(1) |
| K 个一组反转 | 分组头插 + 组间衔接 | O(n) O(1) |
| 删除重复 II | 双指针跳过重复段 | O(n) O(1) |
| 旋转链表 | 成环再断开 | O(n) O(1) |
| 分隔链表 | 双链表法 + 拼接 | O(n) O(1) |
| 扁平化多级链表 | 栈模拟 DFS / 递归 | O(n) O(n) |

> 💡 **链表高阶技巧**：
> 1. **头插法**：反转区间的通用方法，对 [left, right] 内每个节点依次插入到 left 前驱之后
> 2. **成环再断开**：旋转链表的核心思路，避免多次遍历
> 3. **双链表法**：对链表进行条件划分时，维护两条独立链表再拼接
> 4. **栈辅助 DFS**：处理多级结构时很有用，注意入栈顺序


---

# D21 周复习 — 栈·队列·链表

> 第三周复习日：混合刷题 + 迷你测验，巩固栈、队列、链表三章核心知识点。

---

## 📖 本周知识图谱

```
Week 3: 栈 → 队列 → 链表
├── D15 栈基础: 括号匹配、最小栈、逆波兰式
├── D16 栈进阶: 单调栈(接雨水、柱状图)、表达式
├── D17 队列+设计: 滑动窗口、设计类(循环队列/LRU)
├── D18 链表基础: 环检测、反转、合并、两数相加
├── D19 链表进阶: 重排、回文、深拷贝、奇偶链表
└── D20 链表高阶: K组反转、旋转、分区、扁平化
```

**核心思想速记**：
- **栈**：后进先出，适合括号、表达式求值、单调栈（找下一个更大/更小元素）
- **队列**：先进先出，适合 BFS、滑动窗口
- **链表**：画图！dummy 节点、快慢指针、反转三板斧

---

## 🧩 刷题任务（6题）

### 1. 有效的括号 ✅
**Leetcode 20 · T150** | 难度：⭐⭐ | 标签：栈
**题目**：给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

- 左括号必须用相同类型的右括号闭合。

- 左括号必须以正确的顺序闭合。

- 每个右括号都有一个对应的相同类型的左括号。

**示例 1：**
```
**输入：**s = "()"
**输出：**true
```
**示例 2：**
```
**输入：**s = "()[]{}"
**输出：**true
```
**示例 3：**
```
**输入：**s = "(]"
**输出：**false
```
**示例 4：**
```
**输入：**s = "([])"
**输出：**true
```
**示例 5：**
```
**输入：**s = "([)]"
**输出：**false
```
**提示：**

- `1 4`

- `s` 仅由括号 `'()[]{}'` 组成

**难度**：简单
**Leetcode 20 · T150** | 难度：⭐⭐ | 标签：栈

**思路**：遇到左括号入栈，遇到右括号检查栈顶是否匹配。最后栈为空则有效。

```python
def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

**复杂度**：O(n) 时间，O(n) 空间

---

### 2. 简化路径 ✅
**Leetcode 71 · T150** | 难度：⭐⭐ | 标签：栈
**题目**：给你一个字符串 `path` ，表示指向某一文件或目录的 Unix 风格 **绝对路径 **（以 `'/'` 开头），请你将其转化为 **更加简洁的规范路径**。

在 Unix 风格的文件系统中规则如下：

- 一个点 `'.'` 表示当前目录本身。

- 此外，两个点 `'..'` 表示将目录切换到上一级（指向父目录）。

- 任意多个连续的斜杠（即，`'//'` 或 `'///'`）都被视为单个斜杠 `'/'`。

- 任何其他格式的点（例如，`'...'` 或 `'....'`）均被视为有效的文件/目录名称。

返回的 **简化路径** 必须遵循下述格式：

- 始终以斜杠 `'/'` 开头。

- 两个目录名之间必须只有一个斜杠 `'/'` 。

- 最后一个目录名（如果存在）**不能 **以 `'/'` 结尾。

**难度**：中等
**Leetcode 71 · T150** | 难度：⭐⭐ | 标签：栈

**思路**：以 `/` 分割路径，用栈处理各个部分。`..` 弹出栈顶，`.` 和空字符串忽略，其余入栈。最后用 `/` 拼接。

```python
def simplifyPath(path: str) -> str:
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)
```

**复杂度**：O(n) 时间，O(n) 空间

---

### 3. 滑动窗口最大值 ✅
**Leetcode 239 · T150** | 难度：⭐⭐⭐ | 标签：队列/单调队列
**题目**：给你一个整数数组 `nums`，有一个大小为 `k`  *的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 *滑动窗口中的最大值 *。

**示例 1：**
```
```
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
1 [3  -1  -3] 5  3  6  7       3
1  3 [-1  -3  5] 3  6  7       5
1  3  -1 [-3  5  3] 6  7       5
1  3  -1  -3 [5  3  6] 7       6
1  3  -1  -3  5 [3  6  7]      7
```
```
**难度**：困难
**Leetcode 239 · T150** | 难度：⭐⭐⭐ | 标签：队列/单调队列

**思路**：维护单调递减双端队列（存索引）。窗口右移时：① 移除超出窗口左界的索引 ② 移除队尾小于当前值的索引 ③ 当前索引入队 ④ 窗口形成后取队首值。

```python
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()
    res = []
    for i, v in enumerate(nums):
        # 移除超出窗口的索引
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # 维护单调递减
        while dq and nums[dq[-1]] < v:
            dq.pop()
        dq.append(i)
        # 窗口形成后记录结果
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

**复杂度**：O(n) 时间，O(k) 空间

---

### 4. 合并 K 个升序链表 ✅
**Leetcode 23 · T150** | 难度：⭐⭐⭐ | 标签：链表/分治/堆
**题目**：给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

**示例 1：**
```
```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
1->4->5,
1->3->4,
2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
```
```
**示例 2：**
```
```
输入：lists = []
输出：[]
```
```
**示例 3：**
```
```
输入：lists = [[]]
输出：[]
```
```
**提示：**

- `k == lists.length`

- `0 <= k <= 10^4`

- `0 <= lists[i].length <= 500`

- `-10^4 <= lists[i][j] <= 10^4`

- `lists[i]` 按 **升序** 排列

- `lists[i].length` 的总和不超过 `10^4`

**难度**：困难
**Leetcode 23 · T150** | 难度：⭐⭐⭐ | 标签：链表/分治/堆

**思路**：用最小堆（优先队列）每次取最小值。将所有链表头入堆，每次弹出最小节点，将其 next 入堆。

```python
import heapq

def mergeKLists(lists: List[ListNode]) -> ListNode:
    dummy = cur = ListNode(0)
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))

    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

**复杂度**：O(N log k) 时间（N 总节点数，k 链表数），O(k) 空间

---

### 5. 删除链表的倒数第 N 个节点 ✅
**Leetcode 19 · T150** | 难度：⭐⭐ | 标签：链表/快慢指针
**题目**：给你一个链表，删除链表的倒数第 `n`  *个结点，并且返回链表的头结点。

**示例 1：**
```
*
```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```
```
**示例 2：**
```
```
输入：head = [1], n = 1
输出：[]
```
```
**示例 3：**
```
```
输入：head = [1,2], n = 1
输出：[1]
```
```
**提示：**

- 链表中结点的数目为 `sz`

- `1 <= sz <= 30`

- `0 <= Node.val <= 100`

- `1 <= n <= sz`

**进阶：**你能尝试使用一趟扫描实现吗？

**难度**：中等
**Leetcode 19 · T150** | 难度：⭐⭐ | 标签：链表/快慢指针

**思路**：快慢指针 + dummy。快指针先走 n 步，然后快慢一起走，快指针到末尾时慢指针指向待删节点的前驱。

```python
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```

**复杂度**：O(n) 时间，O(1) 空间

---

### 6. 柱状图中最大的矩形 ✅
**Leetcode 84 · T150** | 难度：⭐⭐⭐ | 标签：单调栈
**题目**：给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

**示例 1:**
```
*
```
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```
```
**示例 2：**
```
*
```
输入： heights = [2,4]
输出： 4
```
```
**提示：**

- `1 5`

- `0 4`

**难度**：困难
**Leetcode 84 · T150** | 难度：⭐⭐⭐ | 标签：单调栈

**思路**：单调递增栈。遍历每个柱子的高度，当当前高度小于栈顶高度时，以栈顶高度为矩形高，左右边界为栈中前一个索引和当前索引。

```python
def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    heights = [0] + heights + [0]  # 前后哨兵

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
```

**复杂度**：O(n) 时间，O(n) 空间

---

## 📝 迷你测验

### 选择题（每题 10 分，共 50 分）

**Q1**：以下哪种数据结构最适合实现浏览器的「后退」功能？
- A. 队列
- B. 栈 ✅
- C. 双端队列
- D. 链表

**Q2**：判断链表是否有环，最常用的技巧是？
- A. 递归
- B. 哈希表
- C. 快慢指针 ✅
- D. 双端队列

**Q3**：单调栈的核心应用场景是？
- A. 括号匹配
- B. 寻找下一个更大/更小元素 ✅
- C. 滑动窗口最大值
- D. 链表反转

**Q4**：以下哪个问题不适合用队列解决？
- A. BFS 层序遍历
- B. 滑动窗口
- C. 逆波兰表达式求值 ✅
- D. 打印机任务调度

**Q5**：删除链表头节点时，为什么推荐使用 dummy 节点？
- A. 加快运行速度
- B. 省去特殊判断头节点的逻辑 ✅
- C. 减少空间复杂度
- D. 防止成环

### 填空题（每题 10 分，共 30 分）

**Q6**：反转链表的核心代码 `cur.next = _____`（填 prev），然后 `prev, cur = cur, nxt`。

**Q7**：当快慢指针在环中相遇后，将慢指针移回 head，然后两指针每次各走 ___ 步，相遇处即环入口。（填 1）

**Q8**：用两个栈实现队列，`push` 操作直接入 stack1，`pop` 操作时如果 stack2 为空，则将 stack1 中所有元素 ___ 到 stack2 再 pop。（填 弹出并压入 / 转移）

### 代码填空题（20 分）

**Q9**：补全「反转链表」代码：
```python
def reverseList(head: ListNode) -> ListNode:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        _____________  # 反转指针 (填: cur.next = prev)
        prev = cur
        cur = nxt
    return prev
```

---

## 📊 本周进度自评

| 章节 | 掌握度 | 薄弱环节 |
|------|--------|---------|
| D15 栈基础 | ⭐⭐⭐⭐⭐ | — |
| D16 栈进阶 | ⭐⭐⭐⭐ | 柱状图题还需练 |
| D17 队列 | ⭐⭐⭐⭐ | LRU 设计细节 |
| D18 链表基础 | ⭐⭐⭐⭐⭐ | — |
| D19 链表进阶 | ⭐⭐⭐⭐ | 深拷贝易错 |
| D20 链表高阶 | ⭐⭐⭐ | K 组反转不够熟练 |

> 💡 **复习建议**：
> - 弱题标记 🔁，下周一回头重刷
> - 链表一定要画图！纸上跑一遍指针变化
> - 单调栈模板背熟：`while stack and nums[stack[-1]] > x: pop and update`
> - 队列设计题注意边界条件（空/满/单元素）
>
> **下周预告**：二叉树 🌲 — 前中后序遍历、层序、BST、最近公共祖先


---


---
# 第4周·树与图(复习)
> 共计 7 天

# Day 22: 二叉树遍历

## 📖 知识点
二叉树遍历是所有树问题的基础。核心掌握三种递归遍历（前序、中序、后序）以及层序（BFS）的模板。前序：根→左→右；中序：左→根→右（BST中升序）；后序：左→右→根（适合自底向上处理）。

**递归模板**：
```python
def traverse(root, res):
    if not root:
        return
    res.append(root.val)   # 前序
    traverse(root.left, res)
    # res.append(root.val) # 中序
    traverse(root.right, res)
    # res.append(root.val) # 后序
```

---

## 🧩 刷题任务（6题）

### 1. Maximum Depth of Binary Tree（⭐）来源：L75 / T150
**来源**：[L75](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)
**难度**：简单
**题目**：给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：3
```
**示例 2：**
```
输入：root = [1,null,2]
输出：2
```
**提示：**

- 树中节点的数量在 `[0, 104]` 区间内。

- `-100
**思路**：递归求左右子树深度最大值 + 1。DFS后序，等价于树的高度。
**代码**：
```python
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```
### 2. Same Tree（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/same-tree/)
**难度**：简单
**题目**：给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1：**
```
*
输入：p = [1,2,3], q = [1,2,3]
输出：true
```
**示例 2：**
```
*
输入：p = [1,2], q = [1,null,2]
输出：false
```
**示例 3：**
```
*
输入：p = [1,2,1], q = [1,1,2]
输出：false
```
**提示：**

- 两棵树上的节点数目都在范围 `[0, 100]` 内

- `-104 4`
**思路**：同步遍历两棵树。如果都为空返回 True；一个为空返回 False；值不等返回 False；递归比较左右子树。
**代码**：
```python
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```
### 3. Invert Binary Tree（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/invert-binary-tree/)
**难度**：简单
**题目**：给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。

**示例 1：**
```
*
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```
**示例 2：**
```
*
输入：root = [2,1,3]
输出：[2,3,1]
```
**示例 3：**
```
输入：root = []
输出：[]
```
**提示：**

- 树中节点数目范围在 `[0, 100]` 内

- `-100
**思路**：交换左右子树，然后递归翻转。前序或后序均可。经典题，Homebrew 面试题原型。
**代码**：
```python
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
```
### 4. Symmetric Tree（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/symmetric-tree/)
**难度**：简单
**题目**：给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

**示例 1：**
```
*
输入：root = [1,2,2,3,4,4,3]
输出：true
```
**示例 2：**
```
*
输入：root = [1,2,2,null,3,null,3]
输出：false
```
**提示：**

- 树中节点数目在范围 `[1, 1000]` 内

- `-100

**进阶：**你可以运用递归和迭代两种方法解决这个问题吗？
**思路**：判断树是否轴对称。定义辅助函数比较两个节点：左树的左子树 vs 右树的右子树，左树的右子树 vs 右树的左子树。
**代码**：
```python
def isSymmetric(root: Optional[TreeNode]) -> bool:
    def check(l, r):
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return check(l.left, r.right) and check(l.right, r.left)
    return check(root.left, root.right) if root else True
```
### 5. Leaf-Similar Trees（⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/leaf-similar-trees/)
**难度**：简单
**题目**：请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 **叶值序列 **。

*

举个例子，如上图所示，给定一棵叶值序列为 `(6, 7, 4, 9, 8)` 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 *叶相似 *的。

如果给定的两个根结点分别为 `root1` 和 `root2` 的树是叶相似的，则返回 `true`；否则返回 `false` 。

**示例 1：**
```
*
输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true
```
**示例 2：**
```
*
输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false
```
**提示：**

- 给定的两棵树结点数在 `[1, 200]` 范围内

- 给定的两棵树上的值在 `[0, 200]` 范围内
**思路**：DFS 收集两棵树的叶子序列（左右子树都为空时加入），比较是否相等。
**代码**：
```python
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(node, leaves):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        dfs(node.left, leaves)
        dfs(node.right, leaves)
    l1, l2 = [], []
    dfs(root1, l1), dfs(root2, l2)
    return l1 == l2
```
### 6. Count Good Nodes in Binary Tree（⭐⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/)
**难度**：中等
**题目**：给你一棵根为 `root` 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

**示例 1：**
```
*****
输入：root = [3,1,4,3,null,1,5]
输出：4
解释：图中蓝色节点为好节点。
根节点 (3) 永远是个好节点。
节点 4 -> (3,4) 是路径中的最大值。
节点 5 -> (3,4,5) 是路径中的最大值。
节点 3 -> (3,1,3) 是路径中的最大值。
```
**示例 2：**
```
*****
输入：root = [3,3,null,4,2]
输出：3
解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
```
**示例 3：**
```
输入：root = [1]
输出：1
解释：根节点是好节点。
```
**提示：**

- 二叉树中节点数目范围是 `[1, 10^5]` 。

- 每个节点权值的范围是 `[-10^4, 10^4]` 。
**思路**：DFS 传递当前路径最大值。若当前节点值 ≥ 路径最大值，则计数 +1 并更新最大值。
**代码**：
```python
def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0
        cnt = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        cnt += dfs(node.left, max_val)
        cnt += dfs(node.right, max_val)
        return cnt
    return dfs(root, root.val)
```
## 📝 总结
Day 22 覆盖了二叉树最核心的遍历题型：最大深度（后序）、相同/翻转/对称（同步遍历比较）、叶子序列（前序收集）、好节点计数（路径最大值传递）。熟练掌握递归模板后，这些题都可以在 5 分钟内解决。


---

# Day 23: 树的构建

## 📖 知识点
树的构建问题核心在于利用遍历序列的递归性质还原二叉树。从前序/后序 + 中序构建树时，关键是找到根节点在中序中的位置，划分左右子树区间。序列化/反序列化则是前序/层序的变体，用括号或分隔符标记空节点。

**递归构建模板（前序+中序）**：
```python
def build(preorder, inorder):
    if not inorder:
        return None
    root_val = preorder.pop(0)    # 前序第一个为根
    idx = inorder.index(root_val) # 中序中找根的位置
    root = TreeNode(root_val)
    root.left = build(preorder, inorder[:idx])
    root.right = build(preorder, inorder[idx+1:])
    return root
```

---

## 🧩 刷题任务（6题）

### 1. Construct Binary Tree from Preorder and Inorder Traversal（⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
**难度**：中等
**题目**：给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**先序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

**示例 1:**
```
*
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
```
**示例 2:**
```
输入: preorder = [-1], inorder = [-1]
输出: [-1]
```
**提示:**

- `1
**思路**：前序第一个是根，在中序中找到根的位置，左边为左子树，右边为右子树。递归构建。优化：用哈希表缓存中序索引。
**代码**：
```python
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    idx_map = {v: i for i, v in enumerate(inorder)}
    pre_idx = 0

    def build(l, r):
        nonlocal pre_idx
        if l > r:
            return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)
        mid = idx_map[root_val]
        root.left = build(l, mid - 1)
        root.right = build(mid + 1, r)
        return root

    return build(0, len(inorder) - 1)
```
### 2. Construct Binary Tree from Inorder and Postorder Traversal（⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
**难度**：中等
**题目**：给定两个整数数组 `inorder` 和 `postorder` ，其中 `inorder` 是二叉树的中序遍历， `postorder` 是同一棵树的后序遍历，请你构造并返回这颗 *二叉树* 。

**示例 1:**
```
*
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
```
**示例 2:**
```
输入：inorder = [-1], postorder = [-1]
输出：[-1]
```
**提示:**

- `1
**思路**：后序最后一个（从末尾 pop）是根，在中序中定位后划分左右子树。注意先构建右子树再左子树（因为后序倒着取）。
**代码**：
```python
def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    idx_map = {v: i for i, v in enumerate(inorder)}

    def build(l, r):
        if l > r or not postorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        mid = idx_map[root_val]
        root.right = build(mid + 1, r)  # 后序倒序，先右后左
        root.left = build(l, mid - 1)
        return root

    return build(0, len(inorder) - 1)
```
### 3. Populating Next Right Pointers in Each Node II（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/)
**难度**：中等
**题目**：给定一个二叉树：

struct Node {
int val;
Node *left;
Node *right;
Node *next;
}

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL` 。

初始状态下，所有 next 指针都被设置为 `NULL` 。

**示例 1：**
```
*
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
```
**示例 2：**
```
输入：root = []
输出：[]
```
**提示：**

- 树中的节点数在范围 `[0, 6000]` 内

- `-100

**进阶：**

- 你只能使用常量级额外空间。

- 使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。
**思路**：层序遍历，用 dummy 头节点串联每层。每层遍历时把子节点串成链表，用 prev 追踪上一个节点。不要求完美二叉树。
**代码**：
```python
def connect(root: 'Node') -> 'Node':
    if not root:
        return None
    cur = root
    while cur:
        dummy = Node(0)  # 每层新建哑节点
        prev = dummy
        while cur:
            if cur.left:
                prev.next = cur.left
                prev = prev.next
            if cur.right:
                prev.next = cur.right
                prev = prev.next
            cur = cur.next
        cur = dummy.next  # 下一层
    return root
```
### 4. Flatten Binary Tree to Linked List（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)
**难度**：中等
**题目**：给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。

- 展开后的单链表应该与二叉树 **先序遍历** 顺序相同。

**示例 1：**
```
*
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
```
**示例 2：**
```
输入：root = []
输出：[]
```
**示例 3：**
```
输入：root = [0]
输出：[0]
```
**提示：**

- 树中结点数在范围 `[0, 2000]` 内

- `-100

**进阶：**你可以使用原地算法（`O(1)` 额外空间）展开这棵树吗？
**思路**：后序遍历（右→左→根）或前序迭代。最简洁方法：逆前序遍历，用全局 prev 记录上一个访问的节点，依次拼接成链表。
**代码**：
```python
def flatten(root: Optional[TreeNode]) -> None:
    prev = None

    def dfs(node):
        nonlocal prev
        if not node:
            return
        dfs(node.right)   # 先右
        dfs(node.left)    # 再左
        node.right = prev # 当前右指针指向上一个处理完的节点
        node.left = None
        prev = node

    dfs(root)
```
### 5. Serialize and Deserialize Binary Tree（⭐⭐⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)
**难度**：困难
**题目**：序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

**提示: **输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

**示例 1：**
```
*
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
```
**示例 2：**
```
输入：root = []
输出：[]
```
**示例 3：**
```
输入：root = [1]
输出：[1]
```
**示例 4：**
```
输入：root = [1,2]
输出：[1,2]
```
**提示：**

- 树中结点数在范围 `[0, 104]` 内

- `-1000
**思路**：前序序列化，用 "#" 标记空节点。反序列化时按相同顺序重建。也可用层序（BFS）。
**代码**：
```python
class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        vals = []
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(data.split(","))
        return dfs()
```
### 6. Convert Sorted Array to Binary Search Tree（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)
**难度**：简单
**题目**：给你一个整数数组 `nums` ，其中元素已经按 **升序** 排列，请你将其转换为一棵 平衡 二叉搜索树。

**示例 1：**
```
*
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
```
**示例 2：**
```
*
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
```
**提示：**

- `1 4`

- `-104 4`

- `nums` 按 **严格递增** 顺序排列
**思路**：有序数组中间为根，左半构建左子树，右半构建右子树。二分递归。
**代码**：
```python
def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def build(l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = build(l, mid - 1)
        root.right = build(mid + 1, r)
        return root
    return build(0, len(nums) - 1)
```
## 📝 总结
Day 23 聚焦树的构建：前序+中序/中序+后序还原二叉树（必考），填充 next 指针（层序串联），flatten（逆前序串联），以及序列化/反序列化（前序+空标记）。第 6 题有序数组转 BST 补充了 BST 构建视角，为 Day 26 预热。


---

# Day 24: 树的路径

## 📖 知识点
路径问题核心是 DFS 遍历过程中维护路径信息（和、前缀、节点列表）。三种典型模式：
1. **单一路径和**：从根到叶子，递归减去当前节点值（hasPathSum）
2. **所有路径和**：DFS 收集每条路径（sumNumbers）
3. **任意路径和**：使用前缀和或分治（pathSum III、maxPathSum）

**前缀和技巧**（Path Sum III 关键）：用字典记录从根到当前节点的路径前缀和出现次数，当前前缀和 - target 在字典中的次数即为以当前节点结尾的路径数。

---

## 🧩 刷题任务（6题）

### 1. Path Sum（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/path-sum/)
**难度**：简单
**题目**：给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

**示例 1：**
```
*
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```
**示例 2：**
```
*
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```
**示例 3：**
```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```
**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内

- `-1000
**思路**：DFS 递归，每步减去当前节点值。到达叶子时判断剩余是否等于 0。
**代码**：
```python
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    targetSum -= root.val
    if not root.left and not root.right:  # 叶子节点
        return targetSum == 0
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
```
### 2. Sum Root to Leaf Numbers（⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/sum-root-to-leaf-numbers/)
**难度**：中等
**题目**：给你一个二叉树的根节点 `root` ，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

- 例如，从根节点到叶节点的路径 `1 -> 2 -> 3` 表示数字 `123` 。

计算从根节点到叶节点生成的 **所有数字之和** 。

**叶节点** 是指没有子节点的节点。

**示例 1：**
```
*
输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
```
**示例 2：**
```
*
输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
```
**提示：**

- 树中节点的数目在范围 `[1, 1000]` 内

- `0
**思路**：DFS 传递当前累积值（sum * 10 + val），到达叶子时累加。就是路径的十进制数字和。
**代码**：
```python
def sumNumbers(root: Optional[TreeNode]) -> int:
    def dfs(node, cur):
        if not node:
            return 0
        cur = cur * 10 + node.val
        if not node.left and not node.right:
            return cur
        return dfs(node.left, cur) + dfs(node.right, cur)
    return dfs(root, 0)
```
### 3. Path Sum III（⭐⭐⭐）来源：L75 / O
**来源**：[L75](https://leetcode.cn/problems/path-sum/)
**难度**：简单
**题目**：给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

**示例 1：**
```
*
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```
**示例 2：**
```
*
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```
**示例 3：**
```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```
**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内

- `-1000
**思路**：前缀和 + 回溯。用字典记录根到当前节点路径上的前缀和出现次数。count = prefix_sum - target 的出现次数即为路径数。回溯时恢复字典计数。
**代码**：
```python
def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    prefix = {0: 1}  # 前缀和为 0 的路径有 1 条（空路径）

    def dfs(node, cur):
        if not node:
            return 0
        cur += node.val
        cnt = prefix.get(cur - targetSum, 0)
        prefix[cur] = prefix.get(cur, 0) + 1
        cnt += dfs(node.left, cur)
        cnt += dfs(node.right, cur)
        prefix[cur] -= 1  # 回溯恢复
        return cnt

    return dfs(root, 0)
```
### 4. Binary Tree Maximum Path Sum（⭐⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/path-sum/)
**难度**：简单
**题目**：给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

**示例 1：**
```
*
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```
**示例 2：**
```
*
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```
**示例 3：**
```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```
**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内

- `-1000
**思路**：后序遍历，每个节点返回经过该节点单侧的最大贡献值。全局变量维护最大路径和（节点值 + 左贡献 + 右贡献）。贡献为负时取 0（不选）。
**代码**：
```python
def maxPathSum(root: Optional[TreeNode]) -> int:
    ans = -10**9

    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        left = max(dfs(node.left), 0)   # 负贡献不取
        right = max(dfs(node.right), 0)
        ans = max(ans, node.val + left + right)  # 过当前节点的最大路径
        return node.val + max(left, right)  # 返回单侧最大贡献

    dfs(root)
    return ans
```
### 5. Longest ZigZag Path in a Binary Tree（⭐⭐⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/)
**难度**：中等
**题目**：给你一棵以 `root` 为根的二叉树，二叉树中的交错路径定义如下：

- 选择二叉树中 **任意** 节点和一个方向（左或者右）。

- 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。

- 改变前进方向：左变右或者右变左。

- 重复第二步和第三步，直到你在树中无法继续移动。

交错路径的长度定义为：**访问过的节点数目 - 1**（单个节点的路径长度为 0 ）。

请你返回给定树中最长 **交错路径** 的长度。

**示例 1：**
```
*****
输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
```
**示例 2：**
```
*****
输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。
```
**示例 3：**
```
输入：root = [1]
输出：0
```
**提示：**

- 每棵树最多有 `50000` 个节点。

- 每个节点的值在 `[1, 100]` 之间。
**思路**：DFS 传递方向（左/右）和当前 zigzag 长度。向左走时下一步向右走长度 +1，向左走重置为 1。全局变量记录最大值。
**代码**：
```python
def longestZigZag(root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(node, direction, length):
        nonlocal ans
        ans = max(ans, length)
        if node.left:
            dfs(node.left, 'L', length + 1 if direction != 'L' else 1)
        if node.right:
            dfs(node.right, 'R', length + 1 if direction != 'R' else 1)

    if root.left:
        dfs(root.left, 'L', 1)
    if root.right:
        dfs(root.right, 'R', 1)
    return ans
```
### 6. Prune Tree / Binary Tree Pruning（⭐⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/binary-tree-pruning/)
**难度**：中等
**题目**：给你二叉树的根结点 `root` ，此外树的每个结点的值要么是 `0` ，要么是 `1` 。

返回移除了所有不包含 `1` 的子树的原二叉树。

节点 `node` 的子树为 `node` 本身加上所有 `node` 的后代。

**示例 1：**
```
*
输入：root = [1,null,0,0,1]
输出：[1,null,0,null,1]
解释：
只有红色节点满足条件“所有不包含 1 的子树”。 右图为返回的答案。
```
**示例 2：**
```
*
输入：root = [1,0,1,0,0,0,1]
输出：[1,null,1,null,1]
```
**示例 3：**
```
*
输入：root = [1,1,0,1,1,0,1,0]
输出：[1,1,0,1,1,null,1]
```
**提示：**

- 树中节点的数目在范围 `[1, 200]` 内

- `Node.val` 为 `0` 或 `1` *思路**：后序遍历删除不包含 1 的子树。如果左右子树都被剪掉且自身值为 0，则返回 None。
**代码**：
```python
def pruneTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    return root
```
## 📝 总结
Day 24 集中攻克树的路径问题：从简单路径和 Path Sum（自顶向下递减）到所有路径和 Sum Numbers（累积十进制），再到任意路径和 Path Sum III（前缀和计数）和 Max Path Sum（后序贡献值）。ZigZag 和 Prune Tree 补充了路径遍历的变体。核心思路都是 DFS + 状态传递 + 回溯。


---

# Day 25: BFS + 层序遍历

## 📖 知识点
层序遍历（BFS）使用队列实现，模板：初始化队列放入 root，while 队列非空，取出当前层所有节点（for _ in range(len(q))），处理值并将子节点入队。

**层序模板**：
```python
def levelOrder(root):
    if not root: return []
    res, q = [], collections.deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

---

## 🧩 刷题任务（6题）

### 1. Binary Tree Right Side View（⭐⭐）来源：L75 / T150 / O
**来源**：[L75](https://leetcode.cn/problems/binary-tree-right-side-view/)
**难度**：中等
**题目**：给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**示例 1：**
```
**输入：**root = [1,2,3,null,5,null,4]
**输出：**[1,3,4]
**解释：**
*
```
**示例 2：**
```
**输入：**root = [1,2,3,4,null,null,null,5]
**输出：**[1,3,4,5]
**解释：**
*
```
**示例 3：**
```
**输入：**root = [1,null,3]
**输出：**[1,3]
```
**示例 4：**
```
**输入：**root = []
**输出：**[]
```
**提示:**

- 二叉树的节点个数的范围是 `[0,100]`

- `-100
**思路**：层序遍历，取每层最后一个节点值。也可以用 DFS（根→右→左优先遍历，每层第一个访问到的就是右视图）。
**代码**：
```python
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res, q = [], collections.deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0:           # 每层第一个
                res.append(node.val)
            if node.right: q.append(node.right)  # 先右后左
            if node.left: q.append(node.left)
    return res
```
### 2. Average of Levels in Binary Tree（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)
**难度**：简单
**题目**：给定一个非空二叉树的根节点 `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10-5` 以内的答案可以被接受。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：[3.00000,14.50000,11.00000]
解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。
```
**示例 2:**
```
*
输入：root = [3,9,20,15,7]
输出：[3.00000,14.50000,11.00000]
```
**提示：**

- 树中节点数量在 `[1, 104]` 范围内

- `-231 31 - 1`
**思路**：层序遍历，每层求和后除以该层节点数。
**代码**：
```python
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    res, q = [], collections.deque([root])
    while q:
        total, n = 0, len(q)
        for _ in range(n):
            node = q.popleft()
            total += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(total / n)
    return res
```
### 3. Binary Tree Level Order Traversal（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
**难度**：中等
**题目**：给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```
**示例 2：**
```
输入：root = [1]
输出：[[1]]
```
**示例 3：**
```
输入：root = []
输出：[]
```
**提示：**

- 树中节点数目在范围 `[0, 2000]` 内

- `-1000
**思路**：标准层序遍历，每层结果存入列表。
**代码**：
```python
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res, q = [], collections.deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```
### 4. Binary Tree Zigzag Level Order Traversal（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
**难度**：中等
**题目**：给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
```
**示例 2：**
```
输入：root = [1]
输出：[[1]]
```
**示例 3：**
```
输入：root = []
输出：[]
```
**提示：**

- 树中节点数目在范围 `[0, 2000]` 内

- `-100
**思路**：层序遍历 + 奇偶层反转。偶数层从左到右，奇数层从右到左（用 level 是否反转或双端队列）。
**代码**：
```python
def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res, q, layer = [], collections.deque([root]), 0
    while q:
        level = collections.deque()
        for _ in range(len(q)):
            node = q.popleft()
            if layer % 2 == 0:
                level.append(node.val)   # 从左到右
            else:
                level.appendleft(node.val)  # 从右到左
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(list(level))
        layer += 1
    return res
```
### 5. Maximum Level Sum of a Binary Tree（⭐⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/)
**难度**：中等
**题目**：给你一个二叉树的根节点 `root`。设根节点位于二叉树的第 `1` 层，而根节点的子节点位于第 `2` 层，依此类推。

返回总和 **最大**的那一层的层号 `x`。如果有多层的总和一样大，返回其中**最小** 的层号 `x`。

**示例 1：**
```
*****
输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
```
**示例 2：**
```
输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2
```
**提示：**

- 树中的节点数在 `[1, 104]`范围内

- `-105 5`
**思路**：层序遍历，记录每层和的最大值及其层号。
**代码**：
```python
def maxLevelSum(root: Optional[TreeNode]) -> int:
    max_sum, max_level = -10**9, 1
    q, level = collections.deque([root]), 0
    while q:
        level += 1
        total = 0
        for _ in range(len(q)):
            node = q.popleft()
            total += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if total > max_sum:
            max_sum = total
            max_level = level
    return max_level
```
### 6. Find Bottom Left Tree Value（⭐⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/find-bottom-left-tree-value/)
**难度**：中等
**题目**：给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边 **节点的值。

假设二叉树中至少有一个节点。

**示例 1:**
```
*
输入: root = [2,1,3]
输出: 1
```
**示例 2:**
```
*
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
```
**提示:**

- 二叉树的节点个数的范围是 `[1,104]`

- `-231 31 - 1`
**思路**：层序遍历，每层第一个节点即为最左节点。按顺序遍历（先右后左取最后一个，或先左后右取第一个）。
**代码**：
```python
def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node.right: q.append(node.right)   # 先右后左
        if node.left: q.append(node.left)
    return node.val  # 最后出队的即为最底层最左节点
```
## 📝 总结
Day 25 集中训练 BFS 层序遍历及其变体：标准层序（levelOrder）、zigzag（奇偶反转）、右视图（每层最后一个）、每层平均值、最大层和、最左叶子。核心模板一致——用队列+每层长度控制。变体主要在于每层取元素的顺序和聚合方式。BFS 在树和图中是最高频的遍历方式，务必熟练默写模板。


---

# Day 26: 二叉搜索树（BST）

## 📖 知识点
BST 核心性质：左子树所有节点 < 根 < 右子树所有节点。中序遍历 BST 得到**升序序列**，这是解决大多数 BST 问题的钥匙。常见操作：搜索（O(h)）、插入（O(h)）、删除（O(h)，分三种情况 — 无子、单子、双子（找前驱/后继替换））。

**中序遍历模板**：
```python
def inorder(root, res):
    if not root: return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)
```

---

## 🧩 刷题任务（6题）

### 1. Search in a Binary Search Tree（⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/search-in-a-binary-search-tree/)
**难度**：简单
**题目**：给定二叉搜索树（BST）的根节点 `root` 和一个整数值 `val`。

你需要在 BST 中找到节点值等于 `val` 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 `null` 。

**示例 1:**
```
*
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]
```
**示例 2:**
```
*
输入：root = [4,2,7,1,3], val = 5
输出：[]
```
**提示：**

- 树中节点数在 `[1, 5000]` 范围内

- `1 7`

- `root` 是二叉搜索树

- `1 7`
**思路**：利用 BST 性质比较大小，递归或迭代搜索。
**代码**：
```python
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)
```
### 2. Delete Node in a BST（⭐⭐⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/delete-node-in-a-bst/)
**难度**：中等
**题目**：给定一个二叉搜索树的根节点 **root **和一个值 **key**，删除二叉搜索树中的 **key **对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

- 首先找到需要删除的节点；

- 如果找到了，删除它。

**示例 1:**
```
*
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。
```
**示例 2:**
```
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
```
**示例 3:**
```
输入: root = [], key = 0
输出: []
```
**提示:**

- 节点数的范围 `[0, 104]`.

- `-105 5`

- 节点值唯一

- `root` 是合法的二叉搜索树

- `-105 5`

**进阶：** 要求算法时间复杂度为 O(h)，h 为树的高度。
**思路**：递归找到要删除的节点。分三种情况：无子节点（直接删）、单子节点（子节点替代）、双子节点（找右子树最小节点/中序后继替换值后删除该后继）。
**代码**：
```python
def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right  # 无左或单右
        if not root.right:
            return root.left   # 无右或单左
        # 双子节点：找右子树最小节点
        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val            # 替换值
        root.right = deleteNode(root.right, cur.val)  # 删除后继
    return root
```
### 3. Validate Binary Search Tree（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/validate-binary-search-tree/)
**难度**：中等
**题目**：给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

- 节点的左子树只包含**严格小于**当前节点的数。

- 节点的右子树只包含 **严格大于** 当前节点的数。

- 所有左子树和右子树自身必须也是二叉搜索树。

**示例 1：**
```
*
输入：root = [2,1,3]
输出：true
```
**示例 2：**
```
*
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
```
**提示：**

- 树中节点数目范围在`[1, 104]` 内

- `-231 31 - 1`
**思路**：中序遍历检查是否升序（pre < cur）。或递归传递上下界 (min, max)。
**代码**：
```python
def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
    return dfs(root, -10**18, 10**18)
```
### 4. Kth Smallest Element in a BST（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)
**难度**：中等
**题目**：给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素（`k` 从 1 开始计数）。

**示例 1：**
```
*
输入：root = [3,1,4,null,2], k = 1
输出：1
```
**示例 2：**
```
*
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```
**提示：**

- 树中的节点数为 `n` 。

- `1 4`

- `0 4`

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？
**思路**：中序遍历 BST 得到升序序列，第 k 个元素即为答案。可用递归计数或迭代栈提前终止（更优）。
**代码**：
```python
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
```
### 5. Minimum Absolute Difference in BST（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)
**难度**：简单
**题目**：给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。

**示例 1：**
```
*
输入：root = [4,2,6,1,3]
输出：1
```
**示例 2：**
```
*
输入：root = [1,0,48,null,null,12,49]
输出：1
```
**提示：**

- 树中节点的数目范围是 `[2, 104]`

- `0 5`

**注意：**本题与 783 https://leetcode.cn/problems/minimum-distance-between-bst-nodes/ 相同
**思路**：中序遍历 BST 得到升序序列，相邻元素差值最小即为答案。用 prev 记录前一个节点值。
**代码**：
```python
def getMinimumDifference(root: Optional[TreeNode]) -> int:
    prev, ans = None, 10**9

    def dfs(node):
        nonlocal prev, ans
        if not node:
            return
        dfs(node.left)
        if prev is not None:
            ans = min(ans, node.val - prev)
        prev = node.val
        dfs(node.right)

    dfs(root)
    return ans
```
### 6. Inorder Successor in BST（⭐⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/inorder-successor-in-bst/)
**难度**：中等
**思路**：中序后继是大于 p 的最小节点。递归/迭代：若 p 有右子树，后继为右子树最左节点；否则沿根向下搜索，记录最后一个向左转的节点。
**代码**：
```python
def inorderSuccessor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    successor = None
    while root:
        if p.val < root.val:
            successor = root          # 候选
            root = root.left
        else:
            root = root.right
    return successor
```
## 📝 总结
Day 26 专攻 BST 五大题型：搜索（二分查找思想）、删除（三情况分类）、验证（中序升序/上下界）、第 K 小（中序计数）、最小差值（中序相邻差）、后继（有右子则最左/否则记录左转节点）。BST 题 90% 用中序遍历解决，务必熟练掌握迭代中序写法。


---

# Day 27: 树的综合

## 📖 知识点
Day 27 整合 BST 扩展题型和树上的综合问题：迭代器（中序拆解）、树的变形（递增树、累加树）、两数和（BST 双指针）、LCA（最近公共祖先）、完全二叉树计数。这些题将前几天的遍历、BST 性质、BFS 等知识融合在一起。

**核心思想**：
- BST 迭代器 → 中序拆成迭代器模式（栈模拟）
- 累加树 → 逆中序遍历（右→根→左）
- LCA → 递归分治：左右子树各找一次
- 完全二叉树计数 → 利用完美二叉树性质加速

---

## 🧩 刷题任务（6题）

### 1. BST Iterator（⭐⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/binary-search-tree-iterator/)
**难度**：中等
**题目**：实现一个二叉搜索树迭代器类`BSTIterator` ，表示一个按中序遍历二叉搜索树（BST）的迭代器：

- `BSTIterator(TreeNode root)` 初始化 `BSTIterator` 类的一个对象。BST 的根节点 `root` 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。

- `boolean hasNext()` 如果向指针右侧遍历存在数字，则返回 `true` ；否则返回 `false` 。

- `int next()`将指针向右移动，然后返回指针处的数字。

注意，指针初始化为一个不存在于 BST 中的数字，所以对 `next()` 的首次调用将返回 BST 中的最小元素。

你可以假设 `next()` 调用总是有效的，也就是说，当调用 `next()` 时，BST 的中序遍历中至少存在一个下一个数字。

**示例：**
```
*
输入
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
输出
[null, 3, 7, true, 9, true, 15, true, 20, false]
解释
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // 返回 3
bSTIterator.next();    // 返回 7
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 9
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 15
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 20
bSTIterator.hasNext(); // 返回 False
```
**提示：**

- 树中节点的数目在范围 `[1, 105]` 内

- `0 6`

- 最多调用 `105` 次 `hasNext` 和 `next` 操作

**进阶：**

- 你可以设计一个满足下述条件的解决方案吗？`next()` 和 `hasNext()` 操作均摊时间复杂度为 `O(1)` ，并使用 `O(h)` 内存。其中 `h` 是树的高度。
**思路**：用栈模拟中序遍历。初始化时一直往左入栈；每次 next() 弹出栈顶，然后处理其右子树（入栈右节点及所有左后代）。hasNext() 判断栈是否空。
**代码**：
```python
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)  # 处理右子树
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
```
### 2. Increasing Order Search Tree（⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/increasing-order-search-tree/)
**难度**：简单
**题目**：给你一棵二叉搜索树的 `root` ，请你 **按中序遍历** 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

**示例 1：**
```
*
输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```
**示例 2：**
```
*
输入：root = [5,1,7]
输出：[1,null,5,null,7]
```
**提示：**

- 树中节点数的取值范围是 `[1, 100]`

- `0
**思路**：中序遍历，重新构造一棵只有右子树的树。用 dummy 头节点，cur 指针不断右移连接新节点。
**代码**：
```python
def increasingBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    dummy = TreeNode(0)
    cur = dummy

    def dfs(node):
        nonlocal cur
        if not node:
            return
        dfs(node.left)
        node.left = None
        cur.right = node
        cur = cur.right
        dfs(node.right)

    dfs(root)
    return dummy.right
```
### 3. Convert BST to Greater Tree（⭐⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/convert-bst-to-greater-tree/)
**难度**：中等
**题目**：给出二叉**搜索**树的根节点 `root`，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），将其转换为一个更大的树，使得原始二叉搜索树中的每个节点值都变为原本值加上原本二叉搜索树中所有比该节点值大的节点值的总和。

提醒一下，二叉搜索树满足下列约束条件：

- 节点的左子树仅包含键**小于**节点键的节点。

- 节点的右子树仅包含键** 大于** 节点键的节点。

- 左右子树也必须是二叉搜索树。

**注意：**本题和 1038: https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/ 相同

**示例 1：**
```
*****
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```
**示例 2：**
```
输入：root = [0,null,1]
输出：[1,null,1]
```
**示例 3：**
```
输入：root = [1,0,2]
输出：[3,3,2]
```
**示例 4：**
```
输入：root = [3,2,4,1]
输出：[7,9,4,10]
```
**提示：**

- 树中的节点数介于 `0` 和 `104` 之间。

- 每个节点的值介于 `-104` 和 `104` 之间。

- 树中的所有值 **互不相同** 。

- 给定的树为二叉搜索树。
**思路**：逆中序遍历（右→根→左），累加前缀和并赋值给当前节点。
**代码**：
```python
def convertBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    total = 0

    def dfs(node):
        nonlocal total
        if not node:
            return
        dfs(node.right)          # 先遍历右子树（较大值）
        total += node.val        # 累加
        node.val = total         # 更新节点值
        dfs(node.left)

    dfs(root)
    return root
```
### 4. Two Sum IV - Input is a BST（⭐）来源：O（剑指 Offer）
**来源**：[O（剑指](https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/)
**难度**：简单
**题目**：给定一个二叉搜索树 `root` 和一个目标结果 `k`，如果二叉搜索树中存在两个元素且它们的和等于给定的目标结果，则返回 `true`。

**示例 1：**
```
*
输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
```
**示例 2：**
```
*
输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
```
**提示:**

- 二叉树的节点个数的范围是  `[1, 104]`.

- `-104 4`

- 题目数据保证，输入的 `root` 是一棵 **有效** 的二叉搜索树

- `-105 5`
**思路**：中序遍历得到有序数组后双指针。或 DFS + HashSet 边遍历边检查互补值是否存在。
**代码**：
```python
def findTarget(root: Optional[TreeNode], k: int) -> bool:
    seen = set()

    def dfs(node):
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)

    return dfs(root)
```
### 5. Lowest Common Ancestor of a Binary Tree（⭐⭐）来源：L75 / T150
**来源**：[L75](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)
**难度**：中等
**题目**：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

**示例 1：**
```
*
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
```
**示例 2：**
```
*
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
```
**示例 3：**
```
输入：root = [1,2], p = 1, q = 2
输出：1
```
**提示：**

- 树中节点数目在范围 `[2, 105]` 内。

- `-109 9`

- 所有 `Node.val` `互不相同` 。

- `p != q`

- `p` 和 `q` 均存在于给定的二叉树中。
**思路**：递归查找。当前节点为 p 或 q 则返回；左右子树分别查找。若左右都有结果则当前节点为 LCA；否则返回非空一侧。
**代码**：
```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root   # p 和 q 分别在左右子树
    return left or right
```
### 6. Count Complete Tree Nodes（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/count-complete-tree-nodes/)
**难度**：简单
**题目**：给你一棵** 完全二叉树** 的根节点 `root` ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 `h` 层（从第 0 层开始），则该层包含 `1~ 2h` 个节点。

**示例 1：**
```
*
输入：root = [1,2,3,4,5,6]
输出：6
```
**示例 2：**
```
输入：root = []
输出：0
```
**示例 3：**
```
输入：root = [1]
输出：1
```
**提示：**

- 树中节点的数目范围是`[0, 5 * 104]`

- `0 4`

- 题目数据保证输入的树是 **完全二叉树**

**进阶：**遍历树来统计节点是一种时间复杂度为 `O(n)` 的简单解决方案。你可以设计一个更快的算法吗？
**思路**：完全二叉树利用完美二叉树性质：左右子树高度相等则左子树为满二叉树（节点数 2^h - 1），否则递归计算。平均 O(log²n)。
**代码**：
```python
def countNodes(root: Optional[TreeNode]) -> int:
    def height(node):
        h = 0
        while node:
            node = node.left
            h += 1
        return h

    if not root:
        return 0
    lh, rh = height(root.left), height(root.right)
    if lh == rh:  # 左子树是满二叉树
        return (1 << lh) + countNodes(root.right)
    else:         # 右子树高度矮一层
        return (1 << rh) + countNodes(root.left)
```
## 📝 总结
Day 27 是树的综合日，整合了前 5 天的知识点：BST 迭代器（栈模拟中序）、递增树（中序重构）、累加树（逆中序累加）、两数和（HashSet 遍历）、LCA（递归分治）、完全二叉树计数（利用完美二叉树性质）。这些题在面试中经常作为进阶题出现，考察对树结构的综合理解。


---

# Day 28: 周复习——树与图综合

## 📖 本周知识图谱

```
Week 4 - Trees & Graphs
├── D22: 二叉树遍历（递归前/中/后序，DFS）
├── D23: 树的构建（序列→树，序列化/反序列化）
├── D24: 树的路径（路径和，前缀和，最大路径）
├── D25: BFS + 层序遍历（队列模板，zigzag，右视图）
├── D26: BST（中序有序，搜索/删除/验证/后继）
└── D27: 树的综合（迭代器，累加树，LCA，完全二叉树）
```

**高频考点**（华为 OD 笔试 + 面试）：
1. 二叉树层序遍历及其变体 ⭐⭐⭐
2. BST 验证与中序遍历 ⭐⭐⭐
3. 路径和（Path Sum III 前缀和）⭐⭐⭐
4. LCA 最近公共祖先 ⭐⭐⭐
5. 最大路径和 ⭐⭐⭐
6. 序列化/反序列化 ⭐⭐⭐
7. 树的构建（pre+in / in+post）⭐⭐⭐

---

## 🧩 复习刷题（6题）

### 1. Maximum Depth of Binary Tree（快速热身）⭐
**来源**：[LeetCode](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)
**难度**：简单
**题目**：给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

**示例 1：**
```
*
输入：root = [3,9,20,null,null,15,7]
输出：3
```
**示例 2：**
```
输入：root = [1,null,2]
输出：2
```
**提示：**

- 树中节点的数量在 `[0, 104]` 区间内。

- `-100
**代码**：
```python
def maxDepth(root):
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0
```
### 2. Level Order Traversal（默写模板）⭐⭐
**代码**：
```python
def levelOrder(root):
    if not root: return []
    res, q = [], collections.deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(level)
    return res
```

### 3. Validate BST + Kth Smallest（中序双练）⭐⭐
**代码**：
```python
# 验证 BST
def isValidBST(root):
    def dfs(node, lo, hi):
        if not node: return True
        if not (lo < node.val < hi): return False
        return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
    return dfs(root, -10**18, 10**18)

# 第 K 小（迭代中序）
def kthSmallest(root, k):
    stack, cur = [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0: return cur.val
        cur = cur.right
```

### 4. Path Sum III + Max Path Sum（路径双练）⭐⭐⭐
**来源**：[LeetCode](https://leetcode.cn/problems/path-sum/)
**难度**：简单
**题目**：给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

**示例 1：**
```
*
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```
**示例 2：**
```
*
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```
**示例 3：**
```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```
**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内

- `-1000
**代码**：
```python
# 路径和 III（前缀和）
def pathSum(root, targetSum):
    prefix = {0: 1}
    def dfs(node, cur):
        if not node: return 0
        cur += node.val
        cnt = prefix.get(cur - targetSum, 0)
        prefix[cur] = prefix.get(cur, 0) + 1
        cnt += dfs(node.left, cur) + dfs(node.right, cur)
        prefix[cur] -= 1
        return cnt
    return dfs(root, 0)

# 最大路径和
def maxPathSum(root):
    ans = -10**9
    def dfs(node):
        nonlocal ans
        if not node: return 0
        l = max(dfs(node.left), 0)
        r = max(dfs(node.right), 0)
        ans = max(ans, node.val + l + r)
        return node.val + max(l, r)
    dfs(root)
    return ans
```
### 5. LCA + Build Tree（构建 + 查询双练）⭐⭐⭐
**代码**：
```python
# LCA
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q: return root
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)
    if l and r: return root
    return l or r

# 从前序+中序构建树
def buildTree(preorder, inorder):
    idx_map = {v:i for i,v in enumerate(inorder)}
    pre_idx = 0
    def build(l, r):
        nonlocal pre_idx
        if l > r: return None
        root = TreeNode(preorder[pre_idx])
        mid = idx_map[preorder[pre_idx]]
        pre_idx += 1
        root.left = build(l, mid-1)
        root.right = build(mid+1, r)
        return root
    return build(0, len(inorder)-1)
```

### 6. Serialize + Deserialize（完整实现）⭐⭐⭐
**代码**：
```python
class Codec:
    def serialize(self, root):
        vals = []
        def dfs(n):
            if not n: vals.append("#"); return
            vals.append(str(n.val))
            dfs(n.left); dfs(n.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = iter(data.split(","))
        def dfs():
            v = next(vals)
            if v == "#": return None
            n = TreeNode(int(v))
            n.left = dfs(); n.right = dfs()
            return n
        return dfs()
```

---

## 📝 周总结

### 📊 正确率自测表
| 题型 | 题数 | 思路清晰 | 代码默写 |
|------|------|---------|---------|
| 遍历（递归/迭代） | 6 | □ | □ |
| 树的构建 | 6 | □ | □ |
| 路径问题 | 6 | □ | □ |
| BFS 层序 | 6 | □ | □ |
| BST | 6 | □ | □ |
| 综合 | 6 | □ | □ |

### 🎯 重点复盘
1. **中序遍历**是 BST 的灵魂——验证、第 K 小、最小差值、累加树都靠它
2. **层序遍历模板**必须烂熟于心——右视图、zigzag、平均值都是小改
3. **路径和 III 的前缀和**和**最大路径和的后序贡献**是两道最难题，建议反复看
4. **LCA 递归**理解口诀：左右各找，各有一个返回根，一个有一边则返回那个

### 🧠 易错点提醒
- `preorder.pop(0)` 是 O(n)，用索引或哈希表优化
- 路径和 III 记得回溯 `prefix[cur] -= 1`
- 最大路径和贡献值取 max(..., 0) 避免负值
- 完全二叉树计数用位运算 `1 << h` 等价于 `2**h`
- 删除 BST 节点双子情况要替换值再删后继，不要直接删节点

### 🚀 下期预告
Week 5：回溯算法 → 全排列、子集、组合、N 皇后、单词搜索等


---


---
# 第5周·OD100题(上)
> 共计 7 天

# Day 29: 图-DFS

## 📖 知识点
**DFS on Graph** — 深度优先搜索遍历图,使用递归或显式栈.核心模板:
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```
**适用场景**:连通分量计数、可达性判断、环检测、拓扑排序(后序).

## 🧩 刷题任务（6题）

### 1. Number of Islands（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/number-of-islands/)
**难度**：中等
**题目**：给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**示例 1：**
```
输入：grid = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出：1
```
**示例 2：**
```
输入：grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出：3
```
**提示：**

- `m == grid.length`

- `n == grid[i].length`

- `1
**思路**：遍历网格,遇到'1'则岛屿计数+1,用DFS将其所在连通分量全部标记为已访问(置'0').四方向搜索.
**代码**：
```python
def numIslands(self, grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count
```
### 2. Surrounded Regions（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/surrounded-regions/)
**难度**：中等
**题目**：给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` 组成，**捕获**所有**被围绕的区域**：

- **连接：**一个单元格与水平或垂直方向上相邻的单元格连接。

- **区域：连接所有 **`'O'` 的单元格来形成一个区域。

- **围绕：**如果一个区域中的所有 `'O'` 单元格都不在棋盘的边缘，则该区域被包围。这样的区域 **完全**被 `'X'` 单元格包围。

通过**原地**将输入矩阵中的所有 `'O'` 替换为 `'X'` 来**捕获被围绕的区域**。你不需要返回任何值。

**示例 1：**
```
**输入：**board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
**输出：**[['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]
**解释：**
*
在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。
```
**示例 2：**
```
**输入：**board = [['X']]
**输出：**[['X']]
```
**提示：**

- `m == board.length`

- `n == board[i].length`

- `1
**思路**：从边界上的'O'出发DFS,标记所有与边界连通的'O'为临时字符(如'#'),然后遍历全图:剩余的'O'→'X','#'→'O'.
**代码**：
```python
def solve(self, board):
    if not board:
        return
    m, n = len(board), len(board[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '#'
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(i+di, j+dj)

    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)
    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
```
### 3. Clone Graph（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/clone-graph/)
**难度**：中等
**题目**：给你无向 **连通 **图中一个节点的引用，请你返回该图的 **深拷贝**（克隆）。

图中的每个节点都包含它的值 `val`（`int`） 和其邻居的列表（`list[Node]`）。

class Node {
public int val;
public List neighbors;
}

**测试用例格式：**

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（`val = 1`），第二个节点值为 2（`val = 2`），以此类推。该图在测试用例中使用邻接列表表示。

**邻接列表**是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将**给定节点的拷贝 **作为对克隆图的引用返回。

**示例 1：**
```
*
输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
```
**示例 2：**
```
*
输入：adjList = [[]]
输出：[[]]
解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
```
**示例 3：**
```
输入：adjList = []
输出：[]
解释：这个图是空的，它不含任何节点。
```
**提示：**

- 这张图中的节点数在 `[0, 100]` 之间。

- `1
**思路**：用哈希表记录原节点→克隆节点的映射.DFS递归克隆:复制值,递归克隆邻居,用映射避免重复克隆.
**代码**：
```python
def cloneGraph(self, node):
    if not node:
        return None
    visited = {}

    def dfs(n):
        if n in visited:
            return visited[n]
        clone = Node(n.val)
        visited[n] = clone
        for nei in n.neighbors:
            clone.neighbors.append(dfs(nei))
        return clone

    return dfs(node)
```
### 4. Number of Provinces（⭐⭐）
**来源**：[L75/O](https://leetcode.cn/problems/number-of-provinces/)
**难度**：中等
**题目**：有 `n` 个城市，其中一些彼此相连，另一些没有相连。如果城市 `a` 与城市 `b` 直接相连，且城市 `b` 与城市 `c` 直接相连，那么城市 `a` 与城市 `c` 间接相连。

**省份**是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 `n x n` 的矩阵 `isConnected` ，其中 `isConnected[i][j] = 1` 表示第 `i` 个城市和第 `j` 个城市直接相连，而 `isConnected[i][j] = 0` 表示二者不直接相连。

返回矩阵中**省份** 的数量。

**示例 1：**
```
*
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
```
**示例 2：**
```
*
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
```
**提示：**

- `1
**思路**：邻接矩阵表示图,DFS计数连通分量.visited数组标记已访问城市.
**代码**：
```python
def findCircleNum(self, isConnected):
    n = len(isConnected)
    visited = [False] * n
    count = 0

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if isConnected[i][j] == 1 and not visited[j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count
```
### 5. Evaluate Division（⭐⭐⭐）
**来源**：[L75/O](https://leetcode.cn/problems/evaluate-division/)
**难度**：中等
**题目**：给你一个变量对数组 `equations` 和一个实数值数组 `values` 作为已知条件，其中 `equations[i] = [Ai, Bi]` 和 `values[i]` 共同表示等式 `Ai / Bi = values[i]` 。每个 `Ai` 或 `Bi` 是一个表示单个变量的字符串。

另有一些以数组 `queries` 表示的问题，其中 `queries[j] = [Cj, Dj]` 表示第 `j` 个问题，请你根据已知条件找出 `Cj / Dj = ?` 的结果作为答案。

返回 **所有问题的答案** 。如果存在某个无法确定的答案，则用 `-1.0` 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 `-1.0` 替代这个答案。

**注意：**输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

**注意：**未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。

**示例 1：**
```
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 => -1.0
```
**示例 2：**
```
输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
```
**示例 3：**
```
输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
```
**提示：**

- `1 i.length, Bi.length j.length, Dj.length i, Bi, Cj, Dj` 由小写英文字母与数字组成
**思路**：建带权有向图(变量为节点,a/b=2.0 即 a->b权2.0,b->a权0.5).查询时DFS搜索路径,累计乘积.
**代码**：
```python
def calcEquation(self, equations, values, queries):
    graph = {}
    for (a, b), v in zip(equations, values):
        graph.setdefault(a, {})[b] = v
        graph.setdefault(b, {})[a] = 1.0 / v

    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for nei, val in graph[start].items():
            if nei not in visited:
                ans = dfs(nei, end, visited)
                if ans != -1.0:
                    return val * ans
        return -1.0

    return [dfs(q[0], q[1], set()) for q in queries]
```
### 6. Keys and Rooms（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/keys-and-rooms/)
**难度**：中等
**题目**：有 `n` 个房间，房间按从 `0` 到 `n - 1` 编号。最初，除 `0` 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。然而，你不能在没有获得钥匙的时候进入锁住的房间。

当你进入一个房间，你可能会在里面找到一套 **不同的钥匙**，每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。

给你一个数组 `rooms` 其中 `rooms[i]` 是你进入 `i` 号房间可以获得的钥匙集合。如果能进入 **所有** 房间返回 `true`，否则返回 `false`。

**示例 1：**
```
输入：rooms = [[1],[2],[3],[]]
输出：true
解释：
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
```
**示例 2：**
```
输入：rooms = [[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
```
**提示：**

- `n == rooms.length`

- `2
**思路**：DFS模拟开锁过程.用visited记录已进入的房间,从0开始DFS,每进入一个房间获取钥匙加入可访问邻居.最后检查visited长度是否等于总房间数.
**代码**：
```python
def canVisitAllRooms(self, rooms):
    visited = set()

    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)

    dfs(0)
    return len(visited) == len(rooms)
```
## 📝 总结
- 图DFS核心: visited避免重复,递归或栈实现.
- 网格图的DFS: 注意边界检查和方向数组.
- 带权图: 边存储权重,DFS累积路径值.
- 连通分量计数: 遍历所有节点,对未访问的启动DFS.


---

# Day 30: 图-BFS

## 📖 知识点
**BFS on Graph** — 广度优先搜索,使用队列逐层遍历.适用于最短路径(无权图)、拓扑排序、层次遍历.
```python
from collections import deque
def bfs(start):
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        steps += 1
    return steps
```

## 🧩 刷题任务（6题）

### 1. Course Schedule（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/course-schedule/)
**难度**：中等
**题目**：你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程  `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```
**示例 2：**
```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```
**提示：**

- `1 i, bi
**思路**：拓扑排序(Kahn算法).计算入度,将入度为0的节点入队,逐个出队并减少邻居入度.最后检查修完的课程数是否等于总课程数.
**代码**：
```python
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return count == numCourses
```
### 2. Course Schedule II（⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/course-schedule/)
**难度**：中等
**题目**：你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程  `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```
**示例 2：**
```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```
**提示：**

- `1 i, bi
**思路**：拓扑排序并返回课程顺序.与上题同理,出队时记录到结果列表.若存在环(修不完所有课程)返回空列表.
**代码**：
```python
def findOrder(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return res if len(res) == numCourses else []
```
### 3. Snakes and Ladders（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/snakes-and-ladders/)
**难度**：中等
**题目**：给你一个大小为 `n x n` 的整数矩阵 `board` ，方格按从 `1` 到 `n2` 编号，编号遵循 转行交替方式 ，**从左下角开始**（即，从 `board[n - 1][0]` 开始）的每一行改变方向。

你一开始位于棋盘上的方格  `1`。每一回合，玩家需要从当前方格 `curr` 开始出发，按下述要求前进：

- 选定目标方格 `next` ，目标方格的编号在范围 `[curr + 1, min(curr + 6, n2)]` 。

- 该选择模拟了掷**六面体骰子**的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。

- 传送玩家：如果目标方格 `next` 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 `next` 。

- 当玩家到达编号 `n2` 的方格时，游戏结束。

如果 `board[r][c] != -1` ，位于 `r` 行 `c` 列的棋盘格中可能存在 “蛇” 或 “梯子”。那个蛇或梯子的目的地将会是 `board[r][c]`。编号为 `1` 和 `n2` 的方格不是任何蛇或梯子的起点。

注意，玩家在每次掷骰的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也**不能**继续移动。

- 举个例子，假设棋盘是 `[[-1,4],[-1,3]]` ，第一次移动，玩家的目标方格是 `2` 。那么这个玩家将会顺着梯子到达方格 `3` ，但**不能** 顺着方格 `3` 上的梯子前往方格 `4` 。（简单来说，类似飞行棋，玩家掷出骰子点数后移动对应格数，遇到单向的路径（即梯子或蛇）可以直接跳到路径的终点，但如果多个路径首尾相连，也不能连续跳多个路径）

返回达到编号为 `n2` 的方格所需的最少掷骰次数，如果不可能，则返回 `-1`。

**示例 1：**
```
*
输入：board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。
最后决定移动到方格 36 , 游戏结束。
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。
```
**示例 2：**
```
输入：board = [[-1,-1],[-1,3]]
输出：1
```
**提示：**

- `n == board.length == board[i].length`

- `2 2]` 内

- 编号为 `1` 和 `n2` 的方格上没有蛇或梯子
**思路**：BFS求最短步数.棋盘编号从1到N²,每步走1~6格,踩到梯子/蛇则直接传送到目标格.用visited避免重访.
**代码**：
```python
def snakesAndLadders(self, board):
    n = len(board)
    # 将棋盘编号映射到坐标
    def get_pos(num):
        r = (num - 1) // n
        c = (num - 1) % n
        if r % 2 == 1:  # 奇数行从右往左
            c = n - 1 - c
        return n - 1 - r, c

    q = deque([(1, 0)])  # (格子编号,步数)
    visited = set([1])
    while q:
        num, steps = q.popleft()
        if num == n * n:
            return steps
        for nxt in range(num + 1, min(num + 6, n * n) + 1):
            r, c = get_pos(nxt)
            dest = board[r][c] if board[r][c] != -1 else nxt
            if dest not in visited:
                visited.add(dest)
                q.append((dest, steps + 1))
    return -1
```
### 4. Minimum Genetic Mutation（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/minimum-genetic-mutation/)
**难度**：中等
**题目**：基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 `'A'`、`'C'`、`'G'` 和 `'T'` 之一。

假设我们需要调查从基因序列 `start` 变为 `end` 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

- 例如，`"AACCGGTT" --> "AACCGGTA"` 就是一次基因变化。

另有一个基因库 `bank` 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 `bank` 中）

给你两个基因序列 `start` 和 `end` ，以及一个基因库 `bank` ，请你找出并返回能够使 `start` 变化为 `end` 所需的最少变化次数。如果无法完成此基因变化，返回 `-1` 。

注意：起始基因序列 `start` 默认是有效的，但是它并不一定会出现在基因库中。

**示例 1：**
```
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
```
**示例 2：**
```
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
```
**示例 3：**
```
输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3
```
**提示：**

- `start.length == 8`

- `end.length == 8`

- `0
**思路**：BFS求最短突变路径.每次改变一个碱基,突变结果必须在bank集合中.BFS逐层扩展,首次到达endGene即为最短步数.
**代码**：
```python
def minMutation(self, startGene, endGene, bank):
    bankSet = set(bank)
    if endGene not in bankSet:
        return -1
    genes = ['A', 'C', 'G', 'T']
    q = deque([(startGene, 0)])
    visited = {startGene}
    while q:
        gene, steps = q.popleft()
        if gene == endGene:
            return steps
        for i in range(8):
            for g in genes:
                if g == gene[i]:
                    continue
                nxt = gene[:i] + g + gene[i+1:]
                if nxt in bankSet and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
    return -1
```
### 5. Word Ladder（⭐⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/word-ladder/)
**难度**：困难
**题目**：字典 `wordList` 中从单词 `beginWord`  *到 `endWord` 的 **转换序列 **是一个按下述规格形成的序列 `beginWord -> s1 -> s2 -> ... -> sk`：

- 每一对相邻的单词只差一个字母。

-  对于 `1  `si` 都在 `wordList` 中。注意， `beginWord`  *不需要在 `wordList` 中。

- `sk == endWord`

给你两个单词* *`beginWord`  *和 `endWord` 和一个字典 `wordList` ，返回 *从 `beginWord` 到 `endWord` 的 **最短转换序列**中的**单词数目*** 。如果不存在这样的转换序列，返回 `0` 。

**示例 1：**
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
```
**示例 2：**
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
```
**提示：**

- `1
**思路**：双向BFS优化.从beginWord和endWord同时BFS,每次扩展较小的一层.每个单词改变一个字母,邻接词必须在wordList中.
**代码**：
```python
def ladderLength(self, beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    forward = {beginWord}
    backward = {endWord}
    visited = set()
    steps = 1

    while forward and backward:
        if len(forward) > len(backward):
            forward, backward = backward, forward
        next_level = set()
        for word in forward:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    nxt = word[:i] + c + word[i+1:]
                    if nxt in backward:
                        return steps + 1
                    if nxt in wordSet and nxt not in visited:
                        visited.add(nxt)
                        next_level.add(nxt)
        forward = next_level
        steps += 1
    return 0
```
### 6. Rotting Oranges（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/rotting-oranges/)
**难度**：中等
**题目**：在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；

- 值 `1` 代表新鲜橘子；

- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。

**示例 1：**
```
*****
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
```
**示例 2：**
```
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
```
**示例 3：**
```
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```
**提示：**

- `m == grid.length`

- `n == grid[i].length`

- `1
**思路**：多源BFS.将所有初始腐烂橘子入队,记录新鲜橘子数.BFS逐分钟传播腐烂,每层时间+1.若最后仍有新鲜橘子返回-1.
**代码**：
```python
def orangesRotting(self, grid):
    m, n = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    q.append((ni, nj))
        minutes += 1
    return minutes if fresh == 0 else -1
```
## 📝 总结
- BFS求无权图最短路径: 第一次到达目标即为最短.
- 拓扑排序: 入度表+Kahn队列,检测环.
- 双向BFS: 大幅减少搜索空间(Word Ladder).
- 多源BFS: 将多个起点同时入队(Rotting Oranges).


---

# Day 31: 图进阶

## 📖 知识点
- **多源BFS**: 多个起点同时入队,适合求每个位置到最近起点的距离(01-Matrix).
- **二分图判定**: DFS/BFS二染色,相邻节点不同色.
- **隐式图BFS**: 状态作为节点,合法转换作为边(Open the Lock).
- **DAG所有路径**: DFS回溯求所有从源到汇的路径.

## 🧩 刷题任务（6题）

### 1. Reorder Routes（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
**难度**：中等
**题目**：`n` 座城市，从 `0` 到 `n-1` 编号，其间共有 `n-1` 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

路线用 `connections` 表示，其中 `connections[i] = [a, b]` 表示从城市 `a` 到 `b` 的一条有向路线。

今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

题目数据 **保证** 每个城市在重新规划路线方向后都能到达城市 0 。

**示例 1：**
```
*****
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```
**示例 2：**
```
*****
输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```
**示例 3：**
```
输入：n = 3, connections = [[1,0],[2,0]]
输出：0
```
**提示：**

- `2
**思路**：建双向图,标记边的原始方向.从0出发DFS,若遇到反向走的边则需要反转(计数+1).
**代码**：
```python
def minReorder(self, n, connections):
    graph = [[] for _ in range(n)]
    for a, b in connections:
        graph[a].append((b, 1))   # 正向
        graph[b].append((a, 0))   # 反向

    def dfs(node, parent):
        count = 0
        for nei, direction in graph[node]:
            if nei == parent:
                continue
            if direction == 1:  # 需要反转
                count += 1
            count += dfs(nei, node)
        return count

    return dfs(0, -1)
```
### 2. Nearest Exit from Entrance in Maze（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/)
**难度**：中等
**题目**：给你一个 `m x n` 的迷宫矩阵 `maze` （**下标从 0 开始**），矩阵中有空格子（用 `'.'` 表示）和墙（用 `'+'` 表示）。同时给你迷宫的入口 `entrance` ，用 `entrance = [entrancerow, entrancecol]` 表示你一开始所在格子的行和列。

每一步操作，你可以往 **上**，**下**，**左**或者**右** 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 `entrance` *最近** 的出口。**出口** 的含义是 `maze` *边界** 上的 **空格子**。`entrance` 格子 **不算** 出口。

请你返回从 `entrance` 到最近出口的最短路径的 **步数** ，如果不存在这样的路径，请你返回 `-1` 。

**示例 1：**
```
*
输入：maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
输出：1
解释：总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。
一开始，你在入口格子 (1,2) 处。
- 你可以往左移动 2 步到达 (1,0) 。
- 你可以往上移动 1 步到达 (0,2) 。
从入口处没法到达 (2,3) 。
所以，最近的出口是 (0,2) ，距离为 1 步。
```
**示例 2：**
```
*
输入：maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
输出：2
解释：迷宫中只有 1 个出口，在 (1,2) 处。
(1,0) 不算出口，因为它是入口格子。
初始时，你在入口与格子 (1,0) 处。
- 你可以往右移动 2 步到达 (1,2) 处。
所以，最近的出口为 (1,2) ，距离为 2 步。
```
**示例 3：**
```
*
输入：maze = [[".","+"]], entrance = [0,0]
输出：-1
解释：这个迷宫中没有出口。
```
**提示：**

- `maze.length == m`

- `maze[i].length == n`

- `1 row col
**思路**：BFS从入口走迷宫,遇到在边界的'.'即为出口(入口本身不算).返回最短步数.
**代码**：
```python
def nearestExit(self, maze, entrance):
    m, n = len(maze), len(maze[0])
    q = deque([(entrance[0], entrance[1], 0)])
    visited = set([(entrance[0], entrance[1])])

    while q:
        i, j, steps = q.popleft()
        if (i == 0 or i == m-1 or j == 0 or j == n-1) and [i, j] != entrance:
            return steps
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == '.' and (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((ni, nj, steps+1))
    return -1
```
### 3. All Paths From Source to Target（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/all-paths-from-source-to-target/)
**难度**：中等
**题目**：给你一个有 `n` 个节点的 **有向无环图（DAG）**，请你找出从节点 `0` 到节点 `n-1` 的所有路径并输出（**不要求按特定顺序**）

`graph[i]` 是一个从节点 `i` 可以访问的所有节点的列表（即从节点 `i` 到节点 `graph[i][j]`存在一条有向边）。

**示例 1：**
```
*
输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
```
**示例 2：**
```
*
输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```
**提示：**

- `n == graph.length`

- `2
**思路**：DAG上DFS回溯.从0出发,记录当前路径,到达n-1时保存路径.
**代码**：
```python
def allPathsSourceTarget(self, graph):
    n = len(graph)
    res = []

    def dfs(node, path):
        if node == n - 1:
            res.append(path[:])
            return
        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            path.pop()

    dfs(0, [0])
    return res
```
### 4. 01 Matrix（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/01-matrix/)
**难度**：中等
**题目**：给定一个由 `0` 和 `1` 组成的矩阵 `mat` ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1` 。

**示例 1：**
```
*
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
```
**示例 2：**
```
*
输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
```
**提示：**

- `m == mat.length`

- `n == mat[i].length`

- `1 4`

- `1 4`

- `mat[i][j] is either 0 or 1.`

- `mat` 中至少有一个 `0 `
**思路**：多源BFS.所有0入队(距离0),BFS逐层扩散更新1的距离.每个位置第一次被访问时距离最短.
**代码**：
```python
def updateMatrix(self, mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    dist = [[-1] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        i, j = q.popleft()
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```
### 5. Is Graph Bipartite?（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/is-graph-bipartite/)
**难度**：中等
**题目**：存在一个 **无向图** ，图中有 `n` 个节点。其中每个节点都有一个介于 `0` 到 `n - 1` 之间的唯一编号。给你一个二维数组 `graph` ，其中 `graph[u]` 是一个节点数组，由节点 `u` 的邻接节点组成。形式上，对于 `graph[u]` 中的每个 `v` ，都存在一条位于节点 `u` 和节点 `v` 之间的无向边。该无向图同时具有以下属性：

- 不存在自环（`graph[u]` 不包含 `u`）。

- 不存在平行边（`graph[u]` 不包含重复值）。

- 如果 `v` 在 `graph[u]` 内，那么 `u` 也应该在 `graph[v]` 内（该图是无向图）

- 这个图可能不是连通图，也就是说两个节点 `u` 和 `v` 之间可能不存在一条连通彼此的路径。

**二分图**定义：如果能将一个图的节点集合分割成两个独立的子集 `A` 和 `B` ，并使图中的每一条边的两个节点一个来自 `A` 集合，一个来自 `B` 集合，就将这个图称为**二分图** 。

如果图是二分图，返回 `true`  *；否则，返回 `false` 。

**示例 1：**
```
*
输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。
```
**示例 2：**
```
*
输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。
```
**提示：**

- `graph.length == n`

- `1
**思路**：二染色法.DFS对每个未染色节点染色0,邻接点染为1-当前色.若邻接点已染同色则不是二分图.
**代码**：
```python
def isBipartite(self, graph):
    n = len(graph)
    color = [-1] * n

    def dfs(node, c):
        if color[node] != -1:
            return color[node] == c
        color[node] = c
        for nei in graph[node]:
            if not dfs(nei, 1 - c):
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    return True
```
### 6. Open the Lock（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/open-the-lock/)
**难度**：中等
**题目**：你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'` 。每个拨轮可以自由旋转：例如把 `'9'` 变为 `'0'`，`'0'` 变为 `'9'` 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 `'0000'` ，一个代表四个拨轮的数字的字符串。

列表 `deadends` 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 `target` 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 `-1` 。

**示例 1:**
```
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
```
**示例 2:**
```
输入: deadends = ["8888"], target = "0009"
输出：1
解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
```
**示例 3:**
```
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：无法旋转到目标数字且不被锁定。
```
**提示：**

- `1 deadends[i].length == 4`

- `target.length == 4`

- `target` *不在** `deadends` 之中

- `target` 和 `deadends[i]` 仅由若干位数字组成
**思路**：隐式图BFS.每个密码状态(0000~9999)为节点,每次转动一位(±1).deadends不可访问,求从0000到target的最短步数.
**代码**：
```python
def openLock(self, deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1

    q = deque([("0000", 0)])
    visited = set(["0000"])

    while q:
        state, steps = q.popleft()
        if state == target:
            return steps

        for i in range(4):
            for d in [-1, 1]:
                nxt = list(state)
                nxt[i] = str((int(nxt[i]) + d) % 10)
                nxt = "".join(nxt)
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
    return -1
```
## 📝 总结
- 多源BFS: 所有源点一起入队,距离同步更新.
- 二分图判定: 二染色,相邻异色,DFS/BFS均可.
- 隐式图: 状态定义+合法转移=BFS搜索.
- DAG回溯: 简单DFS,不需要visited(无环).


---

# Day 32: 回溯基础

## 📖 知识点
**回溯(Backtracking)** — 穷举搜索+剪枝.核心模板:
```python
def backtrack(path, choices):
    if 满足条件:
        res.append(path[:])
        return
    for choice in choices:
        做选择
        backtrack(path, choice)
        撤销选择
```
**适用场景**:组合、排列、子集、分割、棋盘问题.
**剪枝**:排序+跳过重复元素、提前判断可行性.

## 🧩 刷题任务（6题）

### 1. Letter Combinations of a Phone Number（⭐⭐）
**来源**：[L75/T150](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)
**难度**：中等
**题目**：给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

*

**示例 1：**
```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```
**示例 2：**
```
输入：digits = "2"
输出：["a","b","c"]
```
**提示：**

- `1
**思路**：数字到字母映射,回溯生成所有组合.每次选择一个字母,递归处理下一个数字.
**代码**：
```python
def letterCombinations(self, digits):
    if not digits:
        return []
    mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl",
               "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    res = []

    def backtrack(idx, path):
        if idx == len(digits):
            res.append("".join(path))
            return
        for c in mapping[digits[idx]]:
            path.append(c)
            backtrack(idx + 1, path)
            path.pop()

    backtrack(0, [])
    return res
```
### 2. Combinations（⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/combinations/)
**难度**：中等
**题目**：给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

你可以按 **任何顺序** 返回答案。

**示例 1：**
```
输入：n = 4, k = 2
输出：
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]
```
**示例 2：**
```
输入：n = 1, k = 1
输出：[[1]]
```
**提示：**

- `1
**思路**：从1~n中选k个数的组合.回溯时限制起始位置避免重复组合.
**代码**：
```python
def combine(self, n, k):
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return res
```
### 3. Combination Sum III（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/combination-sum-iii/)
**难度**：中等
**题目**：找出所有相加之和为 `n`  *的 `k` 个数的组合，且满足下列条件：

- 只使用数字1到9

- 每个数字 **最多使用一次**

返回 *所有可能的有效组合的列表* 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

**示例 1:**
```
输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
```
**示例 2:**
```
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。
```
**示例 3:**
```
输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
```
**提示:**

- `2
**思路**：从1~9中选k个数,和为n.回溯+剪枝:当前和超过n或可选数不够时提前返回.
**代码**：
```python
def combinationSum3(self, k, n):
    res = []

    def backtrack(start, path, cur_sum):
        if len(path) == k:
            if cur_sum == n:
                res.append(path[:])
            return
        for i in range(start, 10):
            if cur_sum + i > n:
                break
            path.append(i)
            backtrack(i + 1, path, cur_sum + i)
            path.pop()

    backtrack(1, [], 0)
    return res
```
### 4. Permutations（⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/permutations/)
**难度**：中等
**题目**：给定一个不含重复数字的数组 `nums` ，返回其 *所有可能的全排列* 。你可以 **按任意顺序** 返回答案。

**示例 1：**
```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
**示例 2：**
```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```
**示例 3：**
```
输入：nums = [1]
输出：[[1]]
```
**提示：**

- `1
**思路**：全排列回溯.用used数组标记已选元素,每次从未选元素中选择.
**代码**：
```python
def permute(self, nums):
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return res
```
### 5. Permutations II（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/permutations/)
**难度**：中等
**题目**：给定一个不含重复数字的数组 `nums` ，返回其 *所有可能的全排列* 。你可以 **按任意顺序** 返回答案。

**示例 1：**
```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
**示例 2：**
```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```
**示例 3：**
```
输入：nums = [1]
输出：[[1]]
```
**提示：**

- `1
**思路**：含重复元素的全排列.先排序,剪枝条件:同一层中跳过重复元素(i>0且nums[i]==nums[i-1]且used[i-1]为False).
**代码**：
```python
def permuteUnique(self, nums):
    nums.sort()
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res
```
### 6. Generate Parentheses（⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/generate-parentheses/)
**难度**：中等
**题目**：数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的 **括号组合。

**示例 1：**
```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```
**示例 2：**
```
输入：n = 1
输出：["()"]
```
**提示：**

- `1
**思路**：回溯生成合法括号对.维护左括号和右括号计数,保证任何时刻左括号数≥右括号数.
**代码**：
```python
def generateParenthesis(self, n):
    res = []

    def backtrack(left, right, path):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if left < n:
            path.append('(')
            backtrack(left + 1, right, path)
            path.pop()
        if right < left:
            path.append(')')
            backtrack(left, right + 1, path)
            path.pop()

    backtrack(0, 0, [])
    return res
```
## 📝 总结
- 组合: 限制起始位置(start index)避免重复.
- 排列: used数组标记,每次全部搜索.
- 去重: 排序+同层剪枝(used[i-1]==False).
- 括号生成: 左右计数约束保证合法性.


---

# Day 33: 回溯进阶

## 📖 知识点
**进阶回溯技巧**:
- **子集枚举**: 每个元素选或不选,或使用循环+start.
- **可重复使用元素**: 递归时start不变(Combination Sum).
- **不可重复使用+去重**: start+1 + 排序剪枝(Combination Sum II).
- **棋盘/矩阵搜索**: 方向数组+visited或原地修改(Word Search).
- **分割问题**: 在不同位置切分,验证合法性(Restore IP).

## 🧩 刷题任务（6题）

### 1. Subsets（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/subsets/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，数组中的元素 **互不相同**。返回该数组所有可能的子集（幂集）。

解集**不能**包含重复的子集。你可以按**任意顺序** 返回解集。

**示例 1：**
```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```
**示例 2：**
```
输入：nums = [0]
输出：[[],[0]]
```
**提示：**

- `1
**思路**：枚举所有子集.每个元素有选与不选两种选择,回溯穷举.
**代码**：
```python
def subsets(self, nums):
    res = []

    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res
```
### 2. Combination Sum（⭐⭐）
**来源**：[T150/O](https://leetcode.cn/problems/combination-sum/)
**难度**：中等
**题目**：给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有* ***不同组合**，并以列表形式返回。你可以按**任意顺序**返回这些组合。

`candidates` 中的**同一个**数字可以**无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

**示例 1：**
```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```
**示例 2：**
```
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```
**示例 3：**
```
输入: candidates = [2], target = 1
输出: []
```
**提示：**

- `1
**思路**：从candidates中选可重复使用的元素求和为target.回溯时start位置不变(可重复选),当前和超过target剪枝.
**代码**：
```python
def combinationSum(self, candidates, target):
    res = []

    def backtrack(start, path, cur_sum):
        if cur_sum == target:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if cur_sum + candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, path, cur_sum + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res
```
### 3. Combination Sum II（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/combination-sum/)
**难度**：中等
**题目**：给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有* ***不同组合**，并以列表形式返回。你可以按**任意顺序**返回这些组合。

`candidates` 中的**同一个**数字可以**无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

**示例 1：**
```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```
**示例 2：**
```
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```
**示例 3：**
```
输入: candidates = [2], target = 1
输出: []
```
**提示：**

- `1
**思路**：每个元素只能用一次+有重复.先排序,同层跳过重复元素,递归时start+1.
**代码**：
```python
def combinationSum2(self, candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, path, cur_sum):
        if cur_sum == target:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if cur_sum + candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, cur_sum + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res
```
### 4. N-Queens II（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/n-queens-ii/)
**难度**：困难
**题目**：**n 皇后问题**研究的是如何将 `n` 个皇后放置在 `n × n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回**n 皇后问题** 不同的解决方案的数量。

**示例 1：**
```
*
输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
```
**示例 2：**
```
输入：n = 1
输出：1
```
**提示：**

- `1
**思路**：回溯放置皇后.用三个集合记录被占用的列、主对角线(row-col)、副对角线(row+col).每行放一个皇后,DFS所有行.
**代码**：
```python
def totalNQueens(self, n):
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            d1, d2 = row - col, row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            cols.add(col); diag1.add(d1); diag2.add(d2)
            count += backtrack(row + 1)
            cols.remove(col); diag1.remove(d1); diag2.remove(d2)
        return count

    return backtrack(0)
```
### 5. Word Search（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/word-search/)
**难度**：中等
**题目**：给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例 1：**
```
*
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true
```
**示例 2：**
```
*
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true
```
**示例 3：**
```
*
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false
```
**提示：**

- `m == board.length`

- `n = board[i].length`

- `1

**进阶：**你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？
**思路**：在网格中回溯搜索单词.从每个匹配首字母的位置出发,四方向DFS,已使用的字母标记为'#'避免重复使用.
**代码**：
```python
def exist(self, board, word):
    m, n = len(board), len(board[0])

    def dfs(i, j, idx):
        if idx == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
            return False
        temp, board[i][j] = board[i][j], '#'
        found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or
                 dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))
        board[i][j] = temp
        return found

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False
```
### 6. Restore IP Addresses（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/restore-ip-addresses/)
**难度**：中等
**题目**：**有效 IP 地址**正好由四个整数（每个整数位于 `0` 到 `255` 之间组成，且不能含有前导 `0`），整数之间用 `'.'` 分隔。

- 例如：`"0.1.2.201"` 和` "192.168.1.1"` 是**有效**IP 地址，但是 `"0.011.255.245"`、`"192.168.1.312"` 和 `"192.168@1.1"` 是**无效** IP 地址。

给定一个只包含数字的字符串 `s` ，用以表示一个 IP 地址，返回所有可能的**有效 IP 地址**，这些地址可以通过在 `s` 中插入 `'.'` 来形成。你 **不能**重新排序或删除 `s` 中的任何数字。你可以按**任何** 顺序返回答案。

**示例 1：**
```
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
```
**示例 2：**
```
输入：s = "0000"
输出：["0.0.0.0"]
```
**示例 3：**
```
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```
**提示：**

- `1
**思路**：分割字符串为4段合法IP.回溯在s的不同位置切割,每段需在0~255且无前导零(除非为0).
**代码**：
```python
def restoreIpAddresses(self, s):
    res = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append(".".join(path))
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                continue
            path.append(segment)
            backtrack(end, path)
            path.pop()

    backtrack(0, [])
    return res
```
## 📝 总结
- 子集 & 组合: start控制不回头,避免重复组合.
- 可重复选 vs 不可重复: start不变 vs start+1.
- 去重: 排序 + i > start跳过同层重复.
- N皇后: 对角线巧妙映射(col±row).
- 网格搜索: 方向数组 + 原地修改回溯.
- 分割问题: 验证每段合法性.


---

# Day 34: Trie（前缀树）

## 📖 知识点
**Trie(前缀树)** — 高效存储和检索字符串集合的树形数据结构.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```
**核心操作**:
- 插入: 沿着路径逐字符创建节点.
- 搜索: 沿着路径逐字符查找.
- 前缀匹配: 判断是否存在以给定前缀开头的单词.
- 通配符搜索: DFS匹配'.'(任意字符).

## 🧩 刷题任务（6题）

### 1. Implement Trie (Prefix Tree)（⭐⭐）
**来源**：[L75/T150/O](https://leetcode.cn/problems/implement-trie-prefix-tree/)
**难度**：中等
**题目**：**Trie**（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

- `Trie()` 初始化前缀树对象。

- `void insert(String word)` 向前缀树中插入字符串 `word` 。

- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。

- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

**示例：**
```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]
解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```
**提示：**

- `1 4` 次
**思路**：实现Trie类的insert,search,startsWith三个方法.用字典存储子节点.
**代码**：
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
```
### 2. Search Suggestions System（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/search-suggestions-system/)
**难度**：中等
**题目**：给你一个产品数组 `products` 和一个字符串 `searchWord` ，`products`  数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 `searchWord` 的每一个字母后，推荐 `products` 数组中前缀与 `searchWord` 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 `searchWord` 每个字母后相应的推荐产品的列表。

**示例 1：**
```
输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]
```
**示例 2：**
```
输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```
**示例 3：**
```
输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
```
**示例 4：**
```
输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]
```
**提示：**

- `1
**思路**：对products排序后构建Trie(或直接排序+二分).每个节点存储该前缀下的前3个推荐(按字典序).也可以在Trie节点存推荐列表.
**代码**：
```python
def suggestedProducts(self, products, searchWord):
    products.sort()
    root = {}
    # 构建Trie,每个节点存字典序前三的推荐
    for p in products:
        node = root
        for c in p:
            if c not in node:
                node[c] = {}
            node = node[c]
            if 'suggest' not in node:
                node['suggest'] = []
            if len(node['suggest']) < 3:
                node['suggest'].append(p)

    res = []
    node = root
    for c in searchWord:
        if c in node:
            node = node[c]
            res.append(node.get('suggest', []))
        else:
            # 后续都为空
            node = {}
            res.append([])
    return res
```
### 3. Add and Search Word（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/design-add-and-search-words-data-structure/)
**难度**：中等
**题目**：请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 `WordDictionary` ：

- `WordDictionary()` 初始化词典对象

- `void addWord(word)` 将 `word` 添加到数据结构中，之后可以对它进行匹配

- `bool search(word)` 如果数据结构中存在字符串与 `word` 匹配，则返回 `true` ；否则，返回  `false` 。`word` 中可能包含一些 `'.'` ，每个 `.` 都可以表示任何一个字母。

**示例：**
```
输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]
解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // 返回 False
wordDictionary.search("bad"); // 返回 True
wordDictionary.search(".ad"); // 返回 True
wordDictionary.search("b.."); // 返回 True
```
**提示：**

- `1 4` 次 `addWord` 和 `search` *思路**：支持通配符'.'(匹配任意字符)的Trie.search时遇到'.'需DFS遍历所有子节点.
**代码**：
```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            c = word[idx]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(node.children[c], idx + 1)

        return dfs(self.root, 0)
```
### 4. Word Search II（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/word-search/)
**难度**：中等
**题目**：给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例 1：**
```
*
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true
```
**示例 2：**
```
*
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true
```
**示例 3：**
```
*
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false
```
**提示：**

- `m == board.length`

- `n = board[i].length`

- `1

**进阶：**你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？
**思路**：Trie + 回溯.先将words构建Trie,然后在board上DFS搜索,同时沿Trie节点移动,匹配到完整单词则加入结果.用'#'标记已访问单元格.
**代码**：
```python
def findWords(self, board, words):
    # 构建Trie
    root = {}
    for w in words:
        node = root
        for c in w:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = w  # 用'#'存储完整单词

    m, n = len(board), len(board[0])
    res = []

    def dfs(i, j, node):
        if '#' in node:
            res.append(node.pop('#'))  # 去重
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node:
            return
        c, board[i][j] = board[i][j], '*'
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(i+di, j+dj, node[c])
        board[i][j] = c

    for i in range(m):
        for j in range(n):
            if board[i][j] in root:
                dfs(i, j, root)
    return res
```
### 5. Replace Words（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/replace-words/)
**难度**：中等
**题目**：在英语中，我们有一个叫做 **词根**(root) 的概念，可以词根 **后面 **添加其他一些词组成另一个较长的单词——我们称这个词为 **衍生词** (**derivative**)。例如，词根 `help`，跟随着 **继承**词 `"ful"`，可以形成新的单词 `"helpful"`。

现在，给定一个由许多 **词根 **组成的词典 `dictionary` 和一个用空格分隔单词形成的句子 `sentence`。你需要将句子中的所有 **衍生词 **用 **词根 **替换掉。如果 **衍生词 **有许多可以形成它的 **词根**，则用 **最短 **的 **词根** 替换它。

你需要输出替换之后的句子。

**示例 1：**
```
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
```
**示例 2：**
```
输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
```
**提示：**

- `1 6`

- `sentence` 仅由小写字母和空格组成。

- `sentence` 中单词的总量在范围 `[1, 1000]` 内。

- `sentence` 中每个单词的长度在范围 `[1, 1000]` 内。

- `sentence` 中单词之间由一个空格隔开。

- `sentence` 没有前导或尾随空格。
**思路**：构建Trie存储词根.对句子每个单词,在Trie中查找最短前缀(词根),找到则替换.
**代码**：
```python
def replaceWords(self, dictionary, sentence):
    root = {}
    for word in dictionary:
        node = root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = True  # 标记为词根结尾

    def replace(word):
        node = root
        for i, c in enumerate(word):
            if '*' in node:
                return word[:i]
            if c not in node:
                return word
            node = node[c]
        return word

    return ' '.join(replace(w) for w in sentence.split())
```
### 6. Magic Dictionary（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/implement-magic-dictionary/)
**难度**：中等
**题目**：设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 **互不相同** 。 如果给出一个单词，请判定能否只将这个单词中**一个**字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 `MagicDictionary` 类：

- `MagicDictionary()` 初始化对象

- `void buildDict(String[] dictionary)` 使用字符串数组 `dictionary` 设定该数据结构，`dictionary` 中的字符串互不相同

- `bool search(String searchWord)` 给定一个字符串 `searchWord` ，判定能否只将字符串中**一个**字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 `true` ；否则，返回 `false` 。

**示例：**
```
输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]
解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
```
**提示：**

- `1
**思路**：前缀树+容错搜索.搜索时允许恰好1个字符不同.在search时跟踪是否已使用一次修改机会.
**代码**：
```python
class MagicDictionary:
    def __init__(self):
        self.root = {}

    def buildDict(self, dictionary):
        for w in dictionary:
            node = self.root
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True

    def search(self, searchWord):
        def dfs(node, idx, modified):
            if idx == len(searchWord):
                return '#' in node and modified
            c = searchWord[idx]
            for child_char, child_node in node.items():
                if child_char == '#':
                    continue
                if child_char == c:
                    if dfs(child_node, idx + 1, modified):
                        return True
                elif not modified:
                    if dfs(child_node, idx + 1, True):
                        return True
            return False

        return dfs(self.root, 0, False)
```
## 📝 总结
- Trie本质: 多叉树,每个节点存子节点映射和结束标记.
- 通配符: '.'匹配任意字符,DFS遍历所有子节点.
- Trie+回溯: 网格搜索时同时推进Trie节点,大幅优化.
- 前缀替换: 沿Trie查找最短前缀.
- 容错搜索: 在DFS中记录修改次数,精确控制错误容忍度.


---

# Day 35: 周复习 — 图、回溯、Trie

## 📖 本周知识体系总览

```
Week 5: 图/回溯/Trie
├── D29 图-DFS       连通分量 | 判环 | 带权图 | 可达性
├── D30 图-BFS       拓扑排序 | 最短路径 | 双向BFS | 多源BFS
├── D31 图进阶       多源BFS | 二分图 | 隐式图 | DAG路径
├── D32 回溯基础     组合 | 排列 | 去重 | 括号生成
├── D33 回溯进阶     子集 | 组合和 | N皇后 | 网格搜索 | 分割
└── D34 Trie         前缀树 | 通配符搜索 | Trie+回溯 | 容错
```

## 🧩 图算法迷你测验（10题）

**Q1**: 无权图中求最短路径用哪种搜索?
<details><summary>答案</summary>BFS,第一次到达目标即为最短.</details>

**Q2**: 拓扑排序的两种实现方式?
<details><summary>答案</summary>Kahn算法(入度表+BFS队列)和DFS后序(逆后序).</details>

**Q3**: 检测图中是否有环的方法?
<details><summary>答案</summary>DFS: 三色标记(白灰黑),发现灰色节点即有环.
Kahn: 拓扑排序后节点数不足即有环.</details>

**Q4**: 双向BFS相比普通BFS的优势?
<details><summary>答案</summary>搜索空间从b^d缩减到2*b^(d/2),大幅减少分支扩展.</details>

**Q5**: 如何判断二分图?
<details><summary>答案</summary>二染色: 相邻节点染不同色,DFS/BFS遍历染色,冲突则不是.</details>

**Q6**: 组合和排列的核心代码区别?
<details><summary>答案</summary>组合用start参数(不回头),排列用used数组(可回头).</details>

**Q7**: 有重复元素的全排列如何去重?
<details><summary>答案</summary>排序+同层剪枝: `if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue`</details>

**Q8**: Word Search I和II的核心区别?
<details><summary>答案</summary>I: 搜索单个单词,每次从网格起点DFS. II: 搜索多个单词,用Trie优化,DFS同时沿Trie节点移动.</details>

**Q9**: Trie的search和startsWith的区别?
<details><summary>答案</summary>search要求is_end=True(完整单词),startsWith只需路径存在.</details>

**Q10**: N-Queens对角线的表示方法?
<details><summary>答案</summary>主对角线: row-col(常数差),副对角线: row+col(常数和).</details>

## 📝 常见错误自查表

| 问题 | 常见错误 | 正确做法 |
|------|---------|---------|
| 图DFS | 忘记visited导致死循环 | 入队/入栈前标记visited |
| BFS最短路径 | 步数计数位置错误 | 每层结束时+1或存步数到队列 |
| 拓扑排序 | 忽略入度更新顺序 | 出队后更新所有邻居入度 |
| 回溯去重 | 使用全局used判断同层重复 | 必须加 `i > start` 条件 |
| 组合可重复选 | 错误start+1 | 递归时start不变 |
| Trie通配符搜索 | 忘记处理'.'的递归回溯 | DFS遍历所有子节点 |
| 网格搜索 | 边界和字符检查顺序 | 先检查边界再检查字符 |

## 🔗 关联题目汇总

| 题型 | 核心题 | 变种 |
|------|-------|------|
| 图DFS | Number of Islands → | Surrounded Regions, Max Area of Island |
| 拓扑排序 | Course Schedule → | Course Schedule II, Alien Dictionary |
| BFS最短路径 | Word Ladder → | Min Genetic Mutation, Open the Lock |
| 多源BFS | Rotting Oranges → | 01 Matrix, Walls and Gates |
| 回溯组合 | Combinations → | Combination Sum (I/II/III), Subsets |
| 回溯排列 | Permutations → | Permutations II, Next Permutation |
| N皇后 | N-Queens II → | N-Queens I, Sudoku Solver |
| 网格搜索 | Word Search → | Word Search II |
| Trie | Implement Trie → | Add and Search Word, Magic Dictionary |

## 📊 难度分布

| 难度 | 题数 | 占比 |
|------|------|------|
| ⭐⭐ (中等) | 30 | 83% |
| ⭐⭐⭐ (较难) | 6 | 17% |
| 总计 | 36 | 100% |


---


---
# 第6周·OD100题(下)
> 共计 7 天

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
**来源**：[T150](https://leetcode.cn/problems/search-insert-position/)
**难度**：简单
**题目**：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

**示例 1:**
```
输入: nums = [1,3,5,6], target = 5
输出: 2
```
**示例 2:**
```
输入: nums = [1,3,5,6], target = 2
输出: 1
```
**示例 3:**
```
输入: nums = [1,3,5,6], target = 7
输出: 4
```
**提示:**

- `1 4`

- `-104 4`

- `nums` 为 **无重复元素 **的 **升序 **排列数组

- `-104 4`
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
**来源**：[T150](https://leetcode.cn/problems/search-a-2d-matrix/)
**难度**：中等
**题目**：给你一个满足下述两条属性的 `m x n` 整数矩阵：

- 每行中的整数从左到右按非严格递增顺序排列。

- 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 `target` ，如果 `target` 在矩阵中，返回 `true` ；否则，返回 `false` 。

**示例 1：**
```
*
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```
**示例 2：**
```
*
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
```
**提示：**

- `m == matrix.length`

- `n == matrix[i].length`

- `1 4 4`
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
**来源**：[L75](https://leetcode.cn/problems/find-peak-element/)
**难度**：中等
**题目**：峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)`* *的算法来解决此问题。

**示例 1：**
```
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
```
**示例 2：**
```
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
或者返回索引 5， 其峰值元素为 6。
```
**提示：**

- `1 31 31 - 1`

- 对于所有有效的 `i` 都有 `nums[i] != nums[i + 1]`
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
**来源**：[T150](https://leetcode.cn/problems/search-in-rotated-sorted-array/)
**难度**：中等
**题目**：整数数组 `nums` 按升序排列，数组中的值 **互不相同**。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0
- `1 4 4`

- `nums` 中的每个值都**独一无二**

- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转

- `-104 4`
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
**来源**：[T150](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)
**难度**：中等
**题目**：给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**
```
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```
**示例 2：**
```
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```
**示例 3：**
```
输入：nums = [], target = 0
输出：[-1,-1]
```
**提示：**

- `0 5`

- `-109 9`

- `nums` 是一个非递减数组

- `-109 9`
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
**来源**：[T150](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)
**难度**：中等
**题目**：已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转**后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：

- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]`

- 若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]`

注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]`**旋转一次**的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值**互不相同**的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的**最小元素** 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**
```
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```
**示例 2：**
```
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
```
**示例 3：**
```
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
```
**提示：**

- `n == nums.length`

- `1
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


---

# Day 37: 二分 + 排序

## 📖 知识点
**按值二分（答案二分）模板**
```python
def feasible(x):
    # 判断当前猜测值 x 是否可行
    pass

left, right = min_possible, max_possible
while left < right:
    mid = left + (right - left) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1
return left
```

**排序算法速览**：
- **快速排序**：O(n log n)，不稳定，原地排序
- **归并排序**：O(n log n)，稳定，需要 O(n) 额外空间
- **Python 内置**：`list.sort()` / `sorted()` 是 Timsort（归并+插入），稳定且高效

**链表排序**：归并排序（找中点 + 合并两个有序链表）

## 🧩 刷题任务（6题）

### 1. 猜数字大小（⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/guess-number-higher-or-lower/)
**难度**：简单
**题目**：我们正在玩猜数字游戏。猜数字游戏的规则如下：

我会从 `1` 到 `n` 随机选择一个数字。 请你猜选出的是哪个数字。（我选的数字在整个游戏中保持不变）。

如果你猜错了，我会告诉你，我选出的数字比你猜测的数字大了还是小了。

你可以通过调用一个预先定义好的接口 `int guess(int num)` 来获取猜测结果，返回值一共有三种可能的情况：

- `-1`：你猜的数字比我选出的数字大 （即 `num > pick`）。

- `1`：你猜的数字比我选出的数字小 （即 `num

返回我选出的数字。

**示例 1：**
```
输入：n = 10, pick = 6
输出：6
```
**示例 2：**
```
输入：n = 1, pick = 1
输出：1
```
**示例 3：**
```
输入：n = 2, pick = 1
输出：1
```
**提示：**

- `1 31 - 1`

- `1
**思路**：标准二分。`guess(n)` 返回 -1/0/1，按照二分模板找目标值。注意 mid 计算用 `left + (right - left) // 2` 避免溢出。
**代码**：
```python
def guessNumber(n):
    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res == 1:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
### 2. 爱吃香蕉的珂珂（⭐⭐）来源：L75 / T150 / O
**来源**：[L75](https://leetcode.cn/problems/koko-eating-bananas/)
**难度**：中等
**题目**：珂珂喜欢吃香蕉。这里有 `n` 堆香蕉，第 `i` 堆中有 `piles[i]` 根香蕉。警卫已经离开了，将在 `h` 小时后回来。

珂珂可以决定她吃香蕉的速度 `k` （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 `k` 根。如果这堆香蕉少于 `k` 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 `h` 小时内吃掉所有香蕉的最小速度 `k`（`k` 为整数）。

**示例 1：**
```
输入：piles = [3,6,7,11], h = 8
输出：4
```
**示例 2：**
```
输入：piles = [30,11,23,4,20], h = 5
输出：30
```
**示例 3：**
```
输入：piles = [30,11,23,4,20], h = 6
输出：23
```
**提示：**

- `1 4`

- `piles.length 9`

- `1 9`
**思路**：按值二分。速度 K 的范围是 [1, max(piles)]。feasible(K) 判断能否在 H 小时内吃完：对每堆香蕉，需要 `(pile + K - 1) // K` 小时。找最小可行 K。
**代码**：
```python
def minEatingSpeed(piles, h):
    def can_finish(k):
        total = 0
        for p in piles:
            total += (p + k - 1) // k
        return total <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
### 3. 寻找两个正序数组的中位数（⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/median-of-two-sorted-arrays/)
**难度**：困难
**题目**：给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

**示例 1：**
```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```
**示例 2：**
```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```
**提示：**

- `nums1.length == m`

- `nums2.length == n`

- `0 6 6`
**思路**：核心思路是对较短的数组做二分划分线。保证左半部分的最大值 ≤ 右半部分的最小值。中位数取决于总长度奇偶性。关键是理解划分线 i 和 j 的关系：i + j = (m + n + 1) // 2。
**代码**：
```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        i = left + (right - left) // 2
        j = (m + n + 1) // 2 - i
        left1 = nums1[i - 1] if i > 0 else -float('inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j - 1] if j > 0 else -float('inf')
        right2 = nums2[j] if j < n else float('inf')
        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2.0
            else:
                return max(left1, left2)
        elif left1 > right2:
            right = i - 1
        else:
            left = i + 1
    return 0.0
```
### 4. 排序链表（⭐⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/sort-list/)
**难度**：中等
**题目**：给你链表的头结点 `head` ，请将其按 **升序**排列并返回**排序后的链表** 。

**示例 1：**
```
*
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```
**示例 2：**
```
*
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```
**示例 3：**
```
输入：head = []
输出：[]
```
**提示：**

- 链表中节点的数目在范围 `[0, 5 * 104]` 内

- `-105 5`

**进阶：**你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
**思路**：链表归并排序。用快慢指针找中点，递归排序左右两半，然后合并两个有序链表。时间 O(n log n)，空间 O(log n)（递归栈）。
**代码**：
```python
def sortList(head):
    if not head or not head.next:
        return head

    # 快慢指针找中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None  # 断开链表

    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
```
### 5. 相对排序数组（⭐）来源：O
**来源**：[O](https://leetcode.cn/problems/relative-sort-array/)
**难度**：简单
**题目**：给你两个数组，`arr1` 和 `arr2`，`arr2` 中的元素各不相同，`arr2` 中的每个元素都出现在 `arr1` 中。

对 `arr1` 中的元素进行排序，使 `arr1` 中项的相对顺序和 `arr2` 中的相对顺序相同。未在 `arr2` 中出现过的元素需要按照升序放在 `arr1` 的末尾。

**示例 1：**
```
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
```
**示例  2:**
```
输入：arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
输出：[22,28,8,6,17,44]
```
**提示：**

- `1
**思路**：计数排序。先统计 arr1 中每个数的出现次数。按 arr2 的顺序输出，再按升序输出剩余数字。因为值范围小（0~1000），用数组计数。
**代码**：
```python
def relativeSortArray(arr1, arr2):
    max_val = max(arr1) if arr1 else 0
    count = [0] * (max_val + 1)
    for x in arr1:
        count[x] += 1

    res = []
    for x in arr2:
        res.extend([x] * count[x])
        count[x] = 0

    for i in range(max_val + 1):
        if count[i] > 0:
            res.extend([i] * count[i])
    return res
```
### 6. 山脉数组的峰顶索引（⭐）来源：O
**来源**：[O](https://leetcode.cn/problems/peak-index-in-a-mountain-array/)
**难度**：中等
**题目**：给定一个长度为 `n` 的整数 **山脉 **数组 `arr` ，其中的值递增到一个 **峰值元素** 然后递减。

返回峰值元素的下标。

你必须设计并实现时间复杂度为 `O(log(n))` 的解决方案。

**示例 1：**
```
输入：arr = [0,1,0]
输出：1
```
**示例 2：**
```
输入：arr = [0,2,1,0]
输出：1
```
**示例 3：**
```
输入：arr = [0,10,5,2]
输出：1
```
**提示：**

- `3 5`

- `0 6`

- 题目数据 **保证** `arr` 是一个山脉数组
**思路**：山脉数组先增后减，峰值满足 arr[mid] > arr[mid-1] 且 arr[mid] > arr[mid+1]。二分法：如果 arr[mid] < arr[mid+1]，说明在上升段，left 右移；否则在下降段，right 左移。
**代码**：
```python
def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```
## 📝 总结
- **按值二分**解决"最小化最大值"类问题：猜答案 → 验证可行性 → 缩小区间
- **链表排序**首选归并排序，快慢指针找中点是关键技巧
- **计数排序**在数据范围小时非常高效（O(n+k)）
- **山脉数组峰值**本质和"寻找峰值"一样，都是比较 mid 和 mid+1


---

# Day 38: 堆

## 📖 知识点
**堆模板**
```python
import heapq

# 最小堆（Python 默认）
heap = []
heapq.heappush(heap, val)
val = heapq.heappop(heap)

# 最大堆（取负数模拟）
heapq.heappush(heap, -val)
val = -heapq.heappop(heap)

# 前 K 个最小元素
heapq.nsmallest(k, iterable)
heapq.nlargest(k, iterable)
```

**堆的典型应用场景**：
1. **Top K 问题**→ 维护大小为 K 的堆（求最大 K 个用最小堆，求最小 K 个用最大堆）
2.**数据流中位数**→ 一个最大堆 + 一个最小堆，保持平衡
3.**合并 K 个有序链表**→ 所有头节点入堆，每次弹出最小的
4.**多路归并**→ 与合并 K 个有序链表类似
5.**贪心 + 堆** → 每次取最优解，然后加入新的候选

**技巧**：
- 需要自定义优先级时，存元组 `(priority, value)`
- Python 的 heapq 不支持自定义比较器，可以用 `(priority, index, value)` 解决平局问题

## 🧩 刷题任务（6题）

### 1. 数组中的第K个最大元素（⭐⭐）来源：L75 / T150 / O
**来源**：[L75](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
**难度**：中等
**题目**：给定整数数组 `nums` 和整数 `k`，请返回数组中第 `**k**` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

**示例 1:**
```
输入: [3,2,1,5,6,4], k = 2
输出: 5
```
**示例 2:**
```
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
**提示： **
- `1 5`
- `-104 4`
```
**思路**：维护大小为 K 的最小堆。遍历数组，当堆大小 < K 时直接入堆；否则若当前元素 > 堆顶，弹出堆顶并入堆新元素。最终堆顶就是第 K 大的元素。
**代码**：
```python
def findKthLargest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
```
### 2. 无限集中的最小数字（⭐⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/smallest-number-in-infinite-set/)
**难度**：中等
**题目**：现有一个包含所有正整数的集合 `[1, 2, 3, 4, 5, ...]` 。

实现 `SmallestInfiniteSet` 类：

- `SmallestInfiniteSet()` 初始化 **SmallestInfiniteSet**对象以包含**所有**正整数。

- `int popSmallest()`**移除** 并返回该无限集中的最小整数。

- `void addBack(int num)` 如果正整数 `num` *不** 存在于无限集中，则将一个 `num` *添加** 到该无限集中。

**示例：**
```
输入
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
输出
[null, null, 1, 2, 3, null, 1, 4, 5]
解释
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。
smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。
smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。
smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中，
// 且 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。
```
**提示：**

- `1
**思路**：用一个最小堆存储当前集合中的数字，一个 visited 集合去重。初始化时把所有 1~1000 入堆。popSmallest 弹出堆顶；addBack 时如果数字不在 visited 中，入堆并标记。
**代码**：
```python
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)
        self.removed = set()

    def popSmallest(self):
        val = heapq.heappop(self.heap)
        self.removed.add(val)
        return val

    def addBack(self, num):
        if num in self.removed:
            self.removed.remove(num)
            heapq.heappush(self.heap, num)
```
### 3. 最大子序列的分数（⭐⭐⭐）来源：L75
**来源**：[L75](https://leetcode.cn/problems/maximum-score-from-removing-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` 和两个整数 `x` 和 `y` 。你可以执行下面两种操作任意次。

- 删除子字符串 `"ab"` 并得到 `x` 分。

- 比方说，从 `"c**ab**xbae"` 删除 `ab` ，得到 `"cxbae"` 。

- 删除子字符串`"ba"` 并得到 `y` 分。

- 比方说，从 `"cabx**ba**e"` 删除 `ba` ，得到 `"cabxe"` 。

请返回对 `s` 字符串执行上面操作若干次能得到的最大得分。

**示例 1：**
```
输入：s = "cdbcbbaaabab", x = 4, y = 5
输出：19
解释：
- 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
- 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
- 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
- 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
总得分为 5 + 4 + 5 + 5 = 19 。
```
**示例 2：**
```
输入：s = "aabbaaxybbaabb", x = 5, y = 4
输出：20
```
**提示：**

- `1 5`

- `1 4`

- `s` 只包含小写英文字母。
**思路**：将两个数组按 nums2 降序配对。遍历时维持一个大小为 k 的最小堆存 nums1 的值，同时维护 sum1。对每个位置，堆满后计算分数 = sum1 * nums2[i]，取最大值。
**代码**：
```python
def maxScore(nums1, nums2, k):
    pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
    heap = []
    sum1 = 0
    res = 0
    for n1, n2 in pairs:
        heapq.heappush(heap, n1)
        sum1 += n1
        if len(heap) > k:
            sum1 -= heapq.heappop(heap)
        if len(heap) == k:
            res = max(res, sum1 * n2)
    return res
```
### 4. IPO（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/ipo/)
**难度**：困难
**题目**：假设 力扣（LeetCode）即将开始 **IPO**。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 `k` 个不同的项目。帮助 力扣 设计完成最多 `k` 个不同项目后得到最大总资本的方式。

给你 `n` 个项目。对于每个项目 `i` ，它都有一个纯利润 `profits[i]` ，和启动该项目需要的最小资本 `capital[i]` 。

最初，你的资本为 `w` 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择**最多**`k` 个不同项目的列表，以**最大化最终资本** ，并输出最终可获得的最多资本。

答案保证在 32 位有符号整数范围内。

**示例 1：**
```
输入：k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
输出：4
解释：
由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
```
**示例 2：**
```
输入：k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
输出：6
```
**提示：**

- `1 5`

- `0 9`

- `n == profits.length`

- `n == capital.length`

- `1 5`

- `0 4`

- `0 9`
**思路**：贪心 + 堆。先按 capital 排序项目。维护一个最大堆（存利润），把所有 capital ≤ w 的项目利润入堆。每次弹出最大利润的项目，w 增加。重复 k 次。
**代码**：
```python
def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    projects = sorted(zip(capital, profits))
    heap = []
    i = 0
    for _ in range(k):
        while i < n and projects[i][0] <= w:
            heapq.heappush(heap, -projects[i][1])
            i += 1
        if not heap:
            break
        w += -heapq.heappop(heap)
    return w
```
### 5. 查找和最小的K对数字（⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/)
**难度**：中等
**题目**：给定两个以 **非递减顺序排列** 的整数数组 `nums1` 和 `nums2` , 以及一个整数 `k` 。

定义一对值 `(u,v)`，其中第一个元素来自 `nums1`，第二个元素来自 `nums2` 。

请找到和最小的 `k` 个数对 `(u1,v1)`, ` (u2,v2)`  ...  `(uk,vk)` 。

**示例 1:**
```
输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [[1,2],[1,4],[1,6]]
解释: 返回序列中的前 3 对数：
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```
**示例 2:**
```
输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [[1,1],[1,1]]
解释: 返回序列中的前 2 对数：
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```
**提示:**

- `1 5`

- `-109 9`

- `nums1` 和 `nums2` 均为 **升序排列**

- `1 4`

- `k
**思路**：多路归并。所有组合可以看作 nums1[i] + nums2[0] 的 i 条"链表"。每次取出最小的和，并将对应的 nums1[i] + nums2[j+1] 入堆。注意去重。
**代码**：
```python
def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []
    heap = []
    # 初始化：每个 nums1[i] + nums2[0]
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
    res = []
    while heap and len(res) < k:
        s, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return res
```
### 6. 数据流的中位数（⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/find-median-from-data-stream/)
**难度**：困难
**题目**：**中位数**是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

- 例如 `arr = [2,3,4]` 的中位数是 `3` 。

- 例如 `arr = [2,3]` 的中位数是 `(2 + 3) / 2 = 2.5` 。

实现 MedianFinder 类:

-
`MedianFinder()` 初始化 `MedianFinder` 对象。

-
`void addNum(int num)` 将数据流中的整数 `num` 添加到数据结构中。

-
`double findMedian()` 返回到目前为止所有元素的中位数。与实际答案相差 `10-5` 以内的答案将被接受。

**示例 1：**
```
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]
解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```
**提示:**

- `-105 5`

- 在调用 `findMedian` 之前，数据结构中至少有一个元素

- 最多 `5 * 104` 次调用 `addNum` 和 `findMedian` *思路**：维护两个堆：最大堆（存左半部分）和最小堆（存右半部分）。保持两个堆的大小平衡（左堆比右堆多 0 或 1 个元素）。添加元素时先入左堆再调整到右堆，保持所有左堆元素 ≤ 右堆元素。
**代码**：
```python
class MedianFinder:
    def __init__(self):
        self.left = []   # 最大堆（存负数）
        self.right = []  # 最小堆

    def addNum(self, num):
        # 先入左堆（最大堆）
        heapq.heappush(self.left, -num)
        # 平衡：左堆最大 ≤ 右堆最小
        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        # 平衡大小：左堆最多比右堆多 1
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0
```
## 📝 总结
- **堆**擅长解决**动态 Top K** 和**流式数据**问题
- 求**最大** K 个元素 → 用**最小堆**（堆顶是门槛，只有比门槛大的才进来）
- 求**最小** K 个元素 → 用**最大堆**（Python 用负数模拟）
- **两个堆**模型可解决中位数、滑动窗口中间值等问题
- 贪心 + 堆的组合在面试中很常见（IPO、最大子序列分数）


---

# Day 39: 位运算

## 📖 知识点
**位运算速查表**
| 运算 | Python 符号 | 说明 |
|------|-------------|------|
| 与 | `&` | 两位都为 1 才为 1 |
| 或 | `\|` | 有一位为 1 即为 1 |
| 异或 | `^` | 相同为 0，不同为 1 |
| 取反 | `~` | 0 变 1，1 变 0 |
| 左移 | `<<` | 左移 n 位相当于乘以 2ⁿ |
| 右移 | `>>` | 右移 n 位相当于除以 2ⁿ |

**常用技巧**：
```python
# 判断第 k 位是否 1
(num >> k) & 1

# 将第 k 位设为 1
num | (1 << k)

# 将第 k 位设为 0
num & ~(1 << k)

# 将第 k 位取反
num ^ (1 << k)

# 去掉最低位的 1
num & (num - 1)

# 获取最低位的 1
num & -num

# 判断 2 的幂
num > 0 and (num & (num - 1)) == 0

# 统计 1 的个数
bin(num).count('1')   # Python 简单写法
# 或内置函数
num.bit_count()       # Python 3.8+
```

**核心场景**：
1. 异或消除法 → 寻找出现奇数次的元素 (x ^ x = 0, x ^ 0 = x)
2. 位掩码 → 用整数的二进制位表示集合状态（状态压缩 DP）
3. 位计数 → 统计二进制中 1 的个数
4. 位运算替代运算 → 快速乘除 2 的幂

## 🧩 刷题任务（6题）

### 1. 两数相除（⭐⭐⭐）来源：O
**来源**：[O](https://leetcode.cn/problems/divide-two-integers/)
**难度**：中等
**题目**：给你两个整数，被除数 `dividend` 和除数 `divisor`。将两数相除，要求 **不使用**乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（`truncate`）其小数部分。例如，`8.345` 将被截断为 `8` ，`-2.7335` 将被截断至 `-2` 。

返回被除数 `dividend` 除以除数 `divisor` 得到的**商** 。

**注意：**假设我们的环境只能存储 **32 位**有符号整数，其数值范围是 `[−231,  231 − 1]` 。本题中，如果商**严格大于**`231 − 1` ，则返回 `231 − 1` ；如果商**严格小于** `-231` ，则返回 `-231` 。

**示例 1:**
```
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = 3.33333.. ，向零截断后得到 3 。
```
**示例 2:**
```
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。
```
**提示：**

- `-231 31 - 1`

- `divisor != 0`
**思路**：不能用乘除模，用加法/减法替代除法。用倍增法加速：不断将除数翻倍直到超过被除数，从大的开始减。注意处理负号和溢出（-2³¹ 转正数会溢出）。
**代码**：
```python
def divide(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    sign = 1 if (dividend > 0) == (divisor > 0) else -1
    a, b = abs(dividend), abs(divisor)
    res = 0
    while a >= b:
        tmp, multiple = b, 1
        while a >= (tmp << 1):
            tmp <<= 1
            multiple <<= 1
        a -= tmp
        res += multiple
    return sign * res
```
### 2. 二进制求和（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/add-binary/)
**难度**：简单
**题目**：给你两个二进制字符串 `a` 和 `b` ，以二进制字符串的形式返回它们的和。

**示例 1：**
```
输入:a = "11", b = "1"
输出："100"
```
**示例 2：**
```
输入：a = "1010", b = "1011"
输出："10101"
```
**提示：**

- `1 4`

- `a` 和 `b` 仅由字符 `'0'` 或 `'1'` 组成

- 字符串如果不是 `"0"` ，就不含前导零
**思路**：逐位相加，维护进位。从右向左遍历两个字符串，和 = a_bit + b_bit + carry。当前位 = 和 % 2，进位 = 和 // 2。最后如果进位还有则补 1。
**代码**：
```python
def addBinary(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        total = x + y + carry
        res.append(str(total % 2))
        carry = total // 2
        i -= 1
        j -= 1
    return ''.join(reversed(res))
```
### 3. 比特位计数（⭐⭐）来源：L75 / O
**来源**：[L75](https://leetcode.cn/problems/counting-bits/)
**难度**：简单
**题目**：给你一个整数 `n` ，对于 `0

**示例 1：**
```
输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
```
**示例 2：**
```
输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```
**提示：**

- `0 5`

**进阶：**

- 很容易就能实现时间复杂度为 `O(n log n)` 的解决方案，你可以在线性时间复杂度 `O(n)` 内用一趟扫描解决此问题吗？

- 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 `__builtin_popcount` ）
**思路**：动态规划 + 位运算。对于任意数字 i，去掉最低位 1 后得到 i & (i-1)，它的 1 的个数加 1 就是 i 的 1 的个数。递推：`dp[i] = dp[i & (i-1)] + 1`。
**代码**：
```python
def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
```
### 4. 只出现一次的数字 II（⭐⭐⭐）来源：O
**来源**：[O](https://leetcode.cn/problems/single-number-ii/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，除某个元素仅出现 **一次**外，其余每个元素都恰出现**三次 。**请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

**示例 1：**
```
输入：nums = [2,2,3,2]
输出：3
```
**示例 2：**
```
输入：nums = [0,1,0,1,0,1,99]
输出：99
```
**提示：**

- `1 4`

- `-231 31 - 1`

- `nums` 中，除某个元素仅出现 **一次**外，其余每个元素都恰出现**三次**
**思路**：每个数字出现 3 次，只有一个出现 1 次。对每一位统计所有数字在该位上的 1 的个数，模 3 后就是目标值在该位上的值。用两个变量（one, two）模拟三进制状态机。
**代码**：
```python
def singleNumber(nums):
    one = two = 0
    for num in nums:
        one = (one ^ num) & ~two
        two = (two ^ num) & ~one
    return one
```
### 5. 最大单词长度乘积（⭐⭐）来源：O
**来源**：[O](https://leetcode.cn/problems/maximum-product-of-word-lengths/)
**难度**：中等
**题目**：给你一个字符串数组 `words` ，找出并返回 `length(words[i]) * length(words[j])` 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 `0` 。

**示例 1：**
```
输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
输出：16
解释：这两个单词为 "abcw", "xtfn"。
```
**示例 2：**
```
输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
输出：4
解释：这两个单词为 "ab", "cd"。
```
**示例 3：**
```
输入：words = ["a","aa","aaa","aaaa"]
输出：0
解释：不存在这样的两个单词。
```
**提示：**

- `2
**思路**：用位掩码表示每个单词的字母集合（int 的 26 位，a 对应最低位）。两个单词无公共字母 → 掩码按位与为 0。预处理所有单词的掩码和长度，双重循环求最大乘积。
**代码**：
```python
def maxProduct(words):
    masks = []
    for w in words:
        mask = 0
        for c in w:
            mask |= 1 << (ord(c) - ord('a'))
        masks.append(mask)
    res = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if masks[i] & masks[j] == 0:
                res = max(res, len(words[i]) * len(words[j]))
    return res
```
### 6. 只出现一次的数字（⭐）来源：L75 / T150
**来源**：[L75](https://leetcode.cn/problems/single-number/)
**难度**：简单
**题目**：给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

**示例 1 ：**
```
**输入：**nums = [2,2,1]
**输出：**1
```
**示例 2 ：**
```
**输入：**nums = [4,1,2,1,2]
**输出：**4
```
**示例 3 ：**
```
**输入：**nums = [1]
**输出：**1
```
**提示：**

- `1 4`

- `-3 * 104 4`

- 除了某个元素只出现一次以外，其余每个元素均出现两次。
**思路**：经典异或解法。a ^ a = 0，a ^ 0 = a。将所有数字异或起来，成对出现的数字会抵消为 0，剩下的就是只出现一次的数字。
**代码**：
```python
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
```
## 📝 总结
- **异或**是位运算中最常用的技巧：自己异或自己得 0，异或 0 得自己
- `i & (i-1)` 去掉最低位 1，可用于计数位 1 或判断 2 的幂
- 位掩码（用 int 的二进制位表示集合）在状态压缩和字符串字母去重中很高效
- 模三状态机（one/two 变量）是解决"出现三次"问题的通用方法
- Python 中整数无限大，但移位操作仍是 O(1)，位运算比算术运算快


---

# Day 40: 数学综合

## 📖 知识点
**数学类问题常见技巧**：
1. **回文数**→ 反转一半数字比较
2.**快速幂** → 二分法，xⁿ = x^(n//2) * x^(n//2)，偶数直接乘，奇数多乘一个 x
3. **开平方**→ 牛顿迭代 / 二分法
4.**阶乘尾随零**→ 统计因子 5 的个数（因为因子 2 比 5 多）
5.**最大公约数**→ 辗转相除法 gcd(a,b) = gcd(b, a%b)
6.**共线问题**→ 斜率（分数化简）或叉积判断
7.**溢出处理** → Python 无需担心，但模拟其他语言要注意

**牛顿迭代法求平方根**：
```python
def sqrt_newton(x):
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r
```

## 🧩 刷题任务（6题）

### 1. 回文数（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/palindrome-number/)
**难度**：简单
**题目**：给你一个整数 `x` ，如果 `x` 是一个回文整数，返回 `true` ；否则，返回 `false` 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

- 例如，`121` 是回文，而 `123` 不是。

**示例 1：**
```
输入：x = 121
输出：true
```
**示例 2：**
```
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```
**示例 3：**
```
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
```
**提示：**

- `-231 31 - 1`

**进阶：**你能不将整数转为字符串来解决这个问题吗？
**思路**：负数和末尾为 0 的正整数不是回文数。反转一半数字：每次取 x 的最低位加到 rev 上，x 去掉最低位。当 x ≤ rev 时停止。最后判断 x == rev 或 x == rev // 10（奇数位的情况）。
**代码**：
```python
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10
```
### 2. 加一（⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/plus-one/)
**难度**：简单
**题目**：给定一个表示 **大整数** 的整数数组 `digits`，其中 `digits[i]` 是整数的第 `i` 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 `0`。

将大整数加 1，并返回结果的数字数组。

**示例 1：**
```
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。
```
**示例 2：**
```
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。
```
**示例 3：**
```
输入：digits = [9]
输出：[1,0]
解释：输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。
```
**提示：**

- `1
**思路**：从最低位开始加 1。如果没有进位就直接返回；有进位则继续处理下一位。如果所有位都进位了（如 999 → 1000），在最高位补 1。
**代码**：
```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```
### 3. 阶乘后的零（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/factorial-trailing-zeroes/)
**难度**：中等
**题目**：给定一个整数 `n` ，返回 `n!` 结果中尾随零的数量。

提示 `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`

**示例 1：**
```
输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0
```
**示例 2：**
```
输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0
```
**示例 3：**
```
输入：n = 0
输出：0
```
**提示：**

- `0 4`

**进阶：**你可以设计并实现对数时间复杂度的算法来解决此问题吗？
**思路**：阶乘中尾随零的个数 = min(因子 2 的个数, 因子 5 的个数)。2 的因子远多于 5，所以只需统计因子 5 的个数。每 5 个数贡献一个 5，每 25 个数多贡献一个 5，依此类推。
**代码**：
```python
def trailingZeroes(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
```
### 4. x 的平方根（⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/sqrtx/)
**难度**：简单
**题目**：给你一个非负整数 `x` ，计算并返回 `x` 的 **算术平方根**。

由于返回类型是整数，结果只保留**整数部分 **，小数部分将被 **舍去 。**

**注意：**不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。

**示例 1：**
```
输入：x = 4
输出：2
```
**示例 2：**
```
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
```
**提示：**

- `0 31 - 1`
**思路**：二分法。在 [0, x] 区间找最大的 mid 使得 mid * mid ≤ x。注意 mid * mid 可能溢出，用 mid ≤ x // mid 判断。
**代码**：
```python
def mySqrt(x):
    if x < 2:
        return x
    left, right = 0, x
    while left < right:
        mid = left + (right - left + 1) // 2
        if mid <= x // mid:
            left = mid
        else:
            right = mid - 1
    return left
```
### 5. Pow(x, n)（⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/powx-n/)
**难度**：中等
**题目**：实现 pow(*x*, *n*) ，即计算 `x` 的整数 `n` 次幂函数（即，`xn` ）。

**示例 1：**
```
输入：x = 2.00000, n = 10
输出：1024.00000
```
**示例 2：**
```
输入：x = 2.10000, n = 3
输出：9.26100
```
**示例 3：**
```
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
```
**提示：**

- `-100.0 31 31-1`

- `n` 是一个整数

- 要么 `x` 不为零，要么 `n > 0` 。

- `-104 n 4`
**思路**：快速幂。n 为负数时取倒数处理。二分法：2¹⁰ = (2⁵)² = (2² * 2² * 2)²。递归或迭代实现。
**代码**：
```python
def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    res = 1.0
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res
```
### 6. 直线上最多的点数（⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/max-points-on-a-line/)
**难度**：困难
**题目**：给你一个数组 `points` ，其中 `points[i] = [xi, yi]` 表示 **X-Y** 平面上的一个点。求最多有多少个点在同一条直线上。

**示例 1：**
```
*
输入：points = [[1,1],[2,2],[3,3]]
输出：3
```
**示例 2：**
```
*
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
```
**提示：**

- `1 4 i, yi 4`

- `points` 中的所有点 **互不相同**
**思路**：对每个点作为起点，统计其他点与它连线的斜率。斜率用最简分数 (dx/g, dy/g) 表示避免浮点误差。垂直线 (dx=0) 和水平线 (dy=0) 单独处理。同一位置的点算重复点。
**代码**：
```python
def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    res = 0
    for i in range(n):
        slope_map = {}
        duplicate = 1
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0 and dy == 0:
                duplicate += 1
                continue
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            key = (dx, dy)
            slope_map[key] = slope_map.get(key, 0) + 1
        res = max(res, duplicate + max(slope_map.values()) if slope_map else duplicate)
    return res
```
## 📝 总结
- **快速幂**（二进制分解）是面试高频考点，必须掌握迭代写法
- **开平方**用二分法最稳妥，注意用 `mid <= x // mid` 避免溢出
- **尾随零问题**核心是因子 5 的计数
- **共线问题**用最简分数表示斜率比浮点数更精确
- 数学题往往能在 O(1) 或 O(log n) 时间内解决，关键是找出数学规律


---

# Day 41: OD 100分实战

## 📖 知识点
**OD 100分题特点**：
- 题目偏模拟和实现，算法难度一般不高（⭐⭐为主）
- 注重输入解析，多数用 `input().split()` 读取
- 注意边界条件和数据范围
- 125% 通过率机制：样例过了不一定满分，要覆盖全情况
- 时间一般限制 1s，Python 注意效率
- 输入可能有空行，建议用 `sys.stdin.read()` 或 `try/except`

**常用输入模板**：
```python
import sys

# 按行读取
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # 处理

# 一次性读取所有
data = sys.stdin.read().split()
```

## 🧩 刷题任务（6题）

### 1. 螺旋数字矩阵（⭐⭐）来源：OD

**题目描述**：
给定一个正整数 n，按照顺时针螺旋顺序生成一个 n × n 的矩阵，矩阵元素为从 1 到 n² 的连续正整数。

**输入描述**：
一个正整数 n（1 ≤ n ≤ 20）

**输出描述**：
n 行，每行 n 个整数，每个整数占 3 位宽度右对齐。

**示例输入**：
```
```
3
```
```
**示例输出**：
```
```
  1  2  3
  8  9  4
  7  6  5
```
```
**思路**：经典螺旋矩阵模拟。定义四个方向（右、下、左、上），用 visited 数组或边界变量控制转向。每次填充后检查下一个位置是否越界或已访问。

**代码**：
```python
def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    # 方向: 右, 下, 左, 上
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = 0, 0
    di = 0  # 当前方向索引
    for num in range(1, n * n + 1):
        matrix[r][c] = num
        # 尝试下一个位置
        nr, nc = r + dirs[di][0], c + dirs[di][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or matrix[nr][nc] != 0:
            di = (di + 1) % 4
            nr, nc = r + dirs[di][0], c + dirs[di][1]
        r, c = nr, nc
    for row in matrix:
        print(' '.join(f'{x:3d}' for x in row))

if __name__ == '__main__':
    n = int(input().strip())
    spiral_matrix(n)
```

---

### 2. 最大矩阵和（⭐⭐）来源：OD

**题目描述**：
给定一个 n × m 的整数矩阵（包含正数和负数），找出一个子矩阵，使得子矩阵内所有元素的和最大，输出这个最大和。

**输入描述**：
第一行两个整数 n 和 m（1 ≤ n, m ≤ 200）
接下来 n 行，每行 m 个整数，表示矩阵元素，值范围 [-1000, 1000]

**输出描述**：
一个整数，表示最大子矩阵和。

**示例输入**：
```
```
3 3
-1 -1 -1
-1  2 -1
-1 -1 -1
```
```
**示例输出**：
```
```
2
```
```
**思路**：把二维问题转为一维最大子数组和（Kadane算法）。枚举起始行和结束行，将行之间的列压缩成一维数组，对该数组求最大子段和，取全局最大值。

**代码**：
```python
def max_subarray_sum(arr):
    max_ending = max_sofar = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_sofar = max(max_sofar, max_ending)
    return max_sofar

def max_matrix_sum(matrix, n, m):
    max_sum = float('-inf')
    for top in range(n):
        col_sum = [0] * m
        for bottom in range(top, n):
            for j in range(m):
                col_sum[j] += matrix[bottom][j]
            max_sum = max(max_sum, max_subarray_sum(col_sum))
    return max_sum

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    matrix = []
    idx = 2
    for _ in range(n):
        row = list(map(int, data[idx:idx + m]))
        matrix.append(row)
        idx += m
    print(max_matrix_sum(matrix, n, m))
```

---

### 3. 数组连续和（⭐）来源：OD

**题目描述**：
给定一个整数数组（可能有负数）和一个目标值 target，统计有多少个连续子数组的和等于 target。

**输入描述**：
第一行两个整数 n 和 target，第二行 n 个整数。

**输出描述**：
一个整数，表示和为 target 的连续子数组个数。

**示例输入**：
```
```
5 0
1 -1 1 -1 1
```
```
**示例输出**：
```
```
3
```
**解释**：[1, -1]（索引0-1），[-1, 1]（索引1-2），[1, -1]（索引2-3），共 3 个。
```
**思路**：前缀和 + 哈希表。用字典记录每个前缀和出现的次数。当前前缀和为 sum，需要找前缀和为 sum - target 的个数。初始化前缀和 0 出现 1 次。

**代码**：
```python
def subarray_sum(nums, target):
    prefix = {0: 1}
    cur_sum = 0
    count = 0
    for num in nums:
        cur_sum += num
        count += prefix.get(cur_sum - target, 0)
        prefix[cur_sum] = prefix.get(cur_sum, 0) + 1
    return count

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().split()
    n, target = int(data[0]), int(data[1])
    nums = list(map(int, data[2:2 + n]))
    print(subarray_sum(nums, target))
```

---

### 4. 等和子数组最小和（⭐⭐⭐）来源：OD

**题目描述**：
给定一个正整数数组，将其分割成 k 个非空连续子数组，使得每个子数组的和相等。求这个相等的和的最小可能值。如果无法分割，输出 -1。

**输入描述**：
第一行两个整数 n（数组长度）和 k（分割份数）。第二行 n 个正整数。

**输出描述**：
一个整数，表示等和子数组的最小和，如果无法分割则输出 -1。

**示例输入**：
```
```
5 3
1 3 2 4 2
```
```
**示例输出**：
```
```
4
```
**解释**：可以分割为 [1,3]（和4）、[2,2]（和4）、[4]（和4），每份和均为 4。
```
**思路**：先求总和 total。如果 total % k != 0，返回 -1。目标子数组和 = total // k。用贪心法从前向后累加，每到目标值就切一段。如果能正好切出 k 段，返回目标值；否则说明需要重新分配或不可能。

注意：题目要求连续子数组且等和，所以贪心切割即可——从前往后，累加恰好等于目标值时切一刀。

**代码**：
```python
def can_partition(nums, k, target):
    cur = 0
    cnt = 0
    for num in nums:
        cur += num
        if cur == target:
            cur = 0
            cnt += 1
        elif cur > target:
            return False
    return cnt == k

def min_equal_sum(nums, k):
    total = sum(nums)
    if total % k != 0:
        return -1
    target = total // k
    # 检查是否每个数都不大于 target
    if any(x > target for x in nums):
        return -1
    if can_partition(nums, k, target):
        return target
    # 如果贪心切分不成功，可能需要更大的 target
    # 尝试从 target 往上找
    for t in range(target + 1, total + 1):
        if total % t == 0 and total // t == k:
            if can_partition(nums, k, t):
                return t
    return -1

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    nums = list(map(int, data[2:2 + n]))
    print(min_equal_sum(nums, k))
```

---

### 5. 字符串分割（⭐⭐）来源：OD-B卷

**题目描述**：
给定一个非空字符串 S，和一个包含不同单词的字典 wordDict（列表），在字符串中增加空格来构建一个句子，使得句子中所有单词都在字典中。返回所有可能的句子。

**输入描述**：
第一行一个字符串 S（长度 ≤ 20）
第二行一个整数 m（字典大小）
接下来 m 行，每行一个单词

**输出描述**：
按字典序升序输出所有可能的句子，每行一个。如果不存在，输出 "null"。

**示例输入**：
```
```
catsanddog
5
cat
cats
and
sand
dog
```
```
**示例输出**：
```
```
cat sand dog
cats and dog
```
```
**思路**：DFS + 回溯/记忆化搜索。从索引 0 开始，尝试匹配字典中的每个单词，匹配成功后递归处理剩余部分。用 memo 缓存避免重复计算。最后排序输出。

**代码**：
```python
def word_break(s, word_dict):
    word_set = set(word_dict)
    memo = {}

    def dfs(start):
        if start in memo:
            return memo[start]
        res = []
        if start == len(s):
            res.append("")
            return res
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                sub_sentences = dfs(end)
                for sub in sub_sentences:
                    if sub:
                        res.append(word + " " + sub)
                    else:
                        res.append(word)
        memo[start] = res
        return res

    result = dfs(0)
    if not result:
        print("null")
    else:
        result.sort()
        for sentence in result:
            print(sentence)

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    m = int(data[1].strip())
    word_dict = [data[i + 2].strip() for i in range(m)]
    word_break(s, word_dict)
```

---

### 6. 回文字符串（⭐⭐）来源：OD-A卷

**题目描述**：
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回最短的这种回文串。

**输入描述**：
一行字符串 s，仅包含小写字母，长度 ≤ 10000

**输出描述**：
一行字符串，为最短的回文串。

**示例输入**：
```
```
aacecaaa
```
```
**示例输出**：
```
```
aaacecaaa
```
**解释**：在开头添加 "a" 得到 "aaacecaaa"。
```
**思路**：本质上是找字符串**从开头开始的最长回文子串**。找到这个回文前缀后，将剩余部分反转拼接到前面即可。可以用 Manacher 算法（O(n)）或中心扩展法（O(n²)）。对于 OD 100分题，中心扩展法足够。

**代码**：
```python
def shortest_palindrome(s):
    n = len(s)
    # 找从开头开始的最长回文子串
    longest = 0
    for i in range(n):
        # 奇数回文
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            if left == 0:
                longest = max(longest, right - left + 1)
            left -= 1
            right += 1
        # 偶数回文
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if left == 0:
                longest = max(longest, right - left + 1)
            left -= 1
            right += 1
    suffix = s[longest:]
    return suffix[::-1] + s

if __name__ == '__main__':
    s = input().strip()
    print(shortest_palindrome(s))
```

## 📝 总结
- **OD 100分题**重在实现能力，算法多为中等难度
- 常用的技巧：前缀和、方向数组模拟、贪心切割、DFS回溯
- 注意 **125% 通过率**：不仅要过样例，还要考虑边界（空数组、大数、重复等）
- 输入解析多用 `sys.stdin.read().split()` 一次性读取
- 多练习模拟题（螺旋矩阵、方向遍历）和经典套路（前缀和、Kadane算法）


---

# Day 42: 周复习

## 📖 本周知识点总览

| 主题 | 核心算法 | 关键模板 | 题量 |
|------|----------|----------|------|
| 二分搜索 | 标准二分、边界查找、旋转数组 | lower_bound / upper_bound | 6 |
| 二分+排序 | 按值二分、链表归并、计数排序 | 答案二分模板 | 6 |
| 堆 | Top K、两堆中位数、贪心+堆 | heapq 操作 | 6 |
| 位运算 | 异或消除、位掩码、状态机 | i&(i-1), x^x=0 | 6 |
| 数学综合 | 快速幂、开平方、回文、共线 | 快速幂迭代 | 6 |
| OD 100分 | 模拟、前缀和、DFS、Manacher | 螺旋矩阵、Kadane | 6 |

## 🧩 刷题任务（混合复习 — 6题）

### 1. 二分搜索：搜索旋转数组 II（⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/)
**难度**：中等
**题目**：已知存在一个按非降序排列的整数数组 `nums` ，数组中的值不必互不相同。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0
- `1 4 4`

- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转

- `-104 4`

**进阶：**

- 此题与 搜索旋转排序数组 相似，但本题中的 `nums`  可能包含 **重复** 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
**思路**：相比 Day 36 的旋转数组搜索，有重复元素时可能出现 `nums[left] == nums[mid] == nums[right]` 无法判断有序段的情况。此时只能 left++、right-- 缩小区间。
**代码**：
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        # 无法判断有序段，缩小范围
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False
```
### 2. 堆：前 K 个高频元素（⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/top-k-frequent-elements/)
**难度**：中等
**题目**：给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

**示例 1：**
```
**输入：**nums = [1,1,1,2,2,3], k = 2
**输出：**[1,2]
```
**示例 2：**
```
**输入：**nums = [1], k = 1
**输出：**[1]
```
**示例 3：**
```
**输入：**nums = [1,2,1,2,1,2,3,1,3,2], k = 2
**输出：**[1,2]
```
**提示：**

- `1 5`

- `-104 4`

- `k` 的取值范围是 `[1, 数组中不相同的元素的个数]`

- 题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的

**进阶：**你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n`  *是数组大小。
**思路**：先用 Counter 统计频率，再用大小为 k 的最小堆。堆中存 (频率, 元素)，按频率排序。
**代码**：
```python
def topKFrequent(nums, k):
    from collections import Counter
    freq = Counter(nums)
    heap = []
    for num, cnt in freq.items():
        heapq.heappush(heap, (cnt, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]
```
### 3. 位运算：子集（⭐⭐）来源：T150 / O
**来源**：[T150](https://leetcode.cn/problems/subsets/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，数组中的元素 **互不相同**。返回该数组所有可能的子集（幂集）。

解集**不能**包含重复的子集。你可以按**任意顺序** 返回解集。

**示例 1：**
```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```
**示例 2：**
```
输入：nums = [0]
输出：[[],[0]]
```
**提示：**

- `1
**思路**：用位掩码枚举。从 0 到 2ⁿ - 1，每个数的二进制位表示对应元素是否选取。
**代码**：
```python
def subsets(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask >> i & 1:
                subset.append(nums[i])
        res.append(subset)
    return res
```
### 4. 数学：快乐数（⭐）来源：L75 / T150
**来源**：[L75](https://leetcode.cn/problems/happy-number/)
**难度**：简单
**题目**：编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」**定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。

- 然后重复这个过程直到这个数变为 1，也可能是**无限循环**但始终变不到 1。

- 如果这个过程**结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**
```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
**示例 2：**
```
输入：n = 2
输出：false
```
**提示：**

- `1 31 - 1`
**思路**：快慢指针检测循环。或者用哈希集合记录已经出现的数字。平方和运算：`sum(int(d)**2 for d in str(n))`。
**代码**：
```python
def isHappy(n):
    def get_next(x):
        total = 0
        while x:
            total += (x % 10) ** 2
            x //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
```
### 4. 数学：快乐数（⭐）来源：L75 / T150
**来源**：[LeetCode](https://leetcode.cn/problems/happy-number/)
**难度**：简单
**题目**：编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」**定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。

- 然后重复这个过程直到这个数变为 1，也可能是**无限循环**但始终变不到 1。

- 如果这个过程**结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**
```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
**示例 2：**
```
输入：n = 2
输出：false
```
**提示：**

- `1 31 - 1`

**题目描述**：
有 N 个任务，每个任务有一个执行时间 t[i] 和一个优先级 p[i]。系统采用时间片轮转调度，时间片大小为 1。每次选择优先级最高的任务执行一个时间片，同优先级按序号从小到大。执行完一个时间片后，任务的优先级减 1。如果任务执行完毕（剩余时间为 0），则不再参与调度。输出所有任务执行完成的顺序（任务序号）。

**输入描述**：
第一行 N（任务数，≤ 1000）
接下来 N 行，每行两个整数 t[i] 和 p[i]（≤ 1000）

**输出描述**：
一行，N 个整数，表示调度完成的任务序号（从 1 开始）。

**示例输入**：
```
```
3
2 3
1 2
3 1
```
```
**示例输出**：
```
```
2 1 3
```
```
**思路**：用最大堆维护 (优先级, -序号, 剩余时间, 序号)。每次弹出优先级最高的任务执行一个时间片，更新优先级和剩余时间，如果还有剩余则重新入堆。

**代码**：
```python
def schedule_tasks(tasks):
    import heapq
    n = len(tasks)
    heap = []
    for i, (t, p) in enumerate(tasks):
        # 最大堆用负数优先级，序号小优先用 -i（序号越小越优先）
        heapq.heappush(heap, (-p, i, t))
    res = []
    while heap:
        neg_p, idx, remain = heapq.heappop(heap)
        p = -neg_p
        remain -= 1
        if remain == 0:
            res.append(idx + 1)  # 1-indexed
        else:
            # 优先级减1
            heapq.heappush(heap, (-(p - 1), idx, remain))
    return res

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    tasks = []
    idx = 1
    for _ in range(n):
        t = int(data[idx])
        p = int(data[idx + 1])
        tasks.append((t, p))
        idx += 2
    res = schedule_tasks(tasks)
    print(' '.join(map(str, res)))
```

### 6. 综合：寻找重复数（⭐⭐⭐⭐）来源：T150
**来源**：[T150](https://leetcode.cn/problems/find-the-duplicate-number/)
**难度**：中等
**题目**：给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。

假设 `nums` 只有 **一个重复的整数**，返回**这个重复的数**。

你设计的解决方案必须**不修改** 数组 `nums` 且只用常量级 `O(1)` 的额外空间。

**示例 1：**
```
输入：nums = [1,3,4,2,2]
输出：2
```
**示例 2：**
```
输入：nums = [3,1,3,4,2]
输出：3
```
**示例 3 :**
```
输入：nums = [3,3,3,3,3]
输出：3
```
**提示：**

- `1 5`

- `nums.length == n + 1`

- `1

**进阶：**

- 如何证明 `nums` 中至少存在一个重复的数字?

- 你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？
**思路**：把数组看成链表，值映射为索引。因为有重复数字，所以有环，用 Floyd 判环法（快慢指针）找环入口。
**代码**：
```python
def findDuplicate(nums):
    # 快慢指针找相遇点
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # 找环入口
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```
## 🧪 小测验（10题）

1. 二分查找中，`while left < right` 和 `while left <= right` 有什么区别？
2. 旋转数组搜索时，如何判断 mid 在左段还是右段？
3. 堆排序的时间复杂度和空间复杂度分别是多少？
4. 什么情况下用最大堆模拟最小堆？Python 里如何实现？
5. 异或运算有哪些性质？举出两个应用场景。
6. `x & (x - 1)` 的作用是什么？`x & -x` 呢？
7. 求 x 的 n 次幂，时间复杂度能做到多少？如何实现？
8. 阶乘尾随零的个数如何计算？为什么只数因子 5 就够了？
9. 快慢指针可以解决哪些问题？列举至少 3 个。
10. 如何判断两个线段（或三个点）是否共线？

**答案**：
1. `left < right` 退出时 left==right，用于找边界；`left <= right` 退出时 left>right，用于精确查找
2. 比较 nums[mid] 和 nums[left]：若 nums[left] ≤ nums[mid] 则在左段，否则在右段
3. 时间 O(n log n)，空间 O(1)（原地建堆）或 O(n)（辅助数组）
4. 需要找第 K 个最小时用最大堆（因为堆顶是门槛）。Python 中存 `-val` 来模拟
5. a^a=0, a^0=a，a^b^a=b（交换律）。应用：找出现奇数次的数、简单加密
6. `x & (x-1)` 去掉最低位 1；`x & -x` 取最低位 1 的值
7. O(log n)，用快速幂（二进制分解）
8. 每 5 个数有一个因子 5，每 25 个数多一个… 因子 2 远多于 5，所以只数 5
9. 判环（链表环）、找中点、找重复数（Floyd）、快乐数检测
10. 计算斜率（最简分数）或叉积：(x2-x1)*(y3-y1) == (x3-x1)*(y2-y1)

## 📝 总结
- 本周覆盖了**二分搜索**、**堆**、**位运算**、**数学**和**OD 100分实战**五大模块
- 核心模板要背熟：lower_bound / upper_bound、快速幂、堆操作、位运算技巧
- OD 100分题注重**模拟能力**和**输入输出处理**，多练自然有感觉
- **快慢指针**和**Floyd 判环**是跨主题的通用技巧
- 每天 6 题，持之以恒，下周进入 Week 7！


---


---
# 第7周·OD200题
> 共计 7 天

# D43 — DP 一维入门 (6题)

---

## 1. Climbing Stairs (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/climbing-stairs/)
**难度**：简单
**题目**：假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**示例 1：**
```
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```
**示例 2：**
```
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```
**提示：**

- `1

**状态定义**：`dp[i]` = 爬到第 `i` 阶的方法数
**转移**：`dp[i] = dp[i-1] + dp[i-2]`
**初始**：`dp[1]=1, dp[2]=2`
**优化**：空间压缩到 O(1)

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# 时间 O(n), 空间 O(1)
```

---

## 2. N-th Tribonacci Number (L75)
**来源**：[LeetCode](https://leetcode.cn/problems/n-th-tribonacci-number/)
**难度**：简单
**题目**：泰波那契序列 Tn 定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 `n`，请返回第 n 个泰波那契数 Tn 的值。

**示例 1：**
```
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```
**示例 2：**
```
输入：n = 25
输出：1389537
```
**提示：**

- `0

**状态定义**：`dp[i]` = 第 i 个 Tribonacci 数
**转移**：`dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`
**初始**：`dp[0]=0, dp[1]=1, dp[2]=1`

```python
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c

# 时间 O(n), 空间 O(1)
```

---

## 3. Min Cost Climbing Stairs (L75/O)
**来源**：[LeetCode](https://leetcode.cn/problems/min-cost-climbing-stairs/)
**难度**：简单
**题目**：给你一个整数数组 `cost` ，其中 `cost[i]` 是从楼梯第 `i` 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 `0` 或下标为 `1` 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

**示例 1：**
```
输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。
```
**示例 2：**
```
输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
```
**提示：**

- `2

**状态定义**：`dp[i]` = 到达第 i 阶的最小花费
**转移**：`dp[i] = cost[i] + min(dp[i-1], dp[i-2])`
**终点**：`min(dp[-1], dp[-2])`，因为可以跨过顶部

```python
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    if n == 2:
        return min(cost)
    a, b = cost[0], cost[1]
    for i in range(2, n):
        a, b = b, cost[i] + min(a, b)
    return min(a, b)

# 时间 O(n), 空间 O(1)
```

---

## 4. House Robber (L75/T150/O)
**题目**：你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你**不触动警报装置的情况下**，一夜之内能够偷窃到的最高金额。

**示例 1：**
```
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```
**示例 2：**
```
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```
**提示：**

- `1

**状态定义**：`dp[i]` = 前 i 间房能偷到的最大金额
**转移**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
**优化**：滚动变量

```python
def rob(nums: list[int]) -> int:
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr

# 时间 O(n), 空间 O(1)
```

---

## 5. House Robber II (O)
**来源**：[O](https://leetcode.cn/problems/house-robber-ii/)
**难度**：中等
**题目**：你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 **围成一圈** ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你**在不触动警报装置的情况下** ，今晚能够偷窃到的最高金额。

**示例 1：**
```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```
**示例 2：**
```
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
偷窃到的最高金额 = 1 + 3 = 4 。
```
**示例 3：**
```
输入：nums = [1,2,3]
输出：3
```
**提示：**

- `1
**思路**：环形 → 拆成两个线性的 House Robber - 情况 A：不抢第 0 间 → `rob(nums[1:])` - 情况 B：不抢最后 1 间 → `rob(nums[:-1])` 取最大值
**代码**：
```python
def rob_linear(nums: list[int]) -> int:
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr

def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

# 时间 O(n), 空间 O(1)
```
## 6. Domino and Tromino (L75)
**来源**：[LeetCode](https://leetcode.cn/problems/domino-and-tromino-tiling/)
**难度**：中等
**题目**：有两种形状的瓷砖：一种是 `2 x 1` 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

*

给定整数 n ，返回可以平铺 `2 x n` 的面板的方法的数量。**返回对**`109 + 7`**取模 **的值。

平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。

**示例 1:**
```
*
输入: n = 3
输出: 5
解释: 五种不同的方法如上所示。
```
**示例 2:**
```
输入: n = 1
输出: 1
```
**提示：**

- `1

**状态定义**：
- `dp[i][0]` = 完全铺满 2×i 列的方法数
- `dp[i][1]` = 铺满 2×i 列，但右上角缺一格的方法数
**转移**：
```
dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]
dp[i][1] = dp[i-2][0] + dp[i-1][1]
```
**初始**：`dp[1][0]=1, dp[0][0]=1, dp[1][1]=0, dp[2][1]=1`

```python
def numTilings(n: int) -> int:
    MOD = 10**9 + 7
    if n == 1:
        return 1
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    dp0[0] = dp0[1] = 1
    dp1[1] = 0
    dp1[2] = 1
    for i in range(2, n + 1):
        dp0[i] = (dp0[i - 1] + dp0[i - 2] + 2 * dp1[i - 1]) % MOD
        dp1[i] = (dp0[i - 2] + dp1[i - 1]) % MOD
    return dp0[n]

# 时间 O(n), 空间 O(n) 可压缩到 O(1)
```


---

# D44 — DP 一维进阶 (6题)

---

## 1. Word Break (T150)

**思路**：`dp[i]` = s[:i] 能否被拆分成字典中的词
**转移**：`dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`
**剪枝**：只检查长度不超过最长单词的 j

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    max_len = max(len(w) for w in wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]

# 时间 O(n * max_len), 空间 O(n + wordDict)
```

---

## 2. Coin Change (T150/O)

**状态定义**：`dp[i]` = 凑成金额 i 的最少硬币数
**转移**：`dp[i] = min(dp[i - coin] + 1 for coin in coins if i >= coin)`
**初始**：`dp[0] = 0`，其余为 `inf`

```python
def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# 时间 O(amount * len(coins)), 空间 O(amount)
```

---

## 3. Longest Increasing Subsequence (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/longest-increasing-subsequence/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

**子序列 **是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

**示例 1：**
```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```
**示例 2：**
```
输入：nums = [0,1,0,3,2,3]
输出：4
```
**示例 3：**
```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```
**提示：**

- `1 4 4`

**进阶：**

- 你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

**状态定义**：`dp[i]` = 以 nums[i] 结尾的 LIS 长度
**转移**：`dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])`
**优化**：`patience sorting` → O(n log n)

```python
def lengthOfLIS(nums: list[int]) -> int:
    tails = []
    for x in nums:
        idx = __import__('bisect').bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)

# 时间 O(n log n), 空间 O(n)
```

---

## 4. Partition Equal Subset Sum (O)
**来源**：[O](https://leetcode.cn/problems/partition-equal-subset-sum/)
**难度**：中等
**题目**：给你一个 **只包含正整数 **的 **非空 **数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

**示例 1：**
```
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
```
**示例 2：**
```
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
```
**提示：**

- `1
**思路**：转化 → 能否选出若干元素凑成总和的一半（0-1 背包）
**代码**：
```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total & 1:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
    return dp[target]

# 时间 O(n * target), 空间 O(target)
```
## 5. Target Sum (O)
**来源**：[O](https://leetcode.cn/problems/target-sum/)
**难度**：中等
**题目**：给你一个非负整数数组 `nums` 和一个整数 `target` 。

向数组中的每个整数前添加 `'+'` 或 `'-'` ，然后串联起所有整数，可以构造一个 **表达式**：

- 例如，`nums = [2, 1]` ，可以在 `2` 之前添加 `'+'` ，在 `1` 之前添加 `'-'` ，然后串联起来得到表达式 `"+2-1"` 。

返回可以通过上述方法构造的、运算结果等于 `target` 的不同**表达式** 的数目。

**示例 1：**
```
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```
**示例 2：**
```
输入：nums = [1], target = 1
输出：1
```
**提示：**

- `1
**思路**：转化成 0-1 背包 `sum(正数) - sum(负数) = target` `sum(正数) = (total + target) // 2` 找能凑成 `(total + target) // 2` 的方法数
**代码**：
```python
def findTargetSumWays(nums: list[int], target: int) -> int:
    total = sum(nums)
    if total < abs(target) or (total + target) & 1:
        return 0
    s = (total + target) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    for num in nums:
        for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[s]

# 时间 O(n * s), 空间 O(s)
```
## 6. Combination Sum IV (O)
**来源**：[O](https://leetcode.cn/problems/combination-sum/)
**难度**：中等
**题目**：给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有* ***不同组合**，并以列表形式返回。你可以按**任意顺序**返回这些组合。

`candidates` 中的**同一个**数字可以**无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

**示例 1：**
```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```
**示例 2：**
```
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```
**示例 3：**
```
输入: candidates = [2], target = 1
输出: []
```
**提示：**

- `1
**思路**：完全背包求排列数
**代码**：
```python
def combinationSum4(nums: list[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]

# 时间 O(target * len(nums)), 空间 O(target)
```

---

# D45 — DP 二维 (6题)

---

## 1. Unique Paths (L75/T150/O)
**来源**：[LeetCode](https://leetcode.cn/problems/unique-paths/)
**难度**：中等
**题目**：一个机器人位于一个 `m x n`* *网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

**示例 1：**
```
*
输入：m = 3, n = 7
输出：28
```
**示例 2：**
```
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
```
**示例 3：**
```
输入：m = 7, n = 3
输出：28
```
**示例 4：**
```
输入：m = 3, n = 3
输出：6
```
**提示：**

- `1 9`

**状态定义**：`dp[i][j]` = 到达 (i,j) 的路径数
**转移**：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`
**优化**：一维滚动数组

```python
def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]

# 时间 O(m*n), 空间 O(n)
```

---

## 2. Unique Paths II (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/unique-paths-ii/)
**难度**：中等
**题目**：给定一个 `m x n` 的整数数组 `grid`。一个机器人初始位于 **左上角**（即 `grid[0][0]`）。机器人尝试移动到 **右下角**（即 `grid[m - 1][n - 1]`）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。机器人的移动路径中不能包含 **任何** 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 `2 * 109`。

**示例 1：**
```
*
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
```
**示例 2：**
```
*
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
```
**提示：**

- `m == obstacleGrid.length`

- `n == obstacleGrid[i].length`

- `1

**思路**：有障碍物时 `dp[i][j] = 0`
**转移**：`if obstacleGrid[i][j] == 0: dp[j] += dp[j-1]`

```python
def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
    return dp[-1]

# 时间 O(m*n), 空间 O(n)
```

---

## 3. Minimum Path Sum (T150/O)
**来源**：[](https://leetcode.cn/problems/path-sum/)
**难度**：简单
**题目**：给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

**示例 1：**
```
*
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```
**示例 2：**
```
*
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```
**示例 3：**
```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```
**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内

- `-1000
**思路**：**状态定义**：`dp[i][j]` = 到 (i,j) 的最小路径和
**转移**：`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`
**代码**：
```python
def minPathSum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]

# 时间 O(m*n), 空间 O(1) 原地修改
```
## 4. Triangle (T150/O)

**思路**：自底向上 DP，`dp[j] = triangle[i][j] + min(dp[j], dp[j+1])`

```python
def minimumTotal(triangle: list[list[int]]) -> int:
    dp = triangle[-1][:]  # 最后一行
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]

# 时间 O(n^2), 空间 O(n)
```

---

## 5. Longest Common Subsequence (L75/O)

**状态定义**：`dp[i][j]` = text1[:i] 和 text2[:j] 的 LCS 长度
**转移**：
```
if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# 时间 O(m*n), 空间 O(m*n) 可优化到 O(n)
```

---

## 6. Interleaving String (T150/O)

**状态定义**：`dp[i][j]` = s1[:i] 和 s2[:j] 能否交错成 s3[:i+j]
**转移**：
```
dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or
           (dp[i][j-1] and s2[j-1]==s3[i+j-1])
```

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n, k = len(s1), len(s2), len(s3)
    if m + n != k:
        return False
    dp = [False] * (n + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            elif j == 0:
                dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
            else:
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
    return dp[n]

# 时间 O(m*n), 空间 O(n)
```


---

# D46 — DP 高级 (6题)

---

## 1. Edit Distance (L75/T150)
**来源**：[](https://leetcode.cn/problems/edit-distance/)
**难度**：中等
**题目**：给你两个单词 `word1` 和 `word2`， *请返回将 `word1` 转换成 `word2` 所使用的最少操作数*  。

你可以对一个单词进行如下三种操作：

- 插入一个字符

- 删除一个字符

- 替换一个字符

**示例 1：**
```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```
**示例 2：**
```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```
**提示：**

- `0
**思路**：**状态定义**：`dp[i][j]` = word1[:i] → word2[:j] 的最小编辑距离
**转移**：
**代码**：
```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

# 时间 O(m*n), 空间 O(m*n) 可压缩到 O(n)
```
## 2. Best Time to Buy and Sell Stock with Transaction Fee (L75)
**来源**：[LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
**难度**：简单
**题目**：给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天**买入这只股票，并选择在**未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```
**示例 2：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```
**提示：**

- `1 5`

- `0 4`

**状态定义**：
- `hold` = 手上有股票时的最大利润
- `cash` = 手上无股票时的最大利润
**转移**：
- `cash = max(cash, hold + price - fee)`
- `hold = max(hold, cash - price)`

```python
def maxProfit(prices: list[int], fee: int) -> int:
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash

# 时间 O(n), 空间 O(1)
```

---

## 3. Best Time to Buy and Sell Stock III (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
**难度**：简单
**题目**：给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天**买入这只股票，并选择在**未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```
**示例 2：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```
**提示：**

- `1 5`

- `0 4`

**思路**：限 2 笔交易，四种状态
- `buy1, sell1, buy2, sell2`

```python
def maxProfit(prices: list[int]) -> int:
    buy1 = buy2 = float('inf')
    sell1 = sell2 = 0
    for p in prices:
        buy1 = min(buy1, p)
        sell1 = max(sell1, p - buy1)
        buy2 = min(buy2, p - sell1)  # 第二次买入成本 = 价格 - 第一次利润
        sell2 = max(sell2, p - buy2)
    return sell2

# 时间 O(n), 空间 O(1)
```

---

## 4. Best Time to Buy and Sell Stock IV (T150)
**来源**：[LeetCode](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
**难度**：简单
**题目**：给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天**买入这只股票，并选择在**未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```
**示例 2：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```
**提示：**

- `1 5`

- `0 4`

**思路**：推广到 k 次交易，当 k ≥ n/2 时退化为无限次
`buy[j]`, `sell[j]` 表示第 j 次交易后的状态

```python
def maxProfit(k: int, prices: list[int]) -> int:
    n = len(prices)
    if n < 2 or k == 0:
        return 0
    if k >= n // 2:  # 无限次交易
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
    buy = [float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    for p in prices:
        for j in range(1, k + 1):
            buy[j] = min(buy[j], p - sell[j - 1])
            sell[j] = max(sell[j], p - buy[j])
    return sell[k]

# 时间 O(n*k), 空间 O(k)
```

---

## 5. Maximal Square (T150)

**状态定义**：`dp[i][j]` = 以 (i,j) 为右下角的最大全 1 正方形边长
**转移**：
```
if matrix[i][j] == '1':
    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

```python
def maximalSquare(matrix: list[list[str]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                max_side = max(max_side, dp[i][j])
    return max_side * max_side

# 时间 O(m*n), 空间 O(m*n) 可压缩到 O(n)
```

---

## 6. Longest Palindromic Substring (T150)
**来源**：[T150](https://leetcode.cn/problems/longest-palindromic-substring/)
**难度**：中等
**题目**：给你一个字符串 `s`，找到 `s` 中最长的 回文 子串。

**示例 1：**
```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```
**示例 2：**
```
输入：s = "cbbd"
输出："bb"
```
**提示：**

- `1
**思路**：中心扩展法（比 DP 更优） DP 版：`dp[i][j]` = s[i:j+1] 是否回文
**代码**：
```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    start, max_len = 0, 1
    for i in range(n):
        # 奇数扩展
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
        # 偶数扩展
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
    return s[start:start + max_len]

# 时间 O(n^2), 空间 O(1)
```

---

# D47 — DP 字符串 (6题)

---

## 1. Palindromic Substrings (O)
**来源**：[O](https://leetcode.cn/problems/palindromic-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

**回文字符串** 是正着读和倒过来读一样的字符串。

**子字符串** 是字符串中的由连续字符组成的一个序列。

**示例 1：**
```
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
```
**示例 2：**
```
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```
**提示：**

- `1
**思路**：中心扩展法，统计所有回文子串 每个字符或每对相邻字符作为中心向两边扩展
**代码**：
```python
def countSubstrings(s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        # 奇数长度回文
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        # 偶数长度回文
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans

# 时间 O(n^2), 空间 O(1)
```
## 2. Longest Fibonacci Subsequence (O)
**来源**：[O](https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/)
**难度**：中等
**题目**：如果序列 `x1, x2, ..., xn` 满足下列条件，就说它是 *斐波那契式 *的：

- `n >= 3`

- 对于所有 `i + 2 i + xi+1 == xi+2`

给定一个 **严格递增 **的正整数数组形成序列 `arr` ，找到 `arr` 中最长的斐波那契式的子序列的长度。如果不存在，返回  `0` 。

**子序列** 是通过从另一个序列 `arr` 中删除任意数量的元素（包括删除 0 个元素）得到的，同时不改变剩余元素顺序。例如，`[3, 5, 8]` 是 `[3, 4, 5, 6, 7, 8]` 的子序列。

**示例 1：**
```
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
```
**示例 2：**
```
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
```
**提示：**

- `3 9`
**思路**：`dp[j][k]` = 以 arr[j], arr[k] 结尾的最长斐波那契子序列长度 `dp[j][k] = max(dp[j][k], dp[i][j] + 1)`
**代码**：
```python
def lenLongestFibSubseq(arr: list[int]) -> int:
    n = len(arr)
    idx = {x: i for i, x in enumerate(arr)}
    dp = [[2] * n for _ in range(n)]
    ans = 0
    for k in range(n):
        for j in range(k):
            target = arr[k] - arr[j]
            if target in idx and idx[target] < j:
                i = idx[target]
                dp[j][k] = dp[i][j] + 1
                ans = max(ans, dp[j][k])
    return ans if ans >= 3 else 0

# 时间 O(n^2), 空间 O(n^2)
```
## 3. Palindrome Partitioning II (O)
**来源**：[O](https://leetcode.cn/problems/palindrome-partitioning-ii/)
**难度**：困难
**题目**：给你一个字符串 `s`，请你将 `s` 分割成一些子串，使每个子串都是回文串。

返回符合要求的 **最少分割次数** 。

**示例 1：**
```
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
```
**示例 2：**
```
输入：s = "a"
输出：0
```
**示例 3：**
```
输入：s = "ab"
输出：1
```
**提示：**

- `1
**思路**：两次 DP 1. `isPal[i][j]` = s[i:j+1] 是否回文 2. `dp[i]` = s[:i+1] 的最少分割次数
**代码**：
```python
def minCut(s: str) -> int:
    n = len(s)
    isPal = [[False] * n for _ in range(n)]
    dp = [n] * n
    for i in range(n):
        for j in range(i + 1):
            if s[i] == s[j] and (i - j <= 2 or isPal[j + 1][i - 1]):
                isPal[j][i] = True
    for i in range(n):
        if isPal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if isPal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

# 时间 O(n^2), 空间 O(n^2)
```
## 4. Paint House (O)
**来源**：[O](https://leetcode.cn/problems/paint-house/)
**难度**：中等
**思路**：**状态定义**：`dp[i][j]` = 第 i 间房刷颜色 j 的最小花费（j=0,1,2）
**转移**：当前颜色不能和前一间相同
**代码**：
```python
def minCost(costs: list[list[int]]) -> int:
    if not costs:
        return 0
    n = len(costs)
    dp = [costs[0][0], costs[0][1], costs[0][2]]
    for i in range(1, n):
        r = costs[i][0] + min(dp[1], dp[2])
        g = costs[i][1] + min(dp[0], dp[2])
        b = costs[i][2] + min(dp[0], dp[1])
        dp = [r, g, b]
    return min(dp)

# 时间 O(n), 空间 O(1)
```
## 5. Minimum Flips to Make String Monotone (O)
**来源**：[O](https://leetcode.cn/problems/minimum-flips-to-make-string-monotone-increasing/)
**思路**：最终字符串形式为 0...01...1 遍历每个位置作为分界点，统计左侧 1 的数量 + 右侧 0 的数量
**代码**：
```python
def minFlipsMonoIncr(s: str) -> int:
    ones = 0
    zeros = s.count('0')
    ans = zeros  # 全翻成 1
    for c in s:
        if c == '0':
            zeros -= 1
        else:
            ones += 1
        ans = min(ans, ones + zeros)
    return ans

# 时间 O(n), 空间 O(1)
```
## 6. Distinct Subsequences (O)
**来源**：[O](https://leetcode.cn/problems/distinct-subsequences/)
**难度**：困难
**题目**：给你两个字符串 `s` 和 `t` ，统计并返回在 `s` 的 **子序列** 中 `t` 出现的个数。

测试用例保证结果在 32 位有符号整数范围内。

**示例 1：**
```
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
```
**示例 2：**
```
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag
babgbag
babgbag
babgbag
babgbag
```
**提示：**

- `1
**思路**：**状态定义**：`dp[i][j]` = s[:i] 中 t[:j] 作为子序列出现的次数
**转移**：
**代码**：
```python
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        prev = 1  # dp[i-1][0]
        for j in range(1, n + 1):
            cur = dp[j]
            if s[i - 1] == t[j - 1]:
                dp[j] += prev
            prev = cur
    return dp[n]

# 时间 O(m*n), 空间 O(n)
```

---

# D48 — 图 + 并查集 + DP 综合 (6题)

---

## 1. Max Area of Island (O)
**来源**：[O](https://leetcode.cn/problems/max-area-of-island/)
**难度**：中等
**题目**：给你一个大小为 `m x n` 的二进制矩阵 `grid` 。

**岛屿**是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在**水平或者竖直的四个方向上 **相邻。你可以假设 `grid` 的四个边缘都被 `0`（代表水）包围着。

岛屿的面积是岛上值为 `1` 的单元格的数目。

计算并返回 `grid` 中最大的岛屿面积。如果没有岛屿，则返回面积为 `0` 。

**示例 1：**
```
*
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
```
**示例 2：**
```
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0
```
**提示：**

- `m == grid.length`

- `n == grid[i].length`

- `1
**思路**：DFS/BFS 遍历每个岛屿，记录最大面积
**代码**：
```python
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = 0
                stack = [(i, j)]
                grid[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                ans = max(ans, area)
    return ans

# 时间 O(m*n), 空间 O(m*n)
```
## 2. Longest Increasing Path in a Matrix (O)
**来源**：[O](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/)
**难度**：困难
**题目**：给定一个 `m x n` 整数矩阵 `matrix` ，找出其中 **最长递增路径**的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你**不能**在**对角线**方向上移动或移动到**边界外**（即不允许环绕）。

**示例 1：**
```
*
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。
```
**示例 2：**
```
*
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
```
**示例 3：**
```
输入：matrix = [[1]]
输出：1
```
**提示：**

- `m == matrix.length`

- `n == matrix[i].length`

- `1 31 - 1`
**思路**：记忆化 DFS + DP `dp[i][j]` = 从 (i,j) 出发的最长递增路径长度 递归搜索四个方向，满足值严格递增
**代码**：
```python
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]

    def dfs(i: int, j: int) -> int:
        if dp[i][j]:
            return dp[i][j]
        best = 1
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                best = max(best, 1 + dfs(ni, nj))
        dp[i][j] = best
        return best

    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))
    return ans

# 时间 O(m*n), 空间 O(m*n)
```
## 3. Redundant Connection (O)
**来源**：[O](https://leetcode.cn/problems/redundant-connection/)
**难度**：中等
**题目**：树可以看成是一个连通且 **无环 **的 **无向 **图。

给定一个图，该图从一棵 `n` 个节点 (节点值 `1～n`) 的树中添加一条边后获得。添加的边的两个不同顶点编号在 `1` 到 `n` 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 `n` 的二维数组 `edges` ，`edges[i] = [ai, bi]` 表示图中在 `ai` 和 `bi` 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 `n` 个节点的树。如果有多个答案，则返回数组 `edges` 中最后出现的那个。

**示例 1：**
```
*
输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]
```
**示例 2：**
```
*
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
```
**提示:**

- `n == edges.length`

- `3
**思路**：并查集，遍历边，若两端已连通则此边冗余
**代码**：
```python
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    parent = list(range(n + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]
    return []

# 时间 O(n·α(n)), 空间 O(n)
```
## 4. Alien Dictionary (O)
**来源**：[O](https://leetcode.cn/problems/alien-dictionary/)
**难度**：困难
**思路**：拓扑排序 1. 比较相邻单词，找出字符顺序关系 2. 建图 + 入度表 3. BFS 拓扑排序
**代码**：
```python
def alienOrder(words: list[str]) -> str:
    adj = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in adj}
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        if len(a) > len(b) and a[:len(b)] == b:
            return ""
        for c1, c2 in zip(a, b):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    indeg[c2] = indeg.get(c2, 0) + 1
                break
    q = [c for c in indeg if indeg[c] == 0]
    res = []
    while q:
        c = q.pop(0)
        res.append(c)
        for nei in adj[c]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return "".join(res) if len(res) == len(adj) else ""

# 时间 O(C) 总字符数, 空间 O(1) 最多 26 个字符
```
## 5. Sequence Reconstruction (O)
**来源**：[O](https://leetcode.cn/problems/sequence-reconstruction/)
**难度**：中等
**思路**：检查 `org` 是否为由 `seqs` 唯一确定的拓扑排序 1. 建图，统计每个节点的前驱集合 2. BFS 验证唯一性：每层队列大小只能为 1
**代码**：
```python
def sequenceReconstruction(org: list[int], seqs: list[list[int]]) -> bool:
    n = len(org)
    pos = {x: i for i, x in enumerate(org)}
    indeg = [0] * (n + 1)
    graph = [set() for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for seq in seqs:
        for x in seq:
            if x < 1 or x > n:
                return False
            visited[x] = True
        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i + 1]
            if b not in graph[a]:
                graph[a].add(b)
                indeg[b] += 1

    if not all(visited[1:]):
        return False

    from collections import deque
    q = deque([x for x in range(1, n + 1) if indeg[x] == 0])
    res = []
    while q:
        if len(q) > 1:
            return False
        x = q.popleft()
        res.append(x)
        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return res == org

# 时间 O(N + E), 空间 O(N + E)
```
## 6. Similar String Groups (O)
**来源**：[O](https://leetcode.cn/problems/similar-string-groups/)
**难度**：困难
**题目**：如果交换字符串 `X` 中的两个不同位置的字母，使得它和字符串 `Y` 相等，那么称 `X` 和 `Y` 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，`"tars"` 和 `"rats"` 是相似的 (交换 `0` 与 `2` 的位置)； `"rats"` 和 `"arts"` 也是相似的，但是 `"star"` 不与 `"tars"`，`"rats"`，或 `"arts"` 相似。

总之，它们通过相似性形成了两个关联组：`{"tars", "rats", "arts"}` 和 `{"star"}`。注意，`"tars"` 和 `"arts"` 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 `strs`。列表中的每个字符串都是 `strs` 中其它所有字符串的一个字母异位词。请问 `strs` 中有多少个相似字符串组？

**示例 1：**
```
输入：strs = ["tars","rats","arts","star"]
输出：2
```
**示例 2：**
```
输入：strs = ["omv","ovm"]
输出：1
```
**提示：**

- `1
**思路**：并查集 两字符串相似（仅交换两个字符或完全相同）则合并 返回连通分量数
**代码**：
```python
def numSimilarGroups(strs: list[str]) -> int:
    n = len(strs)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    def similar(a: str, b: str) -> bool:
        diff = 0
        for ca, cb in zip(a, b):
            if ca != cb:
                diff += 1
                if diff > 2:
                    return False
        return diff == 0 or diff == 2

    for i in range(n):
        for j in range(i + 1, n):
            if similar(strs[i], strs[j]):
                union(i, j)

    return len({find(i) for i in range(n)})

# 时间 O(n² * L), L = 字符串长度, 空间 O(n)
```

---

# D49 — 周复习 (DP 全题型回顾 + 限时小测)

---

## 📋 本周题型总览

| 分类 | 题型 | 代表题目 | 核心技巧 |
|------|------|----------|----------|
| 一维 DP | 线性递推 | Climbing Stairs, Tribonacci | 滚动变量 O(1) |
| 一维 DP | 最值优化 | Min Cost Climbing, Coin Change | 取 min/max |
| 一维 DP | 约束选择 | House Robber I/II | 环形拆线性 |
| 一维 DP | 划分型 | Word Break | 枚举分割点 |
| 一维 DP | 子序列 | LIS | 耐心排序 O(n log n) |
| 一维 DP | 背包 | Partition Equal, Target Sum, Comb Sum IV | 0-1 / 完全背包 |
| 二维 DP | 路径计数 | Unique Paths I/II | 滚动数组 |
| 二维 DP | 路径最值 | Min Path Sum, Triangle | 自底向上 |
| 二维 DP | 双序列 | LCS, Edit Distance, Interleaving | 匹配/不匹配转移 |
| 二维 DP | 正方形 | Maximal Square | 右下角推导 |
| DP 字符串 | 回文 | Palindromic Substrings, LPS | 中心扩展 |
| DP 字符串 | 子序列计数 | Distinct Subsequences | 字符匹配累加 |
| DP 高级 | 股票交易 | Best Time III/IV | 状态机 k 次 |
| DP 高级 | 序列组合 | Longest Fib Subseq | 双索引 map |
| 图/并查集 | 连通性 | Redundant Connection, Similar Groups | 并查集 |
| 图/并查集 | 拓扑排序 | Alien Dictionary, Sequence Reconstruction | 入度 BFS |
| 图/并查集 | 记忆化 DFS | Longest Increasing Path | DFS + DP |

---

## ⏱️ 限时 DP 专项小测（30 分钟）

### 题 1：最长有效括号
给定一个只包含 `(` 和 `)` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

```
输入: s = ")()())"
输出: 4  → "()()"
```

```python
def longestValidParentheses(s: str) -> int:
    dp = [0] * len(s)
    ans = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
            ans = max(ans, dp[i])
    return ans
# 时间 O(n), 空间 O(n)
```

---

### 题 2：最大子数组和
找出和最大的连续子数组，返回最大和。

```
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6  → [4,-1,2,1]
```

```python
def maxSubArray(nums: list[int]) -> int:
    cur = ans = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        ans = max(ans, cur)
    return ans
# 时间 O(n), 空间 O(1)  — Kadane 算法
```

---

### 题 3：最长递增子序列（计数）
返回 LIS 的长度和个数。

```python
def findNumberOfLIS(nums: list[int]) -> int:
    n = len(nums)
    length = [1] * n
    count = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    max_len = max(length)
    return sum(c for l, c in zip(length, count) if l == max_len)
# 时间 O(n²), 空间 O(n)
```

---

### 题 4：完全平方数
给定 n，返回最少需要几个完全平方数（1,4,9,16,…）之和等于 n。

```
输入: n = 12
输出: 3  → 4+4+4
```

```python
def numSquares(n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, int(n ** 0.5) + 1):
        sq = i * i
        for j in range(sq, n + 1):
            dp[j] = min(dp[j], dp[j - sq] + 1)
    return dp[n]
# 时间 O(n√n), 空间 O(n)
```

---

### 题 5：乘积最大子数组
找出乘积最大的连续子数组。

```
输入: [2,3,-2,4]
输出: 6  → [2,3]
```

```python
def maxProduct(nums: list[int]) -> int:
    cur_max = cur_min = ans = nums[0]
    for x in nums[1:]:
        candidates = (x, cur_max * x, cur_min * x)
        cur_max, cur_min = max(candidates), min(candidates)
        ans = max(ans, cur_max)
    return ans
# 时间 O(n), 空间 O(1)
```

---

### 题 6：戳气球（选做，面试 hard）
有 n 个气球，戳破 i 获得 `nums[i-1]*nums[i]*nums[i+1]`，求最大得分。

```python
def maxCoins(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                    nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
    return dp[0][n - 1]
# 时间 O(n³), 空间 O(n²)
```

---

## 🎯 复习建议

1. **一维 DP 模板**：状态定义 → 转移方程 → 初始条件 → 压缩空间
2. **二维 DP 模板**：双循环 → 匹配/不匹配分支 → 滚动数组优化
3. **背包问题**：0-1 背包（逆序）vs 完全背包（正序）vs 排列（外金额内物品）
4. **股票问题**：状态机推演，定义好 k 次交易的 buy/sell 数组
5. **回文问题**：中心扩展比 DP 更优（O(1) 空间）
6. **图/并查集**：拓扑排序唯一性判断、连通分量计数


---


---
# 第8周·模拟与冲刺
> 共计 7 天

# Day 50 — OD 100分 × 6 实战

## 1. 贪心商人 (OD)

**题目**：
一个商人决定在连续 N 天里买卖一种商品。他每天可以买入或卖出最多 1 件商品。已知每天的商品价格列表 prices，商人最初有 0 件商品和无限资金。请计算商人在 N 天内能获得的最大利润。

### 输入格式
```
第一行：N，表示天数 (1 ≤ N ≤ 10^5)
第二行：N 个整数，表示每天的价格 prices[i] (1 ≤ prices[i] ≤ 10^4)
```

### 输出格式
一个整数，表示最大利润。

### 样例输入
```
7
1 2 3 4 5 6 7
```

### 样例输出
```
0
```

**思路**：
贪心策略：每天如果持有商品，则比较当天价格和之前买入价；如果当天价格更高，继续持有；否则卖出并在当天买入。但本题实际是求所有上涨日间的差价之和（可以当天卖当天买，不限制持有数量时，等价于最高点卖最低点买）。

实际上，本题的贪心核心是：如果第 i 天价格 > 第 i-1 天价格，就在第 i-1 天买入、第 i 天卖出，累加差价。

### Python 解法

```python
def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

if __name__ == "__main__":
    N = int(input().strip())
    prices = list(map(int, input().strip().split()))
    print(max_profit(prices))
```

**复杂度**: O(N) 时间, O(1) 空间

---

## 2. 租车骑绿岛 (OD)

**题目**：
一个部门有 N 个人要去绿岛骑自行车，每辆自行车最多载两人。已知每个人的体重，每辆车的载重上限为 limit。问最少需要多少辆车才能让所有人骑上自行车。

### 输入格式
```
第一行：limit (1 ≤ limit ≤ 10^4)
第二行：N (1 ≤ N ≤ 10^5)
第三行：N 个整数，表示每个人的体重 (1 ≤ weight ≤ limit)
```

### 输出格式
一个整数，表示最少需要的车辆数。

### 样例输入
```
150
6
70 80 60 90 50 100
```

### 样例输出
```
4
```

**思路**：
贪心 + 双指针。将体重排序，最轻的和最重的尝试配对。如果最轻 + 最重 ≤ limit，则两人一车；否则最重单独一车。

### Python 解法

```python
def min_boats(limit, weights):
    weights.sort()
    left, right = 0, len(weights) - 1
    boats = 0
    while left <= right:
        if left == right:
            boats += 1
            break
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        boats += 1
    return boats

if __name__ == "__main__":
    limit = int(input().strip())
    n = int(input().strip())
    weights = list(map(int, input().strip().split()))
    print(min_boats(limit, weights))
```

**复杂度**: O(N log N) 时间, O(1) 空间

---

## 3. 打印机队列 (OD)

**题目**：
有一个打印机队列，每个打印任务有优先级（1-9，数字越大优先级越高）。队列按以下规则处理：
1. 每次从队首取出一个任务
2. 如果队列中有比该任务优先级更高的任务，则将该任务移到队尾
3. 否则，执行该任务

给定初始队列和你的任务在队列中的初始位置（0-indexed），问你的任务在第几个被执行。

### 输入格式
```
第一行：T，表示测试用例数
每个测试用例两行：
  第一行：N M (N个任务, M是你的任务位置)
  第二行：N个整数，表示优先级
```

### 输出格式
每个测试用例输出一个整数，表示你的任务被执行的顺序号。

### 样例输入
```
1
6 0
1 1 9 1 1 1
```

### 样例输出
```
5
```

### Python 解法

```python
from collections import deque

def printer_queue(n, m, priorities):
    q = deque([(p, i == m) for i, p in enumerate(priorities)])
    count = 0
    while q:
        cur = q.popleft()
        if any(cur[0] < task[0] for task in q):
            q.append(cur)
        else:
            count += 1
            if cur[1]:
                return count
    return -1

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().strip().split())
        priorities = list(map(int, input().strip().split()))
        print(printer_queue(n, m, priorities))
```

**复杂度**: O(N²) 最坏, 可用优先队列优化

---

## 4. 堆栈中的剩余数字 (OD)

**题目**：
给定一个整数序列，依次入栈。当入栈的数字与栈顶元素之和等于栈中下一个元素时，弹出栈顶两个元素，将它们的和入栈。重复此过程直到无法再合并。输出最终栈中从栈底到栈顶的所有元素。

### 输入格式
```
第一行：N (1 ≤ N ≤ 10^5)
第二行：N 个整数
```

### 输出格式
一行整数，从栈底到栈顶的剩余元素，空格分隔。

### 样例输入
```
5
3 6 4 2 5
```

### 样例输出
```
3 6 9 5
```

**思路**：
模拟栈操作。每次入栈后检查栈顶三个元素是否满足条件。

### Python 解法

```python
def stack_remaining(arr):
    stack = []
    for num in arr:
        stack.append(num)
        while len(stack) >= 3 and stack[-1] + stack[-2] == stack[-3]:
            a = stack.pop()
            b = stack.pop()
            c = stack.pop()
            stack.append(a + b)
    return stack

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = stack_remaining(arr)
    print(" ".join(map(str, result)))
```

**复杂度**: O(N) 时间, O(N) 空间

---

## 5. 全量和已占用字符集 (OD)

**题目**：
给定一个全量字符集（包含所有可用字符及其数量）和一个已占用字符集（已使用的字符及其数量），请计算剩余可用字符集。字符为小写字母，每个字符只出现一次在全量字符集中。

### 输入格式
```
第一行：全量字符集，格式为 a:1,b:2,c:3
第二行：已占用字符集，格式为 a:1,b:1
```

### 输出格式
剩余可用字符集，相同格式，数量为0的不输出。

### 样例输入
```
a:1,b:2,c:3
a:1,b:1
```

### 样例输出
```
b:1,c:3
```

### Python 解法

```python
def parse_char_set(s):
    result = {}
    for part in s.split(","):
        char, count = part.split(":")
        result[char] = int(count)
    return result

def remaining(full_str, used_str):
    full = parse_char_set(full_str)
    used = parse_char_set(used_str)
    for ch, cnt in used.items():
        if ch in full:
            full[ch] -= cnt
            if full[ch] == 0:
                del full[ch]
    return ",".join(f"{ch}:{cnt}" for ch, cnt in sorted(full.items()))

if __name__ == "__main__":
    full_str = input().strip()
    used_str = input().strip()
    print(remaining(full_str, used_str))
```

**复杂度**: O(N) 时间, O(1) 空间

---

## 6. 模拟商场优惠打折 (OD)

**题目**：
商场有三种优惠方式：
1. 满减：满100减10，可叠加（每满100减10）
2. 打折：打92折（乘以0.92，向下取整）
3. 无门槛：每满5件减5（每5件减5，不累计到下一组）

每种优惠只能用一次。给定一个订单总金额和商品数量，求使用一种优惠后的最低价格。

### 输入格式
```
第一行：M N (M 订单金额, N 商品数量)
```

### 输出格式
三个整数，分别表示使用满减、打折、无门槛优惠后的价格，空格分隔。

### 样例输入
```
210 12
```

### 样例输出
```
190 193 200
```

### Python 解法

```python
def discount_full_reduction(m):
    return m - (m // 100) * 10

def discount_percent(m):
    return int(m * 0.92)

def discount_no_threshold(m, n):
    return m - (n // 5) * 5

if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    r1 = discount_full_reduction(m)
    r2 = discount_percent(m)
    r3 = discount_no_threshold(m, n)
    print(r1, r2, r3)
```

**复杂度**: O(1) 时间, O(1) 空间


---

# Day 51 — OD 100分 × 6 实战

## 1. 三叉树高度 (OD)

**题目**：
给定一棵三叉树（每个节点最多有三个子节点）的前序遍历序列和每个节点的子节点数量序列，请计算树的高度（根节点高度为1）。

前序遍历序列：按前序顺序排列的节点值列表
子节点数量序列：与前序遍历对应的每个节点的子节点数量

### 输入格式
```
第一行：N，节点个数
第二行：N个整数，前序遍历序列
第三行：N个整数，对应每个节点的子节点数量 (0 ≤ cnt ≤ 3)
```

### 输出格式
一个整数，表示树的高度。

### 样例输入
```
7
1 2 4 5 6 3 7
2 0 2 0 0 0 0
```

### 样例输出
```
3
```

**思路**：
递归构建 + 深度计算。根据前序遍历和子节点数量递归构建子树，同时记录最大深度。

### Python 解法

```python
def build_tree(preorder, children, idx=0, depth=1):
    if idx >= len(preorder):
        return idx, depth
    node = preorder[idx]
    cnt = children[idx]
    max_depth = depth
    cur_idx = idx + 1
    for _ in range(cnt):
        cur_idx, child_depth = build_tree(preorder, children, cur_idx, depth + 1)
        max_depth = max(max_depth, child_depth)
    return cur_idx, max_depth

if __name__ == "__main__":
    n = int(input().strip())
    preorder = list(map(int, input().strip().split()))
    children = list(map(int, input().strip().split()))
    _, height = build_tree(preorder, children)
    print(height)
```

**复杂度**: O(N) 时间, O(N) 栈空间

---

## 2. 最富裕小家庭 (OD)

**题目**：
在一个家族中，每个成员都有唯一的编号（1-N）。每个成员可能有0个或多个后代。一个小家庭定义为：一对父母和他们的所有直系子女。给定每个成员的财富值和家族的父子关系，请找出财富总和最大的小家庭，输出其财富总和。

### 输入格式
```
第一行：N，成员数量 (1 ≤ N ≤ 10^5)
第二行：N个整数，wealth[i] 表示编号 i+1 的财富
第三行开始每行：A B 表示 A 是 B 的父亲
最后一行：-1 -1
```

### 输出格式
一个整数，最大财富总和。

### 样例输入
```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
-1 -1
```

### 样例输出
```
100
```

### Python 解法

```python
def richest_family(n, wealth, relations):
    children = [[] for _ in range(n + 1)]
    for a, b in relations:
        children[a].append(b)
    max_sum = 0
    for i in range(1, n + 1):
        total = wealth[i - 1]
        for c in children[i]:
            total += wealth[c - 1]
        max_sum = max(max_sum, total)
    return max_sum

if __name__ == "__main__":
    n = int(input().strip())
    wealth = list(map(int, input().strip().split()))
    relations = []
    while True:
        a, b = map(int, input().strip().split())
        if a == -1:
            break
        relations.append((a, b))
    print(richest_family(n, wealth, relations))
```

**复杂度**: O(N) 时间, O(N) 空间

---

## 3. 疫情扩散 (OD-BFS)

**题目**：
在一个 N×M 的网格中，0 表示空地，1 表示健康人，2 表示已感染者。每天感染者的上下左右四个方向上的健康人会变成感染者。问至少需要多少天才能感染所有健康人？如果无法全部感染，输出 -1。

### 输入格式
```
第一行：N M
接下来 N 行，每行 M 个整数（0/1/2）
```

### 输出格式
一个整数，表示最少天数。

### 样例输入
```
3 3
2 1 1
1 1 0
0 1 1
```

### 样例输出
```
4
```

### Python 解法 (BFS)

```python
from collections import deque

def spread_days(grid, n, m):
    q = deque()
    healthy = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                healthy += 1

    if healthy == 0:
        return 0

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    max_days = 0
    while q:
        x, y, d = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 2
                healthy -= 1
                nd = d + 1
                max_days = max(max_days, nd)
                q.append((nx, ny, nd))

    return -1 if healthy > 0 else max_days

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    print(spread_days(grid, n, m))
```

**复杂度**: O(N×M) 时间, O(N×M) 空间

---

## 4. 服务器广播 (OD)

**题目**：
有 N 台服务器，服务器之间通过连接进行广播。如果服务器 A 和 B 直接连接，A 向 B 发一条消息即可通信。如果 A 和 B 不直接连接，但可以通过中间服务器转发。给定 N×N 的邻接矩阵（1表示直接连接），问最少需要向多少台服务器发送初始消息，才能让所有服务器都收到消息。

### 输入格式
```
第一行：N (1 ≤ N ≤ 200)
接下来 N 行：每行 N 个整数（0或1）
```

### 输出格式
一个整数，表示最少初始发送的服务器数量。

### 样例输入
```
4
1 1 0 0
1 1 0 0
0 0 1 1
0 0 1 1
```

### 样例输出
```
2
```

**思路**：
等价于求连通分量数。DFS/BFS/并查集均可。

### Python 解法 (DFS)

```python
def min_broadcast(adj, n):
    visited = [False] * n
    count = 0

    def dfs(u):
        visited[u] = True
        for v in range(n):
            if adj[u][v] == 1 and not visited[v]:
                dfs(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

if __name__ == "__main__":
    n = int(input().strip())
    adj = [list(map(int, input().strip().split())) for _ in range(n)]
    print(min_broadcast(adj, n))
```

**复杂度**: O(N²) 时间, O(N) 空间

---

## 5. 找等值元素 (OD)

**题目**：
给定一个整数矩阵，找出所有出现次数超过矩阵元素总数一半的元素。如果有多个，按值从小到大输出；如果没有，输出 -1。

### 输入格式
```
第一行：N M (N行 M列, 1 ≤ N,M ≤ 100)
接下来 N 行：每行 M 个整数
```

### 输出格式
一行整数，空格分隔，或 -1。

### 样例输入
```
2 3
1 2 2
2 3 3
```

### 样例输出
```
2
```

### Python 解法

```python
def find_majority(matrix, n, m):
    total = n * m
    half = total // 2
    freq = {}
    for row in matrix:
        for val in row:
            freq[val] = freq.get(val, 0) + 1
    result = [k for k, v in freq.items() if v > half]
    if not result:
        return -1
    return " ".join(map(str, sorted(result)))

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    print(find_majority(matrix, n, m))
```

**复杂度**: O(N×M) 时间, O(N×M) 空间

---

## 6. 单入口空闲区域 (OD)

**题目**：
在一个 N×M 的网格中，O 表示空闲区域，X 表示障碍物。有一个唯一的入口（在网格边界上），从入口进入后，可以上下左右移动。问最大的连通空闲区域面积（包含的 O 的数量）。如果入口被障碍物挡住（入口本身是 X），输出 -1。

### 输入格式
```
第一行：N M
第二行：入口坐标 x y (0-indexed)
接下来 N 行：每行 M 个字符（O 或 X）
```

### 输出格式
一个整数，表示最大连通空闲区域面积。

### 样例输入
```
4 4
0 2
O O O X
O X O X
X O O X
O O X X
```

### 样例输出
```
5
```

### Python 解法 (BFS/DFS)

```python
def max_free_area(grid, n, m, start_x, start_y):
    if grid[start_x][start_y] == 'X':
        return -1

    from collections import deque
    q = deque([(start_x, start_y)])
    grid[start_x][start_y] = 'V'  # visited
    count = 1
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'O':
                grid[nx][ny] = 'V'
                count += 1
                q.append((nx, ny))
    return count

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    sx, sy = map(int, input().strip().split())
    grid = [list(input().strip().split()) for _ in range(n)]
    print(max_free_area(grid, n, m, sx, sy))
```

**复杂度**: O(N×M) 时间, O(N×M) 空间


---

# Day 52 — OD 200分 × 3 实战

## 1. 中文分词模拟器 (OD-200)

**题目**：
给定一个中文字符串（不含空格）和一个词典（包含多个词），请实现对字符串的分词。要求输出所有可能的分词方案（按字典序排序）。如果无法分词，输出空列表。

词典中的词都是中文词语，字符串由中文字符组成。

### 输入格式
```
第一行：要分词的字符串 S (1 ≤ |S| ≤ 100)
第二行：词典中的词数量 N (1 ≤ N ≤ 1000)
接下来 N 行：每行一个词
```

### 输出格式
所有可能的分词方案，每个方案中的词用空格分隔，不同方案按字典序排列。
如果无法分词，输出空行。

### 样例输入
```
我爱北京天安门
5
北京
天安门
我爱
我
爱北京
```

### 样例输出
```
我 爱北京 天安门
我爱 北京 天安门
```

**思路**：
使用 DFS/回溯 + 记忆化搜索。从字符串起始位置开始，尝试匹配词典中的词，递归处理剩余部分。用 `@lru_cache` 或字典记录已计算过的起始位置的结果，避免重复计算。

### Python 解法

```python
from functools import lru_cache

def word_break(s, word_set):
    @lru_cache(None)
    def dfs(start):
        if start == len(s):
            return [[]]  # 空列表表示一种有效分割的结尾
        results = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                rest = dfs(end)
                for r in rest:
                    results.append([word] + r)
        return results

    all_results = dfs(0)
    if not all_results:
        print()
        return

    schemes = [" ".join(seq) for seq in all_results]
    schemes.sort()
    for scheme in schemes:
        print(scheme)

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    word_set = set()
    for _ in range(n):
        word_set.add(input().strip())
    word_break(s, word_set)
```

**复杂度分析**:
- 时间复杂度: O(2^N) 最坏（所有字符都能单独成词），但记忆化剪枝后实际远小于此
- 空间复杂度: O(N × M)，其中 M 是方案数

**易错点**:
- 注意中文字符在 Python 中长度为1，无需特殊处理
- 词典用 set 实现 O(1) 查找
- 输出要求按字典序排列

---

## 2. 模拟目录管理功能 (OD-200)

**题目**：
实现一个简易的目录管理功能，支持以下命令：
1. `mkdir dirname` — 在当前目录下创建子目录（同名已存在则忽略）
2. `cd dirname` — 进入子目录（`..` 表示返回上级目录，根目录的 `..` 忽略）
3. `pwd` — 打印当前目录的完整路径

初始在根目录 `/`。

### 输入格式
```
第一行：N (1 ≤ N ≤ 1000)
接下来 N 行：每行一个命令
```

### 输出格式
每遇到 `pwd` 命令，输出一行当前路径。

### 样例输入
```
6
mkdir a
cd a
mkdir b
cd b
pwd
cd ..
pwd
```

### 样例输出
```
/a/b
/a
```

**思路**：
用栈保存当前路径。`mkdir` 时检查子目录是否已存在；`cd` 时处理 `.` 或 `..` 或普通目录名；`pwd` 时输出路径。

注意：由于要支持 `cd dirname` 直接进入，需要维护一个树形结构或简单的路径栈。更简单的方式是维护一个目录树，每个节点包含子目录字典。

### Python 解法

```python
class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}  # name -> Directory

def simulate_commands(commands):
    root = Directory("/")
    current = root
    output = []

    for cmd in commands:
        parts = cmd.split()
        if parts[0] == "mkdir":
            dirname = parts[1]
            if dirname not in current.children:
                current.children[dirname] = Directory(dirname)

        elif parts[0] == "cd":
            dirname = parts[1]
            if dirname == "..":
                # 需要知道父目录，因此我们用栈来存路径
                pass  # 下面用栈方式重新实现
            elif dirname == ".":
                continue
            elif dirname in current.children:
                current = current.children[dirname]

        elif parts[0] == "pwd":
            # 用栈方式更方便获取完整路径
            pass

    # 上面的树结构不方便获取全路径和父节点
    # 改用栈实现
    return root

# ===== 更好的实现：路径栈 =====
def run_commands(commands):
    stack = []  # 存储当前路径的目录名列表
    output = []

    for cmd in commands:
        parts = cmd.split()
        op = parts[0]

        if op == "mkdir":
            dirname = parts[1]
            # 由于题目简化，我们可以用虚拟文件系统
            # 这里假设 mkdir 总是成功（同名校验由模拟题决定）
            # 实际需要维护一个目录存在性集合
            pass

    # 完整实现见下方
    return output

# ===== 完整实现 =====
class FileSystem:
    def __init__(self):
        self.dir_contents = {"/": set()}  # path -> set of subdir names
        self.stack = ["/"]

    def mkdir(self, dirname):
        cur_path = "".join(self.stack) if self.stack[-1] == "/" else "".join(self.stack) + "/"
        # 简化：将当前路径用 tuple 维护
        pass

# ===== 最终简洁实现 =====
def dir_manager(commands):
    path = []
    output = []

    # 用集合存储所有已创建的目录完整路径
    dirs = set()
    dirs.add("/")

    for cmd in commands:
        parts = cmd.split()
        op = parts[0]

        if op == "mkdir":
            name = parts[1]
            cur = "/" + "/".join(path)
            full = cur + ("/" if cur != "/" else "") + name
            dirs.add(full)
            # 注意：题目可能不需要校验重名

        elif op == "cd":
            name = parts[1]
            if name == "..":
                if path:
                    path.pop()
            elif name == ".":
                continue
            else:
                path.append(name)

        elif op == "pwd":
            p = "/" + "/".join(path)
            if p == "":
                p = "/"
            output.append(p)

    return output

# 上面有缺陷，用正确的最终版本：

def directory_manager(commands):
    """
    模拟目录管理。
    使用栈维护当前路径，使用集合维护所有已创建的目录。
    """
    stack = []  # 当前路径栈
    dirs = {"/"}  # 所有已创建的目录
    result = []

    for cmd in commands:
        parts = cmd.split()
        op = parts[0]

        if op == "mkdir":
            dirname = parts[1]
            # 构建完整路径
            if not stack:
                full = "/" + dirname
            else:
                full = "/" + "/".join(stack) + "/" + dirname
            dirs.add(full)

        elif op == "cd":
            target = parts[1]
            if target == "..":
                if stack:
                    stack.pop()
            elif target == ".":
                continue
            else:
                stack.append(target)

        elif op == "pwd":
            if not stack:
                result.append("/")
            else:
                result.append("/" + "/".join(stack))

    return result

if __name__ == "__main__":
    n = int(input().strip())
    commands = [input().strip() for _ in range(n)]
    output = directory_manager(commands)
    for line in output:
        print(line)
```

**复杂度分析**:
- 时间复杂度: O(N × L)，L 为路径平均长度
- 空间复杂度: O(N × L)，存储所有目录路径

**易错点**:
- 根目录打印为 `/` 而不是空字符串
- `cd ..` 在根目录时不做任何操作
- `mkdir` 可能要求校验重名（通常忽略即可）

---

## 3. 贪心歌手 (OD-200)

**题目**：
一个歌手要开演唱会，每唱一首歌需要消耗一定的体力，演唱后会获得快乐值。歌手初始体力为 S，体力不能为负。每首歌可以唱多次，但每次唱消耗和获得的数值不变。请问在体力允许的情况下，歌手能获得的最大快乐值是多少？

这是一个完全背包问题：体力视为背包容量，每首歌视为物品，消耗为重量，快乐值为价值，每种物品无限取用。

### 输入格式
```
第一行：S N (S 初始体力, N 歌曲数, 1 ≤ S ≤ 10^4, 1 ≤ N ≤ 500)
接下来 N 行：每行两个整数 cost_i happy_i (消耗体力, 获得快乐值)
```

### 输出格式
一个整数，表示最大快乐值。

### 样例输入
```
10 3
5 60
3 50
2 30
```

### 样例输出
```
210
```

**思路**：
完全背包 DP。`dp[j]` 表示体力消耗为 j 时能获得的最大快乐值。从小到大遍历体力，对每首歌尝试无限次使用（内层循环从小到大）。

状态转移方程：`dp[j] = max(dp[j], dp[j - cost_i] + happy_i)`

### Python 解法

```python
def max_happiness(s, songs):
    dp = [0] * (s + 1)
    for cost, happy in songs:
        for j in range(cost, s + 1):
            dp[j] = max(dp[j], dp[j - cost] + happy)
    return dp[s]

if __name__ == "__main__":
    s, n = map(int, input().strip().split())
    songs = []
    for _ in range(n):
        cost, happy = map(int, input().strip().split())
        songs.append((cost, happy))
    print(max_happiness(s, songs))
```

**复杂度分析**:
- 时间复杂度: O(N × S) = O(500 × 10^4) = 5×10^6，可接受
- 空间复杂度: O(S)

**优化思路**:
- 如果 N 很大但 S 较小，复杂度由 S 主导
- 可以使用贪心预处理：对于每单位体力效率低的歌曲可以提前过滤

**易错点**:
- 是完全背包不是 0-1 背包，内层循环必须从小到大
- 初始体力 S 可能为 0，此时结果也是 0
- 体力消耗可能为 0，需要处理（如果 cost=0 且 happy>0，可以无限获取快乐值，但在本题中通常 cost ≥ 1）


---

# Day 53 — OD 200分 × 3 实战

## 1. 二进制差异数 (OD-200)

**题目**：
定义两个正整数 A 和 B 的差异值为 A XOR B 的结果中二进制 1 的个数。给定 N 个正整数，请找出差异值最大的一对数，输出最大差异值。如果有多个，输出最大差异值最小的那对（按 A XOR B 的值最小）；如果仍然有多个，输出 A 最小的那对。

### 输入格式
```
第一行：N (2 ≤ N ≤ 10^5)
第二行：N 个正整数 (1 ≤ 数值 ≤ 2^31 - 1)
```

### 输出格式
第一行：A B (按原始顺序中较早出现的在前)
第二行：差异值（1的个数）

### 样例输入
```
5
1 3 5 7 9
```

### 样例输出
```
1 7
3
```

**思路**：
暴力 O(N²) 会超时。可以借助 Trie（字典树）优化。将每个数的二进制表示（31位）插入 Trie，然后对每个数在 Trie 中查找能使 XOR 值最大（即尽可能走不同分支）的数，同时记录结果。

另一种思路：按最高不同位分组，然后组内比较。但 Trie 是最通用的方法。

### Python 解法 (Trie)

```python
class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.val = None

class BinaryTrie:
    def __init__(self, bits=31):
        self.root = TrieNode()
        self.bits = bits

    def insert(self, num):
        node = self.root
        for i in range(self.bits, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.val = num

    def max_xor(self, num):
        """返回与num XOR结果最大的数及其XOR值"""
        node = self.root
        xor_val = 0
        for i in range(self.bits, -1, -1):
            bit = (num >> i) & 1
            # 优先走相反分支
            want = 1 - bit
            if node.children[want]:
                xor_val |= (1 << i)
                node = node.children[want]
            else:
                node = node.children[bit]
        return node.val, xor_val

def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    trie = BinaryTrie(31)
    max_diff = -1
    best_pair = None
    best_xor = None

    # 边插入边查询，保证"较早出现的在前"
    for i, num in enumerate(arr):
        if i > 0:
            other, xor_val = trie.max_xor(num)
            diff = bin(xor_val).count("1")
            if diff > max_diff:
                max_diff = diff
                best_xor = xor_val
                best_pair = (other, num)
            elif diff == max_diff:
                if xor_val < best_xor:
                    best_xor = xor_val
                    best_pair = (other, num)
                elif xor_val == best_xor:
                    if other < best_pair[0]:
                        best_pair = (other, num)
        trie.insert(num)

    print(best_pair[0], best_pair[1])
    print(max_diff)

if __name__ == "__main__":
    solve()
```

**复杂度分析**:
- 时间复杂度: O(N × 31) = O(N)，每次插入和查询都是常数时间
- 空间复杂度: O(N × 31) 最坏

**易错点**:
- 处理 31 位二进制（int 正数范围）
- 边插入边查询保证输出顺序
- 差异值是 XOR 结果中 1 的个数，不是 XOR 值本身

---

## 2. 最大平分数组 (OD-200-DP)

**题目**：
给定一个整数数组，请将其分成两个子数组（子数组保持原顺序连续），使得两个子数组的和相等。如果存在，输出任意一个分割位置（即第一个子数组的最后一个元素的索引，0-indexed）；如果不存在，输出 -1。

### 输入格式
```
第一行：N (1 ≤ N ≤ 10^5)
第二行：N 个整数 (绝对值 ≤ 10^4)
```

### 输出格式
一个整数，分割位置索引，或 -1。

### 样例输入
```
6
1 2 3 0 3 3
```

### 样例输出
```
2
```

**思路**：
计算总和 total。遍历数组，维护前缀和 prefix。当 prefix * 2 == total 时，当前位置就是分割点。

### Python 解法

```python
def find_split(arr):
    total = sum(arr)
    if total % 2 != 0:
        return -1
    half = total // 2
    prefix = 0
    for i in range(len(arr) - 1):  # 至少留一个元素给右边
        prefix += arr[i]
        if prefix == half:
            return i
    return -1

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(find_split(arr))
```

**复杂度分析**:
- 时间复杂度: O(N)
- 空间复杂度: O(1)

**进阶版本**: 如果不要求连续（即子集划分），则为经典平分数组问题，需要 DP + 状态压缩。

### 进阶版 — 不要求连续（子集划分）

```python
def can_partition(nums):
    """判断能否将数组分成两个和相等的子集（不要求连续）"""
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    return dp[target]

def partition_subsets(nums):
    """返回两个子集（元素列表），如果不存在返回空列表"""
    total = sum(nums)
    if total % 2 != 0:
        return [], []
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True
    parent = [-1] * (target + 1)  # 记录路径

    for i, num in enumerate(nums):
        for j in range(target, num - 1, -1):
            if dp[j - num] and not dp[j]:
                dp[j] = True
                parent[j] = i  # 记录达到 j 时使用的最后一个元素索引

    if not dp[target]:
        return [], []

    # 回溯找到子集
    used = [False] * len(nums)
    j = target
    while j > 0:
        idx = parent[j]
        used[idx] = True
        j -= nums[idx]

    subset1 = [nums[i] for i in range(len(nums)) if used[i]]
    subset2 = [nums[i] for i in range(len(nums)) if not used[i]]
    return subset1, subset2

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    s1, s2 = partition_subsets(arr)
    if not s1:
        print(-1)
    else:
        print(" ".join(map(str, s1)))
        print(" ".join(map(str, s2)))
```

**进阶版复杂度**: O(N × target) 时间, O(target) 空间

---

## 3. 无向图染色 (OD-200)

**题目**：
给定一个无向图，用两种颜色（0和1）对每个节点染色，要求相邻节点颜色不同。请判断是否存在这样的染色方案。如果存在，输出任意一种染色方案；如果不存在，输出 -1。

### 输入格式
```
第一行：N M (N 节点数 1≤N≤10^4, M 边数 0≤M≤5×10^4)
接下来 M 行：每行两个整数 u v，表示一条无向边 (0-indexed)
```

### 输出格式
```
如果存在：一行 N 个整数（0或1），表示每个节点的颜色
如果不存在：-1
```

### 样例输入
```
4 4
0 1
1 2
2 3
0 3
```

### 样例输出
```
0 1 0 1
```

**思路**：
图的二染色问题，等价于判断是否是二分图。用 BFS/DFS 遍历每个连通分量，交替染色。如果发现相邻节点颜色相同，则不是二分图。

### Python 解法 (BFS)

```python
from collections import deque

def bipartite(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n  # -1未染色, 0和1两种颜色

    for i in range(n):
        if color[i] != -1:
            continue
        # BFS 染色
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    return False, None
    return True, color

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append((u, v))

    ok, colors = bipartite(n, edges)
    if ok:
        print(" ".join(map(str, colors)))
    else:
        print(-1)
```

**复杂度分析**:
- 时间复杂度: O(N + M)，每个节点和每条边访问一次
- 空间复杂度: O(N + M)

**DFS 解法**:

```python
def bipartite_dfs(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == -1:
                if not dfs(v, c ^ 1):
                    return False
            elif color[v] == c:
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False, None
    return True, color
```

**DFS 复杂度**: 同样 O(N + M) 时间, O(N) 栈空间

**易错点**:
- 图可能不连通，需要遍历所有节点
- 注意 0-indexed 和 1-indexed 的转换
- BFS 和 DFS 都可以，但 BFS 更安全（防止深递归栈溢出）


---

# Day 54 — 🧪 限时模考 #1
## 100分 + 100分 | 60分钟

---

# 模考说明

| 项目 | 内容 |
|------|------|
| 总时间 | 60 分钟 |
| 题量 | 2 题（各 100 分） |
| 总分 | 200 分 |
| 环境 | 可使用本地 IDE，需自行处理输入输出 |
| 建议 | 每题 30 分钟，先易后难 |

**考试纪律**: 限时完成，建议使用真实考试节奏。遇到卡壳超过 15 分钟先做下一题。

---

# 题目一：网络延迟时间 (100分)

## 问题描述
在一个计算机网络中，有 N 个节点（编号 1~N），以及 M 条有向边，每条边表示从节点 u 到节点 v 的传输延迟为 t 毫秒。现从节点 K 发送一个信号，求信号到达所有节点所需的最短时间。如果存在节点无法到达，输出 -1。

## 输入格式
```
第一行：N M K (N个节点, M条边, 起始节点K)
接下来 M 行：每行三个整数 u v t (从u到v的延迟t毫秒, 1 ≤ t ≤ 100)
```

### 约束
- 1 ≤ N ≤ 100
- 0 ≤ M ≤ N×(N-1)
- 1 ≤ K ≤ N
- 图中可能有环

## 输出格式
一个整数，表示信号到达所有节点的最短时间。如果有节点不可达，输出 -1。

## 样例输入
```
4 3 2
2 1 1
2 3 1
3 4 1
```

## 样例输出
```
2
```

## 样例解释
节点2→1(1ms), 节点2→3(1ms), 节点3→4(1ms)。最远节点4需要1+1=2ms。

---

## 评分标准
| 项目 | 分值 |
|------|------|
| 正确实现单源最短路径算法 | 40分 |
| 正确处理不可达节点 | 20分 |
| 正确处理输入输出格式 | 20分 |
| 通过所有测试用例 | 20分 |

---

## 题目二：任务调度器 (100分)

## 问题描述
有一个任务调度器，可以同时执行多个任务（并行），但有一个限制：同一个类型的任务两次执行之间必须有至少 n 个冷却时间单位（即中间间隔 n 个单位时间才能再次执行同一类型任务）。

给定一个任务列表（每个字符代表一种任务类型）和冷却时间 n，请计算完成所有任务所需的最短时间。任务可以按任意顺序执行，每个任务执行需要 1 个单位时间。

### 示例
任务列表: A A A B B B, n = 2
最优调度: A → B → idle → A → B → idle → A → B
总时间: 8

## 输入格式
```
第一行：一个字符串，表示任务列表（仅包含大写字母）
第二行：整数 n (0 ≤ n ≤ 100)
```

## 输出格式
一个整数，表示最短完成时间。

## 样例输入
```
AAABBB
2
```

## 样例输出
```
8
```

## 评分标准
| 项目 | 分值 |
|------|------|
| 正确理解冷却约束 | 30分 |
| 正确实现贪心/模拟调度 | 30分 |
| 正确处理输入输出 | 20分 |
| 通过所有测试用例 | 20分 |

---

# 答案与解析

## 题目一 题解

### 思路分析
这是单源最短路径问题，使用 Dijkstra 算法（因为边权为正）。从节点 K 出发，计算到所有节点的最短距离，取最大值。如果有节点距离仍为 INF，说明不可达，返回 -1。

### Python 解法

```python
import heapq

def network_delay(n, m, k, edges):
    # 构建邻接表
    graph = [[] for _ in range(n + 1)]
    for u, v, t in edges:
        graph[u].append((v, t))

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[k] = 0

    pq = [(0, k)]  # (距离, 节点)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, t in graph[u]:
            nd = d + t
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    max_dist = max(dist[1:])  # 忽略索引0
    return -1 if max_dist == INF else max_dist

if __name__ == "__main__":
    n, m, k = map(int, input().strip().split())
    edges = [tuple(map(int, input().strip().split())) for _ in range(m)]
    print(network_delay(n, m, k, edges))
```

**复杂度**: O(M log N) 时间, O(N + M) 空间

### 备选解法（Floyd-Warshall，N≤100时可用）
```python
def floyd_solution(n, m, k, edges):
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, t in edges:
        dist[u][v] = t

    for mid in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][mid] + dist[mid][j] < dist[i][j]:
                    dist[i][j] = dist[i][mid] + dist[mid][j]

    max_dist = max(dist[k][1:])
    return -1 if max_dist == INF else max_dist
```

**Floyd 复杂度**: O(N³) = 10^6 (N=100 时可接受)

---

## 题目二 题解

### 思路分析
贪心策略：每次优先选择剩余次数最多的任务类型执行（因为它的冷却约束最严格，需要优先安排）。使用最大堆（优先队列）来管理任务类型的剩余次数，使用队列来管理冷却中的任务。

### 核心公式法（更简单）
设最多频次的任务出现了 max_freq 次，有 max_count 种任务具有该频次。则最短时间公式为：
```
time = max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```

### Python 解法（模拟法）

```python
from collections import Counter, deque
import heapq

def task_scheduler(tasks, n):
    count = Counter(tasks)
    max_heap = [-cnt for cnt in count.values()]
    heapq.heapify(max_heap)

    time = 0
    q = deque()  # (剩余次数, 可执行时间)

    while max_heap or q:
        time += 1
        if max_heap:
            cnt = -heapq.heappop(max_heap) - 1  # 执行一个
            if cnt > 0:
                q.append((cnt, time + n))  # n个冷却时间后恢复
        else:
            # 没有可执行的任务，直接跳到下一个任务可执行的时间
            if q:
                cnt, ready_time = q.popleft()
                time = ready_time
                heapq.heappush(max_heap, -cnt)
                continue

        # 检查冷却队列中到时的任务
        while q and q[0][1] == time:
            cnt, _ = q.popleft()
            heapq.heappush(max_heap, -cnt)

    return time
```

**复杂度**: O(T log K)，T 为总执行时间，K 为任务类型数

### Python 解法（公式法 — 推荐）

```python
from collections import Counter

def task_scheduler_formula(tasks, n):
    count = Counter(tasks)
    max_freq = max(count.values())
    max_count = sum(1 for v in count.values() if v == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

if __name__ == "__main__":
    tasks = input().strip()
    n = int(input().strip())
    print(task_scheduler_formula(tasks, n))
```

**复杂度**: O(N) 时间, O(1) 空间（只有26种大写字母）

### 公式解释
- 出现最多次的任务类型是瓶颈
- `(max_freq - 1)` 个完整周期，每个周期 `(n + 1)` 个时间单位
- 最后一个周期只需要放 `max_count` 个任务（相同最大频次的任务类型数）
- 但总长度不能少于任务总数（当 n=0 时公式退化为任务总数）

---

# 模考复盘
- **时间分配**: 每题 ≤ 30 分钟，超时就跳过
- **常见失误**: 
  - Dijkstra 忘记初始化 INF
  - 任务调度公式法忘记取 max(len(tasks), ...)
  - 输入读取错误（如 strip/split 遗漏）
- **分数预估**: 两题全对 → 200分


---

# Day 55 — 🧪 限时模考 #2
## 100分 + 200分 | 90分钟

---

# 模考说明

| 项目 | 内容 |
|------|------|
| 总时间 | 90 分钟 |
| 题量 | 2 题（100分 + 200分） |
| 总分 | 300 分 |
| 环境 | 可使用本地 IDE，需自行处理输入输出 |
| 建议 | 第1题30分钟，第2题60分钟 |

**考试纪律**: 限时完成，200分题难度较高，建议先做100分题保底。

---

# 题目一：最长连续序列 (100分)

## 问题描述
给定一个未排序的整数数组，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。要求时间复杂度 O(N)。

### 示例
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长数字连续序列是 [1, 2, 3, 4]，长度为 4。

## 输入格式
```
第一行：N (1 ≤ N ≤ 10^5)
第二行：N 个整数 (绝对值 ≤ 10^9)
```

## 输出格式
一个整数，表示最长连续序列的长度。

## 样例输入
```
6
100 4 200 1 3 2
```

## 样例输出
```
4
```

## 评分标准
| 项目 | 分值 |
|------|------|
| 正确理解题意（连续指值连续，非下标连续） | 20分 |
| O(N) 时间复杂度实现 | 40分 |
| 正确处理输入输出 | 20分 |
| 通过所有测试用例 | 20分 |

---

# 题目二：最短路径 — 带障碍物 (200分)

## 问题描述
在一个 N×M 的网格中，0 表示可通行，1 表示障碍物。你可以上下左右移动，每次移动一步，耗时 1 分钟。你有一个特殊技能：可以消除最多 K 个障碍物（将 1 变成 0），每次消除耗时 0 分钟（瞬间完成）。请计算从起点 (0,0) 到终点 (N-1, M-1) 所需的最短时间。如果无法到达，输出 -1。

### 示例
网格:
```
0 1 0
0 1 0
0 0 0
```
K = 1
起点 (0,0), 终点 (2,2)
路径: (0,0)→(0,1)消除→(1,1)消除? 等等，K=1只能消除1个。
实际最短路径: (0,0)→(1,0)→(2,0)→(2,1)→(2,2) 不需要消除，长度4。

如果 K = 0，则必须走全 0 路径。

## 输入格式
```
第一行：N M K (1 ≤ N,M ≤ 100, 0 ≤ K ≤ N×M)
接下来 N 行：每行 M 个整数 (0或1)
```

## 输出格式
一个整数，表示最短时间。如果无法到达，输出 -1。

## 样例输入
```
3 3 1
0 1 0
0 1 0
0 0 0
```

## 样例输出
```
4
```

## 评分标准
| 项目 | 分值 |
|------|------|
| 正确理解状态（位置+已消除数） | 40分 |
| 正确实现 BFS 最短路 | 60分 |
| 处理 K 的约束 | 40分 |
| 代码质量与输入输出 | 30分 |
| 通过所有测试用例 | 30分 |

---

# 答案与解析

## 题目一 题解

### 思路分析
O(N) 解法：用 set 存储所有数字。遍历集合，只对「某数-1不在集合中」的数开始计数（即序列起点），然后不断 +1 检查长度。这样每个数最多被访问两次。

### Python 解法

```python
def longest_consecutive(nums):
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # 只从序列起点开始检查
        if num - 1 not in num_set:
            cur = num
            cur_len = 1
            while cur + 1 in num_set:
                cur += 1
                cur_len += 1
            max_len = max(max_len, cur_len)

    return max_len

if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(longest_consecutive(nums))
```

**复杂度**: O(N) 时间, O(N) 空间

**易错点**:
- 必须用 set 去重
- 只对序列起点进行检查（num-1 not in set）保证 O(N)
- 注意空数组边界情况（N≥1所以不需处理）

---

## 题目二 题解

### 思路分析
这是一个三维状态的 BFS 最短路径问题。状态 `(x, y, k_used)` 表示在 (x,y) 且已经消除了 k_used 个障碍物。用 `dist[x][y][k+1]` 数组记录最短步数。

当走到障碍物 (grid[nx][ny] == 1) 且 k_used < K 时，可以消除并进入状态 `(nx, ny, k_used + 1)`，步数 +1。
当走到空地 (grid[nx][ny] == 0) 时，直接进入状态 `(nx, ny, k_used)`，步数 +1。

关键: 第一次访问到某个状态时的步数就是最短的（BFS 性质）。

### Python 解法

```python
from collections import deque

def shortest_path(grid, n, m, K):
    INF = float('inf')
    # dist[x][y][k] = 到 (x,y) 且消除了 k 个障碍物的最短步数
    dist = [[[INF] * (K + 1) for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 0

    q = deque([(0, 0, 0)])  # (x, y, k_used)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, k = q.popleft()
        d = dist[x][y][k]

        # 到达终点
        if x == n - 1 and y == m - 1:
            return d

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    # 障碍物，需要消除
                    if k < K and dist[nx][ny][k + 1] == INF:
                        dist[nx][ny][k + 1] = d + 1
                        q.append((nx, ny, k + 1))
                else:
                    # 空地
                    if dist[nx][ny][k] == INF:
                        dist[nx][ny][k] = d + 1
                        q.append((nx, ny, k))

    return -1

if __name__ == "__main__":
    n, m, K = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    print(shortest_path(grid, n, m, K))
```

**复杂度分析**:
- 时间复杂度: O(N × M × K)，每个状态最多访问一次
- 空间复杂度: O(N × M × K)

N,M ≤ 100, K ≤ N×M = 10000，最坏 100×100×10000 = 10^8 状态，可能超内存。

### 优化思路
K 的实际有效值不超过曼哈顿距离或实际需要的消除数。可以用位图或 visited 集合来优化。

另一种优化：使用 Dijkstra（因为边权为1，BFS即可），但将 K 视为资源。

**进一步优化**: K 的有效上限是网格中障碍物数量，但实际不需要超过 N+M（因为最短路径最多需要消除 N+M 个障碍物）。所以令 `K = min(K, n + m)` 可以大幅降低复杂度。

```python
def shortest_path_optimized(grid, n, m, K):
    K = min(K, n + m)  # 有效上限

    from collections import deque

    INF = float('inf')
    dist = [[[INF] * (K + 1) for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 0

    q = deque([(0, 0, 0)])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, k = q.popleft()
        d = dist[x][y][k]

        if x == n - 1 and y == m - 1:
            return d

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:
                    if k < K and dist[nx][ny][k + 1] == INF:
                        dist[nx][ny][k + 1] = d + 1
                        q.append((nx, ny, k + 1))
                else:
                    if dist[nx][ny][k] == INF:
                        dist[nx][ny][k] = d + 1
                        q.append((nx, ny, k))

    return -1
```

优化后复杂度: O(N × M × min(K, N+M)) ≤ 100×100×200 = 2×10^6，非常安全。

**另一种思路**: 0-1 BFS（但这里所有边权都是1，直接用 BFS 就行）

### 易错点
- K 可能为 0，此时不能消除任何障碍物
- 起点或终点本身就是障碍物（题目一般保证起点为0）
- dist 数组维度为 [N][M][K+1]，K 较大时注意内存
- BFS 到达终点时直接返回，不一定需要处理完所有状态

---

# 模考复盘
| 项目 | 建议 |
|------|------|
| 100分题 | 30分钟内完成，用 set 去重 + 只检查起点 |
| 200分题 | 不要被"消除障碍物"吓到，本质是三维 BFS |
| 时间管理 | 200分题如果 45 分钟无进展，先检查简单边界条件 |
| 常见失误 | K 过大导致内存溢出，加 min(K, N+M) 优化 |

**分数预估**: 100分题全对 + 200分题部分正确 → 200~250分


---

# Day 56 — 🏁 终极冲刺
## 11大算法模板 + 高频易错 + Python速查 + 考前Checklist

---

# 目录
1. [11核心算法模板速查](#1-11核心算法模板速查)
2. [OD高频易错点](#2-od高频易错点)
3. [Python速查](#3-python速查)
4. [考前Checklist](#4-考前checklist)
5. [复杂度速查表](#5-复杂度速查表)

---

# 1. 11核心算法模板速查

## 1.1 DFS (深度优先搜索)

### 树/图的DFS
```python
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

### 网格DFS (岛屿问题)
```python
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = 0  # 标记已访问
    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
        dfs(grid, i + di, j + dj)
```

### 排列/组合 DFS (回溯)
```python
def permute(nums):
    res, path, used = [], [], [False] * len(nums)
    def dfs():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False
    dfs()
    return res
```

---

## 1.2 BFS (广度优先搜索)

### 最短路径 (无权图)
```python
from collections import deque

def bfs(start, target):
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == target:
                return steps
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        steps += 1
    return -1
```

### 多源BFS (如感染/腐烂问题)
```python
def multi_source_bfs(grid):
    q = deque()
    fresh = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    # ... BFS 同标准模板
```

---

## 1.3 二分查找

### 标准二分
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 左边界/右边界
```python
def lower_bound(nums, target):  # 第一个 ≥ target 的位置
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(nums, target):  # 第一个 > target 的位置
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left
```

### 浮点数二分
```python
def float_binary_search():
    lo, hi = 0.0, 1e9
    for _ in range(100):  # 固定迭代次数
        mid = (lo + hi) / 2
        if check(mid):
            hi = mid
        else:
            lo = mid
    return lo
```

---

## 1.4 滑动窗口

### 定长窗口
```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### 可变窗口 (求满足条件的最长/最短)
```python
def min_window(s, t):
    """最小覆盖子串"""
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = 0
    min_len = float('inf')
    start = 0

    for right, ch in enumerate(s):
        if ch in need:
            need[ch] -= 1
            if need[ch] >= 0:
                missing -= 1

        while missing == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            left_ch = s[left]
            if left_ch in need:
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
            left += 1

    return s[start:start + min_len] if min_len != float('inf') else ""
```

### 滑动窗口通用框架
```python
left = 0
for right in range(len(arr)):
    # 右移窗口，加入 arr[right]
    while not_ok():  # 窗口不满足条件
        # 移除 arr[left]
        left += 1
    # 更新答案 (此时窗口满足条件)
```

---

## 1.5 动态规划 (4大模式)

### 模式1: 线性DP (最长递增子序列)
```python
def length_of_LIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

**优化 (二分)**: `tails[k]` 表示长度为 k+1 的 LIS 的最小结尾值。

```python
def length_of_LIS_optimized(nums):
    tails = []
    for num in nums:
        i = 0
        j = len(tails)
        while i < j:
            mid = (i + j) // 2
            if tails[mid] < num:
                i = mid + 1
            else:
                j = mid
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)
```

### 模式2: 区间DP (回文/合并)
```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
```

### 模式3: 背包DP
```python
# 0-1背包 (每个物品取一次)
def zero_one_knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(W, w - 1, -1):  # 从大到小
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]

# 完全背包 (每个物品取无限次)
def complete_knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(w, W + 1):  # 从小到大
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]

# 多重背包 (每个物品有限次)
def multiple_knapsack(weights, values, counts, W):
    dp = [0] * (W + 1)
    for w, v, c in zip(weights, values, counts):
        # 二进制优化
        k = 1
        while k <= c:
            for j in range(W, k * w - 1, -1):
                dp[j] = max(dp[j], dp[j - k * w] + k * v)
            c -= k
            k <<= 1
        if c > 0:
            for j in range(W, c * w - 1, -1):
                dp[j] = max(dp[j], dp[j - c * w] + c * v)
    return dp[W]
```

### 模式4: 状态压缩DP (TSP/子集)
```python
# 示例: 最短Hamilton路径 (TSP)
def tsp(dist, n):
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # 从0出发，状态为只访问了0
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask >> u) & 1:
                continue
            for v in range(n):
                if (mask >> v) & 1:
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
    return min(dp[(1 << n) - 1][i] + dist[i][0] for i in range(1, n))
```

---

## 1.6 并查集 (Union-Find)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # 按秩合并
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]
```

**应用**: 连通分量、最小生成树(Kruskal)、冗余连接

---

## 1.7 前缀树 (Trie)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # 经过该节点的单词数

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, word):
        """删除单词（假设存在）"""
        def _delete(node, word, i):
            if i == len(word):
                node.is_end = False
                return
            ch = word[i]
            _delete(node.children[ch], word, i + 1)
            node.children[ch].count -= 1
            if node.children[ch].count == 0:
                del node.children[ch]

        _delete(self.root, word, 0)
```

**应用**: 单词搜索、自动补全、前缀匹配、最大XOR对

---

## 1.8 单调栈

### 下一个更大元素
```python
def next_greater_element(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # 存索引
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
    return res
```

### 接雨水
```python
def trap(height):
    stack = []
    water = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            h = min(height[left], height[i]) - height[bottom]
            water += width * h
        stack.append(i)
    return water
```

### 柱状图中最大矩形
```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights = [0] + heights + [0]  # 哨兵
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
```

**核心思想**: 栈内保持单调递增/递减，遇到破坏单调性的元素时出栈计算。

---

## 1.9 回溯 (Backtracking)

```python
def backtrack(candidates, target):
    res = []

    def dfs(path, remaining, start):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            # 剪枝: 同层相同值跳过 (避免重复组合)
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            dfs(path, remaining - candidates[i], i + 1)  # i+1: 不能重复使用
            path.pop()

    candidates.sort()
    dfs([], target, 0)
    return res
```

### 回溯通用模板
```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        if 选择不合法: continue
        做选择
        backtrack(新路径, 新选择列表)
        撤销选择
```

---

## 1.10 排序 + 双指针

### 两数之和 (排序后)
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

### 三数之和
```python
def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res
```

### 接雨水 (双指针法)
```python
def trap_two_pointer(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```

---

## 1.11 拓扑排序 (Kahn算法)

```python
from collections import deque

def topological_sort(n, edges):
    indegree = [0] * n
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return result if len(result) == n else []  # 有环返回空
```

---

# 2. OD高频易错点

## 2.1 输入解析陷阱

```
# ❌ 错误: 忘记 strip
n = int(input())

# ✅ 正确:
n = int(input().strip())

# ❌ 错误: 多空格情况
# 输入: "1   2   3"
# list(map(int, input().split()))  ✅ 自动处理多空格

# ⚠️ 行数不定时的读取
lines = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        # 有时用哨兵值判断结束
        a, b = map(int, line.split())
        if a == -1 and b == -1:
            break
        lines.append((a, b))
    except EOFError:
        break
```

## 2.2 边界条件

```
# 需要特别检查的边界:
1. N=1 的情况 (单元素数组、单节点树)
2. 空数组/空图
3. 最大值/最小值约束 (int溢出? Python不用担心)
4. 负数的处理
5. 完全无序/完全有序的输入
6. 所有元素相等
7. K=0 的情况 (如消除障碍物)
8. 目标在起点/终点
```

## 2.3 超时/内存溢出规避

```
# 常见超时原因及解决方案:
1. O(N²) 暴力 → 改为 O(N log N) 或 O(N)
2. DFS 递归过深 → 改为 BFS 或迭代
3. 重复计算 → 加缓存 (lru_cache / memo)
4. 频繁字符串拼接 → 用 list + ''.join()
5. 大量数据排序 → 用计数排序/内置 sorted()

# Python 性能建议:
- 用 sys.stdin.read() 一次读取所有输入
- 避免在循环内 import
- 局部变量引用加速 (local_var = global_var)
- 用 set/dict 代替 list 做查找
- 列表推导式优于 for+append
```

## 2.4 特殊输入格式

```
# 1. 矩阵读取
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 2. 树结构 (类似: 父节点列表, 子节点列表)
parent = list(map(int, input().split()))  # parent[i] 是节点i的父节点

# 3. 多个测试用例
T = int(input())
for _ in range(T):
    n = int(input())
    # 处理每个用例

# 4. 图 (节点编号从1开始)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 索引从1开始
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
```

## 2.5 常见逻辑错误

```
# 1. 0-index vs 1-index 混用
# 解决: 统一使用 0-index，输入时减1

# 2. BFS 忘记标记已访问
# 解决: 入队时就标记，不要出队时标记

# 3. DP 数组维度和初始化错误
# 解决: 画DP表格明确维度含义

# 4. 并查集忘记路径压缩
# 解决: find 函数必须带路径压缩

# 5. 回溯忘记剪枝导致超时
# 解决: 排序 + 同层去重 + 可行性剪枝
```

---

# 3. Python速查

## 3.1 常用内置函数

```python
# 数学
abs(x)           # 绝对值
max/min(iter)    # 最大/最小值
sum(iter)        # 求和
pow(x, y, mod)   # 快速幂取模
divmod(a, b)     # (a//b, a%b)
round(x, n)      # 四舍五入到n位小数

# 类型转换
int(x, base=10)  # 字符串转整数，支持进制
ord(ch)          # 字符转ASCII码
chr(code)        # ASCII码转字符
bin(x)           # 转二进制字符串 '0b101'
hex(x)           # 转十六进制
list(map(int, s.split()))  # 字符串列表转整数列表

# 迭代工具
all(iter)        # 所有元素为True
any(iter)        # 任意元素为True
enumerate(iter)  # (index, value) 迭代
zip(*iterables)  # 并行迭代多个可迭代对象
sorted(iter, key=..., reverse=True)  # 排序
reversed(seq)    # 反转序列
filter(func, iter)  # 过滤
map(func, iter)     # 映射
```

## 3.2 collections 模块

```python
from collections import Counter, defaultdict, deque, OrderedDict

# Counter — 计数
cnt = Counter("aabbbcc")
cnt.most_common(2)   # [('b', 3), ('a', 2)]
cnt['a'] += 1        # 增加计数
list(cnt.elements()) # 展开为列表

# defaultdict — 自动默认值
d = defaultdict(list)   # d[x].append(y) 无需初始化
d = defaultdict(int)    # d[x] += 1 无需初始化
d = defaultdict(set)    # d[x].add(y) 无需初始化

# deque — 双端队列 O(1) 两端操作
q = deque()
q.append(x)       # 右端添加
q.appendleft(x)   # 左端添加
q.pop()           # 右端弹出
q.popleft()       # 左端弹出
q.rotate(k)       # 循环右移k步

# OrderedDict — 有序字典 (Python 3.7+ dict已有序)
od = OrderedDict()
od.move_to_end(key)  # 将key移到末尾
```

## 3.3 itertools 模块

```python
from itertools import permutations, combinations, product, accumulate, chain, groupby

# 排列: 所有可能的排列
list(permutations([1,2,3], 2))  # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 组合: 所有可能的组合
list(combinations([1,2,3], 2))  # [(1,2),(1,3),(2,3)]

# 笛卡尔积
list(product([1,2], ['a','b']))  # [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

# 前缀和
list(accumulate([1,2,3,4]))  # [1, 3, 6, 10]

# 展平嵌套列表
list(chain.from_iterable([[1,2],[3,4]]))  # [1,2,3,4]

# 分组
for key, group in groupby(sorted(data)):
    print(key, list(group))
```

## 3.4 堆 (heapq)

```python
import heapq

# 默认最小堆
heap = []
heapq.heappush(heap, 5)      # 入堆
smallest = heapq.heappop(heap)  # 出堆

# 最大堆: 存负数
heapq.heappush(heap, -x)
max_val = -heapq.heappop(heap)

# 取前K大/小
heapq.nlargest(k, iterable)  # 前K大
heapq.nsmallest(k, iterable) # 前K小

# 堆化
heapq.heapify(list_)  # O(N) 建堆
```

## 3.5 位运算速查

```python
# 常用位操作
x & (x - 1)          # 清除最低位的1
x & -x               # 取最低位的1
(x >> i) & 1         # 取第i位
x | (1 << i)         # 设置第i位为1
x & ~(1 << i)        # 设置第i位为0
x ^ (1 << i)         # 翻转第i位
x.bit_count()        # Python 3.8+: 二进制中1的个数
x.bit_length()       # 二进制位数

# 枚举子集
mask = 0b1011
sub = mask
while sub:
    # 处理子集 sub
    sub = (sub - 1) & mask

# 判断是否为2的幂
x > 0 and (x & (x - 1)) == 0
```

## 3.6 性能加速技巧

```python
# 1. 一次性读取所有输入
import sys
data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))

# 2. 大数组用数组模块
from array import array
arr = array('i', [0]) * 1000000  # 比 list 省内存

# 3. 递归限制
import sys
sys.setrecursionlimit(1000000)

# 4. lru_cache 自动记忆化
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# 5. 三元表达式
res = a if condition else b

# 6. 快速交换
a, b = b, a

# 7. 去重保持顺序
list(dict.fromkeys(items))
```

---

# 4. 考前Checklist

## 4.1 考前24小时

```
✅ 复习11个算法模板 (15分钟过一遍)
✅ 刷2-3道手感题 (热手)
✅ 准备环境:
   - Python 版本确认 (3.8+)
   - IDE/编辑器打开并测试
   - 输入输出测试 (print/input)
✅ 休息:
   - 保证7小时睡眠
   - 设好闹钟
   - 提前30分钟到考场
```

## 4.2 考试中时间管理

```
┌──────────────────────────────────────────────┐
│           90分钟考试时间分配                    │
├──────────────────────────────────────────────┤
│ 0-5min   通读所有题目，标记难度                │
│ 5-35min  做第1题 (100分)                     │
│ 35-40min 休息+饮水+检查第1题                  │
│ 40-80min 做第2题 (200分)                     │
│ 80-90min 检查所有题目+边界条件                │
└──────────────────────────────────────────────┘

遇到卡壳超过15分钟 → 先跳过做下一题
至少留5分钟最后检查
```

## 4.3 做题步骤模板

```
1️⃣ 读题 (2min)
   - 输入输出格式
   - 数据范围 (N, M, K)
   - 时间限制/空间限制

2️⃣ 选算法 (3min)
   - 暴力能否过? (N ≤ 1000 可接受 O(N²))
   - 需要优化? (N ≥ 10^5 需要 O(N) 或 O(N log N))
   - 匹配算法模板

3️⃣ 写代码 (15-20min)
   - 先写输入输出框架
   - 再写核心逻辑
   - 最后加边界处理

4️⃣ 测试 (5min)
   - 跑样例
   - 测边界 (N=1, K=0, 空, 全等)
   - 测极端情况 (最大N, 最大K)
```

## 4.4 常见考试策略

```
✅ DO:
- 先做100分题，保底
- 用 print 调试
- 局部变量优化速度
- 复杂度过不去时尝试空间换时间

❌ DON'T:
- 不要在一个题上死磕超过30分钟
- 不要忘记 import 模块
- 不要忘记处理多测试用例
- 不要提交前忘记去掉调试代码
- 不要用 input() 在循环中读大数据 (用 sys.stdin.read)
```

## 4.5 考前最后10分钟

```
📋 快速检查:
□ 所有 import 都已写
□ 函数定义在调用之前
□ 递归深度没超限
□ 大数组没有 O(N²) 空间
□ 索引没有越界
□ 0-index vs 1-index 一致
□ 负数/空值/边界已处理
□ 变量名没有拼写错误
□ 所有分支都有 return
□ 样例通过
```

---

# 5. 复杂度速查表

## 5.1 时间复杂度

| 算法 | 平均 | 最坏 | 空间 |
|------|------|------|------|
| 二分查找 | O(log N) | O(log N) | O(1) |
| 快速排序 | O(N log N) | O(N²) | O(log N) |
| 归并排序 | O(N log N) | O(N log N) | O(N) |
| 堆排序 | O(N log N) | O(N log N) | O(1) |
| 计数排序 | O(N + K) | O(N + K) | O(K) |
| DFS/BFS | O(V + E) | O(V + E) | O(V) |
| Dijkstra | O((V+E) log V) | O((V+E) log V) | O(V) |
| Floyd | O(V³) | O(V³) | O(V²) |
| Kruskal | O(E log E) | O(E log E) | O(V) |
| Prim | O(E log V) | O(E log V) | O(V) |
| KMP | O(N + M) | O(N + M) | O(M) |
| 并查集 | O(α(N)) | O(α(N)) | O(N) |

## 5.2 数据规模与可行算法速判

```
N ≤ 20      → O(2^N), O(N!)      → 状态压缩/回溯
N ≤ 100     → O(N³)              → Floyd/区间DP
N ≤ 1000    → O(N²)              → 暴力/两层循环DP
N ≤ 10^5    → O(N log N)         → 排序/二分/堆
N ≤ 10^6    → O(N)               → 线性扫描/哈希
N ≤ 10^8    → O(log N)           → 数学公式/二分
```

## 5.3 Python操作复杂度

| 操作 | 复杂度 |
|------|--------|
| list[i] 访问/赋值 | O(1) |
| list.append/pop | O(1) 均摊 |
| list.pop(i) / insert | O(N) |
| list.index / in | O(N) |
| set/dict in 操作 | O(1) 均摊 |
| set/dict add/remove | O(1) 均摊 |
| str + 拼接 | O(N) |
| str.join(list) | O(N) |
| sorted(list) | O(N log N) |
| heapq.heappush/pop | O(log N) |
| deque.popleft/append | O(1) |
| collections.Counter | O(N) |

## 5.4 常见N值对应极限运算量

| N | O(N) | O(N log N) | O(N²) | O(N³) | O(2^N) |
|---|------|------------|-------|-------|--------|
| 10 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 100 | ✓ | ✓ | ✓ | ✓ | ✗ |
| 1,000 | ✓ | ✓ | ✓ | ✗ | ✗ |
| 10,000 | ✓ | ✓ | ✗ | ✗ | ✗ |
| 100,000 | ✓ | ✓ | ✗ | ✗ | ✗ |
| 1,000,000 | ✓ | ✗ | ✗ | ✗ | ✗ |

---

# 📌 最后的话

> **OD考试核心三要素:**
> 1. **读题准**— 理解输入输出，确认数据范围
> 2.**选对法**— 匹配算法模板，不追求最优解，追求可过解
> 3.**写得稳**— 边界处理，0-index统一，输入输出格式正确
>
>**心态:**
> - 100分题保底，200分题冲刺
> - 卡壳15分钟就跳过
> - 留5分钟检查边界
>
> **祝考试顺利！🎉**

---

*本文件是 Week 8 终极冲刺复习资料，涵盖了OD考试所需的全部核心知识点。*


---

