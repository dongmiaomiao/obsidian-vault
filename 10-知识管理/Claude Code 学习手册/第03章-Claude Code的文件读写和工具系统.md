---
title: "第 3 章：Claude Code 的文件读写和工具系统"
type: chapter
part: "第一篇：入门地图 - 从 AI Agent 到 Claude Code"
source: "Claude Code 学习手册"
aliases:
---

第 3 章：Claude Code 的文件读写和工具系统

所属篇章：第一篇：入门地图 - 从 AI Agent 到 Claude Code

主案例语言：C++

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者理解 Claude Code

为什么能处理工程任务：它不是只靠模型记忆，而是通过工具读取、搜索、编辑和执行命令。

本章以一次“小 Bug 修复”为主线，拆解 Claude Code 可能使用的工具链：搜索相关代码、读取关键文件、

提出修改计划、应用补丁、运行测试、总结结果。重点讲“工具选择”而不是“工具百科”，让读者理解什么

时候该让它搜索、什么时候该让它读取、什么时候必须运行命令验证。

学习目标

• 理解“Claude Code 的文件读写和工具系统”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C++ 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C++ 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-03"

claude "基于本章主题“Claude Code 的文件读写和工具系统”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-03

claude "基于本章主题“Claude Code 的文件读写和工具系统”，设计一个最小可执行案例，并给出验证清单。"

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

• 3.1 文件读取工具

• 3.1.1 读取单个文件与搜索文件的区别Claude Code 学习手册

• 3.1.2 先搜索再阅读的效率优势

• 3.1.3 如何要求 Claude Code 给出读取证据

• 3.2 编辑工具

• 3.2.1 小范围修改与大范围重写

• 3.2.2 修改前说明计划

• 3.2.3 修改后查看 diff

• 3.3 Shell 命令工具

• 3.3.1 命令执行为什么重要

• 3.3.2 只读命令、写入命令和危险命令

• 3.3.3 运行测试、格式化和构建

• 3.4 Todo 与任务跟踪

• 3.4.1 为什么复杂任务需要任务列表

• 3.4.2 如何判断 Todo 是否真实推进

• 3.4.3 防止遗漏验证步骤

3.1 文件读取工具

学习目标

• 理解 文件读取工具 在本章主题中的具体作用。

• 能把 文件读取工具 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：读取单个文件与搜索文件的区别、先搜索再阅读的效率优势、如何要求 Claude

Code 给出读取证据。

核心概念

文件读取工具 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 3.1.1 读取单个文件与搜索文件的区别：先解释它解决的问题，再给出一个可观察的操作。

• 3.1.2 先搜索再阅读的效率优势：先解释它解决的问题，再给出一个可观察的操作。

• 3.1.3 如何要求 Claude Code 给出读取证据：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。Claude Code 学习手册

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-03"

claude "只围绕“文件读取工具”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-03

claude "只围绕“文件读取工具”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 文件读取工具 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 文件读取工具 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

3.2 编辑工具

学习目标

• 理解 编辑工具 在本章主题中的具体作用。

• 能把 编辑工具 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：小范围修改与大范围重写、修改前说明计划、修改后查看 diff。

核心概念Claude Code 学习手册

编辑工具 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 3.2.1 小范围修改与大范围重写：先解释它解决的问题，再给出一个可观察的操作。

• 3.2.2 修改前说明计划：先解释它解决的问题，再给出一个可观察的操作。

• 3.2.3 修改后查看 diff：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-03"

claude "只围绕“编辑工具”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-03

claude "只围绕“编辑工具”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 编辑工具 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 编辑工具 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。Claude Code 学习手册

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

3.3 Shell 命令工具

学习目标

• 理解 Shell 命令工具 在本章主题中的具体作用。

• 能把 Shell 命令工具 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：命令执行为什么重要、只读命令、写入命令和危险命令、运行测试、格式化和

构建。

核心概念

Shell 命令工具 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 3.3.1 命令执行为什么重要：先解释它解决的问题，再给出一个可观察的操作。

• 3.3.2 只读命令、写入命令和危险命令：先解释它解决的问题，再给出一个可观察的操作。

• 3.3.3 运行测试、格式化和构建：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-03"

claude "只围绕“Shell 命令工具”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-03

claude "只围绕“Shell 命令工具”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};

std::cout << "Path: " << std::filesystem::absolute(target) << "

";

std::cout << "Exists: " << std::filesystem::exists(target) << "

";Claude Code 学习手册

return 0;

}

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 Shell 命令工具 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Shell 命令工具 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

3.4 Todo 与任务跟踪

学习目标

• 理解 Todo 与任务跟踪 在本章主题中的具体作用。

• 能把 Todo 与任务跟踪 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：为什么复杂任务需要任务列表、如何判断 Todo

是否真实推进、防止遗漏验证步骤。

核心概念

Todo 与任务跟踪 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 3.4.1 为什么复杂任务需要任务列表：先解释它解决的问题，再给出一个可观察的操作。

• 3.4.2 如何判断 Todo 是否真实推进：先解释它解决的问题，再给出一个可观察的操作。

• 3.4.3 防止遗漏验证步骤：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。Claude Code 学习手册

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-03"

claude "只围绕“Todo 与任务跟踪”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-03

claude "只围绕“Todo 与任务跟踪”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 Todo 与任务跟踪 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 Todo 与任务跟踪 解决什么问题。

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

• 案例：让 Claude Code 用搜索定位一个函数，不允许它全量阅读项目。

• 练习：要求它在修改前列出计划和预计修改文件。Claude Code 学习手册

• 练习：让它运行测试并解释失败输出。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• notes/03-tool-chain.md

• 一份“读、搜、改、跑、验”的工具使用流程

• 危险命令识别清单

本章检查清单

• [ ] 我已经完成第 3 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Claude Code

的文件读写和工具系统”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude

Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“学习用项目准备”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

31Claude Code 学习手册

