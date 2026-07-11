---
title: "第 8 章：Git 工作流与提交质量"
type: chapter
part: "第二篇：日常开发工作流 - 先把 Claude Code 用顺手"
source: "Claude Code 学习手册"
aliases:
---

第 8 章：Git 工作流与提交质量

所属篇章：第二篇：日常开发工作流 - 先把 Claude Code 用顺手

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者学会用 Claude Code 辅助 Git 工作，但不让它破坏工作区。

本章强调 Claude Code 在 Git 中的正确角色：帮助理解 diff、生成提交说明、写 PR

描述和检查风险，而不是替人盲目执行破坏性命令。读者要建立“先看状态、再看 diff、再提交”的习惯。

学习目标

• 理解“Git 工作流与提交质量”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-08"

claude "基于本章主题“Git 工作流与提交质量”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-08

claude "基于本章主题“Git 工作流与提交质量”，设计一个最小可执行案例，并给出验证清单。"

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

目录

• 8.1 读懂 diff

• 8.1.1 工作区状态检查Claude Code 学习手册

• 8.1.2 按文件总结行为变化

• 8.1.3 识别无关改动

• 8.2 提交信息

• 8.2.1 Conventional Commit 基础

• 8.2.2 从 diff 生成提交说明

• 8.2.3 修改提交说明使其可审查

• 8.3 分支与 PR 描述

• 8.3.1 分支命名

• 8.3.2 PR 背景、方案和验证

• 8.3.3 风险和回滚说明

• 8.4 避免 Git 灾难

• 8.4.1 不随意 reset

• 8.4.2 不覆盖用户未提交修改

• 8.4.3 高风险 Git 命令确认机制

8.1 读懂 diff

学习目标

• 理解 读懂 diff 在本章主题中的具体作用。

• 能把 读懂 diff 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：工作区状态检查、按文件总结行为变化、识别无关改动。

核心概念

读懂 diff 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 8.1.1 工作区状态检查：先解释它解决的问题，再给出一个可观察的操作。

• 8.1.2 按文件总结行为变化：先解释它解决的问题，再给出一个可观察的操作。

• 8.1.3 识别无关改动：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。Claude Code 学习手册

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-08"

claude "只围绕“读懂 diff”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-08

claude "只围绕“读懂 diff”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 读懂 diff 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 读懂 diff 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

8.2 提交信息

学习目标

• 理解 提交信息 在本章主题中的具体作用。

• 能把 提交信息 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：Conventional Commit 基础、从 diff 生成提交说明、修改提交说明使其可审查。

核心概念Claude Code 学习手册

提交信息 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 8.2.1 Conventional Commit 基础：先解释它解决的问题，再给出一个可观察的操作。

• 8.2.2 从 diff 生成提交说明：先解释它解决的问题，再给出一个可观察的操作。

• 8.2.3 修改提交说明使其可审查：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-08"

claude "只围绕“提交信息”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-08

claude "只围绕“提交信息”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 提交信息 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单Claude Code 学习手册

• [ ] 我能用自己的话解释 提交信息 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

8.3 分支与 PR 描述

学习目标

• 理解 分支与 PR 描述 在本章主题中的具体作用。

• 能把 分支与 PR 描述 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：分支命名、PR 背景、方案和验证、风险和回滚说明。

核心概念

分支与 PR 描述 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 8.3.1 分支命名：先解释它解决的问题，再给出一个可观察的操作。

• 8.3.2 PR 背景、方案和验证：先解释它解决的问题，再给出一个可观察的操作。

• 8.3.3 风险和回滚说明：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-08"

claude "只围绕“分支与 PR 描述”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-08

claude "只围绕“分支与 PR 描述”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;

using System.IO;

public static class ProjectInspector

{

public static void Summarize(string path)Claude Code 学习手册

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

• 练习 1：把 分支与 PR 描述 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 分支与 PR 描述 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

8.4 避免 Git 灾难

学习目标

• 理解 避免 Git 灾难 在本章主题中的具体作用。

• 能把 避免 Git 灾难 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：不随意 reset、不覆盖用户未提交修改、高风险 Git 命令确认机制。

核心概念

避免 Git 灾难 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 8.4.1 不随意 reset：先解释它解决的问题，再给出一个可观察的操作。

• 8.4.2 不覆盖用户未提交修改：先解释它解决的问题，再给出一个可观察的操作。

• 8.4.3 高风险 Git 命令确认机制：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。Claude Code 学习手册

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-08"

claude "只围绕“避免 Git 灾难”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-08

claude "只围绕“避免 Git 灾难”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 避免 Git 灾难 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 避免 Git 灾难 解决什么问题。

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

• 案例：让 Claude Code 根据当前 diff 生成提交说明和 PR 描述。

• 练习：找出 diff 中的无关格式化改动。

• 练习：列出 5 个不应随便授权的 Git 命令。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• docs/pr-template.md

• prompts/git-diff-summary.md

• Git 安全操作清单

本章检查清单

• [ ] 我已经完成第 8 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Git 工作流与提交质量”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让

Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“从一次性问答到可复用工作流”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

76Claude Code 学习手册

