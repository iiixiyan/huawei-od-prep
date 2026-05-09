# Day 29：OD 100分 × 2 (字符串处理)

## 🧩 刷题任务

### 题目1：回文字符串
**难度**：⭐⭐
**OD卷标**：A卷
**题目描述**：
给定一个由小写字母组成的字符串，请判断是否能通过删除**最多一个**字符，使其变成回文字符串。如果能，输出 `YES`；否则输出 `NO`。

**输入格式**：
- 第一行输入一个正整数 n，表示字符串的长度（1 ≤ n ≤ 10^5）
- 第二行输入一个长度为 n 的字符串 s，仅包含小写字母

**输出格式**：
- 输出一行字符串，`YES` 或 `NO`

**样例**：
```
输入：
3
aba
输出：
YES
```

```
输入：
5
abca
输出：
YES
```
（删除 'c' 后得到 "aba"）

**思路分析**：
使用双指针法，从两端向中间比较字符。当遇到第一对不匹配的字符时，有两种删除策略：
1. 删除左边的字符（左指针右移一位）
2. 删除右边的字符（右指针左移一位）
分别检查两种情况下剩余子串是否为回文串。若任一可行则输出 YES，否则 NO。
时间复杂度 O(n)，空间复杂度 O(1)。

**参考代码**：
```python
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def can_be_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True

n = int(input())
s = input().strip()
print("YES" if can_be_palindrome(s) else "NO")
```

**OD备考提示**：
- 注意输入可能有换行符或空格，使用 `.strip()` 清理
- 双指针法是处理回文串类问题的核心模板
- 字符串长度可达 10^5，O(n^2) 的解法会超时，务必用 O(n)

---

### 题目2：字符串分割
**难度**：⭐⭐
**OD卷标**：B卷
**题目描述**：
给定一个非空字符串 s 和一个整数 k，按照以下规则将字符串分割：
1. 从左到右，每 k 个字符为一组进行分割
2. 如果最后一组不足 k 个字符，则丢弃（不输出）
3. 对每一组字符，将其中的字母（a-z, A-Z）按原顺序排列，数字（0-9）按原顺序排列
4. 输出分割后的所有组，每组内部先输出字母再输出数字

**输入格式**：
- 第一行输入一个字符串 s（1 ≤ len(s) ≤ 1000），仅包含字母和数字
- 第二行输入一个正整数 k（1 ≤ k ≤ len(s)）

**输出格式**：
- 输出分割后的结果，每组以空格分隔。如果没有有效分组则输出空行。

**样例**：
```
输入：
a1b2c3d4e5f6
2
输出：
ab12 cd34 ef56
```
解释：按 k=2 分割得到 "a1", "b2", "c3", "d4", "e5", "f6"，每组字母在前数字在后。

**思路分析**：
1. 遍历字符串，每 k 个字符截取为一个子串
2. 对每个子串，分别提取字母列表和数字列表
3. 拼接字母列表 + 数字列表为新的字符串
4. 收集所有有效分组，用空格连接后输出
时间复杂度 O(n)，空间复杂度 O(n)。

**参考代码**：
```python
s = input().strip()
k = int(input().strip())

res = []
for i in range(0, len(s) - k + 1, k):
    group = s[i:i + k]
    letters = [c for c in group if c.isalpha()]
    digits = [c for c in group if c.isdigit()]
    res.append(''.join(letters + digits))

print(' '.join(res) if res else '')
```

**OD备考提示**：
- 注意 `.isalpha()` 和 `.isdigit()` 的使用，不要混淆
- 最后一组不足 k 个丢弃——用步长为 k 的 range 遍历自然会跳过
- 输出空行的情况不要遗漏

## 📝 课后练习
1. **求字符串中所有整数的最小和（C卷）**：给定字符串，提取其中所有整数并求和，注意负号的处理方式
2. **最长子字符串的长度（一）（C卷）**：在一个环形字符串中找相邻相同字符构成的最长子串长度
