# Day 27 — 综合（位运算 · Trie · 区间 · 单调栈）

## 📌 今日重点
- 位运算技巧（XOR、逐位处理）
- Trie 前缀树实现与应用（搜索推荐系统）
- 区间贪心（无重叠区间、射气球）
- 单调栈（每日温度、股票跨度）

---

# 一、位运算

## 位运算核心技巧

```java
// 常用操作
n & 1          // 判断最低位是否为 1
n >>= 1        // 右移一位
n & (n - 1)    // 去掉最低位的 1
n ^ n = 0      // 相同数 XOR 为 0
n ^ 0 = n      // 与 0 XOR 不变
a ^ b ^ a = b  // XOR 可逆
```

---

## 1. 🔹 计数二进制位（338. Counting Bits）

**思路**：DP + 位运算
- 奇数：比特数 = 前一个偶数 + 1（即 `dp[i] = dp[i >> 1] + (i & 1)`）
- 或利用 `i & (i-1)` 去掉最低位 1，`dp[i] = dp[i & (i-1)] + 1`

```java
// DP 法 1：利用最低位
public int[] countBits(int n) {
    int[] dp = new int[n + 1];
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i >> 1] + (i & 1);
    }
    return dp;
}

// DP 法 2：利用 i & (i-1)
public int[] countBits(int n) {
    int[] dp = new int[n + 1];
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i & (i - 1)] + 1;
    }
    return dp;
}
```

**复杂度**：O(n) 时间，O(n) 空间

---

## 2. 🔹 只出现一次的数字（136. Single Number）

**思路**：XOR 性质 —— 相同数字 XOR 为 0，任何数与 0 XOR 为自身

```java
public int singleNumber(int[] nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}
```

**复杂度**：O(n) 时间，O(1) 空间

---

## 3. 🔹 使 a OR b 等于 c 的最小翻转次数（1318. Minimum Flips to Make a OR b Equal to c）

**思路**：逐位判断，三种情况需要翻转
- 如果 c 的当前位 = 0，需要将 a 和 b 的对应位都翻转为 0
- 如果 c 的当前位 = 1，需要至少一个翻转为 1

```java
public int minFlips(int a, int b, int c) {
    int flips = 0;
    for (int i = 0; i < 32; i++) {
        int bitA = (a >> i) & 1;
        int bitB = (b >> i) & 1;
        int bitC = (c >> i) & 1;

        if (bitC == 1) {
            // 需要至少一个为 1
            if (bitA == 0 && bitB == 0) flips += 1;
        } else {
            // 需要两个都为 0
            flips += bitA + bitB;
        }
    }
    return flips;
}
```

**复杂度**：O(32) = O(1) 时间，O(1) 空间

---

# 二、Trie（前缀树）

## Trie 节点模板

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
```

---

## 4. 🔹 实现 Trie（前缀树）（208. Implement Trie）

**思路**：每个节点含 26 个子节点指针 + isEnd 标记

```java
class Trie {
    private TrieNode root;

    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
    }

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }

    private TrieNode searchPrefix(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return null;
            node = node.children[idx];
        }
        return node;
    }
}
```

**复杂度**：
| 操作 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| insert | O(L) | O(L × 26) |
| search | O(L) | O(1) |
| startsWith | O(L) | O(1) |

---

## 5. 🔹 搜索推荐系统（1268. Search Suggestions System）

**思路**：Trie + DFS（或 排序+二分）
- **方法一（Trie+DFS）**：建 Trie，搜索前缀，DFS 收集最多 3 个单词
- **方法二（排序+二分）**：排序 products，每次搜索前缀后二分找起始位置

```java
// 方法一：Trie + DFS
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}

class Solution {
    private TrieNode root;

    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        root = new TrieNode();

        // 建 Trie
        for (String p : products) {
            TrieNode node = root;
            for (char c : p.toCharArray()) {
                int idx = c - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.isEnd = true;
        }

        // 实际上 Trie 节点需要存储单词或使用 StringBuilder
        // 更简洁的方法是排序 + 双指针/二分
        return null; // 占位，见方法二
    }
}

// 方法二：排序 + 二分（笔试更简洁）
public List<List<String>> suggestedProducts(String[] products, String searchWord) {
    Arrays.sort(products);
    List<List<String>> result = new ArrayList<>();
    int left = 0, right = products.length - 1;

    for (int i = 0; i < searchWord.length(); i++) {
        char c = searchWord.charAt(i);
        // 左指针右移，找到第一个前缀匹配
        while (left <= right && (products[left].length() <= i || products[left].charAt(i) < c))
            left++;
        // 右指针左移，找到最后一个前缀匹配
        while (left <= right && (products[right].length() <= i || products[right].charAt(i) > c))
            right--;

        List<String> suggestions = new ArrayList<>();
        for (int j = left; j <= right && j < left + 3; j++) {
            suggestions.add(products[j]);
        }
        result.add(suggestions);
    }
    return result;
}
```

**复杂度**（排序+二分法）：
| 时间复杂度 | 空间复杂度 |
|-----------|-----------|
| O(n log n + m × n) | O(log n) 排序栈空间 |

---

# 三、区间贪心

## 区间问题模板

```java
// 区间排序：按结束时间（或开始时间）
Arrays.sort(intervals, (a, b) -> a[1] - b[1]); // 按结束时间升序

