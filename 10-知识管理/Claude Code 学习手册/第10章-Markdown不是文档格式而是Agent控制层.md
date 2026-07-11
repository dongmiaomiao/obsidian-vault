---
title: "第 10 章：Markdown 不是文档格式，而是 Agent"
type: chapter
part: "第二篇：日常开发工作流 - 先把 Claude Code 用顺手"
source: "Claude Code 学习手册"
aliases:
---

第 10 章：Markdown 不是文档格式，而是 Agent

控制层

所属篇章：第三篇：Markdown、记忆和本地知识库

主案例语言：Python

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者理解 Markdown 在 Claude Code 中不仅是给人看的文档，也是给 Agent

读取、遵守和执行的控制层。

本章以重写一段混乱项目说明为主线。读者先学习写给 Agent 的 Markdown

应该短、准、可执行，再把项目说明、规则、命令、文档索引分层。重点说明 Markdown

的质量会直接影响 Claude Code 的行为稳定性。

学习目标

• 理解“Markdown 不是文档格式，而是 Agent 控制层”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 Python 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 Python 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-10"

claude "基于本章主题“Markdown 不是文档格式，而是 Agent 控制层”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-10

claude "基于本章主题“Markdown 不是文档格式，而是 Agent 控制层”，设计一个最小可执行案例，并给出验证清单。"

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

print(summarize_target("README.md"))Claude Code 学习手册

目录

• 10.1 Markdown 基础够用版

• 10.1.1 标题层级

• 10.1.2 列表、代码块和表格

• 10.1.3 链接和文件路径

• 10.2 写给人和写给 Agent 的区别

• 10.2.1 人类说明可以含糊

• 10.2.2 Agent 规则必须可执行

• 10.2.3 必须、禁止、建议、例外

• 10.3 文档分层

• 10.3.1 README.md

• 10.3.2 CLAUDE.md

• 10.3.3 docs/rules/

• 10.4 文档老化问题

• 10.4.1 文档与代码不一致

• 10.4.2 文档过长导致模型忽略重点

• 10.4.3 建立文档更新机制

10.1 Markdown 基础够用版

学习目标

• 理解 Markdown 基础够用版 在本章主题中的具体作用。

• 能把 Markdown 基础够用版 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：标题层级、列表、代码块和表格、链接和文件路径。

核心概念

Markdown 基础够用版 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 10.1.1 标题层级：先解释它解决的问题，再给出一个可观察的操作。

• 10.1.2 列表、代码块和表格：先解释它解决的问题，再给出一个可观察的操作。

• 10.1.3 链接和文件路径：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤Claude Code 学习手册

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-10"

claude "只围绕“Markdown 基础够用版”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-10

claude "只围绕“Markdown 基础够用版”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 Markdown 基础够用版 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Markdown 基础够用版 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

10.2 写给人和写给 Agent 的区别

学习目标

• 理解 写给人和写给 Agent 的区别 在本章主题中的具体作用。

• 能把 写给人和写给 Agent 的区别 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。Claude Code 学习手册

• 能说明本节三个重点：人类说明可以含糊、Agent 规则必须可执行、必须、禁止、建议、例外。

核心概念

写给人和写给 Agent 的区别 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude

Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 10.2.1 人类说明可以含糊：先解释它解决的问题，再给出一个可观察的操作。

• 10.2.2 Agent 规则必须可执行：先解释它解决的问题，再给出一个可观察的操作。

• 10.2.3 必须、禁止、建议、例外：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-10"

claude "只围绕“写给人和写给 Agent 的区别”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-10

claude "只围绕“写给人和写给 Agent 的区别”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 写给人和写给 Agent 的区别 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。Claude Code 学习手册

检查清单

• [ ] 我能用自己的话解释 写给人和写给 Agent 的区别 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

10.3 文档分层

学习目标

• 理解 文档分层 在本章主题中的具体作用。

• 能把 文档分层 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：README.md、CLAUDE.md、docs/rules/。

核心概念

文档分层 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 10.3.1 README.md：先解释它解决的问题，再给出一个可观察的操作。

• 10.3.2 CLAUDE.md：先解释它解决的问题，再给出一个可观察的操作。

• 10.3.3 docs/rules/：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-10"

claude "只围绕“文档分层”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-10

claude "只围绕“文档分层”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()Claude Code 学习手册

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

• 练习 1：把 文档分层 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 文档分层 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

10.4 文档老化问题

学习目标

• 理解 文档老化问题 在本章主题中的具体作用。

• 能把 文档老化问题 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：文档与代码不一致、文档过长导致模型忽略重点、建立文档更新机制。

核心概念

文档老化问题 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 10.4.1 文档与代码不一致：先解释它解决的问题，再给出一个可观察的操作。

• 10.4.2 文档过长导致模型忽略重点：先解释它解决的问题，再给出一个可观察的操作。

• 10.4.3 建立文档更新机制：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI

或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。Claude Code 学习手册

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-10"

claude "只围绕“文档老化问题”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-10

claude "只围绕“文档老化问题”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 文档老化问题 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 文档老化问题 解决什么问题。

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

中Claude Code 学习手册

本章案例与练习

• 案例：把一段口语化项目规范改成结构化 Markdown。

• 练习：将规则标注为“必须、禁止、建议、例外”。

• 练习：检查一个文档是否适合给 Agent 读取。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• docs/markdown-for-agent.md

• Markdown 写作检查清单

• 一份改写后的项目规则文档

本章检查清单

• [ ] 我已经完成第 10 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Markdown 不是文档格式，而是 Agent

控制层”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code

在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“CLAUDE.md 记忆系统”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

94Claude Code 学习手册

