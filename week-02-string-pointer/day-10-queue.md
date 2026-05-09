# Day 10 — Queue（队列）

## 今日目标
- 理解队列（Queue）的 **FIFO（先进先出）** 特性
- 掌握 Python 中队列的常用实现方式
- 学会用队列处理滑动窗口和循环投票问题

---

## 📚 知识点：队列（Queue）

### 核心特性
| 操作 | 描述 | 时间复杂度 |
|------|------|-----------|
| `enqueue(x)` | 将元素 x 加入队尾 | O(1) |
| `dequeue()` | 移除队首元素 | O(1) |
| `front()` | 查看队首元素 | O(1) |
| `is_empty()` | 判断队列是否为空 | O(1) |

### Python 队列实现

**1. collections.deque（推荐）**
```python
from collections import deque

q = deque()          # 初始化
q.append(1)          # 入队（右端）
q.append(2)
front = q[0]         # 查看队首
val = q.popleft()    # 出队（左端）
```

**2. queue.Queue（线程安全，不推荐竞赛用）**
```python
from queue import Queue
q = Queue()
q.put(1)
val = q.get()
```

> ⚡ **OD 考点**：`deque` 是 Python 刷题最常用的队列实现，两端操作都是 O(1)。

### 队列 vs 栈 对比
| 特性 | 栈 (Stack) | 队列 (Queue) |
|------|-----------|-------------|
| 原则 | LIFO（后进先出） | FIFO（先进先出） |
| 入/出 | 同一端操作 | 两端操作 |
| 常用场景 | 括号匹配、撤销、DFS | BFS、任务调度、滑动窗口 |

---

## 🧩 题目 1：最近的请求次数

**LeetCode 933. Number of Recent Calls**

### 问题描述
实现 `RecentCounter` 类，统计过去 3000 毫秒内的请求次数。

- `ping(t)`：在时间 t 添加一个新请求（t 是严格递增的）
- 返回在 `[t-3000, t]` 范围内的请求次数

**示例**
```
输入：
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]

输出：
[null, 1, 2, 3, 3]

解释：
ping(1)    → 时间 [1-3000, 1] = [-2999,1] 范围内有 1 个请求 → 1
ping(100)  → 时间 [-2900, 100] 范围内有 2 个请求 → 2
ping(3001) → 时间 [1, 3001] 范围内有 3 个请求 → 3
ping(3002) → 时间 [2, 3002] 范围内有 3 个请求 → 3（移除了 t=1）
```

### 思路分析
🚀 **队列+滑动窗口**

由于时间 t 是严格递增的，每次 `ping(t)`：
1. 将新时间 t 入队
2. 移除队首所有 `< t-3000` 的过期请求（窗口外的）
3. 返回队列长度

### 代码实现
```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t: int) -> int:
        self.queue.append(t)
        # 移除所有小于 t-3000 的旧请求
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

# 使用
obj = RecentCounter()
print(obj.ping(1))     # 1
print(obj.ping(100))   # 2
print(obj.ping(3001))  # 3
print(obj.ping(3002))  # 3
```

**复杂度分析**
- 时间复杂度：O(n) 均摊，每个元素入队一次出队一次
- 空间复杂度：O(n)，队列中最多存储窗口内的所有元素

---

## 🧩 题目 2：Dota2 参议院

**LeetCode 649. Dota2 Senate**

### 问题描述
Dota2 参议院由 Radiant（R）和 Dire（D）两派组成。投票流程：
1. 参议员按给定顺序围坐一圈
2. 每轮每个参议员可以行使 **一次** 权利：禁止一名对方参议员的投票权
3. 所有参议员行使完权利后，被禁止的参议员跳过，重复直到一派全灭

返回哪一派会获胜。

