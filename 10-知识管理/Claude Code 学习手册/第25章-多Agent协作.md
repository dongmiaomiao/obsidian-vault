---
title: "第 25 章：多 Agent 协作"
type: chapter
part: "第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins"
source: "Claude Code 学习手册"
aliases:
---

第 25 章：多 Agent 协作

所属篇章：第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins

主案例语言：Python

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者从单个子代理升级到并行探索、流水线和 Agent Teams。

本章展示多 Agent 协作不是越多越好。并行探索适合互不依赖的分析任务，流水线适合上下游明确的任

务。读者要学会设计交接格式，让一个代理的输出能被下一个代理使用。

学习目标

• 理解“多 Agent 协作”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 Python 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 Python 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-25"

claude "基于本章主题“多 Agent 协作”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-25

claude "基于本章主题“多 Agent 协作”，设计一个最小可执行案例，并给出验证清单。"

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

目录

• 25.1 并行探索

• 25.1.1 API 视角Claude Code 学习手册

• 25.1.2 数据库视角

• 25.1.3 认证或权限视角

• 25.2 流水线编排

• 25.2.1 Bug 定位

• 25.2.2 Bug 修复

• 25.2.3 验证和报告

• 25.3 Agent Teams

• 25.3.1 reviewer

• 25.3.2 tester

• 25.3.3 doc-writer

• 25.4 多 Agent 成本控制

• 25.4.1 并行只用于独立任务

• 25.4.2 输出必须短而结构化

• 25.4.3 主会话负责整合

25.1 并行探索

学习目标

• 理解 并行探索 在本章主题中的具体作用。

• 能把 并行探索 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：API 视角、数据库视角、认证或权限视角。

核心概念

并行探索 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 25.1.1 API 视角：先解释它解决的问题，再给出一个可观察的操作。

• 25.1.2 数据库视角：先解释它解决的问题，再给出一个可观察的操作。

• 25.1.3 认证或权限视角：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。Claude Code 学习手册

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-25"

claude "只围绕“并行探索”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-25

claude "只围绕“并行探索”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 并行探索 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 并行探索 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

25.2 流水线编排

学习目标

• 理解 流水线编排 在本章主题中的具体作用。

• 能把 流水线编排 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：Bug 定位、Bug 修复、验证和报告。

核心概念Claude Code 学习手册

流水线编排 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 25.2.1 Bug 定位：先解释它解决的问题，再给出一个可观察的操作。

• 25.2.2 Bug 修复：先解释它解决的问题，再给出一个可观察的操作。

• 25.2.3 验证和报告：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-25"

claude "只围绕“流水线编排”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-25

claude "只围绕“流水线编排”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 流水线编排 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 流水线编排 解决什么问题。Claude Code 学习手册

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

25.3 Agent Teams

学习目标

• 理解 Agent Teams 在本章主题中的具体作用。

• 能把 Agent Teams 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：reviewer、tester、doc-writer。

核心概念

Agent Teams 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 25.3.1 reviewer：先解释它解决的问题，再给出一个可观察的操作。

• 25.3.2 tester：先解释它解决的问题，再给出一个可观察的操作。

• 25.3.3 doc-writer：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-25"

claude "只围绕“Agent Teams”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-25

claude "只围绕“Agent Teams”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),Claude Code 学习手册

"exists": target.exists(),

"suffix": target.suffix,

}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Agent Teams 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Agent Teams 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

25.4 多 Agent 成本控制

学习目标

• 理解 多 Agent 成本控制 在本章主题中的具体作用。

• 能把 多 Agent 成本控制 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：并行只用于独立任务、输出必须短而结构化、主会话负责整合。

核心概念

多 Agent 成本控制 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 25.4.1 并行只用于独立任务：先解释它解决的问题，再给出一个可观察的操作。

• 25.4.2 输出必须短而结构化：先解释它解决的问题，再给出一个可观察的操作。

• 25.4.3 主会话负责整合：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。Claude Code 学习手册

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-25"

claude "只围绕“多 Agent 成本控制”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-25

claude "只围绕“多 Agent 成本控制”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 多 Agent 成本控制 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 多 Agent 成本控制 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查

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

本章案例与练习Claude Code 学习手册

• 案例：三个探索代理分别分析 API、数据库、认证问题。

• 练习：设计 Bug 修复流水线。

• 练习：比较单 Agent 和多 Agent 的成本与效果。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• .claude/agents/api-explorer.md

• .claude/agents/db-explorer.md

• .claude/agents/auth-explorer.md

• docs/agent-pipeline.md

本章检查清单

• [ ] 我已经完成第 25 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“多 Agent 协作”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude

Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“Hooks 事件驱动自动化”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

229Claude Code 学习手册

