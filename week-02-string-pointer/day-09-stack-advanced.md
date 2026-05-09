# Day 09 — Stack 进阶：嵌套结构解码

## 今日目标
- 掌握栈处理嵌套结构的通用技巧
- 学会「数字栈 + 字母栈」双栈模式
- 理解递归与栈的等价关系

---

## 📚 知识点：嵌套结构的栈处理

### 嵌套结构的特点
```
"3[a2[c]]" → "accaccacc"
         ↑
   数字和字母交替出现，需要多层展开
```

### 双栈解法核心思想
遇到嵌套问题时，用 **两个栈** 分别跟踪：
- **数字栈**：记录当前层重复次数
- **字符串栈**：记录当前层之前的中间结果

> 关键：遇到 `[` 时入栈保存状态，遇到 `]` 时出栈恢复状态。

---

## 🧩 题目：字符串解码

**LeetCode 394. Decode String**

### 问题描述
给定一个经过编码的字符串，返回解码后的字符串。

编码规则：`k[encoded_string]`，其中 `encoded_string` 内部的字符串重复 `k` 次。

- k 保证是正整数
- 输入字符串总是有效的
- 可以嵌套，如 `3[a2[c]]`
- 原始字符串不包含数字，数字只用于重复标记

**示例**
```
输入: s = "3[a]2[bc]"
输出: "aaabcbc"

输入: s = "3[a2[c]]"
输出: "accaccacc"

输入: s = "2[abc]3[cd]ef"
输出: "abcabccdcdcdef"

输入: s = "abc3[cd]xyz"
输出: "abccdcdcdxyz"
```

### 思路分析

#### 方案一：双栈法（推荐）

遍历字符串，分四种情况：

| 当前字符 | 处理方式 |
|---------|---------|
| **数字** | 累加构建完整数字（可能是多位数，如 `12[a]`） |
| **`[`** | 将当前数字和当前字符串入栈保存，然后重置 |
| **字母** | 将字母拼接到当前字符串 |
| **`]`** | 出栈，将当前字符串重复后拼接到上一个字符串后面 |

#### 图解过程

以 `"3[a2[c]]"` 为例：

```
初始: cur_str = "", num = 0

'3'  → num = 3
'['  → 数字栈: [3], 字符串栈: [""], 重置 cur_str="", num=0
'a'  → cur_str = "a"
'2'  → num = 2
'['  → 数字栈: [3,2], 字符串栈: ["", "a"], 重置 cur_str="", num=0
'c'  → cur_str = "c"
']'  → 弹出: num=2, prev_str="a"
        cur_str = "a" + "c" * 2 = "acc"
']'  → 弹出: num=3, prev_str=""
        cur_str = "" + "acc" * 3 = "accaccacc"

结果: "accaccacc"
```

#### 方案二：递归法

递归本质上是利用系统调用栈来处理嵌套，与双栈等价。

```python
def decodeString(s: str) -> str:
    def dfs(i: int):
        res = []
        num = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                i, inner = dfs(i + 1)
                res.append(inner * num)
                num = 0
            elif ch == ']':
                return i, ''.join(res)
            else:
                res.append(ch)
            i += 1
        return i, ''.join(res)
    
    return dfs(0)[1]
```

### 代码实现（双栈法）

```python
def decodeString(s: str) -> str:
    num_stack = []      # 存储重复次数
    str_stack = []      # 存储各层之前的字符串
    cur_num = 0         # 当前数字
    cur_str = []        # 当前字符串（用列表方便拼接）
    
    for ch in s:
        if ch.isdigit():
            # 1. 数字：累加（处理多位数）
            cur_num = cur_num * 10 + int(ch)
        elif ch == '[':
            # 2. 左括号：入栈保存当前状态，重置
            num_stack.append(cur_num)
            str_stack.append(''.join(cur_str))
            cur_num = 0
            cur_str = []
        elif ch == ']':
            # 3. 右括号：出栈，拼接
            repeat = num_stack.pop()
            prev_str = str_stack.pop()
            cur_str = list(prev_str) + ''.join(cur_str) * repeat
        else:
            # 4. 普通字母：追加到当前字符串
            cur_str.append(ch)
    
    return ''.join(cur_str)
```

**复杂度分析**
- 时间复杂度：O(n)，n 为解码后字符串长度（严格说是 O(S) 其中 S 是输出长度）
- 空间复杂度：O(n)，栈空间

---

## 📝 嵌套结构解题模板

### 通用双栈模板
```python
def solve_nested(encoded_str):
    stack1 = []  # 数字/计数栈
    stack2 = []  # 结果/状态栈
    cur_val = 0
    cur_res = []
    
    for ch in encoded_str:
        if is_digit(ch):
            cur_val = cur_val * 10 + int(ch)
        elif open_bracket(ch):
            stack1.append(cur_val)
            stack2.append(cur_res)
            cur_val = 0
            cur_res = []
        elif close_bracket(ch):
            count = stack1.pop()
            prev = stack2.pop()
            cur_res = prev + cur_res * count
        else:
            cur_res.append(ch)
    
    return ''.join(cur_res)
```

### 识别嵌套问题的信号词
- `k[encoded_string]` 格式
- 括号嵌套多层
- 需要从最内层开始处理
- 压缩/展开类问题

---

## 💪 课后练习

| 题目 | 难度 | 推荐用时 | 考察点 |
|------|------|---------|--------|
| LeetCode 394. 字符串解码 | 🟠 中等 | 20min | 双栈/递归 |
| LeetCode 71. 简化路径 | 🟠 中等 | 15min | 栈+路径处理 |
| LeetCode 388. 文件的最长绝对路径 | 🟠 中等 | 20min | 栈+嵌套 |
| LeetCode 726. 原子的数量 | 🔴 困难 | 30min | 双栈+哈希表 |
| LeetCode 224. 基本计算器 | 🔴 困难 | 30min | 双栈+表达式 |

### 解题小贴士
1. 🎯 数字可能是多位数 → 记得 `num = num * 10 + digit`
2. 🎯 字符串拼接用列表 `[]` 而不是 `str +=` → 避免频繁创建新字符串
3. 🎯 `]` 对应的一定是最近的 `[` → 天然匹配栈

> **OD 高频指数**：⭐⭐⭐⭐（中等偏上难度，考察更全面的栈运用能力）
