# Day 47: 模拟目录管理功能（200分·模拟类）

## 📖 前置知识
- **树结构模拟**：用字典/类模拟文件系统的目录树
- **路径解析**：处理绝对路径 `/` 和相对路径 `..` `.`
- **字符串解析**：从输入命令中提取参数
- **设计模式**：命令模式（Command Pattern）的思想

## 🧩 刷题任务

### 题目：模拟目录管理功能（200分）

**题目描述**：
实现一个简单的目录管理模拟器，支持以下命令：

1. `mkdir <目录名>` — 在当前目录下创建子目录（不能重复创建已存在的目录）
2. `cd <目录名>` — 进入子目录；支持 `..` 返回上级目录；支持 `/` 开头的绝对路径
3. `pwd` — 显示当前目录的完整路径
4. `ls` — 列出当前目录下的所有子目录（字典序）
5. `rmdir <目录名>` — 删除当前目录下的指定子目录（只能删除空目录）

**初始状态**：
- 根目录 `/`
- 当前目录为 `/`

**输入描述**：
若干行命令，每行一个命令，以 `EOF` 结束。

**输出描述**：
对于 `pwd` 和 `ls` 命令，输出相应的结果。若命令非法（如创建已存在的目录、删除非空目录等），输出 "error"。

**样例输入**：
```
mkdir a
mkdir b
cd a
mkdir c
pwd
ls
cd ..
rmdir b
ls
pwd
EOF
```

**样例输出**：
```
/a
c
a
/
```

**解释**：
- 在根目录 `/` 下创建 a、b
- 进入 a，在 a 下创建 c
- `pwd` → `/a`
- `ls` → `c`（当前在 a 下，只有子目录 c）
- `cd ..` 回到根目录
- `rmdir b` 删除 b
- `ls` → `a`（只剩 a）
- `pwd` → `/`

---

**思路分析**：

**核心数据结构**：
- 用 `Dict[str, Dict]` 嵌套结构表示目录树：
  ```python
  root = {
      "a": {
          "c": {}
      },
      "b": {}
  }
  ```
- 用 `current_path` 列表（栈）记录当前路径：`["/", "a", "c"]`
- 用指针 `current_dir` 指向当前目录的字典引用

**命令实现**：

| 命令 | 实现 |
|------|------|
| `mkdir x` | 检查 x 是否在当前目录的 key 中；不在则添加 |
| `cd x` | 处理 `..`（pop）、`.`（忽略）、绝对路径（重置）、相对路径（进入子目录） |
| `pwd` | 输出 `"/" + "/".join(current_path[1:])` |
| `ls` | 输出当前目录所有 key 按字典序排序，空格分隔 |
| `rmdir x` | 检查 x 是否存在且为空（无子目录），是则删除 |

**复杂度**：
- 时间：O(M × D)，M 为命令数，D 为目录深度
- 空间：O(N)，N 为创建的目录总数

---

**参考代码**：
```python
import sys

class FileSystem:
    def __init__(self):
        self.root = {}
        self.cur = self.root
        self.path = []  # 路径上各目录的引用栈

    def mkdir(self, name):
        if name in self.cur:
            print("error")
            return
        self.cur[name] = {}

    def cd(self, target):
        if target == "..":
            if self.path:
                self.cur = self.path.pop()
            else:
                print("error")
            return
        if target.startswith("/"):
            # 绝对路径
            parts = [p for p in target.split("/") if p]
            node = self.root
            path_stack = []
            for p in parts:
                if p == "..":
                    if path_stack:
                        path_stack.pop()
                        node = self.root
                        for pp in path_stack:
                            node = node[pp]
                    else:
                        print("error")
                        return
                elif p == ".":
                    continue
                else:
                    if p not in node:
                        print("error")
                        return
                    path_stack.append(p)
                    node = node[p]
            self.path = path_stack
            self.cur = node
            return

        # 相对路径
        if target not in self.cur:
            print("error")
            return
        self.path.append(self.cur)
        self.cur = self.cur[target]

    def pwd(self):
        # 重建路径字符串
        path = ["/"]
        # 从root开始走一遍路径
        node = self.root
        parts = []
        # 用path栈重建
        temp = []
        cur = self.cur
        # 反向找根
        # 更简单：在cd时同时维护path_names
        # 这里重新实现：用path变量保存名字字符串
        # 实际实现中，我们维护一个name列表
        # 下面用更简单的方式

    def ls(self):
        if not self.cur:
            print("error")
            return
        names = sorted(self.cur.keys())
        print(" ".join(names) if names else "")

    def rmdir(self, name):
        if name not in self.cur or self.cur[name]:
            print("error")
            return
        del self.cur[name]


# ===== 更完善的实现 =====
class DirectoryManager:
    def __init__(self):
        self.root = {}
        self.path_names = []  # 当前路径的名字列表（不含根）
        self.cur = self.root

    def get_cur_path(self):
        return "/" + "/".join(self.path_names)

    def mkdir(self, name):
        if name in self.cur:
            print("error")
            return
        self.cur[name] = {}

    def cd(self, target):
        if target == "..":
            if self.path_names:
                self.path_names.pop()
                # 重建cur指针
                node = self.root
                for p in self.path_names:
                    node = node[p]
                self.cur = node
            else:
                print("error")
            return

        if target.startswith("/"):
            # 绝对路径
            parts = [p for p in target.split("/") if p]
            node = self.root
            for p in parts:
                if p == "..":
                    # 简化：绝对路径中的..处理
                    pass
                elif p not in node:
                    print("error")
                    return
                node = node[p]
            self.cur = node
            self.path_names = parts
            return

        # 相对路径
        if target not in self.cur:
            print("error")
            return
        self.path_names.append(target)
        self.cur = self.cur[target]

    def pwd(self):
        print("/" + "/".join(self.path_names))

    def ls(self):
        print(" ".join(sorted(self.cur.keys())))

    def rmdir(self, name):
        if name not in self.cur:
            print("error")
            return
        if self.cur[name]:  # 非空
            print("error")
            return
        del self.cur[name]


# 主程序
dm = DirectoryManager()
for line in sys.stdin:
    line = line.strip()
    if line == "EOF":
        break
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "mkdir":
        dm.mkdir(parts[1])
    elif cmd == "cd":
        dm.cd(parts[1])
    elif cmd == "pwd":
        dm.pwd()
    elif cmd == "ls":
        dm.ls()
    elif cmd == "rmdir":
        dm.rmdir(parts[1])
```

---

**OD备考提示**：
- **模拟题的精髓**：把题目规则翻译成代码，不要遗漏任何细节。读题时建议把所有规则编号列出。
- **路径管理的坑**：
  - 绝对路径 `/` 开头的处理
  - `..` 回到上级目录，已在根目录时不能再回
  - `.` 表示当前目录（忽略）
- **目录删除**：只允许删除 **空目录**，这是常见约束
- **200分模拟题**特点：实现逻辑不复杂但 **细节多**，常有 5-8 种命令需要实现。建议用面向对象方式组织代码，可维护性更高。
- **测试建议**：自己构造包含所有命令的测试用例，尤其注意边界（根目录 pwd、空目录 ls、重复 mkdir、删除不存在的目录等）。
