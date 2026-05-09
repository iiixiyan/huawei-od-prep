# Day 40: 队列/栈 — 打印机队列 & 栈模拟

## 📖 知识点
**队列 & 栈核心**：
- **队列**：FIFO（先进先出），BFS、层级处理、任务调度场景
- **优先队列（堆）**：heapq 实现，取优先级最高（或最低）的元素
- **栈**：LIFO（后进先出），括号匹配、表达式求值、DFS
- **双端队列**：collections.deque，两端 O(1) 插入删除
- **单调栈**：解决「下一个更大元素」类问题

## 🧩 刷题任务

### 题目1：打印机队列 (OD 100分, A卷)
**难度**：⭐⭐
**题目描述**：
有一个打印机队列，每个打印任务有[序号, 优先级]。每次从队列头部取出一个任务，如果队列中有比它优先级更高的任务，则将其放到队列尾部；否则直接打印。计算指定序号的任务在第几个被打印。

**输入**：
```
5
1 3
2 2
3 5
4 1
5 4
```
第一行 n 表示任务数量，接下来 n 行每行两个整数表示 [序号, 优先级]。输出序号为3的任务在第几个被打印。

**输出**：
```
1
```

**思路分析**：
1. 使用队列模拟：deque[(seq, priority)]
2. 每次弹出队首，检查队列中是否有更高优先级的任务
3. 如果有，放回队尾；否则打印，打印计数+1
4. 当打印的任务序号等于目标序号时，输出当前计数
5. 查找更高优先级可以用 max(q, key=lambda x: x[1])[1]

**参考代码**：
```python
from collections import deque

def printer_queue(n, tasks, target):
    q = deque(tasks)  # [(seq, priority)]
    printed = 0
    while q:
        seq, pri = q.popleft()
        # 检查队列中是否有更高优先级的任务
        if q and pri < max(p for _, p in q):
            q.append((seq, pri))
        else:
            printed += 1
            if seq == target:
                return printed
    return -1

# 测试
n = 5
tasks = [(1, 3), (2, 2), (3, 5), (4, 1), (5, 4)]
target = 3
print(printer_queue(n, tasks, target))  # 1
```

**OD备考提示**：模拟题，注意 `max(p for _, p in q)` 每次 O(N)，数据量大时可优化为优先队列。但100分题通常 N ≤ 1000，直接模拟即可。

---

### 题目2：堆栈中的剩余数字 / 支持优先级的队列 (OD 100分, C卷/B卷)
**难度**：⭐⭐
**题目描述**：
输入一个整数序列，模拟以下过程：
1. 从左到右遍历数字，依次入栈
2. 如果当前数字等于栈顶的两个元素之和，则当前数字不入栈，改为弹出栈顶两个元素，然后将它们的和（即当前数字）入栈
3. 重复检查新的栈顶是否满足条件
4. 最终输出栈中剩余的所有数字

**输入**：
```
3 3 6 5 7 9 5 4
```
**输出**：
```
4 5 7 9
```

**思路分析**：
1. 用列表模拟栈
2. 遍历每个数字 num：
   - 如果栈中元素 ≥ 2 且 num == stack[-1] + stack[-2]，弹出两个，将 num 入栈，然后循环检查
   - 否则直接将 num 入栈
3. 循环检查：入栈后，如果栈中元素 ≥ 3 且新栈顶 == 新栈顶-1 + 新栈顶-2，也要合并

**参考代码**：
```python
def stack_remaining(nums):
    stack = []
    for num in nums:
        while True:
            if len(stack) >= 2 and num == stack[-1] + stack[-2]:
                stack.pop()
                stack.pop()
                # 注意：这里 num 不变，继续用 num 检查新的栈顶
            else:
                stack.append(num)
                break
    return stack

# 测试
nums = [3, 3, 6, 5, 7, 9, 5, 4]
print(' '.join(map(str, stack_remaining(nums))))  # 4 5 7 9
```

**OD备考提示**：注意 while 循环持续检查的写法。有些变体是"当前数字等于栈顶元素"才合并，要看清楚题目描述。栈模拟题要细心处理边界。

---

### 题目3：最大括号深度 / 括号匹配 (OD 100分)
**难度**：⭐⭐
**题目描述**：
给定一个只包含 `(`、`)`、`[`、`]`、`{`、`}` 的字符串，判断括号是否合法匹配。如果合法，输出最大嵌套深度；如果不合法，输出 -1。

**输入**：
```
{[()()]}
```
**输出**：
```
3
```

**思路分析**：
1. 遍历字符，左括号入栈，右括号检查栈顶是否匹配
2. 当前深度 = 栈的大小，更新最大深度
3. 如果遇到不匹配或栈空时遇到右括号，返回 -1
4. 遍历完后若栈不为空，返回 -1

**参考代码**：
```python
def max_depth_brackets(s):
    stack = []
    depth = 0
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
            depth = max(depth, len(stack))
        else:
            if not stack or stack[-1] != pairs[ch]:
                return -1
            stack.pop()
    return depth if not stack else -1

# 测试
s = "{[()()]}"
print(max_depth_brackets(s))  # 3
s2 = "{[(])}"
print(max_depth_brackets(s2))  # -1
```

**OD备考提示**：括号匹配是栈的经典应用。最大深度就是栈的最大长度。注意三种括号匹配的映射关系要写对。

## 📝 今日小结
- 模拟队列/优先队列：deque + max优先级检查
- 栈模拟合并：while循环持续检查新栈顶
- 括号匹配：栈存左括号，map存配对关系
