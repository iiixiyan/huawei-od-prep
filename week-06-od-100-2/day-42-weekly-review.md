# Day 42: 周复习 — 错题复盘 + 小测

## 📖 本周核心知识图谱

| 数据结构 | 核心算法 | 代表题目 | 掌握程度 |
|---------|---------|---------|---------|
| 矩阵 | 螺旋遍历、Kadane降维 | 螺旋矩阵、最大矩阵和 | ⭐⭐⭐ |
| 图/BFS | 多源BFS、连通分量 | 疫情扩散、服务器广播 | ⭐⭐⭐ |
| 树/DFS | 递归遍历、高度计算 | 三叉搜索树、小家庭 | ⭐⭐ |
| 贪心 | 差值累加、双指针 | 贪心商人、租车骑绿岛 | ⭐⭐⭐ |
| 队列/栈 | 模拟、单调栈 | 打印机队列、括号匹配 | ⭐⭐⭐ |

## 🧩 错题复盘区

### 高频易错点1：矩阵扩散中天数统计
```python
# ❌ 错误：天数在出队时统计，导致多算一天
days = 0
while q:
    x, y = q.popleft()
    days += 1  # 这样不对
    ...

# ✅ 正确：在入队时记录天数
q.append((nx, ny, d + 1))
# 然后取所有 d 的最大值
```

### 高频易错点2：贪心商人——只交易一次 vs 多次
```python
# 只交易一次（找最低买最高卖）
def max_profit_once(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit

# 多次交易（本题）——累加所有上坡
def max_profit_multi(prices):
    return sum(max(0, prices[i+1] - prices[i]) for i in range(len(prices)-1))
```

### 高频易错点3：括号匹配栈空检查
```python
# ❌ 忘记检查栈空
for ch in s:
    if ch in ')]}':
        if pairs[ch] != stack[-1]:  # 可能 IndexError
            ...
        stack.pop()

# ✅ 先检查栈空
for ch in s:
    if ch in ')]}':
        if not stack or stack[-1] != pairs[ch]:
            return -1
        stack.pop()
```

### 高频易错点4：树节点编号从1开始
```python
# 题目中节点编号从1开始，数组从0开始
# ❌ 错误
wealth[child]  # 如果 child=1，实际对应 wealth[0]

# ✅ 正确
wealth[child - 1]
```

## 🧩 小测 (15分钟限时)

### 第1题（2分）
螺旋矩阵的边界收缩法中，填充完上边界后应该：
A. top++  B. top--  C. bottom++  D. left++
<details>
<summary>答案</summary>
A. top++，因为上边界已经填完，需要向下收缩
</details>

### 第2题（2分）
以下哪些题目适合用多源BFS解决？
A. 矩阵扩散  B. 服务器连通分量  C. 查字典  D. 括号匹配
<details>
<summary>答案</summary>
A和B。多源BFS适合多个起点同时扩散的场景
</details>

### 第3题（3分）
给定 prices = [7,1,5,3,6,4]，计算多次交易的最大利润：
<details>
<summary>答案</summary>
7。过程：1买5卖赚4，3买6卖赚3，总计7。
</details>

### 第4题（3分）
判断括号字符串 `"{[()]}[{}]"` 的最大深度：
<details>
<summary>答案</summary>
3。栈的最大长度为3（'{','[','('）。
</details>

### 第5题（3分）
以下关于贪心算法的描述，错误的是：
A. 局部最优解一定能得到全局最优解
B. 适合活动选择问题
C. 适合股票多次交易问题
D. 需要证明贪心选择性质
<details>
<summary>答案</summary>
A。贪心不是所有问题都能得到全局最优解，需要满足贪心选择性质和最优子结构。
</details>

### 第6题（4分）
编写一个函数，输入一个 m×n 的01矩阵，输出最大连通1的个数（上下左右连通）。
```python
def max_island_area(grid, m, n):
    # 请补全代码
```
<details>
<summary>答案</summary>

```python
from collections import deque
def max_island_area(grid, m, n):
    visited = [[False]*n for _ in range(m)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                area = 0
                while q:
                    x,y = q.popleft()
                    area += 1
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                max_area = max(max_area, area)
    return max_area
```
</details>

### 第7题（3分）
三叉搜索树中，插入值 new_val = 1200，当前节点值 node.val = 600，插入到哪个子树？
A. left  B. mid  C. right
<details>
<summary>答案</summary>
C. right。因为 1200 > 600 + 500 = 1100。
</details>

## 📊 本周进度检查
- [ ] Day 36: 矩阵操作 — 螺旋矩阵、最大子矩阵和
- [ ] Day 37: 图&BFS — 多源BFS、连通分量
- [ ] Day 38: 树&DFS — 三叉搜索树、小家庭
- [ ] Day 39: 贪心 — 股票利润、分组贪心
- [ ] Day 40: 队列/栈 — 打印机队列、栈合并、括号匹配
- [ ] Day 41: 综合练习 — 找等值元素、单入口区域
- [ ] Day 42: 错题复盘 + 小测 ✅

> **Week 6 学习目标达成**：掌握 OD 100分中矩阵、图、树、贪心、队列/栈五大类题型的核心解法，能独立完成15分钟内 AC 一道模板题。
