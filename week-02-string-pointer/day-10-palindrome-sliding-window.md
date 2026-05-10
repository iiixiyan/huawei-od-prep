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

### 1. 验证回文串（⭐） / O
**来源**：[T150](https://leetcode.cn/problems/valid-palindrome/)
**难度**：简单
**题目**：如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串**。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是**回文串** ，返回 `true`；否则，返回 `false`。

**示例 1：**
```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```
**示例 2：**
```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```
**示例 3：**
```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```
**提示：**

- `1 <= s.length <= 2 * 10^5`
- `s` 仅由可打印的 ASCII 字符组成
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
### 2. 验证回文串 II（⭐⭐）
**来源**：[O](https://leetcode.cn/problems/valid-palindrome/)
**难度**：简单
**题目**：如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串**。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是**回文串** ，返回 `true`；否则，返回 `false`。

**示例 1：**
```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```
**示例 2：**
```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```
**示例 3：**
```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```
**提示：**

- `1 <= s.length <= 10^5`
- `s` 仅由可打印的 ASCII 字符组成
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
### 3. 回文子串（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/palindromic-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

**回文字符串** 是正着读和倒过来读一样的字符串。

**子字符串** 是字符串中的由连续字符组成的一个序列。

**示例 1：**
```
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
```
**示例 2：**
```
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```
**提示：**

- `1 <= s.length <= 1000`
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
### 4. 最长回文子串（⭐⭐⭐）
**来源**：[T150](https://leetcode.cn/problems/palindromic-substrings/)
**难度**：中等
**题目**：给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

**回文字符串** 是正着读和倒过来读一样的字符串。

**子字符串** 是字符串中的由连续字符组成的一个序列。

**示例 1：**
```
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
```
**示例 2：**
```
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```
**提示：**

- `1 <= s.length <= 1000`
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
### 5. 字符串的排列（⭐⭐⭐）
**来源**：[O](https://leetcode.cn/problems/permutation-in-string/)
**难度**：中等
**题目**：给你两个字符串 `s1` 和 `s2` ，写一个函数来判断 `s2` 是否包含 `s1` 的 排列。如果是，返回 `true` ；否则，返回 `false` 。

换句话说，`s1` 的排列之一是 `s2` 的 **子串** 。

**示例 1：**
```
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```
**示例 2：**
```
输入：s1= "ab" s2 = "eidboaoo"
输出：false
```
**提示：**

- `1 <= s1.length <= 10^4`
- `1 <= s2.length <= 10^4`
- `s1` 和 `s2` 仅包含小写字母
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
### 6. 反转字符串（⭐）
**来源**：[O](https://leetcode.cn/problems/reverse-string/)
**难度**：简单
**题目**：编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `s` 的形式给出。

不要给另外的数组分配额外的空间，你必须**原地修改输入数组**、使用 O(1) 的额外空间解决这一问题。

**示例 1：**
```
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```
**示例 2：**
```
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```
**提示：**

- `1 <= s.length <= 10^5`
- `s[i]` 都是 ASCII 码表中的可打印字符
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
## 📌 总结
- 回文问题首选**中心扩展法**，比 DP 更直观且空间 O(1)
- **滑动窗口**的核心是窗口收缩和扩展的条件
- 华为 OD 回问题型常考：**验证回文串 II**（允许删一个字符）、**最长回文子串**