// 遍历并贪心选择
int end = intervals[0][1];
for (int i = 1; i < intervals.length; i++) {
    if (intervals[i][0] >= end) {
        // 不重叠，更新 end
        end = intervals[i][1];
        count++;
    }
}
```

---

## 6. 🔹 无重叠区间（435. Non-overlapping Intervals）

**思路**：按结束时间升序排序 → 贪心选择最早结束的区间 → 移除重叠的

```java
public int eraseOverlapIntervals(int[][] intervals) {
    if (intervals.length == 0) return 0;

    Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

    int count = 1; // 保留的区间数
    int end = intervals[0][1];

    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] >= end) {
            // 不重叠，保留
            count++;
            end = intervals[i][1];
        }
        // 重叠的区间直接跳过（移除）
    }
    return intervals.length - count;
}
```

**复杂度**：O(n log n) 时间，O(1) 空间（排序栈除外）

---

## 7. 🔹 用最少数量的箭引爆气球（452. Minimum Number of Arrows to Burst Balloons）

**思路**：按结束坐标升序排序 → 每次射箭射最右边的位置 → 重叠的气球一箭搞定

```java
public int findMinArrowShots(int[][] points) {
    if (points.length == 0) return 0;

    // 注意：用 Integer.compare 避免溢出
    Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

    int arrows = 1;
    int end = points[0][1];

    for (int i = 1; i < points.length; i++) {
        if (points[i][0] > end) {
            // 不重叠，需要新的一箭
            arrows++;
            end = points[i][1];
        }
        // 重叠的气球用已有的箭
    }
    return arrows;
}
```

**复杂度**：O(n log n) 时间，O(1) 空间

**区间问题对比**：

| 问题 | 排序方式 | 贪心策略 |
|------|---------|---------|
| 435. 无重叠区间 | 按结束时间升序 | 保留最早结束的 |
| 452. 射气球 | 按结束坐标升序 | 箭射在结束位置 |
| 253. 会议室 II | 按开始时间升序 | 小顶堆跟踪结束时间 |
| 56. 合并区间 | 按开始时间升序 | 合并重叠区间 |

---

# 四、单调栈

## 单调栈模板

```java
// 单调递增栈（找下一个更小的元素）
Deque<Integer> stack = new ArrayDeque<>();
for (int i = 0; i < n; i++) {
    while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
        // 出栈，处理结果
        stack.pop();
    }
    stack.push(i);
}

// 单调递减栈（找下一个更大的元素）
Deque<Integer> stack = new ArrayDeque<>();
for (int i = 0; i < n; i++) {
    while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
        // 出栈，处理结果
        stack.pop();
    }
    stack.push(i);
}
```

---

## 8. 🔹 每日温度（739. Daily Temperatures）

**思路**：单调递减栈（栈内存下标，对应的温度递减）
- 遍历温度数组，当前温度 > 栈顶温度 → 出栈并计算结果

```java
public int[] dailyTemperatures(int[] temperatures) {
    int n = temperatures.length;
    int[] answer = new int[n];
    Deque<Integer> stack = new ArrayDeque<>(); // 存下标，温度递减

    for (int i = 0; i < n; i++) {
        while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
            int prev = stack.pop();
            answer[prev] = i - prev;
        }
        stack.push(i);
    }
    // 栈中剩余的下标对应的 answer 默认为 0（无需处理）
    return answer;
}
```

**复杂度**：O(n) 时间，O(n) 空间

---

## 9. 🔹 股票价格跨度（901. Online Stock Span）

**思路**：单调递减栈，栈内存 (价格, 跨度)
- 将之前所有 <= 当前价格的元素弹出，累加跨度

```java
class StockSpanner {
    Deque<int[]> stack; // [price, span]

    public StockSpanner() {
        stack = new ArrayDeque<>();
    }

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1];
        }
        stack.push(new int[]{price, span});
        return span;
    }
}
```

**复杂度**：均摊 O(1) 时间，O(n) 空间

**单调栈应用总结**：

| 题目 | 栈类型 | 含义 |
|------|-------|------|
| 739. 每日温度 | 递减栈 | 找下一个更高温度的距离 |
| 901. 股票跨度 | 递减栈 | 找连续 <= 当前价格的天数 |
| 84. 柱状图中最大矩形 | 递增栈 | 找左右第一个更小的柱子 |
| 42. 接雨水 | 递减栈 | 找左右两边更高的柱子 |

---

## 5. 课后练习（LeetCode）

| 题目 | 难度 | 题型 |
|------|------|------|
| 338. Counting Bits | 🟢 简单 | 位运算 + DP |
| 136. Single Number | 🟢 简单 | XOR |
| 1318. Min Flips | 🟡 中等 | 逐位判断 |
| 208. Implement Trie | 🟡 中等 | Trie |
| 1268. Search Suggestions | 🟡 中等 | Trie / 排序+二分 |
| 435. Non-overlapping Intervals | 🟡 中等 | 区间贪心 |
| 452. Burst Balloons | 🟡 中等 | 区间贪心 |
| 739. Daily Temperatures | 🟡 中等 | 单调栈 |
| 901. Online Stock Span | 🟡 中等 | 单调栈 |

---

## ⏱ 今日建议
- **位运算**：记住 XOR 三条性质和 `n & (n-1)` 这个神器
- **Trie**：节点设计包含 26 个子节点 + isEnd，搜索推荐系统用排序+二分更简单
- **区间贪心**：先按结束时间排序再贪心是万能模板
- **单调栈**：先想清楚要找的是「更大」还是「更小」，决定栈的单调性
- 今天题量大，优先掌握前三节（位运算、区间、单调栈），Trie 了解即可
