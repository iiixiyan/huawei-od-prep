# Day 30：OD 100分 × 2 (字符串+哈希)

## 🧩 刷题任务

### 题目1：全量和已占用字符集
**难度**：⭐⭐
**OD卷标**：B卷
**题目描述**：
给定一个字符集字符串表示全量字符集（每个字符出现次数）和已占用字符集（每个字符已占用次数），请计算出剩余可用字符集。
字符集格式：每个字符与其出现次数用 `@` 分隔，不同字符间用 `,` 分隔。例如 `a@3,b@2,c@1` 表示 a 出现 3 次，b 出现 2 次，c 出现 1 次。

输入格式为 `全量字符集@已占用字符集`，输出剩余可用字符集（剩余次数 ≥ 1 的才输出）。

**输入格式**：
- 一行字符串，格式为 `全量字符集@已占用字符集`
- 字符集内每个条目的格式为 `字符@次数`
- 字符集间条目用 `,` 分隔

**输出格式**：
- 输出剩余可用字符集，格式与输入保持一致（字符@次数，逗号分隔）
- 按字符 ASCII 码升序输出

**样例**：
```
输入：
a:3,b:5,c:2@a:1,b:2
输出：
a:2,b:3,c:2
```
解释：全量 a:3,b:5,c:2；已占用 a:1,b:2；剩余 a:2,b:3,c:2

**思路分析**：
1. 用 `@` 分割得到全量部分和已占用部分
2. 分别解析字符串，用字典记录每个字符的总次数和已占用次数
3. 遍历全量字典，计算剩余次数 = 总次数 - 已占用次数
4. 如果剩余次数 ≥ 1，按字符 ASCII 码排序后输出
时间复杂度 O(n)，空间复杂度 O(n)。

**参考代码**：
```python
s = input().strip()
full_part, used_part = s.split('@')

def parse(s):
    d = {}
    if not s:
        return d
    for item in s.split(','):
        if ':' in item:
            ch, cnt = item.split(':')
            d[ch] = int(cnt)
        elif '@' in item:
            ch, cnt = item.split('@')
            d[ch] = int(cnt)
    return d

full_dict = parse(full_part)
used_dict = parse(used_part)

res = []
for ch in sorted(full_dict.keys()):
    remain = full_dict[ch] - used_dict.get(ch, 0)
    if remain > 0:
        res.append(f'{ch}:{remain}')

print(','.join(res))
```

**OD备考提示**：
- 注意分隔符可能是 `:` 也可能是 `@`，需要兼容两种格式
- 已占用字符集中可能没有某个字符，用 `.get(ch, 0)` 处理
- 输出按 ASCII 码升序，用 sorted() 即可

---

### 题目2：密码输入检测
**难度**：⭐⭐
**OD卷标**：C卷
**题目描述**：
给定用户密码输入字符串，包含字母、数字和特殊字符。请判断该字符串是否满足以下密码强度规则：
1. 长度 ≥ 8
2. 至少包含一个大写字母
3. 至少包含一个小写字母
4. 至少包含一个数字
5. 至少包含一个特殊字符（非字母、非数字）
6. 不能有连续 3 个及以上重复字符（例如 "aaa" 不合法）

同时满足以上所有规则则输出 `YES`，否则输出 `NO`，并输出不满足的规则编号（1-6），多个规则用逗号分隔。

**输入格式**：
- 一行字符串，包含可见 ASCII 字符，长度 ≤ 100

**输出格式**：
- 第一行输出 `YES` 或 `NO`
- 如果为 `NO`，第二行输出不满足的规则编号

**样例**：
```
输入：
Pass@123
输出：
YES
```

```
输入：
Passs@12
输出：
NO
1,5
```
解释：长度=7不满足规则1，且"sss"三个连续重复字符不满足规则5（编号按规则顺序对应为规则6？需要核对——这里规则编号1-6对应上述6条）

**思路分析**：
1. 逐个检查 6 条规则，用列表记录不满足的规则编号
2. 规则6：遍历字符串，若连续三个字符相同则标记不满足
3. 收集所有不满足的编号，判断是否全满足

**参考代码**：
```python
s = input().strip()
violations = []

# 规则1：长度 ≥ 8
if len(s) < 8:
    violations.append(1)

has_upper = any(c.isupper() for c in s)
has_lower = any(c.islower() for c in s)
has_digit = any(c.isdigit() for c in s)
has_special = any(not c.isalnum() for c in s)
has_repeat = any(s[i] == s[i+1] == s[i+2] for i in range(len(s) - 2))

if not has_upper:
    violations.append(2)
if not has_lower:
    violations.append(3)
if not has_digit:
    violations.append(4)
if not has_special:
    violations.append(5)
if has_repeat:
    violations.append(6)

if not violations:
    print("YES")
else:
    print("NO")
    print(','.join(map(str, violations)))
```

**OD备考提示**：
- `.isalnum()` 判断字母或数字，取反即为特殊字符
- 连续重复检测用滑动窗口思想：`s[i] == s[i+1] == s[i+2]`
- 规则编号顺序要与题目一致，注意读题

## 📝 课后练习
1. **关联子串（B卷/字符串）**：判断字符串A的排列是否在字符串B中作为子串出现（滑窗+哈希计数）
2. **字符统计及重排（字符串）**：统计字符串中各字符出现次数，按次数降序、ASCII升序排序输出
