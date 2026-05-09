# Day 12: 字符串综合

## 📖 知识点

**字符串进阶题型：**
- **异位词匹配**：滑动窗口 + 计数数组
- **原地压缩**：双指针读写
- **递增三元组**：贪心维护最小值和中间值
- **文本对齐**：模拟 + 空格均匀分配
- **拓扑排序**：外星词典（图论 + 字符串比较）
- **时间处理**：分钟统一 + 环状最小差值

---

## 🧩 刷题任务

### 1. 找到字符串中所有字母异位词（⭐⭐⭐） 来源：O
**思路**：固定窗口大小 = len(p)。计数数组统计字符频次。滑动窗口时加入新字符、移除旧字符，比较计数是否一致。

**代码**：
```python
def findAnagrams(s: str, p: str) -> list[int]:
    n, m = len(s), len(p)
    if n < m:
        return []
    cnt_p = [0] * 26
    cnt_w = [0] * 26
    a_ord = ord('a')
    for ch in p:
        cnt_p[ord(ch) - a_ord] += 1
    res = []
    for i, ch in enumerate(s):
        cnt_w[ord(ch) - a_ord] += 1
        if i >= m:
            cnt_w[ord(s[i - m]) - a_ord] -= 1
        if cnt_w == cnt_p:
            res.append(i - m + 1)
    return res
```

---

### 2. 字符串压缩（⭐⭐） 来源：L75
**思路**：双指针原地压缩。读指针遍历，写指针写入。统计连续相同字符的个数，个数 > 1 时写入数字（可能多位数）。

**代码**：
```python
def compress(chars: list[str]) -> int:
    write = 0
    i = 0
    n = len(chars)
    while i < n:
        ch = chars[i]
        cnt = 1
        while i + cnt < n and chars[i + cnt] == ch:
            cnt += 1
        chars[write] = ch
        write += 1
        if cnt > 1:
            for c in str(cnt):
                chars[write] = c
                write += 1
        i += cnt
    return write
```

---

### 3. 递增的三元子序列（⭐⭐） 来源：L75
**思路**：贪心。维护两个变量 `first` 和 `second`（分别表示最小值、第二小的值）。遍历数组，遇到比 first 小的更新 first，比 first 大且比 second 小更新 second，比 second 大则找到。

**代码**：
```python
def increasingTriplet(nums: list[int]) -> bool:
    first = second = float('inf')
    for x in nums:
        if x <= first:
            first = x
        elif x <= second:
            second = x
        else:
            return True
    return False
```

---

### 4. 文本左右对齐（⭐⭐⭐⭐） 来源：T150
**思路**：贪心分组，每行尽量多放单词。当前行长度 + 下一个单词长度 + 1 <= maxWidth 则加入。最后一行左对齐，其他行均匀分配空格。

**代码**：
```python
def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    res = []
    i = 0
    n = len(words)
    while i < n:
        # 确定当前行能放哪些单词
        j = i
        cur_len = 0
        while j < n and cur_len + len(words[j]) + (j - i) <= maxWidth:
            cur_len += len(words[j])
            j += 1
        # 当前行单词索引 [i, j)
        words_cnt = j - i
        spaces = maxWidth - cur_len
        # 最后一行或只有一个单词 → 左对齐
        if j == n or words_cnt == 1:
            line = " ".join(words[i:j])
            line += " " * (maxWidth - len(line))
        else:
            # 均匀分配空格
            each = spaces // (words_cnt - 1)
            extra = spaces % (words_cnt - 1)
            line = ""
            for k in range(words_cnt - 1):
                line += words[i + k] + " " * (each + (1 if k < extra else 0))
            line += words[j - 1]
        res.append(line)
        i = j
    return res
```

---

### 5. 火星词典 / 外星词典（⭐⭐⭐⭐） 来源：O
**思路**：拓扑排序。比较相邻单词找到第一个不同字符，构建有向边。对所有字母进行拓扑排序（BFS / DFS）。

**代码**：
```python
def alienOrder(words: list[str]) -> str:
    from collections import defaultdict, deque
    # 建图
    g = defaultdict(set)
    indeg = defaultdict(int)
    for w in words:
        for ch in w:
            indeg.setdefault(ch, 0)
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # 检查非法情况：w1 是 w2 的前缀但更长
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in g[c1]:
                    g[c1].add(c2)
                    indeg[c2] += 1
                break
    # 拓扑排序
    q = deque([c for c, d in indeg.items() if d == 0])
    res = ""
    while q:
        c = q.popleft()
        res += c
        for nxt in g[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return res if len(res) == len(indeg) else ""
```

---

### 6. 最小时间差（⭐⭐） 来源：O
**思路**：将时间转换为分钟（0~1439）。排序后计算相邻差值，并处理首尾差值（环状）。

**代码**：
```python
def findMinDifference(timePoints: list[str]) -> int:
    minutes = []
    for t in timePoints:
        h, m = map(int, t.split(":"))
        minutes.append(h * 60 + m)
    minutes.sort()
    n = len(minutes)
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, minutes[i + 1] - minutes[i])
    # 首位环状差值
    ans = min(ans, 1440 - minutes[-1] + minutes[0])
    return ans
```

---

## 📌 总结
- Day 12 综合度较高，涵盖异位词、压缩、贪心、模拟、图论、时间处理
- **华为 OD 高频**：字符串压缩、递增三元组、异位词
- **文本对齐**和**外星词典**虽难，但出现频率不高，适合学有余力时攻破

