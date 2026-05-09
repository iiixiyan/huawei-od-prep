# Day 33: 回溯进阶

## 📖 知识点
**进阶回溯技巧**:
- **子集枚举**: 每个元素选或不选,或使用循环+start.
- **可重复使用元素**: 递归时start不变(Combination Sum).
- **不可重复使用+去重**: start+1 + 排序剪枝(Combination Sum II).
- **棋盘/矩阵搜索**: 方向数组+visited或原地修改(Word Search).
- **分割问题**: 在不同位置切分,验证合法性(Restore IP).

## 🧩 刷题任务（6题）

### 1. Subsets（⭐⭐） 来源：O
**思路**：枚举所有子集.每个元素有选与不选两种选择,回溯穷举.
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

### 2. Combination Sum（⭐⭐） 来源：T150/O
**思路**：从candidates中选可重复使用的元素求和为target.回溯时start位置不变(可重复选),当前和超过target剪枝.
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

### 3. Combination Sum II（⭐⭐） 来源：O
**思路**：每个元素只能用一次+有重复.先排序,同层跳过重复元素,递归时start+1.
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

### 4. N-Queens II（⭐⭐⭐） 来源：T150
**思路**：回溯放置皇后.用三个集合记录被占用的列、主对角线(row-col)、副对角线(row+col).每行放一个皇后,DFS所有行.
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

### 5. Word Search（⭐⭐⭐） 来源：T150
**思路**：在网格中回溯搜索单词.从每个匹配首字母的位置出发,四方向DFS,已使用的字母标记为'#'避免重复使用.
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

### 6. Restore IP Addresses（⭐⭐） 来源：O
**思路**：分割字符串为4段合法IP.回溯在s的不同位置切割,每段需在0~255且无前导零(除非为0).
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
