---
title: "第 17 章：驯服 Opus"
type: chapter
part: "第四篇：提示词、Opus 4.7 和模型驾驭"
source: "Claude Code 学习手册"
aliases:
---

第 17 章：驯服 Opus

4.7：模型、努力级别和思考预算

所属篇章：第四篇：提示词、Opus 4.7 和模型驾驭

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

帮助读者理解什么时候使用更强模型、更高努力级别和深度思考提示，而不是无差别消耗高成本资源。

本章从“任务价值”和“失败成本”角度讲模型选择。Opus 4.7 的使用重点放在复杂架构、跨模块 Bug、安全

风险和高价值决策上。读者要建立成本意识：简单文档修改不需要重型模型，复杂问题也不能只靠一句深

度思考提示。

学习目标

• 理解“驯服 Opus 4.7：模型、努力级别和思考预算”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-17"

claude "基于本章主题“驯服 Opus 4.7：模型、努力级别和思考预算”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-17

claude "基于本章主题“驯服 Opus 4.7：模型、努力级别和思考预算”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：

using System;

using System.IO;

public static class ProjectInspector

{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);

Console.WriteLine($"Path: {fullPath}");

Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");

}

}

ProjectInspector.Summarize("README.md");

目录Claude Code 学习手册

• 17.1 模型选择

• 17.1.1 简单任务与复杂任务

• 17.1.2 高风险任务与低风险任务

• 17.1.3 成本、速度和质量的权衡

• 17.2 Effort 与 Thinking

• 17.2.1 努力级别的用途

• 17.2.2 思考预算与输出质量

• 17.2.3 何时不需要高思考

• 17.3 ultrathink 类提示

• 17.3.1 适合复杂推理的问题

• 17.3.2 不适合简单重复任务

• 17.3.3 深度分析后的验证要求

• 17.4 Opus 4.7 提示词建议

• 17.4.1 架构评审提示词

• 17.4.2 Bug 深挖提示词

• 17.4.3 重构计划提示词

17.1 模型选择

学习目标

• 理解 模型选择 在本章主题中的具体作用。

• 能把 模型选择 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：简单任务与复杂任务、高风险任务与低风险任务、成本、速度和质量的权衡。

核心概念

模型选择 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 17.1.1 简单任务与复杂任务：先解释它解决的问题，再给出一个可观察的操作。

• 17.1.2 高风险任务与低风险任务：先解释它解决的问题，再给出一个可观察的操作。

• 17.1.3 成本、速度和质量的权衡：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。Claude Code 学习手册

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-17"

claude "只围绕“模型选择”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-17

claude "只围绕“模型选择”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;

using System.IO;

public static class ProjectInspector

{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);

Console.WriteLine($"Path: {fullPath}");

Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");

}

}

ProjectInspector.Summarize("README.md");

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 模型选择 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 模型选择 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

17.2 Effort 与 Thinking

学习目标

• 理解 Effort 与 Thinking 在本章主题中的具体作用。

• 能把 Effort 与 Thinking 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。Claude Code 学习手册

• 能说明本节三个重点：努力级别的用途、思考预算与输出质量、何时不需要高思考。

核心概念

Effort 与 Thinking 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 17.2.1 努力级别的用途：先解释它解决的问题，再给出一个可观察的操作。

• 17.2.2 思考预算与输出质量：先解释它解决的问题，再给出一个可观察的操作。

• 17.2.3 何时不需要高思考：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-17"

claude "只围绕“Effort 与 Thinking”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-17

claude "只围绕“Effort 与 Thinking”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;

using System.IO;

public static class ProjectInspector

{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);

Console.WriteLine($"Path: {fullPath}");

Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");

}

}

ProjectInspector.Summarize("README.md");

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Effort 与 Thinking 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。Claude Code 学习手册

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Effort 与 Thinking 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

17.3 ultrathink 类提示

学习目标

• 理解 ultrathink 类提示 在本章主题中的具体作用。

• 能把 ultrathink 类提示 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：适合复杂推理的问题、不适合简单重复任务、深度分析后的验证要求。

核心概念

ultrathink 类提示 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 17.3.1 适合复杂推理的问题：先解释它解决的问题，再给出一个可观察的操作。

• 17.3.2 不适合简单重复任务：先解释它解决的问题，再给出一个可观察的操作。

• 17.3.3 深度分析后的验证要求：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-17"

claude "只围绕“`ultrathink` 类提示”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-17

claude "只围绕“`ultrathink` 类提示”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;Claude Code 学习手册

using System.IO;

public static class ProjectInspector

{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);

Console.WriteLine($"Path: {fullPath}");

Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");

}

}

ProjectInspector.Summarize("README.md");

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 ultrathink 类提示 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 ultrathink 类提示 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

17.4 Opus 4.7 提示词建议

学习目标

• 理解 Opus 4.7 提示词建议 在本章主题中的具体作用。

• 能把 Opus 4.7 提示词建议 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：架构评审提示词、Bug 深挖提示词、重构计划提示词。

核心概念

Opus 4.7 提示词建议 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 17.4.1 架构评审提示词：先解释它解决的问题，再给出一个可观察的操作。

• 17.4.2 Bug 深挖提示词：先解释它解决的问题，再给出一个可观察的操作。

• 17.4.3 重构计划提示词：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。Claude Code 学习手册

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-17"

claude "只围绕“Opus 4.7 提示词建议”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-17

claude "只围绕“Opus 4.7 提示词建议”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;

using System.IO;

public static class ProjectInspector

{

public static void Summarize(string path)

{

var fullPath = Path.GetFullPath(path);

Console.WriteLine($"Path: {fullPath}");

Console.WriteLine($"Exists: {File.Exists(fullPath) ||

Directory.Exists(fullPath)}");

}

}

ProjectInspector.Summarize("README.md");

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Opus 4.7 提示词建议 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Opus 4.7 提示词建议 解决什么问题。

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

缩小范围，明确只处理一个小节或一个文件Claude Code 学习手册

常见问题

表现

处理方式

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

• 案例：同一复杂 Bug 分别用普通提示和深度分析提示处理。

• 练习：为 5 类任务选择模型和努力级别。

• 练习：记录输出质量、耗时和成本感知差异。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• prompts/opus47-architecture-review.md

• prompts/opus47-deep-bug-analysis.md

• 模型选择决策表

本章检查清单

• [ ] 我已经完成第 17 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“驯服 Opus

4.7：模型、努力级别和思考预算”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让

Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“复杂工程任务的提示词编排”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

157Claude Code 学习手册

