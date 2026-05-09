# Day 54 — 错题回顾 Phase 2 (OD专项复盘)

> 🎯 **回顾 Weeks 5-7** | OD专项题型 + 应试策略
> 
> 重点：OD常见题型模式、输入输出陷阱、时间分配策略

---

## 一、OD考试特点总结

| 维度 | 特点 |
|------|------|
| 题型 | 2-3道编程题，分值分布 100+100 或 100+200 或 200+200 |
| 时间 | 60-120分钟，按分值分配 |
| 难度 | 100分题≈LeetCode Medium，200分题≈LeetCode Hard |
| 评分 | 按隐藏测试用例通过比例给分，部分正确也有分 |
| 语言 | Python最推荐（开发效率高，内置数据结构丰富） |
| 考核重点 | 算法思维 + 代码实现能力 + 边界处理 |

---

## 二、OD常见题型模式（Week 5-7）

### 📌 Week 5: 字符串处理 + 模拟

**核心题型**：
1. **字符串解码**：括号展开、压缩字符串还原
2. **表达式求值**：中缀转后缀、双栈法
3. **大数运算**：大整数加减乘（字符串模拟）
4. **字符串匹配**：KMP、Rabin-Karp（较少考，滑动窗口更常见）

**高频陷阱**：
- 字符索引混淆（0-indexed vs 1-indexed）
- 空格、换行符处理（`strip()` vs 不 `strip()`）
- 多行输入读取（用 `sys.stdin.read().split()` 一次性读入）

### 📌 Week 6: 图论 + 搜索

**核心题型**：
1. **最短路径**：Dijkstra、BFS（无权图）
2. **状态压缩**：钥匙与锁问题（`(x, y, key_mask)` 状态）
3. **拓扑排序**：依赖关系、课程表
4. **连通分量**：并查集、DFS/BFS 连通域

**高频陷阱**：
- 忘记标记 visited → 死循环
- BFS 出队时才标记 → 大量重复入队导致超时
- 状态压缩 BFS 时 dist 数组过大 → 改用 dict
- 并查集路径压缩漏写 → 超时

### 📌 Week 7: 高级DP + 复杂模拟

**核心题型**：
1. **区间DP**：合并石子、回文串分割
2. **树形DP**：二叉树打家劫舍
3. **状压DP**：TSP、旅行商简化版
4. **复杂模拟**：大模拟题（游戏规则、系统流程）

**高频陷阱**：
- 区间DP循环顺序错误（应先枚举区间长度，再枚举起点）
- 树形DP递归返回值含义不清
- 模拟题漏掉某条规则 → 需要仔细读题

---

## 三、输入输出陷阱汇总

### ⚠️ 读取方式选错

```python
# ✅ 推荐：统一用 sys.stdin.read()
import sys
data = sys.stdin.read().split()
# 按需解析：data[0], data[1], ...

# 如果只有一行
s = sys.stdin.readline().strip()  # 或用 input().strip()

# 多行不定长输入
lines = sys.stdin.read().splitlines()
```

### ⚠️ 常见输入格式及处理

| 输入格式 | 处理方式 |
|---------|---------|
| 第一行 n，第二行 n 个整数 | `n = int(input()); nums = list(map(int, input().split()))` |
| 第一行 n m，接下来 n 行每行 m 个字符 | `n, m = map(int, input().split()); grid = [list(input().strip()) for _ in range(n)]` |
| 直到文件结束 | `for line in sys.stdin: 处理` |
| 整数和字符串混合 | 统一 `split()` 后按索引取，需要的用 `int()` |

### ⚠️ 输出格式错误

```python
# ✅ 空格分隔
print(a, b, c)

# ✅ 换行分隔列表
for x in result:
    print(x)

# ✅ 不换行
print("result:", end=" ")

# ❌ 注意：OD中输出多余空格或换行可能被判错
# 不要 print(f"{a} {b} {c} ") — 末尾多余空格
```

---

## 四、超时优化技巧

### 常见超时原因及解决

| 原因 | 症状 | 解决方案 |
|------|------|---------|
| O(n²) 算法 | n=10⁵ 时超时 | 用哈希表/O(n log n)/滑动窗口 |
| 递归深度过大 | Python递归栈溢出 | 改迭代或用 sys.setrecursionlimit |
| BFS重复入队 | 出队时标记visited | 入队时立即标记 |
| 频繁创建/复制大数组 | 内存+时间双重压力 | 用索引操作，避免切片 |
| 字符串拼接 | O(n²)时间 | 用 list + `''.join()` |
| 不必要的数据结构转换 | 慢 | 直接使用合适的数据结构 |

### Python性能写作技巧

```python
# ❌ 慢
result = ""
for ch in s:
    result += ch

# ✅ 快
result = []
for ch in s:
    result.append(ch)
result = "".join(result)

# ❌ 慢：频繁创建list
nums = [0] * n
for i in range(n):
    nums[i] = i * 2

# ✅ 快：列表推导式
nums = [i * 2 for i in range(n)]

# ❌ 慢：用list模拟deque的popleft
# q.pop(0)  # O(n)

# ✅ 快：使用collections.deque
from collections import deque
q = deque()
q.popleft()  # O(1)
```

---

