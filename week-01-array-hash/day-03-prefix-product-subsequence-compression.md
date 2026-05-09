# Day 03: 前缀积 / 子序列 / 压缩

## 📖 知识点讲解

### 前缀积 + 后缀积

计算"除自身外"的乘积时，用两个数组分别记录前缀积和后缀积：

```python
def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n   # prefix[i] = nums[0] * ... * nums[i-1]
    suffix = [1] * n   # suffix[i] = nums[i+1] * ... * nums[n-1]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]
    
    return [prefix[i] * suffix[i] for i in range(n)]
```

**空间优化**：用一个输出数组先存前缀积，第二次遍历时用变量动态维护后缀积。

### 贪心判断递增三元组

维护两个变量 `first`（最小值）和 `second`（第二小值），遍历时更新：
- 如果当前值 <= first，更新 first
- 否则如果当前值 <= second，更新 second
- 否则说明找到了第三大的数 → 存在递增三元组

### 双指针原地压缩

```python
def compress(chars):
    write = 0   # 写入位置
    read = 0    # 读取位置
    while read < len(chars):
        ch = chars[read]
        count = 0
        while read < len(chars) and chars[read] == ch:
            read += 1
            count += 1
        chars[write] = ch
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write  # 新长度
```

---

## 🧩 刷题任务

### 题目1：Product of Array Except Self（除自身以外数组的乘积）
**难度**：⭐⭐
**题目描述**：
给你一个整数数组 `nums`，返回数组 `answer`，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积。题目保证所有前缀积和后缀积都在 32 位整数范围内。**请不要使用除法**，且在 O(n) 时间内完成。

**思路分析**：
1. 创建结果数组 `answer`，长度与 `nums` 相同
2. 第一遍遍历：`answer[i]` 存储 `nums[0]` 到 `nums[i-1]` 的积（左前缀积）
3. 第二遍遍历：用变量 `R` 维护右侧后缀积，从右向左更新 `answer[i] *= R`，然后 `R *= nums[i]`

- 时间复杂度：O(n)
- 空间复杂度：O(1)（不计输出空间）

**参考代码**：
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # 左前缀积
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # 右后缀积，动态维护
        R = 1
        for i in range(n-1, -1, -1):
            answer[i] *= R
            R *= nums[i]
        
        return answer
```

---

### 题目2：Increasing Triplet Subsequence（递增三元子序列）
**难度**：⭐⭐
**题目描述**：
给你一个整数数组 `nums`，判断是否存在长度为 3 的递增子序列（下标 `i < j < k` 且 `nums[i] < nums[j] < nums[k]`）。要求时间复杂度 O(n)，空间复杂度 O(1)。

**思路分析**：
维护两个变量：
- `first`：当前遇到的最小值
- `second`：当前遇到的大于 `first` 的最小值
遍历数组：
1. 如果 `num <= first`：更新 `first = num`
2. 否则如果 `num <= second`：更新 `second = num`
3. 否则（`num > second > first`）：找到递增三元组，返回 True

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num          # 最小
            elif num <= second:
                second = num         # 第二小（比 first 大）
            else:
                return True          # 找到了第三大的
        return False
```

---

### 题目3：String Compression（压缩字符串）
**难度**：⭐⭐
**题目描述**：
给你一个字符数组 `chars`，请使用原地算法压缩：将连续重复字符替换为"字符+出现次数"。如果只有 1 个，则只保留字符。返回压缩后的新长度。不要使用额外空间，必须原地修改输入数组。

**思路分析**：
使用双指针：
- `read` 指针：遍历原数组，统计连续相同字符的个数
- `write` 指针：指向当前写入位置
遍历过程中，读取字符，统计个数，写入字符和（如果大于1）数字部分。

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # 写入位置
        read = 0   # 读取位置
        
        while read < len(chars):
            ch = chars[read]
            count = 0
            # 统计连续相同字符数量
            while read < len(chars) and chars[read] == ch:
                read += 1
                count += 1
            
            # 写入字符
            chars[write] = ch
            write += 1
            
            # 如果计数大于1，写入数字
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
```
