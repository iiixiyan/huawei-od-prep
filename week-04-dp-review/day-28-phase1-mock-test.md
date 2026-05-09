# Day 28 — Phase 1 模拟考（限时 120 分钟）

## 📋 考试说明

| 项目 | 内容 |
|------|------|
| 总分 | 200 分（每题 100 分） |
| 时间 | 120 分钟 |
| 题型 | 两道编程题，华为 OD 风格 |
| 语言 | Java / Python / C++ 均可 |
| 评分 | 按测试用例通过率给分（每题 10 个用例，每个 10 分） |

---

# 第一题：数组好对最小距离（100 分）

## 题目描述

给定一个长度为 n 的整数数组 `nums` 和一个目标值 `k`。

定义一对元素 `(nums[i], nums[j])`（其中 `i < j`）为**「好对」**，当且仅当 `nums[i] + nums[j] == k`。

请找出所有好对中，`j - i`（下标距离）的最小值。如果不存在任何好对，返回 `-1`。

## 输入格式

```
第一行：一个整数 n，表示数组长度（2 ≤ n ≤ 10^5）
第二行：n 个整数，表示数组 nums（-10^9 ≤ nums[i] ≤ 10^9）
第三行：一个整数 k（-10^9 ≤ k ≤ 10^9）
```

## 输出格式

输出一个整数，表示好对的最小下标距离。如果不存在好对，输出 -1。

## 样例

### 样例 1
```
输入：
6
1 3 5 7 2 4
9

输出：
1
```

**解释**：
- `nums[3] = 7`，`nums[4] = 2`，和 = 9，下标距离 = 1
- `nums[2] = 5`，`nums[5] = 4`，和 = 9，下标距离 = 3
- 最小距离为 1

### 样例 2
```
输入：
4
1 2 3 4
10

输出：
-1
```

**解释**：没有任何两个元素的和等于 10。

### 样例 3
```
输入：
5
2 2 2 2 2
4

输出：
1
```

**解释**：任意相邻的 2 都能组成和 4，最小距离 = 1。

## 数据范围

| 参数 | 范围 |
|------|------|
| n | 2 ≤ n ≤ 10^5 |
| nums[i] | -10^9 ≤ nums[i] ≤ 10^9 |
| k | -10^9 ≤ k ≤ 10^9 |

## 参考思路

**核心思想**：哈希表记录每个值**最近一次出现的下标**。

**一次遍历（推荐）**：
1. 初始化 HashMap：`value → 最近下标`
2. 遍历数组，对于当前下标 i 和值 nums[i]：
   - 计算 complement = k - nums[i]
   - 如果 complement 在 map 中，计算距离 `i - map.get(complement)`，更新全局最小值
   - 更新 `map.put(nums[i], i)`（保留最近出现的下标）
3. 返回最小距离，若无则为 -1

**时间复杂度**：O(n)
**空间复杂度**：O(n)

