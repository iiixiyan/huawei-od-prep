# Day 25 — DP 1D（一维动态规划）

## 📌 今日重点
- 一维 DP 状态定义与转移方程
- 滚动数组优化空间
- 状态机 DP（多状态转移）
- 数学递推 DP（平铺问题）

---

## 1. 一维 DP 核心三板斧

```java
// 1. 定义状态
dp[i] = 以 i 结尾 / 前 i 个元素的 ... 

// 2. 状态转移
dp[i] = f(dp[i-1], dp[i-2], ...)

// 3. 初始条件
dp[0] = ..., dp[1] = ...
```

### 空间优化模板
```java
// 只依赖前两个状态 → 滚动变量
int prev2 = ..., prev1 = ...;
for (int i = 2; i <= n; i++) {
    int cur = f(prev1, prev2);
    prev2 = prev1;
    prev1 = cur;
}
```

---

## 2. 高频题型与题解

### 🔹 泰波那契数（1137. N-th Tribonacci Number）
**思路**：纯递推，滚动数组 O(1) 空间

```java
public int tribonacci(int n) {
    if (n == 0) return 0;
    if (n <= 2) return 1;
    int a = 0, b = 1, c = 1;
    for (int i = 3; i <= n; i++) {
        int d = a + b + c;
        a = b;
        b = c;
        c = d;
    }
    return c;
}
```

### 🔹 爬楼梯的最小花费（746. Min Cost Climbing Stairs）
**思路**：一维 DP
- `dp[i]` = 到达第 i 级台阶的最小花费
- 可以从 i-1 或 i-2 过来
- 注意：最后要到达 `cost.length`（楼顶）

```java
public int minCostClimbingStairs(int[] cost) {
    int n = cost.length;
    int[] dp = new int[n + 1];
    for (int i = 2; i <= n; i++) {
        dp[i] = Math.min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
    }
    return dp[n];
}

// 滚动优化
public int minCostClimbingStairs(int[] cost) {
    int n = cost.length;
    int prev2 = 0, prev1 = 0; // dp[0] = 0, dp[1] = 0
    for (int i = 2; i <= n; i++) {
        int cur = Math.min(prev1 + cost[i-1], prev2 + cost[i-2]);
        prev2 = prev1;
        prev1 = cur;
    }
    return prev1;
}
```

### 🔹 打家劫舍（198. House Robber）
**思路**：状态机 DP / 一维 DP
- `dp[i]` = 偷到第 i 间房屋时的最大金额
- 第 i 间：偷 = `dp[i-2] + nums[i]`，不偷 = `dp[i-1]`
- 取最大值

```java
// 一维数组版
public int rob(int[] nums) {
    int n = nums.length;
    if (n == 1) return nums[0];
    int[] dp = new int[n];
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);
    for (int i = 2; i < n; i++) {
        dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
    }
    return dp[n-1];
}

// 滚动变量版 O(1)
public int rob(int[] nums) {
    int prev2 = 0, prev1 = 0; // dp[-2]=0, dp[-1]=0
    for (int num : nums) {
        int cur = Math.max(prev1, prev2 + num);
        prev2 = prev1;
        prev1 = cur;
    }
    return prev1;
}

// 状态机版（方便扩展到打家劫舍 III）
public int rob(int[] nums) {
    int yes = 0, no = 0; // 偷/不偷当前房屋
    for (int num : nums) {
        int newYes = no + num;
        int newNo = Math.max(yes, no);
        yes = newYes;
        no = newNo;
    }
    return Math.max(yes, no);
}
```

### 🔹 多米诺和托米诺平铺（790. Domino and Tromino Tiling）
**思路**：数学递推 DP

这是一个 2×n 的棋盘铺砖问题，考虑第 i 列的四种状态：
- `dp[i][0]` = 两列都铺满
- `dp[i][1]` = 上列铺满，下列空一格
- `dp[i][2]` = 下列铺满，上列空一格
- `dp[i][3]` = 两列都空（等价于 `dp[i-1][0]`）

**转移方程**（简化后只需要一维）：
- `dp[i] = 2*dp[i-1] + dp[i-3]`（其中 dp[0]=1, dp[1]=1, dp[2]=2）

```java
public int numTilings(int n) {
    int MOD = 1_000_000_007;
    if (n <= 2) return n;
    long[] dp = new long[n + 1];
    dp[0] = 1; dp[1] = 1; dp[2] = 2;
    for (int i = 3; i <= n; i++) {
        dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD;
    }
    return (int) dp[n];
}
```

**推导**：当 n ≥ 3 时，考虑最右列怎么放：
1. 竖放一个多米诺 → `dp[i-1]`
2. 两个横放的多米诺（占 i-1 和 i 列）→ `dp[i-2]`
3. 托米诺 L 形组合 → 产生 `dp[i-3]` 但有两种镜像，所以 + `dp[i-3]`

总计：`dp[i] = dp[i-1] + dp[i-2] + 2*dp[i-3]` → 化简为 `2*dp[i-1] + dp[i-3]`

---

## 3. 一维 DP 高频模式

| 模式 | 状态定义 | 转移方程示例 |
|------|---------|-------------|
| **斐波那契型** | dp[i] = f(dp[i-1], dp[i-2]) | 爬楼梯、打家劫舍 |
| **状态机型** | dp[i][0/1]（偷/不偷） | 打家劫舍、股票买卖 |
| **整数拆分** | dp[i] = max(j * (i-j), j * dp[i-j]) | 整数拆分 |
| **单词拆分** | dp[i] = dp[j] && set.contains(s[j:i]) | 单词拆分 |
| **数学递推** | dp[i] = a*dp[i-1] + b*dp[i-k] | 多米诺平铺 |

---

## 4. 华为 OD 常考一维 DP

| 题目 | 说明 |
|------|------|
| **746. Min Cost Climbing Stairs** | ⭐ 高频，滚动数组 |
| **198. House Robber** | ⭐ 高频，状态机 |
| **213. House Robber II** | 环形，分类讨论 |
| **740. Delete and Earn** | 转化为打家劫舍 |
| **790. Domino and Tromino** | 数学递推 |
| **139. Word Break** | 单词拆分 |
| **322. Coin Change** | 最少硬币数 |

---

## 5. 课后练习（LeetCode）

| 题目 | 难度 | 说明 |
|------|------|------|
| 1137. Tribonacci | 🟢 简单 | 递推 |
| 746. Min Cost Climbing Stairs | 🟢 简单 | 一维 DP |
| 198. House Robber | 🟡 中等 | 状态机 DP |
| 790. Domino and Tromino | 🟡 中等 | 数学 DP |
| 213. House Robber II | 🟡 中等 | 打家劫舍变体 |
| 322. Coin Change | 🟡 中等 | 完全背包 |

---

## ⏱ 今日建议
- **先定义状态**，再写转移方程，最后处理边界
- **滚动数组**面试必问，用 O(1) 空间替换 O(n)
- **状态机 DP**（yes/no 两状态）比一维 DP 更通用
- 多米诺平铺记住递推公式即可，不必深究推导
