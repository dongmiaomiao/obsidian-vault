---
title: "第 1 章：为什么 Claude Code 不只是聊天机器人"
type: chapter
part: "第一篇：入门地图 - 从 AI Agent 到 Claude Code"
source: "Claude Code 学习手册"
aliases:
---

第 1 章：为什么 Claude Code 不只是聊天机器人

所属篇章：第一篇：入门地图 - 从 AI Agent 到 Claude Code

主案例语言：Python

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

帮助读者建立第一个正确心智模型：Claude Code

是能读取项目、调用工具、修改文件、运行命令并受权限约束的 AI 编码

Agent，不是只回答问题的聊天窗口。

本章先用一个简单函数分析任务展示聊天模型和 Claude Code 的区别，再解释 Claude Code 的核心闭环

：理解目标、探索项目、使用工具、修改文件、验证结果、总结交付。重点强调“上下文不是魔法”“权限不

是麻烦”“验证不是可选项”。读者应明白，后续所有高级功能都建立在这个闭环之上。

学习目标

• 理解“为什么 Claude Code 不只是聊天机器人”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 Python 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 Python 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-01"

claude "基于本章主题“为什么 Claude Code 不只是聊天机器人”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-01

claude "基于本章主题“为什么 Claude Code 不只是聊天机器人”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),

"exists": target.exists(),

"suffix": target.suffix,

}

if __name__ == "__main__":

print(summarize_target("README.md"))

目录Claude Code 学习手册

• 1.1 AI Chat、AI Agent、AI 编码 Agent 的区别

• 1.1.1 普通聊天模型能做什么

• 1.1.2 AI Agent 多了哪些能力

• 1.1.3 AI 编码 Agent 为什么需要文件系统、命令行和权限

• 1.2 Claude Code 的核心工作方式

• 1.2.1 用户目标如何变成模型任务

• 1.2.2 模型如何选择读取、搜索、编辑、执行命令

• 1.2.3 工具结果如何反过来影响下一步决策

• 1.3 新手最容易误解的地方

• 1.3.1 以为模型天然知道整个项目

• 1.3.2 以为说一句“帮我修好”就足够

• 1.3.3 以为 AI 修改代码不需要验证

• 1.4 本书的学习方法

• 1.4.1 每章先做一个小任务

• 1.4.2 用检查清单判断是否真正掌握

• 1.4.3 把成功经验写回 Markdown 和规则文件

1.1 AI Chat、AI Agent、AI 编码 Agent 的区别

学习目标

• 理解 AI Chat、AI Agent、AI 编码 Agent 的区别 在本章主题中的具体作用。

• 能把 AI Chat、AI Agent、AI 编码 Agent 的区别 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：普通聊天模型能做什么、AI Agent 多了哪些能力、AI 编码 Agent

为什么需要文件系统、命令行和权限。

核心概念

AI Chat、AI Agent、AI 编码 Agent 的区别

的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 1.1.1 普通聊天模型能做什么：先解释它解决的问题，再给出一个可观察的操作。

• 1.1.2 AI Agent 多了哪些能力：先解释它解决的问题，再给出一个可观察的操作。

• 1.1.3 AI 编码 Agent

为什么需要文件系统、命令行和权限：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。Claude Code 学习手册

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-01"

claude "只围绕“AI Chat、AI Agent、AI 编码 Agent 的区别”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-01

claude "只围绕“AI Chat、AI Agent、AI 编码 Agent 的区别”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),

"exists": target.exists(),

"suffix": target.suffix,

}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 AI Chat、AI Agent、AI 编码 Agent 的区别

改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 AI Chat、AI Agent、AI 编码 Agent 的区别 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

1.2 Claude Code 的核心工作方式

学习目标

• 理解 Claude Code 的核心工作方式 在本章主题中的具体作用。Claude Code 学习手册

• 能把 Claude Code 的核心工作方式 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：用户目标如何变成模型任务、模型如何选择读取、搜索、编辑、执行命令、工

具结果如何反过来影响下一步决策。

核心概念

Claude Code 的核心工作方式 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude

Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 1.2.1 用户目标如何变成模型任务：先解释它解决的问题，再给出一个可观察的操作。

• 1.2.2 模型如何选择读取、搜索、编辑、执行命令：先解释它解决的问题，再给出一个可观察的操作。

• 1.2.3 工具结果如何反过来影响下一步决策：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-01"

claude "只围绕“Claude Code 的核心工作方式”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-01

claude "只围绕“Claude Code 的核心工作方式”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),

"exists": target.exists(),

"suffix": target.suffix,

}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习Claude Code 学习手册

• 练习 1：把 Claude Code 的核心工作方式 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Claude Code 的核心工作方式 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

1.3 新手最容易误解的地方

学习目标

• 理解 新手最容易误解的地方 在本章主题中的具体作用。

• 能把 新手最容易误解的地方 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：以为模型天然知道整个项目、以为说一句“帮我修好”就足够、以为 AI

修改代码不需要验证。

核心概念

新手最容易误解的地方 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 1.3.1 以为模型天然知道整个项目：先解释它解决的问题，再给出一个可观察的操作。

• 1.3.2 以为说一句“帮我修好”就足够：先解释它解决的问题，再给出一个可观察的操作。

• 1.3.3 以为 AI 修改代码不需要验证：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-01"

claude "只围绕“新手最容易误解的地方”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-01

claude "只围绕“新手最容易误解的地方”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"Claude Code 学习手册

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),

"exists": target.exists(),

"suffix": target.suffix,

}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 新手最容易误解的地方 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 新手最容易误解的地方 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

1.4 本书的学习方法

学习目标

• 理解 本书的学习方法 在本章主题中的具体作用。

• 能把 本书的学习方法 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：每章先做一个小任务、用检查清单判断是否真正掌握、把成功经验写回

Markdown 和规则文件。

核心概念

本书的学习方法 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 1.4.1 每章先做一个小任务：先解释它解决的问题，再给出一个可观察的操作。

• 1.4.2 用检查清单判断是否真正掌握：先解释它解决的问题，再给出一个可观察的操作。

• 1.4.3 把成功经验写回 Markdown 和规则文件：先解释它解决的问题，再给出一个可观察的操作。Claude Code 学习手册

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-01"

claude "只围绕“本书的学习方法”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-01

claude "只围绕“本书的学习方法”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),

"exists": target.exists(),

"suffix": target.suffix,

}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 本书的学习方法 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 本书的学习方法 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查Claude Code 学习手册

常见问题

表现

处理方式

任务描述过宽

Claude Code

一次读取过多文件或输出泛泛总结

缩小范围，明确只处理一个小节或一个文件

缺少验收标准

看起来完成，但无法判断是否正确

在提示词中加入测试、检查清单或输出格式

忽略上下文边界

模型引用无关资料或过期规则

要求列出依据文件，并清理无关上下文

没有记录结果

下次还要重新解释同一规则

将有效流程沉淀到 Markdown、命令或 Skill

中

本章案例与练习

• 案例：同一个 Bug 让普通聊天模型和 Claude Code 分别分析，比较输出差异。

• 练习：写出 3 个 Claude Code 适合做、普通聊天模型不适合直接做的工程任务。

• 练习：画一张“用户、Claude Code、工具、项目文件、终端命令”的关系图。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• notes/01-agent-vs-chat.md

• 一张 Claude Code 工作闭环图

• 5 条个人使用 Claude Code 的基础原则

本章检查清单

• [ ] 我已经完成第 1 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“为什么 Claude Code

不只是聊天机器人”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code

在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“环境、账号、模型和第一个任务”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

13Claude Code 学习手册

