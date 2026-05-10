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

### 1. 找到字符串中所有字母异位词（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
**难度**：中等
**题目**：给定两个字符串 `s` 和 `p`，找到 `s`** **中所有 `p`** **的 **异位词 **的子串，返回这些子串的起始索引。不考虑答案输出的顺序。


**示例 1:**


输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

** 示例 2:**


输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


**提示:**

- `1 4`

- `s` 和 `p` 仅包含小写字母
**思路**：固定窗口大小 = len(p)。计数数组统计字符频次。滑动窗口时加入新字符、移除旧字符，比较计数是否一致。
**代码**：
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
### 2. 字符串压缩（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/string-compression/)
**难度**：中等
**题目**：给你一个字符数组 `chars` ，请使用下述算法压缩：


从一个空字符串 `s` 开始。对于 `chars` 中的每组 **连续重复字符** ：

- 如果这一组长度为 `1` ，则将字符追加到 `s` 中。

- 否则，需要向 `s` 追加字符，后跟这一组的长度。

压缩后得到的字符串 `s` **不应该直接返回** ，需要转储到字符数组 `chars` 中。需要注意的是，如果组长度为 `10` 或 `10` 以上，则在 `chars` 数组中会被拆分为多个字符。


请在 **修改完输入数组后** ，返回该数组的新长度。


你必须设计并实现一个只使用常量额外空间的算法来解决此问题。


**注意：**数组中超出返回长度的字符无关紧要，应予忽略。


**示例 1：**


输入：chars = ["a","a","b","b","c","c","c"]
输出：6
解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。

**示例 2：**


输入：chars = ["a"]
输出：1
解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。

**示例 3：**


输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：4
解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。


**提示：**

- `1
**思路**：双指针原地压缩。读指针遍历，写指针写入。统计连续相同字符的个数，个数 > 1 时写入数字（可能多位数）。
**代码**：
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
### 3. 递增的三元子序列（⭐⭐）
**来源**：[L75](https://leetcode.cn/problems/increasing-triplet-subsequence/)
**难度**：中等
**题目**：给你一个整数数组 `nums` ，判断这个数组中是否存在长度为 `3` 的递增子序列。


如果存在这样的三元组下标 `(i, j, k)` 且满足 `i
- `1 5`

- `-231 31 - 1`


**进阶：**你能实现时间复杂度为 `O(n)` ，空间复杂度为 `O(1)` 的解决方案吗？
**思路**：贪心。维护两个变量 `first` 和 `second`（分别表示最小值、第二小的值）。遍历数组，遇到比 first 小的更新 first，比 first 大且比 second 小更新 second，比 second 大则找到。
**代码**：
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
### 4. 文本左右对齐（⭐⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/text-justification/)
**难度**：困难
**题目**：给定一个单词数组 `words` 和一个长度 `maxWidth` ，重新排版单词，使其成为每行恰好有 `maxWidth` 个字符，且左右两端对齐的文本。


你应该使用 “**贪心算法**” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 `' '` 填充，使得每行恰好有 *maxWidth* 个字符。


要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。


文本的最后一行应为左对齐，且单词之间不插入**额外的**空格。


**注意:**

- 单词是指由非空格字符组成的字符序列。

- 每个单词的长度大于 0，小于等于 *maxWidth*。

- 输入单词数组 `words` 至少包含一个单词。


**示例 1:**


输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
"This    is    an",
"example  of text",
"justification.  "
]

**示例 2:**


输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
"What   must   be",
"acknowledgment  ",
"shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
因为最后一行应为左对齐，而不是左右两端对齐。
第二行同样为左对齐，这是因为这行只包含一个单词。

**示例 3:**


输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
"Science  is  what we",
"understand      well",
"enough to explain to",
"a  computer.  Art is",
"everything  else  we",
"do                  "
]


**提示:**

- `1
**思路**：贪心分组，每行尽量多放单词。当前行长度 + 下一个单词长度 + 1 <= maxWidth 则加入。最后一行左对齐，其他行均匀分配空格。
**代码**：
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
### 5. 火星词典 / 外星词典（⭐⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/alien-dictionary/)
**难度**：困难
**思路**：拓扑排序。比较相邻单词找到第一个不同字符，构建有向边。对所有字母进行拓扑排序（BFS / DFS）。
**代码**：
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
### 6. 最小时间差（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/minimum-time-difference/)
**难度**：中等
**题目**：给定一个 24 小时制（小时:分钟 **"HH:MM"**）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。


**示例 1：**


输入：timePoints = ["23:59","00:00"]
输出：1

**示例 2：**


输入：timePoints = ["00:00","23:59","00:00"]
输出：0


**提示：**

- `2 4`

- `timePoints[i]` 格式为 **"HH:MM"**
**思路**：将时间转换为分钟（0~1439）。排序后计算相邻差值，并处理首尾差值（环状）。
**代码**：
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
## 📌 总结
- Day 12 综合度较高，涵盖异位词、压缩、贪心、模拟、图论、时间处理
- **华为 OD 高频**：字符串压缩、递增三元组、异位词
- **文本对齐**和**外星词典**虽难，但出现频率不高，适合学有余力时攻破

