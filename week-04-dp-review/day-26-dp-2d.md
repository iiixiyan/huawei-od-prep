# Day 26 — DP 2D（二维动态规划）

## 📌 今日重点
- 二维 DP 状态定义与转移方程
- 不同路径（组合数 / DP）
- LCS 模板（最长公共子序列）
- 编辑距离 DP
- 股票状态机（含手续费）

---

## 1. 二维 DP 核心模板

```java
// 1. 定义状态
// dp[i][j] = 以 (i,j) 结尾 / 前 i 个和前 j 个的 ...
int[][] dp = new int[m][n];

// 2. 状态转移
dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1], ...);

// 3. 初始化
dp[0][0] = ..., dp[0][j] = ..., dp[i][0] = ...;
```

---

## 2. 高频题型与题解

### 🔹 不同路径（62. Unique Paths）
**思路**：
- `dp[i][j]` = 到达 (i,j) 的路径数
- 只能向右或向下 → `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
- 第一行和第一列都是 1

```java
// DP 版 O(mn)
public int uniquePaths(int m, int n) {
    int[][] dp = new int[m][n];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    return dp[m-1][n-1];
}

// 滚动数组优化 O(n)
public int uniquePaths(int m, int n) {
    int[] dp = new int[n];
    Arrays.fill(dp, 1);
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[j] += dp[j-1];
        }
    }
    return dp[n-1];
}
```

**复杂度分析**：
| 方法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 二维 DP | O(mn) | O(mn) |
| 滚动数组 | O(mn) | O(n) |
| 组合数 C(m+n-2, m-1) | O(min(m,n)) | O(1) |

**组合数公式**：从左上到右下共需走 `(m-1 + n-1)` 步，选 `(m-1)` 步向下 → `C(m+n-2, m-1)`

---

### 🔹 最长公共子序列（1143. Longest Common Subsequence）
**思路**：二维 DP 经典模板
- `dp[i][j]` = text1[0..i-1] 和 text2[0..j-1] 的 LCS 长度
- 若 `text1[i-1] == text2[j-1]`：`dp[i][j] = dp[i-1][j-1] + 1`
- 否则：`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

```java
public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    int[][] dp = new int[m+1][n+1];

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1.charAt(i-1) == text2.charAt(j-1)) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}

// 滚动数组优化（O(n) 空间）
public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    int[] dp = new int[n+1];
    for (int i = 1; i <= m; i++) {
        int prev = 0; // 相当于 dp[i-1][j-1]
        for (int j = 1; j <= n; j++) {
            int temp = dp[j];
            if (text1.charAt(i-1) == text2.charAt(j-1)) {
                dp[j] = prev + 1;
            } else {
                dp[j] = Math.max(dp[j], dp[j-1]);
            }
            prev = temp;
        }
    }
    return dp[n];
}
```

**复杂度分析**：
| 方法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 二维 DP | O(mn) | O(mn) |
| 滚动数组 | O(mn) | O(n) |

---

### 🔹 买卖股票的最佳时机含手续费（714. Best Time to Buy and Sell Stock with Transaction Fee）
**思路**：状态机 DP（两状态）
- `hold` = 持有股票时的最大利润
- `cash` = 不持有股票时的最大利润
- 买入时扣钱，卖出时扣手续费

```java
public int maxProfit(int[] prices, int fee) {
    int hold = -prices[0];   // 第 0 天买入
    int cash = 0;            // 第 0 天不持有
    for (int i = 1; i < prices.length; i++) {
        // 前一天持有不动 或 前一天现金今天买入
        int newHold = Math.max(hold, cash - prices[i]);
        // 前一天现金不动 或 前一天持有今天卖出（扣手续费）
        int newCash = Math.max(cash, hold + prices[i] - fee);
        hold = newHold;
        cash = newCash;
    }
    return cash;
}
```

**复杂度分析**：
| 时间复杂度 | 空间复杂度 |
|-----------|-----------|
| O(n) | O(1) |

**状态机模板（通用股票问题）**：
```
// 状态定义
dp[i][k][0] = 第 i 天，最多交易 k 次，不持有股票
dp[i][k][1] = 第 i 天，最多交易 k 次，持有股票

// 转移
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i] - fee)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```

---

