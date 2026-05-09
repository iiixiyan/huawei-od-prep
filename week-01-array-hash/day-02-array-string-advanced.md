# Day 02: Array/String 进阶

## 📖 知识点讲解

### 贪心策略在数组中的应用

贪心（Greedy）指每一步都选择当前最优解，从而期望得到全局最优。适用条件：**局部最优能推出全局最优**。

典型特征：
- 从左到右遍历，根据当前状态做决策
- 通常只需 O(n) 一次扫描
- 常与"是否可行"类问题结合

### 双指针原地交换

```python
# 双指针原地交换模板（反转/筛选）
left, right = 0, len(arr) - 1
while left < right:
    # 根据条件移动指针或交换
    if condition(left):
        left += 1
    elif condition(right):
        right -= 1
    else:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

### 单词反转思路

"先整体反转，再局部反转" 是处理单词顺序反转的经典范式：
1. 去除多余空格
2. 反转整个字符串
3. 反转每个单词

---

## 🧩 刷题任务

### 题目1：Can Place Flowers（种花问题）
**难度**：⭐⭐
**题目描述**：
你有一个花坛，由 `n` 个位置组成，用 `flowerbed` 数组表示（0 表示空，1 表示已种花）。相邻位置不能同时种花。给定 `n` 朵新花，判断能否在不打破规则的情况下种下所有花。

**思路分析**：
贪心策略：从左到右遍历，如果当前位置为空（0）且前后也为空，就种花（`flowerbed[i] = 1`），计数加1。
- 边界处只需检查一侧
- 提前终止：当种花数 >= n 时返回 True

- 时间复杂度：O(n)
- 空间复杂度：O(1)

**参考代码**：
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # 检查当前位置是否可以种花
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
```

---

### 题目2：Reverse Vowels of a String（反转字符串中的元音字母）
**难度**：⭐
**题目描述**：
给你一个字符串 `s`，仅反转字符串中的所有元音字母（a, e, i, o, u，包含大小写），其他字符位置不变。

**思路分析**：
1. 将字符串转为字符列表
2. 双指针 `left` 从左向右、`right` 从右向左移动
3. 各找到一个元音后交换，继续移动
4. 最后将列表转回字符串

- 时间复杂度：O(n)
- 空间复杂度：O(n)（Python 字符串不可变，需要列表）

**参考代码**：
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1
        
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            # 交换元音
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        return ''.join(chars)
```

---

### 题目3：Reverse Words in a String（反转字符串中的单词）
**难度**：⭐⭐
**题目描述**：
给你一个字符串 `s`，反转字符串中单词的顺序。注意：单词间可能有多个空格，结果中单词间应只保留一个空格，且无首尾空格。

**思路分析**：
方法一（Pythonic）：`split` 分割 → 反转列表 → `join`
方法二（手写双指针）：
1. 去除首尾空格
2. 从后向前遍历，用双指针提取单词
3. 添加到结果列表后 join

- 时间复杂度：O(n)
- 空间复杂度：O(n)

**参考代码**：
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Python 一行解法
        return ' '.join(s.split()[::-1])
        
    def reverseWords_manual(self, s: str) -> str:
        """手写双指针法"""
        words = []
        i = len(s) - 1
        
        while i >= 0:
            # 跳过空格
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            # 找到单词起始位置
            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1
            words.append(s[j + 1:i + 1])
            i = j
        
        return ' '.join(words)
```
