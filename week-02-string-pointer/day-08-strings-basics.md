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

### 1. 反转字符串中的元音字母（⭐） 来源：L75
**思路**：左右双指针，分别向中间移动。左指针找元音，右指针找元音，找到后交换。注意大小写都算元音。

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

---

### 2. 反转字符串中的单词（⭐⭐） 来源：L75 / T150
**思路**：先整体反转（逆序），再逐个单词反转回来；或者直接用 split 分割后逆序拼接。注意处理多余空格。

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

---

### 3. 最长公共前缀（⭐⭐） 来源：T150
**思路**：取第一个字符串作为初始前缀，遍历后续字符串，逐一比对缩短前缀。遇到空串或前缀为空时提前返回。

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

---

### 4. Z 字形变换（⭐⭐⭐） 来源：T150
**思路**：模拟 Z 字形。用 `numRows` 个 `StringBuilder`，指针 curRow 上下摆动 (down/up)，把字符添加到对应行。最后拼接所有行。

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

---

### 5. 最后一个单词的长度（⭐） 来源：T150
**思路**：从末尾向前遍历，跳过末尾空格，计数非空格字符，遇到空格则停止。

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

---

### 6. 找出字符串中第一个匹配项的下标（⭐⭐） 来源：T150
**思路**：
- 暴力：滑窗逐一比较（O(n*m)）
- KMP：O(n+m) 预处理 next 数组，利用已匹配信息避免回溯

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

---

## 📌 总结
- Day 08 覆盖了字符串最基础的 6 种题型：双指针交换、单词反转、前缀匹配、坐标变换、逆序遍历、子串匹配
- 华为 OD 机考中**字符串反转、最长公共前缀、子串匹配**出现频率很高，务必熟练