## 参考代码（Java）

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }
        int k = sc.nextInt();

        // HashMap: value -> 最近一次出现的下标
        Map<Integer, Integer> map = new HashMap<>();
        int minDist = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int complement = k - nums[i];
            if (map.containsKey(complement)) {
                int dist = i - map.get(complement);
                minDist = Math.min(minDist, dist);
            }
            // 更新当前值的下标（保留最近出现的）
            map.put(nums[i], i);
        }

        System.out.println(minDist == Integer.MAX_VALUE ? -1 : minDist);
    }
}
```

## 评分标准

| 测试用例 | 分值 | 考察点 |
|---------|------|--------|
| #1 | 10 | 样例 1 |
| #2 | 10 | 样例 2（无好对） |
| #3 | 10 | 样例 3（全相同） |
| #4 | 10 | 存在多个好对，最小距离在中间 |
| #5 | 10 | 最小好对距离在开头 |
| #6 | 10 | 最小好对距离在结尾 |
| #7 | 10 | 包含负数和大数 |
| #8 | 10 | 大规模 n=10^5，O(n²) 会超时 |
| #9 | 10 | k 为极大/极小边界值 |
| #10 | 10 | 重复元素，多种配对可能 |

> **注意**：暴力 O(n²) 解法只能通过 #1~#3 约 30 分。

---

# 第二题：数字三角形最小波动（100 分）

## 题目描述

给定一个 n 层的数字三角形。第 i 层（从 1 开始计数）包含 i 个正整数，排列如下：

```
第 1 层：  a[1][1]
第 2 层：  a[2][1]  a[2][2]
第 3 层：  a[3][1]  a[3][2]  a[3][3]
...
第 n 层：  a[n][1]  a[n][2]  ...  a[n][n]
```

从三角形顶部 `a[1][1]` 出发，每次可以向下移动到下一行的**正下方**（即从 `a[i][j]` 到 `a[i+1][j]`）或**右下方**（即从 `a[i][j]` 到 `a[i+1][j+1]`），到达三角形底部任意位置时结束。

定义一条路径的**「波动值」**为路径上**相邻两个数字之差的绝对值之和**。具体公式：

```
波动值 = Σ |a[i][pi] - a[i+1][p_{i+1}]|   (i = 1 到 n-1)
```

其中 pi 为第 i 层选择的列下标。

求从顶部到底部所有路径中，**最小波动值**是多少。

## 输入格式

```
第一行：一个整数 n（1 ≤ n ≤ 200），表示三角形的层数
接下来的 n 行：
  第 i 行包含 i 个正整数，表示三角形第 i 层的数字（1 ≤ a[i][j] ≤ 10^6）
```

## 输出格式

输出一个整数，表示最小波动值。

## 样例

### 样例 1
```
输入：
4
5
3 8
1 9 2
7 4 6 8

输出：
7
```

**解释**：
有效路径及波动值计算：

- 5 → 3 → 1 → 4: |5-3| + |3-1| + |1-4| = 2 + 2 + 3 = **7**
- 5 → 3 → 1 → 7: |5-3| + |3-1| + |1-7| = 2 + 2 + 6 = 10
- 5 → 3 → 9 → 6: 2 + 6 + 3 = 11
- 5 → 8 → 9 → 4: 3 + 1 + 5 = 9
- 5 → 8 → 9 → 6: 3 + 1 + 3 = **7**

两条路径均可得到波动值 7，输出 7。

### 样例 2
```
输入：
2
10
5 20

输出：
5
```

**解释**：
- 10 → 5: |10-5| = 5
- 10 → 20: |10-20| = 10
- 最小为 5

### 样例 3
```
输入：
1
100

输出：
0
```

**解释**：只有一层，没有相邻数字对，波动值为 0。

## 数据范围

| 参数 | 范围 |
|------|------|
| n | 1 ≤ n ≤ 200 |
| a[i][j] | 1 ≤ a[i][j] ≤ 10^6 |

## 参考思路

**核心思想**：二维 DP，`dp[i][j]` 表示从顶部到达第 i 层第 j 列的最小波动值。

**状态定义**：
- `dp[i][j]` = 从 `a[1][1]` 到达 `a[i][j]` 的最小波动值

**状态转移**：
- `dp[i][j]` 只能从上一层的同一列 `dp[i-1][j]` 或上一层的左一列 `dp[i-1][j-1]` 转移而来
- `dp[i][j] = min(dp[i-1][j] + |a[i-1][j] - a[i][j]|, dp[i-1][j-1] + |a[i-1][j-1] - a[i][j]|)`
- 注意处理边界：`j = 1` 时只能从正上方来，`j = i` 时只能从左上方来

**初始化**：
- `dp[1][1] = 0`（只有一个元素，没有波动）

**答案**：
- `min(dp[n][j])` 其中 j = 1..n

**时间复杂度**：O(n²)
**空间复杂度**：O(n²)，可优化为 O(n) 滚动数组

## 参考代码（Java）

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] a = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        // dp[i][j] = 到达 (i,j) 的最小波动值
        int[][] dp = new int[n + 1][n + 1];
        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);
        dp[1][1] = 0; // 起点没有波动

        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                // 从正上方来 (i-1, j)
                if (j <= i - 1 && dp[i-1][j] != Integer.MAX_VALUE) {
                    int cost = dp[i-1][j] + Math.abs(a[i-1][j] - a[i][j]);
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
                // 从右上方来 (i-1, j-1)
                if (j - 1 >= 1 && dp[i-1][j-1] != Integer.MAX_VALUE) {
                    int cost = dp[i-1][j-1] + Math.abs(a[i-1][j-1] - a[i][j]);
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        }

        int ans = Integer.MAX_VALUE;
        for (int j = 1; j <= n; j++) {
            ans = Math.min(ans, dp[n][j]);
        }
        System.out.println(ans);
    }
}
```

