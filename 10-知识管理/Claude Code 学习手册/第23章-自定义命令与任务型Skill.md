---
title: "第 23 章：自定义命令与任务型 Skill"
type: chapter
part: "第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins"
source: "Claude Code 学习手册"
aliases:
---

第 23 章：自定义命令与任务型 Skill

所属篇章：第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者掌握 slash command 的使用场景，并理解命令与 Skill 的边界。

本章把常用任务从提示词模板升级为命令。读者要知道命令适合固定流程，比如审查diff、生成提交说明、解释文件；Skill 适合需要长期知识、规范和模板的任务。

学习目标

• 理解“自定义命令与任务型 Skill”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-23"

claude "基于本章主题“自定义命令与任务型 Skill”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-23

claude "基于本章主题“自定义命令与任务型 Skill”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");

• 23.1 Slash Commands

• 23.1.1 /review

• 23.1.2 /commit

• 23.1.3 /explain

• 23.2 命令与 Skill 的区别

• 23.2.1 固定流程用命令

• 23.2.2 专业知识用 Skill

• 23.2.3 复杂组合谨慎设计

• 23.3 参数化命令

• 23.3.1 文件路径参数

• 23.3.2 输出格式参数

• 23.3.3 默认行为和错误提示

• 23.4 命令库管理

• 23.4.1 .claude/commands/

• 23.4.2 命令分组

• 23.4.3 命令索引文档

23.1 Slash Commands

学习目标

• 理解 Slash Commands 在本章主题中的具体作用。

• 能把 Slash Commands 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：/review、/commit、/explain。

核心概念

Slash Commands 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 23.1.1 /review：先解释它解决的问题，再给出一个可观察的操作。

• 23.1.2 /commit：先解释它解决的问题，再给出一个可观察的操作。

• 23.1.3 /explain：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-23"

claude "只围绕“Slash Commands”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-23

claude "只围绕“Slash Commands”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Slash Commands 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Slash Commands 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

23.2 命令与 Skill 的区别

学习目标

• 理解 命令与 Skill 的区别 在本章主题中的具体作用。

• 能把 命令与 Skill 的区别 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：固定流程用命令、专业知识用 Skill、复杂组合谨慎设计。

核心概念

命令与 Skill 的区别 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 23.2.1 固定流程用命令：先解释它解决的问题，再给出一个可观察的操作。

• 23.2.2 专业知识用 Skill：先解释它解决的问题，再给出一个可观察的操作。

• 23.2.3 复杂组合谨慎设计：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-23"

claude "只围绕“命令与 Skill 的区别”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-23

claude "只围绕“命令与 Skill 的区别”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 命令与 Skill 的区别 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 命令与 Skill 的区别 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

23.3 参数化命令

学习目标

• 理解 参数化命令 在本章主题中的具体作用。

• 能把 参数化命令 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：文件路径参数、输出格式参数、默认行为和错误提示。

核心概念

参数化命令 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 23.3.1 文件路径参数：先解释它解决的问题，再给出一个可观察的操作。

• 23.3.2 输出格式参数：先解释它解决的问题，再给出一个可观察的操作。

• 23.3.3 默认行为和错误提示：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-23"

claude "只围绕“参数化命令”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-23

claude "只围绕“参数化命令”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 参数化命令 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 参数化命令 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

23.4 命令库管理

学习目标

• 理解 命令库管理 在本章主题中的具体作用。

• 能把 命令库管理 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：.claude/commands/、命令分组、命令索引文档。

核心概念

命令库管理 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 23.4.1 .claude/commands/：先解释它解决的问题，再给出一个可观察的操作。

• 23.4.2 命令分组：先解释它解决的问题，再给出一个可观察的操作。

• 23.4.3 命令索引文档：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-23"

claude "只围绕“命令库管理”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-23

claude "只围绕“命令库管理”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 命令库管理 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 命令库管理 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查

常见问题

表现

处理方式

任务描述过宽Claude Code 一次读取过多文件或输出泛泛总结缩小范围，明确只处理一个小节或一个文件缺少验收标准看起来完成，但无法判断是否正确在提示词中加入测试、检查清单或输出格式忽略上下文边界模型引用无关资料或过期规则要求列出依据文件，并清理无关上下文没有记录结果下次还要重新解释同一规则将有效流程沉淀到 Markdown、命令或 Skill 中

本章案例与练习

• 案例：创建 /review、/commit、/todo 三个命令。

• 练习：给 /analyze 添加路径参数。

• 练习：把一个复杂命令改造成 Skill。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• .claude/commands/review.md

• .claude/commands/commit.md

• .claude/commands/explain.md

• 命令库索引

本章检查清单

• [ ] 我已经完成第 23 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“自定义命令与任务型Skill”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接下一章将进入“SubAgents 基础”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skills

