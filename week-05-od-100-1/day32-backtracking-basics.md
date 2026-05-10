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

### 1. Letter Combinations of a Phone Number（⭐⭐） 来源：L75/T150
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

- `1 <= digits.length <= 4`

- `digits[i]` 是范围 `['2', '9']` 的一个数字。

**难度**：中等
**思路**：数字到字母映射,回溯生成所有组合.每次选择一个字母,递归处理下一个数字.
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

### 2. Combinations（⭐⭐） 来源：T150/O
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

- `1 <= n <= 20`

- `1 <= k <= n`

**难度**：中等
**思路**：从1~n中选k个数的组合.回溯时限制起始位置避免重复组合.
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

### 3. Combination Sum III（⭐⭐） 来源：L75
**题目**：找出所有相加之和为 `n`* *的 `k`** **个数的组合，且满足下列条件：

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

- `2 <= k <= 9`

- `1 <= n <= 60`

**难度**：中等
**思路**：从1~9中选k个数,和为n.回溯+剪枝:当前和超过n或可选数不够时提前返回.
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

### 4. Permutations（⭐⭐） 来源：T150/O
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

- `1 <= nums.length <= 6`

- `-10 <= nums[i] <= 10`

- `nums` 中的所有整数 **互不相同**

**难度**：中等
**思路**：全排列回溯.用used数组标记已选元素,每次从未选元素中选择.
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

### 5. Permutations II（⭐⭐） 来源：O
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

- `1 <= nums.length <= 6`

- `-10 <= nums[i] <= 10`

- `nums` 中的所有整数 **互不相同**

**难度**：中等
**思路**：含重复元素的全排列.先排序,剪枝条件:同一层中跳过重复元素(i>0且nums[i]==nums[i-1]且used[i-1]为False).
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

### 6. Generate Parentheses（⭐⭐） 来源：T150/O
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

- `1 <= n <= 8`

**难度**：中等
**思路**：回溯生成合法括号对.维护左括号和右括号计数,保证任何时刻左括号数≥右括号数.
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
