---
title: "第 22 章：Skills 基础"
type: chapter
part: "第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins"
source: "Claude Code 学习手册"
aliases:
---

第 22 章：Skills 基础

所属篇章：第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins

主案例语言：Python

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者掌握 Skill 的用途和最小结构，把重复知识和流程封装成可复用能力。

本章从一个最小 SKILL.md 开始，解释 Skill 的触发依赖描述，而不是靠用户每次手动复制长提示。随后加入引用资料和模板，展示渐进式披露如何节省 token。

学习目标

• 理解“Skills 基础”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 Python 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 Python 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-22"

claude "基于本章主题“Skills 基础”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-22

claude "基于本章主题“Skills 基础”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),"exists": target.exists(),"suffix": target.suffix,}

if __name__ == "__main__":

print(summarize_target("README.md"))

• 22.1 Skill 解决什么问题

• 22.1.1 重复任务

• 22.1.2 专业知识

• 22.1.3 团队标准

• 22.2 SKILL.md 结构

• 22.2.1 名称和描述

• 22.2.2 使用步骤

• 22.2.3 资源文件引用

• 22.3 渐进式披露

• 22.3.1 主文件保持短小

• 22.3.2 详细规则放入 references/

• 22.3.3 模板放入 templates/

• 22.4 Skill 案例

• 22.4.1 代码审查 Skill

• 22.4.2 API 文档 Skill

• 22.4.3 团队规范 Skill

22.1 Skill 解决什么问题

学习目标

• 理解 Skill 解决什么问题 在本章主题中的具体作用。

• 能把 Skill 解决什么问题 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：重复任务、专业知识、团队标准。

核心概念

Skill 解决什么问题 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 22.1.1 重复任务：先解释它解决的问题，再给出一个可观察的操作。

• 22.1.2 专业知识：先解释它解决的问题，再给出一个可观察的操作。

• 22.1.3 团队标准：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI 或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-22"

claude "只围绕“Skill 解决什么问题”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-22

claude "只围绕“Skill 解决什么问题”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),"exists": target.exists(),"suffix": target.suffix,}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Skill 解决什么问题 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Skill 解决什么问题 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

22.2 SKILL.md 结构

学习目标

• 理解 SKILL.md 结构 在本章主题中的具体作用。

• 能把 SKILL.md 结构 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：名称和描述、使用步骤、资源文件引用。

核心概念

SKILL.md 结构 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 22.2.1 名称和描述：先解释它解决的问题，再给出一个可观察的操作。

• 22.2.2 使用步骤：先解释它解决的问题，再给出一个可观察的操作。

• 22.2.3 资源文件引用：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI 或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-22"

claude "只围绕“`SKILL.md` 结构”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-22

claude "只围绕“`SKILL.md` 结构”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),"exists": target.exists(),"suffix": target.suffix,}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 SKILL.md 结构 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 SKILL.md 结构 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

22.3 渐进式披露

学习目标

• 理解 渐进式披露 在本章主题中的具体作用。

• 能把 渐进式披露 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：主文件保持短小、详细规则放入 references/、模板放入 templates/。

核心概念

渐进式披露 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 22.3.1 主文件保持短小：先解释它解决的问题，再给出一个可观察的操作。

• 22.3.2 详细规则放入 references/：先解释它解决的问题，再给出一个可观察的操作。

• 22.3.3 模板放入 templates/：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI 或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-22"

claude "只围绕“渐进式披露”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-22

claude "只围绕“渐进式披露”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),

"exists": target.exists(),"suffix": target.suffix,}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 渐进式披露 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 渐进式披露 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

22.4 Skill 案例

学习目标

• 理解 Skill 案例 在本章主题中的具体作用。

• 能把 Skill 案例 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：代码审查 Skill、API 文档 Skill、团队规范 Skill。

核心概念

Skill 案例 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 22.4.1 代码审查 Skill：先解释它解决的问题，再给出一个可观察的操作。

• 22.4.2 API 文档 Skill：先解释它解决的问题，再给出一个可观察的操作。

• 22.4.3 团队规范 Skill：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 Python。用一个小型 Python CLI 或脚本项目作为观察对象，重点展示文件读取、测试和自动化流程。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-22"

claude "只围绕“Skill 案例”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-22

claude "只围绕“Skill 案例”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

from pathlib import Path

PROJECT_ROOT = Path.cwd()

def summarize_target(path: str) -> dict:

target = PROJECT_ROOT / path

return {

"path": str(target),"exists": target.exists(),"suffix": target.suffix,}

if __name__ == "__main__":

print(summarize_target("README.md"))

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Skill 案例 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Skill 案例 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查

常见问题

表现

处理方式

任务描述过宽Claude Code 一次读取过多文件或输出泛泛总结缩小范围，明确只处理一个小节或一个文件缺少验收标准看起来完成，但无法判断是否正确在提示词中加入测试、检查清单或输出格式忽略上下文边界模型引用无关资料或过期规则要求列出依据文件，并清理无关上下文没有记录结果下次还要重新解释同一规则将有效流程沉淀到 Markdown、命令或 Skill 中本章案例与练习

• 案例：创建 code-reviewing/SKILL.md。

• 练习：把长规则拆成 references/。

• 练习：用 Skill 生成一份 API 文档。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• .claude/skills/code-reviewing/SKILL.md

• .claude/skills/api-documenting/SKILL.md

• Skill 设计检查清单

本章检查清单

• [ ] 我已经完成第 22 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Skills 基础”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接下一章将进入“自定义命令与任务型 Skill”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skills

