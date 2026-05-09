# Day 40: 数学综合

## 📖 知识点
**数学类问题常见技巧**：
1. **回文数** → 反转一半数字比较
2. **快速幂** → 二分法，xⁿ = x^(n//2) * x^(n//2)，偶数直接乘，奇数多乘一个 x
3. **开平方** → 牛顿迭代 / 二分法
4. **阶乘尾随零** → 统计因子 5 的个数（因为因子 2 比 5 多）
5. **最大公约数** → 辗转相除法 gcd(a,b) = gcd(b, a%b)
6. **共线问题** → 斜率（分数化简）或叉积判断
7. **溢出处理** → Python 无需担心，但模拟其他语言要注意

**牛顿迭代法求平方根**：
```python
def sqrt_newton(x):
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r
```

## 🧩 刷题任务（6题）

### 1. 回文数（⭐）来源：T150
**思路**：负数和末尾为 0 的正整数不是回文数。反转一半数字：每次取 x 的最低位加到 rev 上，x 去掉最低位。当 x ≤ rev 时停止。最后判断 x == rev 或 x == rev // 10（奇数位的情况）。

**代码**：
```python
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10
```

### 2. 加一（⭐）来源：T150
**思路**：从最低位开始加 1。如果没有进位就直接返回；有进位则继续处理下一位。如果所有位都进位了（如 999 → 1000），在最高位补 1。

**代码**：
```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

### 3. 阶乘后的零（⭐⭐）来源：T150
**思路**：阶乘中尾随零的个数 = min(因子 2 的个数, 因子 5 的个数)。2 的因子远多于 5，所以只需统计因子 5 的个数。每 5 个数贡献一个 5，每 25 个数多贡献一个 5，依此类推。

**代码**：
```python
def trailingZeroes(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
```

### 4. x 的平方根（⭐⭐）来源：T150 / O
**思路**：二分法。在 [0, x] 区间找最大的 mid 使得 mid * mid ≤ x。注意 mid * mid 可能溢出，用 mid ≤ x // mid 判断。

**代码**：
```python
def mySqrt(x):
    if x < 2:
        return x
    left, right = 0, x
    while left < right:
        mid = left + (right - left + 1) // 2
        if mid <= x // mid:
            left = mid
        else:
            right = mid - 1
    return left
```

### 5. Pow(x, n)（⭐⭐）来源：T150
**思路**：快速幂。n 为负数时取倒数处理。二分法：2¹⁰ = (2⁵)² = (2² * 2² * 2)²。递归或迭代实现。

**代码**：
```python
def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    res = 1.0
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res
```

### 6. 直线上最多的点数（⭐⭐⭐）来源：T150
**思路**：对每个点作为起点，统计其他点与它连线的斜率。斜率用最简分数 (dx/g, dy/g) 表示避免浮点误差。垂直线 (dx=0) 和水平线 (dy=0) 单独处理。同一位置的点算重复点。

**代码**：
```python
def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    res = 0
    for i in range(n):
        slope_map = {}
        duplicate = 1
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0 and dy == 0:
                duplicate += 1
                continue
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            key = (dx, dy)
            slope_map[key] = slope_map.get(key, 0) + 1
        res = max(res, duplicate + max(slope_map.values()) if slope_map else duplicate)
    return res
```

## 📝 总结
- **快速幂**（二进制分解）是面试高频考点，必须掌握迭代写法
- **开平方**用二分法最稳妥，注意用 `mid <= x // mid` 避免溢出
- **尾随零问题**核心是因子 5 的计数
- **共线问题**用最简分数表示斜率比浮点数更精确
- 数学题往往能在 O(1) 或 O(log n) 时间内解决，关键是找出数学规律
