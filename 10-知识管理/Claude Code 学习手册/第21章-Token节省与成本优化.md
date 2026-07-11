---
title: "第 21 章：Token 节省与成本优化"
type: chapter
part: "第五篇：上下文、Token 和成本控制"
source: "Claude Code 学习手册"
aliases:
---

第 21 章：Token 节省与成本优化

所属篇章：第五篇：上下文、Token 和成本控制

主案例语言：C++

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者学会从文件读取、输出长度、模型选择和上下文结构上节省 token。

本章建立成本意识，但不把 token 优化变成省略必要信息。读者要掌握三个原则：少读但读对，少说但说

准，稳定信息长期沉淀，临时信息短期使用。

学习目标

• 理解“Token 节省与成本优化”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C++ 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C++ 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-21"

claude "基于本章主题“Token 节省与成本优化”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-21

claude "基于本章主题“Token 节省与成本优化”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};

std::cout << "Path: " << std::filesystem::absolute(target) << "

";

std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

目录

• 21.1 Token 花在哪里

• 21.1.1 用户输入

• 21.1.2 文件内容Claude Code 学习手册

• 21.1.3 工具输出

• 21.1.4 模型回答

• 21.2 少读文件

• 21.2.1 用搜索定位

• 21.2.2 用索引导航

• 21.2.3 大日志先摘要

• 21.3 少输出废话

• 21.3.1 只要结论

• 21.3.2 限定格式

• 21.3.3 避免重复解释

• 21.4 缓存友好写法

• 21.4.1 稳定规则和临时任务分离

• 21.4.2 文档结构稳定

• 21.4.3 避免频繁改动大上下文

21.1 Token 花在哪里

学习目标

• 理解 Token 花在哪里 在本章主题中的具体作用。

• 能把 Token 花在哪里 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：用户输入、文件内容、工具输出。

核心概念

Token 花在哪里 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 21.1.1 用户输入：先解释它解决的问题，再给出一个可观察的操作。

• 21.1.2 文件内容：先解释它解决的问题，再给出一个可观察的操作。

• 21.1.3 工具输出：先解释它解决的问题，再给出一个可观察的操作。

• 21.1.4 模型回答：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。Claude Code 学习手册

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-21"

claude "只围绕“Token 花在哪里”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-21

claude "只围绕“Token 花在哪里”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};

std::cout << "Path: " << std::filesystem::absolute(target) << "

";

std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Token 花在哪里 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Token 花在哪里 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

21.2 少读文件

学习目标

• 理解 少读文件 在本章主题中的具体作用。

• 能把 少读文件 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：用搜索定位、用索引导航、大日志先摘要。

核心概念Claude Code 学习手册

少读文件 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 21.2.1 用搜索定位：先解释它解决的问题，再给出一个可观察的操作。

• 21.2.2 用索引导航：先解释它解决的问题，再给出一个可观察的操作。

• 21.2.3 大日志先摘要：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-21"

claude "只围绕“少读文件”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-21

claude "只围绕“少读文件”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};

std::cout << "Path: " << std::filesystem::absolute(target) << "

";

std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 少读文件 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 少读文件 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。Claude Code 学习手册

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

21.3 少输出废话

学习目标

• 理解 少输出废话 在本章主题中的具体作用。

• 能把 少输出废话 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：只要结论、限定格式、避免重复解释。

核心概念

少输出废话 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 21.3.1 只要结论：先解释它解决的问题，再给出一个可观察的操作。

• 21.3.2 限定格式：先解释它解决的问题，再给出一个可观察的操作。

• 21.3.3 避免重复解释：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-21"

claude "只围绕“少输出废话”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-21

claude "只围绕“少输出废话”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};

std::cout << "Path: " << std::filesystem::absolute(target) << "

";

std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;Claude Code 学习手册

}

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 少输出废话 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 少输出废话 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

21.4 缓存友好写法

学习目标

• 理解 缓存友好写法 在本章主题中的具体作用。

• 能把 缓存友好写法 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：稳定规则和临时任务分离、文档结构稳定、避免频繁改动大上下文。

核心概念

缓存友好写法 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 21.4.1 稳定规则和临时任务分离：先解释它解决的问题，再给出一个可观察的操作。

• 21.4.2 文档结构稳定：先解释它解决的问题，再给出一个可观察的操作。

• 21.4.3 避免频繁改动大上下文：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShellClaude Code 学习手册

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-21"

claude "只围绕“缓存友好写法”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-21

claude "只围绕“缓存友好写法”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};

std::cout << "Path: " << std::filesystem::absolute(target) << "

";

std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 缓存友好写法 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 缓存友好写法 解决什么问题。

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

本章案例与练习

• 案例：同一任务分别用“全量读取”和“搜索定位”执行，对比效率。

• 练习：把长日志压缩成结构化故障摘要。

• 练习：为常见任务制定模型和 token 策略。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。Claude Code 学习手册

本章交付物

• docs/token-budget.md

• prompts/concise-output.md

• 成本优化检查清单

本章检查清单

• [ ] 我已经完成第 21 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Token 节省与成本优化”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让

Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“Skills 基础”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

193Claude Code 学习手册

