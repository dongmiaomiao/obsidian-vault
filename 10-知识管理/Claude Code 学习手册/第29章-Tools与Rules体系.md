---
title: "第 29 章：Tools 与 Rules 体系"
type: chapter
part: "第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins"
source: "Claude Code 学习手册"
aliases:
---

第 29 章：Tools 与 Rules 体系

所属篇章：第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

把 Claude Code 的工具能力和规则约束放在同一张地图里，帮助读者理解“能做什么”和“该怎么做”的区别。

本章提供工具和规则的统一视角。工具决定 Claude Code 能做什么，规则决定它应该如何做，权限决定它被允许做什么。读者要建立自己的工具速查和权限边界文档。

学习目标

• 理解“Tools 与 Rules 体系”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-29"

claude "基于本章主题“Tools 与 Rules 体系”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-29

claude "基于本章主题“Tools 与 Rules 体系”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：using System;using System.IO;public static class ProjectInspector{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);Console.WriteLine($"Path: {fullPath}");Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");}

}

ProjectInspector.Summarize("README.md");

• 29.1 工具系统全景

• 29.1.1 读取类工具

• 29.1.2 搜索类工具

• 29.1.3 编辑类工具

• 29.1.4 执行类工具

• 29.2 Rules 指令规则

• 29.2.1 编码规则

• 29.2.2 测试规则

• 29.2.3 提交规则

• 29.3 权限规则

• 29.3.1 可读范围

• 29.3.2 可写范围

• 29.3.3 可执行命令

• 29.4 工具百科入口

• 29.4.1 常用工具速查

• 29.4.2 风险等级

• 29.4.3 示例命令

29.1 工具系统全景

学习目标

• 理解 工具系统全景 在本章主题中的具体作用。

• 能把 工具系统全景 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：读取类工具、搜索类工具、编辑类工具。

核心概念

工具系统全景 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 29.1.1 读取类工具：先解释它解决的问题，再给出一个可观察的操作。

• 29.1.2 搜索类工具：先解释它解决的问题，再给出一个可观察的操作。

• 29.1.3 编辑类工具：先解释它解决的问题，再给出一个可观察的操作。

• 29.1.4 执行类工具：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-29"

claude "只围绕“工具系统全景”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-29

claude "只围绕“工具系统全景”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 工具系统全景 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 工具系统全景 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

29.2 Rules 指令规则

学习目标

• 理解 Rules 指令规则 在本章主题中的具体作用。

• 能把 Rules 指令规则 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：编码规则、测试规则、提交规则。

核心概念

Rules 指令规则 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 29.2.1 编码规则：先解释它解决的问题，再给出一个可观察的操作。

• 29.2.2 测试规则：先解释它解决的问题，再给出一个可观察的操作。

• 29.2.3 提交规则：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-29"

claude "只围绕“Rules 指令规则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-29

claude "只围绕“Rules 指令规则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 Rules 指令规则 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Rules 指令规则 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

29.3 权限规则

学习目标

• 理解 权限规则 在本章主题中的具体作用。

• 能把 权限规则 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：可读范围、可写范围、可执行命令。

核心概念

权限规则 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 29.3.1 可读范围：先解释它解决的问题，再给出一个可观察的操作。

• 29.3.2 可写范围：先解释它解决的问题，再给出一个可观察的操作。

• 29.3.3 可执行命令：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-29"

claude "只围绕“权限规则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-29

claude "只围绕“权限规则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 权限规则 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 权限规则 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

29.4 工具百科入口

学习目标

• 理解 工具百科入口 在本章主题中的具体作用。

• 能把 工具百科入口 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：常用工具速查、风险等级、示例命令。

核心概念

工具百科入口 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 29.4.1 常用工具速查：先解释它解决的问题，再给出一个可观察的操作。

• 29.4.2 风险等级：先解释它解决的问题，再给出一个可观察的操作。

• 29.4.3 示例命令：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API 项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-29"

claude "只围绕“工具百科入口”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-29

claude "只围绕“工具百科入口”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 工具百科入口 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 工具百科入口 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查

常见问题

表现

处理方式

任务描述过宽Claude Code 一次读取过多文件或输出泛泛总结缩小范围，明确只处理一个小节或一个文件

常见问题

表现

处理方式

缺少验收标准看起来完成，但无法判断是否正确在提示词中加入测试、检查清单或输出格式忽略上下文边界模型引用无关资料或过期规则要求列出依据文件，并清理无关上下文没有记录结果下次还要重新解释同一规则将有效流程沉淀到 Markdown、命令或 Skill 中本章案例与练习

• 案例：记录一次任务中的工具调用链。

• 练习：把工具按读、写、执行、搜索分类。

• 练习：为项目写最小权限规则。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• docs/tool-reference.md

• docs/rules-reference.md

• 工具风险等级表

本章检查清单

• [ ] 我已经完成第 29 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Tools 与 Rules 体系”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接下一章将进入“Skill、Agent、MCP、Plugin 的组合模式”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skills

