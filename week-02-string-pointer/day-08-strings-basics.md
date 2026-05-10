# Day 08: 字符串基础

## 📖 知识点

**字符串常见操作：**
- 双指针（头尾指针、快慢指针）
- 字符串不可变 → 转 list 操作再 join
- 原地反转、单词反转
- 前缀匹配、Z 字形变换坐标映射
- 滑动窗口/KMP 子串匹配

**核心套路：**
1. **反转类**：左右指针交换 or 切片逆序
2. **前缀类**：逐个字符比对，不同时截断
3. **坐标变换类**：找规律映射行/列索引
4. **子串匹配**：暴力滑窗 O(n*m) 或 KMP O(n+m)

---

## 🧩 刷题任务

### 1. 反转字符串中的元音字母（⭐）
**来源**：[L75](https://leetcode.cn/problems/reverse-vowels-of-a-string/)
**难度**：简单
**题目**：给你一个字符串 `s` ，仅反转字符串中的所有元音字母，并返回结果字符串。


元音字母包括 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，且可能以大小写两种形式出现不止一次。


**示例 1：**

**输入：**s = "IceCreAm"


**输出：**"AceCreIm"


**解释：**


`s` 中的元音是 `['I', 'e', 'e', 'A']`。反转这些元音，`s` 变为 `"AceCreIm"`.

**示例 2：**

**输入：**s = "leetcode"


**输出：**"leotcede"


**提示：**

- `1 5`

- `s` 由 **可打印的 ASCII** 字符组成
**思路**：左右双指针，分别向中间移动。左指针找元音，右指针找元音，找到后交换。注意大小写都算元音。
**代码**：
**代码**：
```python
def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    cs = list(s)
    l, r = 0, len(cs) - 1
    while l < r:
        while l < r and cs[l] not in vowels:
            l += 1
        while l < r and cs[r] not in vowels:
            r -= 1
        cs[l], cs[r] = cs[r], cs[l]
        l += 1
        r -= 1
    return "".join(cs)
```
### 2. 反转字符串中的单词（⭐⭐） / T150
**来源**：[L75](https://leetcode.cn/problems/reverse-words-in-a-string/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。


**单词** 是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的 **单词** 分隔开。


返回 **单词** 顺序颠倒且 **单词** 之间用单个空格连接的结果字符串。


**注意：**输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。


**示例 1：**


输入：s = "the sky is blue"
输出："blue is sky the"

**示例 2：**


输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。

**示例 3：**


输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。


**提示：**

- `1 4`

- `s` 包含英文大小写字母、数字和空格 `' '`

- `s` 中 **至少存在一个** 单词


**进阶：**如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 `O(1)` 额外空间复杂度的 **原地** 解法。
**思路**：先整体反转（逆序），再逐个单词反转回来；或者直接用 split 分割后逆序拼接。注意处理多余空格。
**代码**：
**代码**：
```python
def reverseWords(s: str) -> str:
    # 方法1：split + 逆序
    return " ".join(reversed(s.split()))

    # 方法2：双指针原地翻转（适合面试）
    # cs = list(s.strip())
    # # 先整体翻转
    # cs.reverse()
    # # 再逐个单词翻转
    # n = len(cs)
    # i = 0
    # while i < n:
    #     if cs[i] == ' ':
    #         i += 1
    #         continue
    #     j = i
    #     while j < n and cs[j] != ' ':
    #         j += 1
    #     # 翻转单词 cs[i:j]
    #     l, r = i, j - 1
    #     while l < r:
    #         cs[l], cs[r] = cs[r], cs[l]
    #         l += 1
    #         r -= 1
    #     i = j
    # # 清理多余空格
    # return " ".join("".join(cs).split())
```
### 3. 最长公共前缀（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/longest-common-prefix/)
**难度**：简单
**题目**：编写一个函数来查找字符串数组中的最长公共前缀。


如果不存在公共前缀，返回空字符串 `""`。


**示例 1：**


输入：strs = ["flower","flow","flight"]
输出："fl"

**示例 2：**


输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


**提示：**

- `1
**思路**：取第一个字符串作为初始前缀，遍历后续字符串，逐一比对缩短前缀。遇到空串或前缀为空时提前返回。
**代码**：
**代码**：
```python
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```
### 4. Z 字形变换（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/zigzag-conversion/)
**难度**：中等
**题目**：将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。


比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：


P   A   H   N
A P L S I I G
Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。


请你实现这个将字符串进行指定行数变换的函数：


string convert(string s, int numRows);

 


**示例 1：**


输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
**示例 2：**

输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

**示例 3：**


输入：s = "A", numRows = 1
输出："A"

 


**提示：**

- `1
**思路**：模拟 Z 字形。用 `numRows` 个 `StringBuilder`，指针 curRow 上下摆动 (down/up)，把字符添加到对应行。最后拼接所有行。
**代码**：
**代码**：
```python
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * numRows
    cur, direction = 0, 1  # 1 = down, -1 = up
    for ch in s:
        rows[cur] += ch
        cur += direction
        if cur == 0 or cur == numRows - 1:
            direction *= -1
    return "".join(rows)
```
### 5. 最后一个单词的长度（⭐）
**来源**：[T150](https://leetcode.cn/problems/length-of-last-word/)
**难度**：简单
**题目**：给你一个字符串 `s`，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 **最后一个** 单词的长度。


**单词** 是指仅由字母组成、不包含任何空格字符的最大子字符串。


**示例 1：**


输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为 5。

**示例 2：**


输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为 4。

**示例 3：**


输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为 6 的“joyboy”。


**提示：**

- `1 4`

- `s` 仅有英文字母和空格 `' '` 组成

- `s` 中至少存在一个单词
**思路**：从末尾向前遍历，跳过末尾空格，计数非空格字符，遇到空格则停止。
**代码**：
**代码**：
```python
def lengthOfLastWord(s: str) -> int:
    count = 0
    i = len(s) - 1
    # 跳过末尾空格
    while i >= 0 and s[i] == ' ':
        i -= 1
    # 统计单词长度
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1
    return count
```
### 6. 找出字符串中第一个匹配项的下标（⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)
**难度**：简单
**题目**：给你两个字符串 `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串的第一个匹配项的下标（下标从 0 开始）。如果 `needle` 不是 `haystack` 的一部分，则返回  `-1`** **。


**示例 1：**


输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。

**示例 2：**


输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。


**提示：**

- `1 4`

- `haystack` 和 `needle` 仅由小写英文字符组成
**思路**：- 暴力：滑窗逐一比较（O(n*m)） - KMP：O(n+m) 预处理 next 数组，利用已匹配信息避免回溯
**代码**：
**代码**：
```python
def strStr(haystack: str, needle: str) -> int:
    # 暴力解法（面试够用）
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1

    # KMP（进阶）
    # if not needle:
    #     return 0
    # n, m = len(haystack), len(needle)
    # # 构建 next 数组
    # next_arr = [0] * m
    # j = 0
    # for i in range(1, m):
    #     while j > 0 and needle[i] != needle[j]:
    #         j = next_arr[j - 1]
    #     if needle[i] == needle[j]:
    #         j += 1
    #     next_arr[i] = j
    # # 匹配
    # j = 0
    # for i in range(n):
    #     while j > 0 and haystack[i] != needle[j]:
    #         j = next_arr[j - 1]
    #     if haystack[i] == needle[j]:
    #         j += 1
    #     if j == m:
    #         return i - m + 1
    # return -1
```
## 📌 总结
- Day 08 覆盖了字符串最基础的 6 种题型：双指针交换、单词反转、前缀匹配、坐标变换、逆序遍历、子串匹配
- 华为 OD 机考中**字符串反转、最长公共前缀、子串匹配**出现频率很高，务必熟练

