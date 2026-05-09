# Day 35: 周复习 — 图、回溯、Trie

## 📖 本周知识体系总览

```
Week 5: 图/回溯/Trie
├── D29 图-DFS       连通分量 | 判环 | 带权图 | 可达性
├── D30 图-BFS       拓扑排序 | 最短路径 | 双向BFS | 多源BFS
├── D31 图进阶       多源BFS | 二分图 | 隐式图 | DAG路径
├── D32 回溯基础     组合 | 排列 | 去重 | 括号生成
├── D33 回溯进阶     子集 | 组合和 | N皇后 | 网格搜索 | 分割
└── D34 Trie         前缀树 | 通配符搜索 | Trie+回溯 | 容错
```

## 🧩 图算法迷你测验（10题）

**Q1**: 无权图中求最短路径用哪种搜索?
<details><summary>答案</summary>BFS,第一次到达目标即为最短.</details>

**Q2**: 拓扑排序的两种实现方式?
<details><summary>答案</summary>Kahn算法(入度表+BFS队列)和DFS后序(逆后序).</details>

**Q3**: 检测图中是否有环的方法?
<details><summary>答案</summary>DFS: 三色标记(白灰黑),发现灰色节点即有环.
Kahn: 拓扑排序后节点数不足即有环.</details>

**Q4**: 双向BFS相比普通BFS的优势?
<details><summary>答案</summary>搜索空间从b^d缩减到2*b^(d/2),大幅减少分支扩展.</details>

**Q5**: 如何判断二分图?
<details><summary>答案</summary>二染色: 相邻节点染不同色,DFS/BFS遍历染色,冲突则不是.</details>

**Q6**: 组合和排列的核心代码区别?
<details><summary>答案</summary>组合用start参数(不回头),排列用used数组(可回头).</details>

**Q7**: 有重复元素的全排列如何去重?
<details><summary>答案</summary>排序+同层剪枝: `if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue`</details>

**Q8**: Word Search I和II的核心区别?
<details><summary>答案</summary>I: 搜索单个单词,每次从网格起点DFS. II: 搜索多个单词,用Trie优化,DFS同时沿Trie节点移动.</details>

**Q9**: Trie的search和startsWith的区别?
<details><summary>答案</summary>search要求is_end=True(完整单词),startsWith只需路径存在.</details>

**Q10**: N-Queens对角线的表示方法?
<details><summary>答案</summary>主对角线: row-col(常数差),副对角线: row+col(常数和).</details>

## 📝 常见错误自查表

| 问题 | 常见错误 | 正确做法 |
|------|---------|---------|
| 图DFS | 忘记visited导致死循环 | 入队/入栈前标记visited |
| BFS最短路径 | 步数计数位置错误 | 每层结束时+1或存步数到队列 |
| 拓扑排序 | 忽略入度更新顺序 | 出队后更新所有邻居入度 |
| 回溯去重 | 使用全局used判断同层重复 | 必须加 `i > start` 条件 |
| 组合可重复选 | 错误start+1 | 递归时start不变 |
| Trie通配符搜索 | 忘记处理'.'的递归回溯 | DFS遍历所有子节点 |
| 网格搜索 | 边界和字符检查顺序 | 先检查边界再检查字符 |

## 🔗 关联题目汇总

| 题型 | 核心题 | 变种 |
|------|-------|------|
| 图DFS | Number of Islands → | Surrounded Regions, Max Area of Island |
| 拓扑排序 | Course Schedule → | Course Schedule II, Alien Dictionary |
| BFS最短路径 | Word Ladder → | Min Genetic Mutation, Open the Lock |
| 多源BFS | Rotting Oranges → | 01 Matrix, Walls and Gates |
| 回溯组合 | Combinations → | Combination Sum (I/II/III), Subsets |
| 回溯排列 | Permutations → | Permutations II, Next Permutation |
| N皇后 | N-Queens II → | N-Queens I, Sudoku Solver |
| 网格搜索 | Word Search → | Word Search II |
| Trie | Implement Trie → | Add and Search Word, Magic Dictionary |

## 📊 难度分布

| 难度 | 题数 | 占比 |
|------|------|------|
| ⭐⭐ (中等) | 30 | 83% |
| ⭐⭐⭐ (较难) | 6 | 17% |
| 总计 | 36 | 100% |