**示例**
```
输入: senate = "RD"
输出: "Radiant"
解释: 
  R 禁止 D → D 被跳过 → 只剩 R → Radiant 获胜

输入: senate = "RDD"
输出: "Dire"
解释:
  第1轮: R 禁止一个 D, D 禁止 R, D 禁止... 
  实际上 R 先出手 → D1被禁 → D2禁止R → R被禁 → 只剩 D → Dire 获胜
```

### 思路分析

🚀 **队列+贪心模拟**

核心思想：每个参议员都想禁止 **下一个** 对方派系的参议员，这样可以最大限度地保护己方。

用两个队列分别存储 R 和 D 的索引位置。模拟过程：
1. 比较两个队列队首的索引
2. 索引小的先行使权利 → 禁止对方队首 → 被禁者出队
3. 行使权利的参议员进入下一轮（索引 + n，n 为总人数，表示排到队尾）

### 代码实现
```python
from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    # 两个队列分别存储 R 和 D 的索引
    r_queue = deque()
    d_queue = deque()
    
    for i, party in enumerate(senate):
        if party == 'R':
            r_queue.append(i)
        else:
            d_queue.append(i)
    
    # 模拟投票
    while r_queue and d_queue:
        r_idx = r_queue.popleft()
        d_idx = d_queue.popleft()
        
        if r_idx < d_idx:
            # R 先出手，禁止 D，R 进入下一轮
            r_queue.append(r_idx + n)
        else:
            # D 先出手，禁止 R，D 进入下一轮
            d_queue.append(d_idx + n)
    
    return "Radiant" if r_queue else "Dire"
```

**复杂度分析**
- 时间复杂度：O(n)，每个元素出队一次入队一次
- 空间复杂度：O(n)

### 图解过程
```
输入: "RDD" (n=3)

初始: R队=[0], D队=[1,2]

第1轮:
  R队首=0, D队首=1
  0 < 1 → R先出手，D1被禁
  R0进入下一轮 → R队=[3]
  D队首出队 → D队=[2]
  
  (R队和D队都非空，继续)
  R队首=3, D队首=2
  3 > 2 → D2先出手，R0被禁
  D2进入下一轮 → D队=[5]
  R队首出队 → R队=[]
  
R队为空 → "Dire" 获胜 ✓
```

---

## 📝 队列核心套路总结

### 队列的三大应用场景

| 场景 | 典型问题 | 关键信号 |
|------|---------|---------|
| **滑动窗口** | 最近请求次数、滑动窗口最大值 | "最近"、"窗口"、"范围内" |
| **BFS** | 树的层序遍历、最短路径 | "最短"、"层次" |
| **循环/轮转模拟** | Dota2参议院、任务调度器 | "循环"、"轮流"、"依次" |

### 队列解题四步法
1. **入队时机** — 什么情况下元素入队？
2. **出队条件** — 什么情况下元素出队？
3. **队首用途** — 队首元素代表什么含义？
4. **结果构建** — 队列长度、队首访问、队列元素拼接？

---

## 💪 课后练习

| 题目 | 难度 | 推荐用时 | 考察点 |
|------|------|---------|--------|
| LeetCode 933. 最近的请求次数 | 🟢 简单 | 10min | 队列滑动窗口 |
| LeetCode 649. Dota2 参议院 | 🟠 中等 | 20min | 队列+贪心 |
| LeetCode 622. 设计循环队列 | 🟠 中等 | 20min | 队列底层实现 |
| LeetCode 641. 设计循环双端队列 | 🟠 中等 | 20min | 双端队列实现 |
| LeetCode 387. 字符串中的第一个唯一字符 | 🟢 简单 | 10min | 队列+哈希 |

### 易错提醒
1. ⚠️ `deque.popleft()` 不能对空队列调用 → 一定要判空
2. ⚠️ 循环问题中，进入下一轮的元素索引要 `+ n` 来保持相对顺序
3. ⚠️ 滑动窗口记得「先入队后清理过期」或「先清理后入队」，保持一致性

> **OD 高频指数**：⭐⭐⭐⭐（队列单独出题频率不如栈，但常作为 BFS 等算法的子组件）