## 五、10 道快速自测题（OD专项）

**Q1**: 输入第一行为 `n`，第二行为 `n` 个用逗号分隔的整数，如何读取？  
<details><summary>答案</summary>`n = int(input()); nums = list(map(int, input().split(',')))`</details>

**Q2**: BFS求无权图最短路径时，dist 数组初始化为什么值？如何判断未访问？  
<details><summary>答案</summary>初始化为 `-1` 或 `float('inf')`。起点 `dist[start] = 0`，未访问的条件是 `dist[nx] == -1`。</details>

**Q3**: 并查集的 find 函数带路径压缩如何写？  
<details><summary>答案</summary>`def find(x): if parent[x] != x: parent[x] = find(parent[x]); return parent[x]`</details>

**Q4**: 二维矩阵中，如何判断一个坐标 `(i, j)` 在边界内？  
<details><summary>答案</summary>`0 <= i < rows and 0 <= j < cols`</details>

**Q5**: 区间调度问题（最多不重叠区间）用贪心还是DP？  
<details><summary>答案</summary>贪心：按结束时间排序，选最早结束的区间。时间复杂度 O(n log n)。</details>

**Q6**: Python中 `list.pop(0)` 的时间复杂度是多少？应该用什么替代？  
<details><summary>答案</summary>O(n)。用 `collections.deque.popleft()` 替代，时间复杂度 O(1)。</details>

**Q7**: 在OD考试中，如果一道题想不出最优解，应该怎么做？  
<details><summary>答案</summary>先写暴力解（通常能过30-50%的测试用例），拿到部分分数。然后尝试优化。不要在一棵树上吊死。</details>

**Q8**: 字典的 `defaultdict` 和普通字典有什么区别？什么场景用？  
<details><summary>答案</summary>`defaultdict` 在访问不存在的键时自动创建默认值。用于计数、分组等场景，省去 `if key in dict` 判断。`from collections import defaultdict; d = defaultdict(int)`</details>

**Q9**: 内存超限（MLE）通常是什么原因？如何排查？  
<details><summary>答案</summary>常见原因：创建了过大的数组（如 `[N][M][K]`）、递归栈过深、使用过多全局缓存。排查：估算数组大小，换用 dict 或滚动数组。</details>

**Q10**: 时间分配：如果考试有 100分题 + 200分题，共90分钟，如何分配时间？  
<details><summary>答案</summary>100分题 20-25分钟（含测试），200分题 50分钟（含测试），15分钟检查调试。如果100分题15分钟做不出来，先看200分题，回来再补。</details>

---

## 六、考试策略：时间分配 & 部分得分技巧

### 📊 时间分配矩阵

| 题型配置 | 总时间 | 第一题 | 第二题 | 第三题 | 检查 |
|---------|--------|-------|-------|-------|------|
| 100+100 | 60min | 25min | 25min | - | 10min |
| 100+200 | 90min | 25min | 50min | - | 15min |
| 200+200 | 120min | 50min | 50min | - | 20min |
| 100+100+200 | 150min | 20min | 20min | 70min | 40min |

### 🎯 部分得分战术

```
优先级：
1. 所有题都写出暴力解（至少拿30%分数）
2. 确保一题AC（拿满该题分数）
3. 优化第二题
4. 检查边界、重读题
```

**暴力解法示例**：

```python
# 如果不会状态压缩BFS，至少写普通BFS（不加钥匙逻辑）
# 虽然只能过部分用例，但比空着好

# 如果不会DP，写回溯搜索
# 虽然n稍大就超时，但小数据能过

# 如果不会最优解，写最直观的解法并注释说"这是暴力解"
```

### ✅ 考试前5分钟

1. 快速浏览所有题目，判断难度
2. 标记每题的输入输出格式
3. 决定做题顺序：**先易后难，先小分后大分**

### ⏰ 每道题的检查清单

- [ ] 输入读取正确
- [ ] 输出格式（空格、换行、大小写）完全匹配样例
- [ ] 边界情况：n=1, 空数组, 全相同元素, 最大值/最小值
- [ ] 变量名没有拼写错误
- [ ] 没有死循环（while条件确保能退出）
- [ ] 递归有终止条件
- [ ] 提交前去掉调试用的 print

---

## 七、OD易错题型专项

### 📌 排序 + 自定义比较

```python
# Python 自定义排序
from functools import cmp_to_key

def compare(a, b):
    # 返回负值：a排在b前
    # 返回正值：b排在a前
    # 返回0：相等
    if a[0] != b[0]:
        return a[0] - b[0]  # 升序
    return b[1] - a[1]      # 第二关键字降序

sorted_list = sorted(data, key=cmp_to_key(compare))
```

### 📌 区间合并

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(list(interval))
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```

### 📌 大数运算字符串模拟

```python
def add_strings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        a = int(num1[i]) if i >= 0 else 0
        b = int(num2[j]) if j >= 0 else 0
        s = a + b + carry
        result.append(str(s % 10))
        carry = s // 10
        i, j = i - 1, j - 1
    return ''.join(reversed(result))
```

---

> 📌 **最后提醒**：OD考试不仅考算法，还考**抗压能力**和**策略选择**。遇到不会的题不要慌，先拿能拿的分。每一分都很重要！
