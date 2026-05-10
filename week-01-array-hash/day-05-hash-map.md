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
**来源**：[LeetCode](https://leetcode.cn/problems/group-anagrams/)
**难度**：中等
**题目**：给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

**示例 1:**
```
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
- 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
- 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
- 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
```
**示例 2:**
```
输入: strs = [""]
输出: [[""]]
```
**示例 3:**
```
输入: strs = ["a"]
输出: [["a"]]
```
**提示：**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
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
**来源**：[LeetCode](https://leetcode.cn/problems/valid-anagram/)
**难度**：简单
**题目**：给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。

**示例 1:**
```
输入: s = "anagram", t = "nagaram"
输出: true
```
**示例 2:**
```
输入: s = "rat", t = "car"
输出: false
```
**提示:**

- `1 <= s.length <= 5 * 10^4`
- `s` 和 `t` 仅包含小写字母

**进阶: **如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
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
**来源**：[LeetCode](https://leetcode.cn/problems/isomorphic-strings/)
**难度**：简单
**题目**：给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

**示例 1：**
```
输入：s = "egg", t = "add"
输出：true
解释：
字符串 `s` 和 `t` 可以通过以下方式变得相同：
- 将 `'e'` 映射为 `'a'`。
- 将 `'g'` 映射为 `'d'`。
```
**示例 2：**
```
输入：s = "f11", t = "b23"
输出：false
解释：
字符串 `s` 和 `t` 无法变得相同，因为 `'1'` 需要同时映射到 `'2'` 和 `'3'`。
```
**示例 3：**
```
输入：s = "paper", t = "title"
输出：true
```
**提示：**

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` 和 `t` 由任意有效的 ASCII 字符组成
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
**来源**：[LeetCode](https://leetcode.cn/problems/word-pattern/)
**难度**：简单
**题目**：给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循**指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。具体来说：

- `pattern` 中的每个字母都 **恰好**映射到 `s` 中的一个唯一单词。

- `s` 中的每个唯一单词都**恰好** 映射到 `pattern` 中的一个字母。

- 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

**示例1:**
```
输入: pattern = "abba", s = "dog cat cat dog"
输出: true
```
**示例 2:**
```
输入:pattern = "abba", s = "dog cat cat fish"
输出: false
```
**示例 3:**
```
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
```
**提示:**

- `1 <= pattern.length <= 300`
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
**来源**：[LeetCode](https://leetcode.cn/problems/find-the-difference-of-two-arrays/)
**难度**：简单
**题目**：给你两个下标从 `0` 开始的整数数组 `nums1` 和 `nums2` ，请你返回一个长度为 `2` 的列表 `answer` ，其中：

- `answer[0]` 是 `nums1` 中所有**不**存在于 `nums2` 中的 **不同** 整数组成的列表。

- `answer[1]` 是 `nums2` 中所有**不**存在于 `nums1` 中的 **不同** 整数组成的列表。

**注意：**列表中的整数可以按 **任意** 顺序返回。

**示例 1：**
```
输入：nums1 = [1,2,3], nums2 = [2,4,6]
输出：[[1,3],[4,6]]
解释：
对于 nums1 ，nums1[1] = 2 出现在 nums2 中下标 0 处，然而 nums1[0] = 1 和 nums1[2] = 3 没有出现在 nums2 中。因此，answer[0] = [1,3]。
对于 nums2 ，nums2[0] = 2 出现在 nums1 中下标 1 处，然而 nums2[1] = 4 和 nums2[2] = 6 没有出现在 nums1 中。因此，answer[1] = [4,6]。
```
**示例 2：**
```
输入：nums1 = [1,2,3,3], nums2 = [1,1,2,2]
输出：[[3],[]]
解释：
对于 nums1 ，nums1[2] 和 nums1[3] 没有出现在 nums2 中。由于 nums1[2] == nums1[3] ，二者的值只需要在 answer[0] 中出现一次，故 answer[0] = [3]。
nums2 中的每个整数都在 nums1 中出现，因此，answer[1] = [] 。
```
**提示：**

- `1 <= nums1.length, nums2.length <= 1000`
**思路**：将 nums1 转为 set，遍历 nums2，如果元素在 set 中则加入结果集并从 set 移除（避免重复）。或者用两个 set 求交集运算。
**代码**：
```python
def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]
```
### 6. 独一无二的出现次数（⭐）
**来源**：[LeetCode](https://leetcode.cn/problems/unique-number-of-occurrences/)
**难度**：简单
**题目**：给你一个整数数组 `arr`，如果每个数的出现次数都是独一无二的，就返回 `true`；否则返回 `false`。

**示例 1：**
```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
```
**示例 2：**
```
输入：arr = [1,2]
输出：false
```
**示例 3：**
```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
```
**提示：**

- `1 <= arr.length <= 1000`
**思路**：用 Counter 统计每个数字的出现次数，然后检查这些次数是否互不相同。用 set 去重，比较 set 大小和 Counter 大小是否相等。
**代码**：
```python
def uniqueOccurrences(arr: list[int]) -> bool:
    from collections import Counter
    count = Counter(arr)
    return len(set(count.values())) == len(count)
```
## 📝 总结
- **字母异位词分组**的核心是找到一种标准化表示（sorted string 或 count tuple）作为哈希表的 key
- **同构字符串 / 单词规律**都涉及双射（双向映射），必须用两个哈希表保证一一对应
- **Counter**是 Python 中非常实用的计数工具，配合 set 可以快速判断频率的独特性
- **Python set 的集合运算**（差集、交集、并集）在处理数组比较时很便捷
