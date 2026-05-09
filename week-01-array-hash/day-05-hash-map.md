# Day 05: 哈希映射

## 📖 知识点
**哈希映射 (HashMap) / Counter**：
- 键值对存储，O(1) 平均时间复杂度的增删改查
- Python 中的 dict、collections.Counter、defaultdict
- 常见应用模式：
  - **字符映射**：建立两个字符之间的一对一映射关系（双射）
  - **分组**：用排序后的字符串作为 key 分组字母异位词
  - **计数**：统计出现次数，验证频率关系

## 🧩 刷题任务（6题）

### 1. 字母异位词分组（⭐⭐⭐）
**来源**：T150 / O
**思路**：将每个字符串排序后的结果作为 key，原字符串加入对应 value 列表。或者用字符计数元组作为 key（长度为 26 的 tuple），避免排序的 O(k log k)。
**代码**：
```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        # 排序法
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# 计数法（避免排序，用元组作为 key）
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     from collections import defaultdict
#     groups = defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for ch in s:
#             count[ord(ch) - ord("a")] += 1
#         groups[tuple(count)].append(s)
#     return list(groups.values())
```

### 2. 有效的字母异位词（⭐）
**来源**：O
**思路**：用长度为 26 的数组计数 s 和 t 中字符出现的次数。如果两个字符串长度不同直接返回 False。最后检查计数数组是否全为零。
**代码**：
```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord("a")] += 1
    for ch in t:
        idx = ord(ch) - ord("a")
        count[idx] -= 1
        if count[idx] < 0:
            return False
    return True
```

### 3. 同构字符串（⭐⭐）
**来源**：T150
**思路**：双射（双向映射）。用两个字典分别存储 s→t 和 t→s 的映射关系。遍历时检查两个方向的映射是否一致：如果 s[i] 已映射到别的字符，或 t[i] 已被别的字符映射，则返回 False。
**代码**：
```python
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for ch_s, ch_t in zip(s, t):
        if (ch_s in map_s_to_t and map_s_to_t[ch_s] != ch_t) or \
           (ch_t in map_t_to_s and map_t_to_s[ch_t] != ch_s):
            return False
        map_s_to_t[ch_s] = ch_t
        map_t_to_s[ch_t] = ch_s
    return True
```

### 4. 单词规律（⭐⭐）
**来源**：T150
**思路**：与同构字符串类似，将 pattern 中的每个字母和 words 中的每个单词建立双射关系。先按空格分割字符串得到单词列表，然后使用两个字典建立双向映射。
**代码**：
```python
def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for ch, word in zip(pattern, words):
        if ch in char_to_word and char_to_word[ch] != word:
            return False
        if word in word_to_char and word_to_char[word] != ch:
            return False
        char_to_word[ch] = word
        word_to_char[word] = ch
    return True
```

### 5. 两个数组的交集（⭐）
**来源**：L75
**思路**：将 nums1 转为 set，遍历 nums2，如果元素在 set 中则加入结果集并从 set 移除（避免重复）。或者用两个 set 求交集运算。
**代码**：
```python
def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]
```

### 6. 独一无二的出现次数（⭐）
**来源**：L75
**思路**：用 Counter 统计每个数字的出现次数，然后检查这些次数是否互不相同。用 set 去重，比较 set 大小和 Counter 大小是否相等。
**代码**：
```python
def uniqueOccurrences(arr: list[int]) -> bool:
    from collections import Counter
    count = Counter(arr)
    return len(set(count.values())) == len(count)
```

## 📝 总结
- **字母异位词分组** 的核心是找到一种标准化表示（sorted string 或 count tuple）作为哈希表的 key
- **同构字符串 / 单词规律** 都涉及双射（双向映射），必须用两个哈希表保证一一对应
- **Counter** 是 Python 中非常实用的计数工具，配合 set 可以快速判断频率的独特性
- **Python set 的集合运算**（差集、交集、并集）在处理数组比较时很便捷