### 🔹 编辑距离（72. Edit Distance）
**思路**：二维 DP，三种操作（插入、删除、替换）
- `dp[i][j]` = word1[0..i-1] 转换成 word2[0..j-1] 所需最少操作数
- 若 `word1[i-1] == word2[j-1]`：`dp[i][j] = dp[i-1][j-1]`
- 否则：`dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
  - `dp[i-1][j]`：删除 word1[i-1]
  - `dp[i][j-1]`：插入 word2[j-1]
  - `dp[i-1][j-1]`：替换 word1[i-1] → word2[j-1]

```java
public int minDistance(String word1, String word2) {
    int m = word1.length(), n = word2.length();
    int[][] dp = new int[m+1][n+1];

    // 初始化：空串编辑距离
    for (int i = 0; i <= m; i++) dp[i][0] = i; // 删除所有字符
    for (int j = 0; j <= n; j++) dp[0][j] = j; // 插入所有字符

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1.charAt(i-1) == word2.charAt(j-1)) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + Math.min(
                    dp[i-1][j],    // 删除
                    Math.min(
                        dp[i][j-1],    // 插入
                        dp[i-1][j-1]   // 替换
                    )
                );
            }
        }
    }
    return dp[m][n];
}

// 滚动数组优化
public int minDistance(String word1, String word2) {
    int m = word1.length(), n = word2.length();
    int[] dp = new int[n+1];
    for (int j = 0; j <= n; j++) dp[j] = j;

    for (int i = 1; i <= m; i++) {
        int prev = dp[0]; // dp[i-1][j-1]
        dp[0] = i;        // dp[i][0] = i
        for (int j = 1; j <= n; j++) {
            int temp = dp[j];
            if (word1.charAt(i-1) == word2.charAt(j-1)) {
                dp[j] = prev;
            } else {
                dp[j] = 1 + Math.min(dp[j], Math.min(dp[j-1], prev));
            }
            prev = temp;
        }
    }
    return dp[n];
}
```

**复杂度分析**：
| 方法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 二维 DP | O(mn) | O(mn) |
| 滚动数组 | O(mn) | O(n) |

---

## 3. 二维 DP 高频模式

| 模式 | 状态定义 | 转移方程 |
|------|---------|---------|
| **路径计数** | dp[i][j] = 到达 (i,j) 路径数 | dp[i-1][j] + dp[i][j-1] |
| **路径最大/最小** | dp[i][j] = 路径最大/小和 | a[i][j] + max/min(dp[i-1][j], dp[i][j-1]) |
| **LCS/编辑距离** | dp[i][j] = 前 i 和前 j 的关系 | 相等继承，不等取三种操作 min |
| **子矩阵/正方形** | dp[i][j] = 以 (i,j) 为右下角 | 根据题意递推 |

---

## 4. 华为 OD 常考二维 DP

| 题目 | 说明 |
|------|------|
| **62. Unique Paths** | ⭐ 高频，滚动数组优化 |
| **63. Unique Paths II** | 有障碍物，初始化注意 |
| **64. Minimum Path Sum** | 路径最小和，模板题 |
| **1143. Longest Common Subsequence** | ⭐ 高频，LCS 模板 |
| **72. Edit Distance** | ⭐ 高频，编辑距离 |
| **714. Best Time to Buy and Sell Stock with Fee** | ⭐ 状态机 DP |
| **221. Maximal Square** | 最大正方形，`dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` |

---

## 5. 课后练习（LeetCode）

| 题目 | 难度 | 说明 |
|------|------|------|
| 62. Unique Paths | 🟡 中等 | 路径计数 DP |
| 63. Unique Paths II | 🟡 中等 | 有障碍物 |
| 64. Minimum Path Sum | 🟡 中等 | 最小路径和 |
| 1143. Longest Common Subsequence | 🟡 中等 | LCS 模板 |
| 72. Edit Distance | 🟡 中等 | 编辑距离 |
| 714. Best Time to Buy and Sell Stock with Fee | 🟡 中等 | 状态机 DP |
| 221. Maximal Square | 🟡 中等 | 最大正方形 |

---

## ⏱ 今日建议
- **二维 DP 先画 DP 表**，观察依赖方向（左上、上、左）
- **滚动数组是必会技巧**，笔试时空间 O(mn) → O(n) 可能被要求
- **LCS 和编辑距离**的 DP table 行/列数 +1（处理空串边界）
- **股票状态机**记住两状态（hold/cash）即可应对带手续费的变体
- 面试时先用完整 DP 表写出正确逻辑，再优化空间
