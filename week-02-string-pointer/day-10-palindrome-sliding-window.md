# Day 10: 回文 / 滑动窗口

## 📖 知识点

**回文串核心套路：**
- **中心扩展法**：每个字符/两个字符为中心向外扩展 O(n²)
- **动态规划**：`dp[i][j] = s[i]==s[j] and dp[i+1][j-1]`
- **Manacher 算法**：O(n) 求最长回文子串（进阶）

**滑动窗口模板：**
```python
while right < n:
    扩展窗口
    while 窗口不满足条件:
        缩小窗口
    更新答案
```

---

## 🧩 刷题任务

### 1. 验证回文串（⭐） 来源：T150 / O
**思路**：双指针左右逼近。忽略非字母数字字符，忽略大小写。遇到非字母数字跳过。

**代码**：
```python
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
```

---

### 2. 验证回文串 II（⭐⭐） 来源：O
**思路**：最多删除一个字符。双指针遇到不匹配时，尝试删除左指针或右指针位置的字符，分别检查剩余子串是否为回文。

**代码**：
```python
def validPalindrome(s: str) -> bool:
    def check(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return check(l + 1, r) or check(l, r - 1)
        l += 1
        r -= 1
    return True
```

---

### 3. 回文子串（⭐⭐⭐） 来源：O
**思路**：中心扩展法。每个字符（奇数长度）和每两个字符之间（偶数长度）作为中心向外扩展，统计回文个数。

**代码**：
```python
def countSubstrings(s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        # 奇数长度回文
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        # 偶数长度回文
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans
```

---

### 4. 最长回文子串（⭐⭐⭐） 来源：T150
**思路**：中心扩展法，维护最长回文的起止位置。遍历每个中心，扩展获取回文长度。

**代码**：
```python
def longestPalindrome(s: str) -> str:
    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    longest = ""
    for i in range(len(s)):
        # 奇数长度
        odd = expand(i, i)
        # 偶数长度
        even = expand(i, i + 1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest
```

---

### 5. 字符串的排列（⭐⭐⭐） 来源：O
**思路**：滑动窗口 + 计数。固定窗口大小为 len(s1)，统计 s1 字符计数，在 s2 上滑动窗口，每次加入新字符、移除旧字符，比较计数是否一致。

**代码**：
```python
def checkInclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False
    cnt1 = [0] * 26
    cnt2 = [0] * 26
    a_ord = ord('a')
    for ch in s1:
        cnt1[ord(ch) - a_ord] += 1
    for i, ch in enumerate(s2):
        cnt2[ord(ch) - a_ord] += 1
        if i >= n1:
            cnt2[ord(s2[i - n1]) - a_ord] -= 1
        if cnt1 == cnt2:
            return True
    return False
```

---

### 6. 反转字符串（⭐） 来源：O
**思路**：左右指针交换字符。原地修改。

**代码**：
```python
def reverseString(s: list[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```

---

## 📌 总结
- 回文问题首选**中心扩展法**，比 DP 更直观且空间 O(1)
- **滑动窗口**的核心是窗口收缩和扩展的条件
- 华为 OD 回问题型常考：**验证回文串 II**（允许删一个字符）、**最长回文子串**

