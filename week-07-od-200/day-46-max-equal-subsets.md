# Day 46: 最大平分数组（200分·DP类）

## 📖 前置知识
- **0-1背包 DP**：`dp[i][w]` 表示前 i 个物品能否凑出重量 w，优化为一维 `dp[w]`
- **状态压缩 / 位运算 DP**：用二进制位表示子集状态
- **DFS + 剪枝**：当 N 较小时，搜索 + 剪枝有时比 DP 更有效
- **组合优化**：将数组分成 K 个和相等的子集，这是经典的 NP-hard 问题的变体

## 🧩 刷题任务

### 题目：最大平分数组（200分）

**题目描述**：
给定一个正整数数组，请将其分成尽可能多的子集，使得每个子集的元素和相等。每个元素只能使用一次，且必须用完所有元素。

求最多能分成多少个这样的子集。

**输入描述**：
第一行：整数 N（1 ≤ N ≤ 15）
第二行：N 个正整数，表示数组元素（每个数 ≤ 10000）

**输出描述**：
一个整数，表示最多能分成的子集个数。如果无法完全平分，输出 0。

**样例输入**：
```
7
4 3 2 3 5 2 1
```

**样例输出**：
```
2
```

**解释**：
总和 = 20。可以分成两个和为 10 的子集：
子集1: [5, 3, 2]（和为10）
子集2: [4, 3, 2, 1]（和为10）
因此最多分成 2 个子集。

---

**思路分析**：

**转化为判定问题**：
设数组总和为 `total`，要分成 k 个子集，则每个子集的和 `target = total / k` 必须是整数。

从大到小枚举 k（从 N 向下到 1），判断能否分成 k 个和为 target 的子集。第一个可行的 k 即为答案。

**判断能否分成 k 个等和子集**：

**方法一：DFS + 回溯 + 剪枝（适合 N ≤ 15）**
1. 排序降序（大的先放，减少搜索分支）
2. 用长度为 k 的数组 `subset_sums` 记录每个子集当前和
3. 将每个元素尝试放入某个子集中
4. 剪枝：
   - 最大元素 > target → 不可能
   - 相同和的子集跳过（避免重复搜索）
   - 当前子集和 + 当前元素 > target → 跳过

**方法二：状态压缩 DP**
- 用二进制 mask 表示已使用的元素
- `dp[mask]` 表示该状态下的当前子集和（取模 target）
- 状态转移：对每个未使用的元素，尝试加入
- 最终 `dp[(1<<N)-1] == 0` 表示可以成功划分

**复杂度**：
- 时间：O(N × 2^N)（状态压缩DP法，N ≤ 15 时可行）
- 空间：O(2^N)

---

**参考代码**：
```python
def can_partition(nums, k):
    """判断能否将 nums 分成 k 个和相等的子集"""
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k
    if max(nums) > target:
        return False

    nums.sort(reverse=True)  # 降序优化
    n = len(nums)
    used = [False] * n

    def backtrack(start, cur_sum, done_count):
        """done_count: 已完成（达到target）的子集数"""
        if done_count == k:
            return True
        if cur_sum == target:
            return backtrack(0, 0, done_count + 1)

        for i in range(start, n):
            if used[i]:
                continue
            if cur_sum + nums[i] > target:
                continue
            # 剪枝：相同值的元素，如果前一个没用，这个也不用试
            if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
                continue
            used[i] = True
            if backtrack(i + 1, cur_sum + nums[i], done_count):
                return True
            used[i] = False
            # 如果第一个数放入失败，直接返回False（重要剪枝）
            if cur_sum == 0:
                return False
        return False

    return backtrack(0, 0, 0)


def max_equal_sum_subsets(arr):
    total = sum(arr)
    n = len(arr)

    # 从大到小枚举子集个数
    for k in range(n, 0, -1):
        if total % k == 0:
            if can_partition(arr, k):
                return k
    return 0


# 输入处理
N = int(input())
arr = list(map(int, input().split()))
print(max_equal_sum_subsets(arr))
```

---

**OD备考提示**：
- **N ≤ 15 是信号**：看到这么小的 N，立刻想到位运算 / 状态压缩 / 回溯搜索。这是出题人故意留的线索。
- **枚举方向**：从大到小枚举 k（先试大 k），一旦找到立刻返回——因为要找最大子集数。
- **剪枝是灵魂**：不加剪枝的回溯会 TLE。以下剪枝必须：
  1. 降序排序
  2. `if cur_sum == 0: return False`（第一个元素放不进当前子集 → 不可行）
  3. 相同值去重剪枝
  4. 超过 target 直接跳过
- **DP 替代方案**：若回溯剪枝仍超时，可用状态压缩 DP（更稳定）。
- **华为 OD 200分 DP 题特点**：不会考纯裸背包，通常是背包 + 搜索 + 贪心的混合体。
