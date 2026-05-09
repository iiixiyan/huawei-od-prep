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
