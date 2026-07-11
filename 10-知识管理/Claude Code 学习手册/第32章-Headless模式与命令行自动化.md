---
title: "第 32 章：Headless 模式与命令行自动化"
type: chapter
part: "第七篇：自动化、GitHub、CI 和可编程 Agent"
source: "Claude Code 学习手册"
aliases:
---

第 32 章：Headless 模式与命令行自动化

所属篇章：第七篇：自动化、GitHub、CI 和可编程 Agent

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者理解如何在非交互场景中调用 Claude Code 处理重复任务。

本章把 Claude Code 从“人坐在终端前对话”扩展到脚本化调用。重点是输出格式、权限边界和可重复运行，不鼓励无人值守直接修改生产代码。

学习目标

• 理解“Headless 模式与命令行自动化”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-32"

claude "基于本章主题“Headless 模式与命令行自动化”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-32

claude "基于本章主题“Headless 模式与命令行自动化”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");

• 32.1 Headless 是什么

• 32.1.1 交互模式与非交互模式

• 32.1.2 适合自动化的任务

• 32.1.3 不适合自动化的任务

• 32.2 批处理任务

• 32.2.1 批量检查文件

• 32.2.2 批量生成摘要

• 32.2.3 批量生成报告

• 32.3 输出格式

• 32.3.1 Markdown 报告

• 32.3.2 JSON 输出

• 32.3.3 可解析错误信息

• 32.4 自动化边界

• 32.4.1 只读自动化优先

• 32.4.2 写操作需要确认

• 32.4.3 自动化日志和审计

32.1 Headless 是什么

学习目标

• 理解 Headless 是什么 在本章主题中的具体作用。

• 能把 Headless 是什么 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：交互模式与非交互模式、适合自动化的任务、不适合自动化的任务。

核心概念

Headless 是什么 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 32.1.1 交互模式与非交互模式：先解释它解决的问题，再给出一个可观察的操作。

• 32.1.2 适合自动化的任务：先解释它解决的问题，再给出一个可观察的操作。

• 32.1.3 不适合自动化的任务：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-32"

claude "只围绕“Headless 是什么”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-32

claude "只围绕“Headless 是什么”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 Headless 是什么 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Headless 是什么 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

32.2 批处理任务

学习目标

• 理解 批处理任务 在本章主题中的具体作用。

• 能把 批处理任务 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：批量检查文件、批量生成摘要、批量生成报告。

核心概念

批处理任务 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 32.2.1 批量检查文件：先解释它解决的问题，再给出一个可观察的操作。

• 32.2.2 批量生成摘要：先解释它解决的问题，再给出一个可观察的操作。

• 32.2.3 批量生成报告：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-32"

claude "只围绕“批处理任务”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-32

claude "只围绕“批处理任务”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 批处理任务 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 批处理任务 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

32.3 输出格式

学习目标

• 理解 输出格式 在本章主题中的具体作用。

• 能把 输出格式 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：Markdown 报告、JSON 输出、可解析错误信息。

核心概念

输出格式 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 32.3.1 Markdown 报告：先解释它解决的问题，再给出一个可观察的操作。

• 32.3.2 JSON 输出：先解释它解决的问题，再给出一个可观察的操作。

• 32.3.3 可解析错误信息：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-32"

claude "只围绕“输出格式”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-32

claude "只围绕“输出格式”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 输出格式 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 输出格式 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

32.4 自动化边界

学习目标

• 理解 自动化边界 在本章主题中的具体作用。

• 能把 自动化边界 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：只读自动化优先、写操作需要确认、自动化日志和审计。

核心概念

自动化边界 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 32.4.1 只读自动化优先：先解释它解决的问题，再给出一个可观察的操作。

• 32.4.2 写操作需要确认：先解释它解决的问题，再给出一个可观察的操作。

• 32.4.3 自动化日志和审计：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-32"

claude "只围绕“自动化边界”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-32

claude "只围绕“自动化边界”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 自动化边界 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 自动化边界 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查

常见问题

表现

处理方式

任务描述过宽Claude Code 一次读取过多文件或输出泛泛总结缩小范围，明确只处理一个小节或一个文件缺少验收标准看起来完成，但无法判断是否正确在提示词中加入测试、检查清单或输出格式忽略上下文边界模型引用无关资料或过期规则要求列出依据文件，并清理无关上下文没有记录结果下次还要重新解释同一规则将有效流程沉淀到 Markdown、命令或 Skill 中

本章案例与练习

• 案例：批量为多个模块生成文档质量报告。

• 练习：要求输出 JSON 并验证可解析。

• 练习：设计只读自动化流程。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• scripts/claude-doc-check.md

• 自动化输出格式规范

• Headless 使用边界清单

本章检查清单

• [ ] 我已经完成第 32 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Headless 模式与命令行自动化”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接下一章将进入“Agent SDK 入门”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skills