### 滚动数组优化版（O(n) 空间）

```java
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] a = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[1] = 0;

        for (int i = 2; i <= n; i++) {
            int[] newDp = new int[n + 1];
            Arrays.fill(newDp, Integer.MAX_VALUE);
            for (int j = 1; j <= i; j++) {
                if (j <= i - 1 && dp[j] != Integer.MAX_VALUE) {
                    newDp[j] = Math.min(newDp[j],
                        dp[j] + Math.abs(a[i-1][j] - a[i][j]));
                }
                if (j - 1 >= 1 && dp[j-1] != Integer.MAX_VALUE) {
                    newDp[j] = Math.min(newDp[j],
                        dp[j-1] + Math.abs(a[i-1][j-1] - a[i][j]));
                }
            }
            dp = newDp;
        }

        int ans = Integer.MAX_VALUE;
        for (int j = 1; j <= n; j++) {
            ans = Math.min(ans, dp[j]);
        }
        System.out.println(ans);
    }
}
```

## 评分标准

| 测试用例 | 分值 | 考察点 |
|---------|------|--------|
| #1 | 10 | 样例 1（n=4 常规） |
| #2 | 10 | 样例 2（n=2） |
| #3 | 10 | 样例 3（n=1 边界） |
| #4 | 10 | n=3，三角形各值相等（波动为 0） |
| #5 | 10 | n=5，值单调递增 |
| #6 | 10 | n=5，值单调递减 |
| #7 | 10 | n=10，随机值 |
| #8 | 10 | n=50，大数值范围 |
| #9 | 10 | n=100，中等规模 |
| #10 | 10 | n=200，最大规模，验证 O(n²) 通过 |

> **注意**：暴力 DFS 全路径搜索在 n=200 时路径数为 2^(n-1) ≈ 2^199，无法通过 #8~#10。

---

## 📊 参考评分细则

### 得分区间参考

| 总分 | 评级 | 说明 |
|------|------|------|
| 180~200 | ⭐ A | 两道题均接近满分，DP 与哈希表掌握扎实 |
| 140~179 | 👍 B | 一道题满分，另一道部分用例通过 |
| 80~139 | 📖 C | 基础解法能跑通部分用例，需要加强优化 |
| < 80 | 🔄 D | 需要重新复习 Week 1~4 基础内容 |

### 常见扣分点

| 问题 | 扣分幅度 |
|------|---------|
| 未处理输入边界（n=1 等） | -10~20 分 |
| 未使用 long 处理大数溢出 | -10 分 |
| O(n²) 暴力导致超时 | -60~70 分 |
| 数组越界（三角形边界判断遗漏） | -10~20 分 |
| 未正确更新 HashMap 下标 | -10~20 分 |
| 编译错误 | 整题 0 分 |

---

## ⏱ 考试策略建议

| 阶段 | 时间 | 行动 |
|------|------|------|
| 前 5 分钟 | 5min | 通读两题，评估难度 |
| 第 1 题 | 30~40min | 先写 O(n) 哈希解法，测试样例 |
| 第 2 题 | 40~50min | 先写 O(n²) 二维 DP，再优化空间 |
| 最后 20~30min | 20min | 补充测试用例、修复边界、检查溢出 |
| 最后 5 分钟 | 5min | 检查输入输出格式、提交 |

> **核心原则**：确保第 1 题全过（100 分）> 第 2 题部分过（50+ 分）> 两道题都勉强过（各 30 分）
