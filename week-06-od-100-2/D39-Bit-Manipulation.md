# Day 39: 位运算

## 📖 知识点
**位运算速查表**
| 运算 | Python 符号 | 说明 |
|------|-------------|------|
| 与 | `&` | 两位都为 1 才为 1 |
| 或 | `\|` | 有一位为 1 即为 1 |
| 异或 | `^` | 相同为 0，不同为 1 |
| 取反 | `~` | 0 变 1，1 变 0 |
| 左移 | `<<` | 左移 n 位相当于乘以 2ⁿ |
| 右移 | `>>` | 右移 n 位相当于除以 2ⁿ |

**常用技巧**：
```python
# 判断第 k 位是否 1
(num >> k) & 1

# 将第 k 位设为 1
num | (1 << k)

# 将第 k 位设为 0
num & ~(1 << k)

# 将第 k 位取反
num ^ (1 << k)

# 去掉最低位的 1
num & (num - 1)

# 获取最低位的 1
num & -num

# 判断 2 的幂
num > 0 and (num & (num - 1)) == 0

# 统计 1 的个数
bin(num).count('1')   # Python 简单写法
# 或内置函数
num.bit_count()       # Python 3.8+
```

**核心场景**：
1. 异或消除法 → 寻找出现奇数次的元素 (x ^ x = 0, x ^ 0 = x)
2. 位掩码 → 用整数的二进制位表示集合状态（状态压缩 DP）
3. 位计数 → 统计二进制中 1 的个数
4. 位运算替代运算 → 快速乘除 2 的幂

## 🧩 刷题任务（6题）

### 1. 两数相除（⭐⭐⭐）来源：O
**思路**：不能用乘除模，用加法/减法替代除法。用倍增法加速：不断将除数翻倍直到超过被除数，从大的开始减。注意处理负号和溢出（-2³¹ 转正数会溢出）。

**代码**：
```python
def divide(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    sign = 1 if (dividend > 0) == (divisor > 0) else -1
    a, b = abs(dividend), abs(divisor)
    res = 0
    while a >= b:
        tmp, multiple = b, 1
        while a >= (tmp << 1):
            tmp <<= 1
            multiple <<= 1
        a -= tmp
        res += multiple
    return sign * res
```

### 2. 二进制求和（⭐）来源：T150
**思路**：逐位相加，维护进位。从右向左遍历两个字符串，和 = a_bit + b_bit + carry。当前位 = 和 % 2，进位 = 和 // 2。最后如果进位还有则补 1。

**代码**：
```python
def addBinary(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        total = x + y + carry
        res.append(str(total % 2))
        carry = total // 2
        i -= 1
        j -= 1
    return ''.join(reversed(res))
```

### 3. 比特位计数（⭐⭐）来源：L75 / O
**思路**：动态规划 + 位运算。对于任意数字 i，去掉最低位 1 后得到 i & (i-1)，它的 1 的个数加 1 就是 i 的 1 的个数。递推：`dp[i] = dp[i & (i-1)] + 1`。

**代码**：
```python
def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
```

### 4. 只出现一次的数字 II（⭐⭐⭐）来源：O
**思路**：每个数字出现 3 次，只有一个出现 1 次。对每一位统计所有数字在该位上的 1 的个数，模 3 后就是目标值在该位上的值。用两个变量（one, two）模拟三进制状态机。

**代码**：
```python
def singleNumber(nums):
    one = two = 0
    for num in nums:
        one = (one ^ num) & ~two
        two = (two ^ num) & ~one
    return one
```

### 5. 最大单词长度乘积（⭐⭐）来源：O
**思路**：用位掩码表示每个单词的字母集合（int 的 26 位，a 对应最低位）。两个单词无公共字母 → 掩码按位与为 0。预处理所有单词的掩码和长度，双重循环求最大乘积。

**代码**：
```python
def maxProduct(words):
    masks = []
    for w in words:
        mask = 0
        for c in w:
            mask |= 1 << (ord(c) - ord('a'))
        masks.append(mask)
    res = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if masks[i] & masks[j] == 0:
                res = max(res, len(words[i]) * len(words[j]))
    return res
```

### 6. 只出现一次的数字（⭐）来源：L75 / T150
**思路**：经典异或解法。a ^ a = 0，a ^ 0 = a。将所有数字异或起来，成对出现的数字会抵消为 0，剩下的就是只出现一次的数字。

**代码**：
```python
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
```

## 📝 总结
- **异或**是位运算中最常用的技巧：自己异或自己得 0，异或 0 得自己
- `i & (i-1)` 去掉最低位 1，可用于计数位 1 或判断 2 的幂
- 位掩码（用 int 的二进制位表示集合）在状态压缩和字符串字母去重中很高效
- 模三状态机（one/two 变量）是解决"出现三次"问题的通用方法
- Python 中整数无限大，但移位操作仍是 O(1)，位运算比算术运算快
