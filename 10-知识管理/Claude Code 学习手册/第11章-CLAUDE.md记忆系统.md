---
title: "第 11 章：CLAUDE.md 记忆系统"
type: chapter
part: "第三篇：Markdown、记忆和本地知识库"
source: "Claude Code 学习手册"
aliases:
---

第 11 章：CLAUDE.md 记忆系统

所属篇章：第三篇：Markdown、记忆和本地知识库

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者掌握 Claude Code 项目记忆的核心文件：CLAUDE.md。

本章从最小 CLAUDE.md 开始，只包含项目简介、运行命令、测试命令和基本风格。随后逐步加入个人偏

好和项目规则，并展示臃肿规则如何降低效果。读者要学会让 Claude Code

读取并复述规则，验证它是否真的理解。

学习目标

• 理解“CLAUDE.md 记忆系统”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-11"

claude "基于本章主题“`CLAUDE.md` 记忆系统”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-11

claude "基于本章主题“`CLAUDE.md` 记忆系统”，设计一个最小可执行案例，并给出验证清单。"

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

• 11.1 CLAUDE.md 的作用Claude Code 学习手册

• 11.1.1 项目目标

• 11.1.2 常用命令

• 11.1.3 编码和测试规则

• 11.2 个人偏好与项目规则

• 11.2.1 个人习惯

• 11.2.2 项目约束

• 11.2.3 团队规范

• 11.3 好的 CLAUDE.md 写法

• 11.3.1 短而明确

• 11.3.2 能被执行

• 11.3.3 按任务场景组织

• 11.4 记忆维护

• 11.4.1 定期删除过期规则

• 11.4.2 用测试命令验证规则

• 11.4.3 记录规则变更原因

11.1 CLAUDE.md 的作用

学习目标

• 理解 CLAUDE.md 的作用 在本章主题中的具体作用。

• 能把 CLAUDE.md 的作用 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：项目目标、常用命令、编码和测试规则。

核心概念

CLAUDE.md 的作用 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 11.1.1 项目目标：先解释它解决的问题，再给出一个可观察的操作。

• 11.1.2 常用命令：先解释它解决的问题，再给出一个可观察的操作。

• 11.1.3 编码和测试规则：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。Claude Code 学习手册

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-11"

claude "只围绕“`CLAUDE.md` 的作用”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-11

claude "只围绕“`CLAUDE.md` 的作用”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 CLAUDE.md 的作用 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 CLAUDE.md 的作用 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

11.2 个人偏好与项目规则

学习目标

• 理解 个人偏好与项目规则 在本章主题中的具体作用。

• 能把 个人偏好与项目规则 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：个人习惯、项目约束、团队规范。Claude Code 学习手册

核心概念

个人偏好与项目规则 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 11.2.1 个人习惯：先解释它解决的问题，再给出一个可观察的操作。

• 11.2.2 项目约束：先解释它解决的问题，再给出一个可观察的操作。

• 11.2.3 团队规范：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-11"

claude "只围绕“个人偏好与项目规则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-11

claude "只围绕“个人偏好与项目规则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 个人偏好与项目规则 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。Claude Code 学习手册

检查清单

• [ ] 我能用自己的话解释 个人偏好与项目规则 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

11.3 好的 CLAUDE.md 写法

学习目标

• 理解 好的 CLAUDE.md 写法 在本章主题中的具体作用。

• 能把 好的 CLAUDE.md 写法 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：短而明确、能被执行、按任务场景组织。

核心概念

好的 CLAUDE.md 写法 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 11.3.1 短而明确：先解释它解决的问题，再给出一个可观察的操作。

• 11.3.2 能被执行：先解释它解决的问题，再给出一个可观察的操作。

• 11.3.3 按任务场景组织：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-11"

claude "只围绕“好的 `CLAUDE.md` 写法”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-11

claude "只围绕“好的 `CLAUDE.md` 写法”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

using System;

using System.IO;

public static class ProjectInspectorClaude Code 学习手册

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

• 练习 1：把 好的 CLAUDE.md 写法 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 好的 CLAUDE.md 写法 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

11.4 记忆维护

学习目标

• 理解 记忆维护 在本章主题中的具体作用。

• 能把 记忆维护 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：定期删除过期规则、用测试命令验证规则、记录规则变更原因。

核心概念

记忆维护 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 11.4.1 定期删除过期规则：先解释它解决的问题，再给出一个可观察的操作。

• 11.4.2 用测试命令验证规则：先解释它解决的问题，再给出一个可观察的操作。

• 11.4.3 记录规则变更原因：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。Claude Code 学习手册

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-11"

claude "只围绕“记忆维护”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-11

claude "只围绕“记忆维护”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 记忆维护 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 记忆维护 解决什么问题。

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

要求列出依据文件，并清理无关上下文Claude Code 学习手册

常见问题

表现

处理方式

没有记录结果

下次还要重新解释同一规则

将有效流程沉淀到 Markdown、命令或 Skill

中

本章案例与练习

• 案例：为学习项目创建最小 CLAUDE.md。

• 练习：把个人偏好和项目规则拆开。

• 练习：让 Claude Code 审查 CLAUDE.md 是否空泛、重复、过期。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• CLAUDE.md

• notes/claude-memory-review.md

• 个人规则与项目规则分层表

本章检查清单

• [ ] 我已经完成第 11 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“CLAUDE.md 记忆系统”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让

Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“项目规则、AGENTS.md 和规则文件夹”，继续把本章方法扩展到新的 Claude Code

使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

103Claude Code 学习手册

