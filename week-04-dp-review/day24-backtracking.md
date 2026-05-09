# Day 24 — Backtracking（回溯）

## 📌 今日重点
- 回溯算法的标准模板（做选择 → 递归 → 撤销选择）
- 剪枝优化技巧
- 组合 / 子集 / 排列三类问题的区别
- 电话号码字母组合（高频手撕题）

---

## 1. 回溯算法核心模板

```java
void backtrack(路径, 选择列表) {
    if (满足结束条件) {
        result.add(路径);
        return;
    }
    
    for (选择 : 选择列表) {
        做选择;             // 将选择加入路径
        backtrack(路径, 新选择列表);
        撤销选择;           // 从路径移除选择
    }
}
```

### 四个关键点
| 要素 | 说明 |
|------|------|
| **路径** | 已经做出的选择 |
| **选择列表** | 当前可以做的选择 |
| **结束条件** | 到达决策树底层 |
| **剪枝** | 提前终止不可能的分支 |

---

## 2. 高频题型与题解

### 🔹 电话号码的字母组合（17. Letter Combinations of a Phone Number）

**思路**：回溯 / 迭代法
- 数字 2-9 映射到字母
- 每次取一个数字对应的所有字母，递归拼接

```java
class Solution {
    private static final String[] KEYBOARD = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.isEmpty()) return result;
        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(String digits, int idx, StringBuilder sb, List<String> result) {
        if (idx == digits.length()) {
            result.add(sb.toString());
            return;
        }
        String letters = KEYBOARD[digits.charAt(idx) - '0'];
        for (char c : letters.toCharArray()) {
            sb.append(c);
            backtrack(digits, idx + 1, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
```

**⭐ 华为 OD 高频**：这道题经常作为回溯入门手撕题，也可能要求用迭代（Queue 逐层扩展）：

```java
// 迭代法（BFS 思路）
public List<String> letterCombinations(String digits) {
    LinkedList<String> queue = new LinkedList<>();
    if (digits.isEmpty()) return queue;
    queue.offer("");
    for (int i = 0; i < digits.length(); i++) {
        String letters = KEYBOARD[digits.charAt(i) - '0'];
        int size = queue.size();
        for (int j = 0; j < size; j++) {
            String cur = queue.poll();
            for (char c : letters.toCharArray()) {
                queue.offer(cur + c);
            }
        }
    }
    return queue;
}
```

### 🔹 组合总和 III（216. Combination Sum III）

**思路**：回溯 + 剪枝
- 从 1~9 中选 k 个数，和为 n
- 剪枝 1：当前和 > 目标 → 停止
- 剪枝 2：剩余数字不够凑 k 个 → 停止

```java
public List<List<Integer>> combinationSum3(int k, int n) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(1, k, n, new ArrayList<>(), result);
    return result;
}

private void backtrack(int start, int k, int remain, 
                       List<Integer> path, List<List<Integer>> result) {
    // 剪枝
    if (remain < 0) return;
    if (path.size() == k) {
        if (remain == 0) result.add(new ArrayList<>(path));
        return;
    }
    // 剪枝：剩余数字不够
    for (int i = start; i <= 9; i++) {
        if (9 - i + 1 < k - path.size()) break; // 重要剪枝
        path.add(i);
        backtrack(i + 1, k, remain - i, path, result);
        path.remove(path.size() - 1);
    }
}
```

---

## 3. 回溯三大类问题对比

| 类型 | 核心区别 | 关键代码 |
|------|---------|---------|
| **组合**（Combination） | 顺序无关，start 递增 | `backtrack(i+1, ...)` |
| **子集**（Subset） | 每个节点都加入结果 | 无结束条件，每次递归前加 |
| **排列**（Permutation） | 顺序有关，用 used 数组 | `backtrack(used, ...)` |

### 组合 vs 子集 vs 排列模板

```java
// 组合：C(n, k)，选 k 个
void backtrack(int start, int k, ...) {
    if (path.size() == k) { result.add(...); return; }
    for (int i = start; i <= n; i++) {
        path.add(i);
        backtrack(i + 1, k, ...);
        path.removeLast();
    }
}

// 子集：所有子集
void backtrack(int start, ...) {
    result.add(new ArrayList<>(path)); // 每个节点都加入
    for (int i = start; i < nums.length; i++) {
        path.add(nums[i]);
        backtrack(i + 1, ...);
        path.removeLast();
    }
}

// 排列：全排列
void backtrack(boolean[] used, ...) {
    if (path.size() == n) { result.add(...); return; }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.add(nums[i]);
        backtrack(used, ...);
        path.removeLast();
        used[i] = false;
    }
}
```

---

## 4. 剪枝技巧总结

| 剪枝类型 | 例子 | 代码 |
|----------|------|------|
| **可行性剪枝** | 当前和 > target | `if (sum > target) return;` |
| **数字不够** | 剩余数字 < 还需要 | `if (n - i + 1 < k - path.size()) break;` |
| **重复剪枝** | 同层相同数字跳过 | `if (i > start && nums[i] == nums[i-1]) continue;` |
| **最优性剪枝** | 当前已不如最优 | `if (cur >= best) return;` |

---

## 5. 课后练习（LeetCode）

| 题目 | 难度 | 说明 |
|------|------|------|
| 17. Letter Combinations | 🟡 中等 | 回溯/BFS |
| 216. Combination Sum III | 🟡 中等 | 组合+剪枝 |
| 39. Combination Sum | 🟡 中等 | 无重复数字，可重复选 |
| 40. Combination Sum II | 🟡 中等 | 有重复，去重剪枝 |
| 46. Permutations | 🟡 中等 | 全排列 |
| 78. Subsets | 🟡 中等 | 子集 |
| 90. Subsets II | 🟡 中等 | 子集去重 |

---

## ⏱ 今日建议
- **回溯三板斧**：做选择 → 递归 → 撤销选择，死记模板
- **排列用 used 数组**，组合/子集用 start 索引
- **去重剪枝**三步：排序 → `i > start && nums[i] == nums[i-1]` → continue
- 电话字母组合用 StringBuilder 而不是 String 拼接，效率更高
- 华为 OD 笔试回溯题一般不会太难，**组合/子集类**出现频率更高
