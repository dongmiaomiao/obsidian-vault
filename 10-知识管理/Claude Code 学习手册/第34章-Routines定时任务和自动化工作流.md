---
title: "第 34 章：Routines、定时任务和自动化工作流"
type: chapter
part: "第七篇：自动化、GitHub、CI 和可编程 Agent"
source: "Claude Code 学习手册"
aliases:
---

第 34 章：Routines、定时任务和自动化工作流

所属篇章：第七篇：自动化、GitHub、CI 和可编程 Agent

主案例语言：Python

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者把重复检查、总结和报告转化为可治理的例行自动化。

本章强调自动化需要治理。Routine 适合做周期性总结和检查，但不适合在没有审核的情况下做破坏性操

作。读者要建立自动化清单，知道哪些任务在运行、何时运行、输出到哪里。

学习目标

• 理解“Routines、定时任务和自动化工作流”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 Python 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 Python 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-34"

claude "基于本章主题“Routines、定时任务和自动化工作流”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-34

claude "基于本章主题“Routines、定时任务和自动化工作流”，设计一个最小可执行案例，并给出验证清单。"

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

• 34.1 Routine 思维

• 34.1.1 重复任务识别Claude Code 学习手册

• 34.1.2 固定输入和固定输出

• 34.1.3 触发频率

• 34.2 定时检查

• 34.2.1 依赖检查

• 34.2.2 测试状态检查

• 34.2.3 文档健康检查

• 34.3 目标与通道

• 34.3.1 输出到报告

• 34.3.2 输出到当前线程

• 34.3.3 不直接做高风险修改

• 34.4 自动化治理

• 34.4.1 自动化清单

• 34.4.2 暂停条件

• 34.4.3 复盘和调整

34.1 Routine 思维

学习目标

• 理解 Routine 思维 在本章主题中的具体作用。

• 能把 Routine 思维 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：重复任务识别、固定输入和固定输出、触发频率。

核心概念

Routine 思维 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 34.1.1 重复任务识别：先解释它解决的问题，再给出一个可观察的操作。

• 34.1.2 固定输入和固定输出：先解释它解决的问题，再给出一个可观察的操作。

• 34.1.3 触发频率：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。Claude Code 学习手册

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-34"

claude "只围绕“Routine 思维”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-34

claude "只围绕“Routine 思维”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 Routine 思维 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Routine 思维 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

34.2 定时检查

学习目标

• 理解 定时检查 在本章主题中的具体作用。

• 能把 定时检查 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：依赖检查、测试状态检查、文档健康检查。

核心概念Claude Code 学习手册

定时检查 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 34.2.1 依赖检查：先解释它解决的问题，再给出一个可观察的操作。

• 34.2.2 测试状态检查：先解释它解决的问题，再给出一个可观察的操作。

• 34.2.3 文档健康检查：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-34"

claude "只围绕“定时检查”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-34

claude "只围绕“定时检查”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 定时检查 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 定时检查 解决什么问题。Claude Code 学习手册

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

34.3 目标与通道

学习目标

• 理解 目标与通道 在本章主题中的具体作用。

• 能把 目标与通道 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：输出到报告、输出到当前线程、不直接做高风险修改。

核心概念

目标与通道 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 34.3.1 输出到报告：先解释它解决的问题，再给出一个可观察的操作。

• 34.3.2 输出到当前线程：先解释它解决的问题，再给出一个可观察的操作。

• 34.3.3 不直接做高风险修改：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-34"

claude "只围绕“目标与通道”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-34

claude "只围绕“目标与通道”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 目标与通道 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 目标与通道 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

34.4 自动化治理

学习目标

• 理解 自动化治理 在本章主题中的具体作用。

• 能把 自动化治理 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：自动化清单、暂停条件、复盘和调整。

核心概念

自动化治理 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 34.4.1 自动化清单：先解释它解决的问题，再给出一个可观察的操作。

• 34.4.2 暂停条件：先解释它解决的问题，再给出一个可观察的操作。

• 34.4.3 复盘和调整：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。Claude Code 学习手册

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-34"

claude "只围绕“自动化治理”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-34

claude "只围绕“自动化治理”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 自动化治理 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 自动化治理 解决什么问题。

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

• 案例：设计每周项目质量巡检。

• 练习：写一个每日待办总结任务。

• 练习：为自动化写暂停条件。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• docs/routines.md

• 周期性质量巡检模板

• 自动化治理清单

本章检查清单

• [ ] 我已经完成第 34 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Routines、定时任务和自动化工作流”建立了一套可执行学习流程。真正的掌握标准不是记住概

念，而是能让 Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“GitHub PR / CI 工作流”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

310Claude Code 学习手册

