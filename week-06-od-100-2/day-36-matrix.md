# Day 36: 矩阵操作 — Spiral Matrix & Matrix Max Sum

## 📖 知识点
**矩阵遍历技巧**：
- **螺旋矩阵（Spiral Matrix）**：按「右→下→左→上」四个方向循环，用 visited 数组或边界收缩法（top/bottom/left/right 指针）控制方向切换
- **矩阵最大子矩阵和**：将二维问题降维成一维最大子数组和（Kadane算法），枚举起始行和结束行，对列做列前缀和压缩
- **矩阵扩散/BFS**：多源BFS模拟逐层扩散，适合"感染"类问题

## 🧩 刷题任务

### 题目1：螺旋数字矩阵 (OD C卷/E卷 100分)
**难度**：⭐⭐
**题目描述**：
给定一个正整数 m 和 n，按顺时针螺旋顺序生成一个 m 行 n 列的矩阵，填充数字 1 到 m*n。

**输入**：
```
m=3, n=3
```
**输出**：
```
1 2 3
8 9 4
7 6 5
```

**思路分析**：
1. 初始化 m×n 矩阵全为 0，设定四个边界 top=0, bottom=m-1, left=0, right=n-1
2. 当前数字 cur=1，循环直到 cur > m*n
3. 从左到右填充上边界(top行)，top++；从上到下填充右边界(right列)，right--；从右到左填充下边界(bottom行)，bottom--；从下到上填充左边界(left列)，left++
4. 每次填充后检查边界是否越界

**参考代码**：
```python
def spiral_matrix(m, n):
    matrix = [[0] * n for _ in range(m)]
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    cur = 1
    max_val = m * n
    while cur <= max_val:
        # left -> right
        for j in range(left, right + 1):
            if cur > max_val: break
            matrix[top][j] = cur
            cur += 1
        top += 1
        # top -> bottom
        for i in range(top, bottom + 1):
            if cur > max_val: break
            matrix[i][right] = cur
            cur += 1
        right -= 1
        # right -> left
        for j in range(right, left - 1, -1):
            if cur > max_val: break
            matrix[bottom][j] = cur
            cur += 1
        bottom -= 1
        # bottom -> top
        for i in range(bottom, top - 1, -1):
            if cur > max_val: break
            matrix[i][left] = cur
            cur += 1
        left += 1
    return matrix

# 测试
m, n = 3, 3
res = spiral_matrix(m, n)
for row in res:
    print(' '.join(map(str, row)))
```

**OD备考提示**：螺旋矩阵是OD常考题，注意边界收缩的顺序和越界检查。建议用 while 循环 + 四个边界变量，比 visited 数组更高效。

---

### 题目2：最大矩阵和 (OD 100分)
**难度**：⭐⭐
**题目描述**：
给定一个 n×m 的整数矩阵（包含负数），找出一个连续子矩阵（非空），使得该子矩阵内所有元素的和最大，输出该最大值。

**输入**：
```
3 4
-2 1 -3 4
-1 2 3 -1
1 1 -3 2
```
**输出**：
```
7
```
（解释：子矩阵 [[2,3],[1,1]] 的和为 7）

**思路分析**：
1. 枚举起始行 top 和结束行 bottom
2. 对每对 (top, bottom)，计算每一列的列和，得到一个一维数组 col_sum
3. 对 col_sum 运行 Kadane 算法求最大子数组和
4. 时间复杂度 O(n²×m)，n≤200 时可通过

**参考代码**：
```python
def max_matrix_sum(matrix, n, m):
    ans = float('-inf')
    for top in range(n):
        col_sum = [0] * m
        for bottom in range(top, n):
            # 累加当前行到col_sum
            for j in range(m):
                col_sum[j] += matrix[bottom][j]
            # Kadane求一维最大子数组和
            cur_max = col_sum[0]
            total = col_sum[0]
            for j in range(1, m):
                total = max(col_sum[j], total + col_sum[j])
                cur_max = max(cur_max, total)
            ans = max(ans, cur_max)
    return ans

# 测试
n, m = 3, 4
matrix = [
    [-2, 1, -3, 4],
    [-1, 2, 3, -1],
    [1, 1, -3, 2]
]
print(max_matrix_sum(matrix, n, m))  # 7
```

**OD备考提示**：一维 Kadane 算法要滚瓜烂熟（dp[i] = max(nums[i], dp[i-1] + nums[i])）。矩阵压缩成行枚举是核心技巧。注意全负数时取最大值而非0。

## 📝 今日小结
- 螺旋矩阵：边界收缩法，四个方向循环
- 最大子矩阵和：行枚举 + Kadane降维
- 矩阵 BFS 扩散：多源 BFS 队列
