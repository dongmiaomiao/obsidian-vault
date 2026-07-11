---
title: "第 44 章：实战一 - 个人 Python 项目从 Bug 到"
type: chapter
part: "第九篇：高级驾驭工程 - 从会用到会设计 Agent 工作系统"
source: "Claude Code 学习手册"
aliases:
---

第 44 章：实战一 - 个人 Python 项目从 Bug 到

PR

所属篇章：第十篇：完整实战案例

主案例语言：C#

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

通过完整个人项目，把前面学到的代码理解、Bug 修复、测试、记忆、Git 和 PR 流程串起来。

本章是个人实战案例，必须完整闭环。读者从项目初始化开始，编写规则和记忆，修复真实

Bug，补充测试，生成 PR 描述，最后把成功流程沉淀为模板。

学习目标

• 理解“实战一 - 个人 Python 项目从 Bug 到 PR”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C# 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C# 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-44"

claude "基于本章主题“实战一 - 个人 Python 项目从 Bug 到 PR”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-44

claude "基于本章主题“实战一 - 个人 Python 项目从 Bug 到 PR”，设计一个最小可执行案例，并给出验证清单。"

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

• 44.1 项目初始化

• 44.1.1 创建或选择 Python 项目

• 44.1.2 添加测试和文档

• 44.1.3 制造可控 Bug

• 44.2 规则与记忆

• 44.2.1 编写 CLAUDE.md

• 44.2.2 添加测试规则

• 44.2.3 添加 Git 规则

• 44.3 Bug 定位与修复

• 44.3.1 读取失败日志

• 44.3.2 建立假设

• 44.3.3 先写测试再修复

• 44.3.4 运行验证

• 44.4 PR 与复盘

• 44.4.1 生成 PR 描述

• 44.4.2 更新知识库

• 44.4.3 将流程沉淀为命令或 Skill

44.1 项目初始化

学习目标

• 理解 项目初始化 在本章主题中的具体作用。

• 能把 项目初始化 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：创建或选择 Python 项目、添加测试和文档、制造可控 Bug。

核心概念

项目初始化 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 44.1.1 创建或选择 Python 项目：先解释它解决的问题，再给出一个可观察的操作。

• 44.1.2 添加测试和文档：先解释它解决的问题，再给出一个可观察的操作。

• 44.1.3 制造可控 Bug：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤Claude Code 学习手册

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-44"

claude "只围绕“项目初始化”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-44

claude "只围绕“项目初始化”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 项目初始化 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 项目初始化 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

44.2 规则与记忆

学习目标

• 理解 规则与记忆 在本章主题中的具体作用。

• 能把 规则与记忆 转化为一个可执行、可验证的 Claude Code 任务。Claude Code 学习手册

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：编写 CLAUDE.md、添加测试规则、添加 Git 规则。

核心概念

规则与记忆 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 44.2.1 编写 CLAUDE.md：先解释它解决的问题，再给出一个可观察的操作。

• 44.2.2 添加测试规则：先解释它解决的问题，再给出一个可观察的操作。

• 44.2.3 添加 Git 规则：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-44"

claude "只围绕“规则与记忆”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-44

claude "只围绕“规则与记忆”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 规则与记忆 改写成一个包含目标、范围、限制、输出格式的提示词。Claude Code 学习手册

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 规则与记忆 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

44.3 Bug 定位与修复

学习目标

• 理解 Bug 定位与修复 在本章主题中的具体作用。

• 能把 Bug 定位与修复 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：读取失败日志、建立假设、先写测试再修复。

核心概念

Bug 定位与修复 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 44.3.1 读取失败日志：先解释它解决的问题，再给出一个可观察的操作。

• 44.3.2 建立假设：先解释它解决的问题，再给出一个可观察的操作。

• 44.3.3 先写测试再修复：先解释它解决的问题，再给出一个可观察的操作。

• 44.3.4 运行验证：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-44"

claude "只围绕“Bug 定位与修复”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-44

claude "只围绕“Bug 定位与修复”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"Claude Code 学习手册

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

• 练习 1：把 Bug 定位与修复 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Bug 定位与修复 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

44.4 PR 与复盘

学习目标

• 理解 PR 与复盘 在本章主题中的具体作用。

• 能把 PR 与复盘 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：生成 PR 描述、更新知识库、将流程沉淀为命令或 Skill。

核心概念

PR 与复盘 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 44.4.1 生成 PR 描述：先解释它解决的问题，再给出一个可观察的操作。

• 44.4.2 更新知识库：先解释它解决的问题，再给出一个可观察的操作。

• 44.4.3 将流程沉淀为命令或 Skill：先解释它解决的问题，再给出一个可观察的操作。Claude Code 学习手册

本节主案例语言是 C#。用一个 C# 控制台或 Web API

项目作为观察对象，重点展示项目结构、构建命令和类型约束。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-44"

claude "只围绕“PR 与复盘”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-44

claude "只围绕“PR 与复盘”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 PR 与复盘 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 PR 与复盘 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查Claude Code 学习手册

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

本章案例与练习

• 案例：完成一个 Python CLI 或 API 项目的 Bug 修复 PR。

• 练习：人工审查 Claude Code 生成的 diff。

• 练习：把修复过程写入知识库。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• 一个完整 Bug 修复分支

• CLAUDE.md

• 测试文件

• PR 描述

• 复盘文档

本章检查清单

• [ ] 我已经完成第 44 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“实战一 - 个人 Python 项目从 Bug 到

PR”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code

在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“实战二 - 团队 Claude Code 工具包”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memoryClaude Code 学习手册

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

401Claude Code 学习手册

