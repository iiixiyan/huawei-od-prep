# Day 01: 数组基础操作

## 📖 知识点
**双指针原地操作**：在数组问题中，双指针技巧常用于原地修改数组，避免额外空间。两个指针从不同位置遍历，一个指向"当前写入位置"，另一个指向"当前读取位置"，在不使用额外数组的情况下完成元素删除、去重、合并等操作。

核心模式：
- **读写指针**：`slow` 指向已处理部分的末尾，`fast` 遍历整个数组
- **头尾指针**：左右夹逼，常用于有序数组的合并或交换
- **同向双指针**：两个指针同向移动，速度不同

## 🧩 刷题任务（6题）

### 1. 交替合并字符串（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/merge-strings-alternately/)
**难度**：简单
**题目**：给你两个字符串 `word1` 和 `word2` 。请你从 `word1` 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。


返回 **合并后的字符串** 。


 


**示例 1：**


输入：word1 = "abc", word2 = "pqr"
输出："apbqcr"
解释：字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r

**示例 2：**


输入：word1 = "ab", word2 = "pqrs"
输出："apbqrs"
解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
word1：  a   b
word2：    p   q   r   s
合并后：  a p b q   r   s

**示例 3：**


输入：word1 = "abcd", word2 = "pq"
输出："apbqcd"
解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
word1：  a   b   c   d
word2：    p   q
合并后：  a p b q c   d

 


**提示：**

- `1
**思路**：双指针分别遍历两个字符串，交替取字符拼接。当指针越界时，将剩余部分直接追加到结果末尾。
**代码**：
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
**来源**：[LeetCode](https://leetcode.cn/problems/merge-sorted-array/)
**难度**：简单
**题目**：给你两个按 **非递减顺序** 排列的整数数组 `nums1`* *和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。


请你 **合并** `nums2`* *到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。


**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。


**示例 1：**


输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

**示例 2：**


输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

**示例 3：**


输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。


**提示：**

- `nums1.length == m + n`

- `nums2.length == n`

- `0 9 9`


**进阶：**你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？
**思路**：从后往前遍历，将较大的元素放到 nums1 末尾。三个指针：`p1=nums1有效末尾`、`p2=nums2末尾`、`p=合并后的末尾`。避免了从前往后需要移动大量元素的 O(n²) 问题。
**代码**：
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
    # 如果 nums2 还有剩余，复制过去
    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]
```
### 3. 移除元素（⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/remove-element/)
**难度**：简单
**题目**：给你一个数组 `nums`* *和一个值 `val`，你需要 **原地** 移除所有数值等于 `val`* *的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。


假设 `nums` 中不等于 `val` 的元素数量为 `k`，要通过此题，您需要执行以下操作：

- 更改 `nums` 数组，使 `nums` 的前 `k` 个元素包含不等于 `val` 的元素。`nums` 的其余元素和 `nums` 的大小并不重要。

- 返回 `k`。

**用户评测：**


评测机将使用以下代码测试您的解决方案：


int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
// 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i
- `0
**思路**：快慢指针。`slow` 指向下一个待写入位置，`fast` 遍历数组。当 `nums[fast] != val` 时，将 `nums[fast]` 复制到 `nums[slow]`，并 `slow += 1`。最终 `slow` 即为新数组长度。
**代码**：
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
**来源**：[LeetCode](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)
**难度**：简单
**题目**：给你一个 **非严格递增排列** 的数组 `nums` ，请你** 原地** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。


考虑 `nums` 的唯一元素的数量为 `k`。去重后，返回唯一元素的数量 `k`。


`nums` 的前 `k` 个元素应包含 **排序后** 的唯一数字。下标 `k - 1` 之后的剩余元素可以忽略。


**判题标准:**


系统会用下面的代码来测试你的题解:


int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i
- `1 4`

- `-100 0`

- `nums` 已按 **非递减** 顺序排列。
**思路**：快慢指针。`slow` 指向已去重部分的末尾，`fast` 遍历。当 `nums[fast] != nums[slow-1]` 时，说明遇到新元素，写入 `nums[slow]` 并移动 `slow`。因为数组已有序，相同元素必然相邻。
**代码**：
**代码**：
```python
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 1  # 第一个元素默认保留
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```
### 5. 删除有序数组中的重复项 II（⭐⭐⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)
**难度**：简单
**题目**：给你一个 **非严格递增排列** 的数组 `nums` ，请你** 原地** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。


考虑 `nums` 的唯一元素的数量为 `k`。去重后，返回唯一元素的数量 `k`。


`nums` 的前 `k` 个元素应包含 **排序后** 的唯一数字。下标 `k - 1` 之后的剩余元素可以忽略。


**判题标准:**


系统会用下面的代码来测试你的题解:


int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i
- `1 4`

- `-100 0`

- `nums` 已按 **非递减** 顺序排列。
**思路**：在 I 的基础上允许每个元素最多出现两次。用 `slow` 指向下一个写入位置，判断条件改为 `nums[fast] != nums[slow-2]`。因为如果 `nums[slow-2] == nums[fast]`，说明已经有至少两个相同元素了。
**代码**：
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
**来源**：[LeetCode](https://leetcode.cn/problems/majority-element/)
**难度**：简单
**题目**：给定一个大小为 `n`* *的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。


你可以假设数组是非空的，并且给定的数组总是存在多数元素。


**示例 1：**


输入：nums = [3,2,3]
输出：3

**示例 2：**


输入：nums = [2,2,1,1,1,2,2]
输出：2


**提示：**


- `n == nums.length`

- `1 4`

- `-109 9`

- 输入保证数组中一定有一个多数元素。


**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
**思路**：**Boyer-Moore 投票算法**。核心思想：不同元素相互抵消。维护一个 `candidate` 和 `count`。遍历时如果 `count == 0`，选当前元素为 candidate；遇到相同元素 count+1，不同则 count-1。最终 candidate 即为多数元素（因为题目保证多数元素的出现次数 > n/2）。
**代码**：
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
