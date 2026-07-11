---
title: "第 24 章：SubAgents 基础"
type: chapter
part: "第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins"
source: "Claude Code 学习手册"
aliases:
---

第 24 章：SubAgents 基础

所属篇章：第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins

主案例语言：C++

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

让读者理解子代理的价值：隔离上下文、限制权限、承担专职任务。

本章先创建一个只读 code-reviewer，再创建 test-runner 或log-analyzer。重点是让读者理解子代理不只是“角色扮演”，而是权限、上下文和输出格式的工程边界。

学习目标

• 理解“SubAgents 基础”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C++ 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C++ 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-24"

claude "基于本章主题“SubAgents 基础”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-24

claude "基于本章主题“SubAgents 基础”，设计一个最小可执行案例，并给出验证清单。"

案例中的最小代码对象如下：

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};std::cout << "Path: " << std::filesystem::absolute(target) << "

";std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

• 24.1 子代理解决什么问题

• 24.1.1 专职角色

• 24.1.2 上下文隔离

• 24.1.3 权限边界

• 24.2 子代理配置

• 24.2.1 名称和描述

• 24.2.2 系统提示

• 24.2.3 工具权限

• 24.3 高噪声任务隔离

• 24.3.1 测试运行器

• 24.3.2 日志分析器

• 24.3.3 只返回结论

• 24.4 子代理反模式

• 24.4.1 简单任务不用拆

• 24.4.2 职责不能重叠

• 24.4.3 子代理输出必须可用

24.1 子代理解决什么问题

学习目标

• 理解 子代理解决什么问题 在本章主题中的具体作用。

• 能把 子代理解决什么问题 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：专职角色、上下文隔离、权限边界。

核心概念

子代理解决什么问题 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 24.1.1 专职角色：先解释它解决的问题，再给出一个可观察的操作。

• 24.1.2 上下文隔离：先解释它解决的问题，再给出一个可观察的操作。

• 24.1.3 权限边界：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-24"

claude "只围绕“子代理解决什么问题”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-24

claude "只围绕“子代理解决什么问题”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};std::cout << "Path: " << std::filesystem::absolute(target) << "

";std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 子代理解决什么问题 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 子代理解决什么问题 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

24.2 子代理配置

学习目标

• 理解 子代理配置 在本章主题中的具体作用。

• 能把 子代理配置 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：名称和描述、系统提示、工具权限。

核心概念

子代理配置 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 24.2.1 名称和描述：先解释它解决的问题，再给出一个可观察的操作。

• 24.2.2 系统提示：先解释它解决的问题，再给出一个可观察的操作。

• 24.2.3 工具权限：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-24"

claude "只围绕“子代理配置”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-24

claude "只围绕“子代理配置”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};std::cout << "Path: " << std::filesystem::absolute(target) << "

";std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 子代理配置 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 子代理配置 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

24.3 高噪声任务隔离

学习目标

• 理解 高噪声任务隔离 在本章主题中的具体作用。

• 能把 高噪声任务隔离 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：测试运行器、日志分析器、只返回结论。

核心概念

高噪声任务隔离 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 24.3.1 测试运行器：先解释它解决的问题，再给出一个可观察的操作。

• 24.3.2 日志分析器：先解释它解决的问题，再给出一个可观察的操作。

• 24.3.3 只返回结论：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-24"

claude "只围绕“高噪声任务隔离”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-24

claude "只围绕“高噪声任务隔离”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};std::cout << "Path: " << std::filesystem::absolute(target) << "

";std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 高噪声任务隔离 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 高噪声任务隔离 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

24.4 子代理反模式

学习目标

• 理解 子代理反模式 在本章主题中的具体作用。

• 能把 子代理反模式 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：简单任务不用拆、职责不能重叠、子代理输出必须可用。

核心概念

子代理反模式 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code 来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 24.4.1 简单任务不用拆：先解释它解决的问题，再给出一个可观察的操作。

• 24.4.2 职责不能重叠：先解释它解决的问题，再给出一个可观察的操作。

• 24.4.3 子代理输出必须可用：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-24"

claude "只围绕“子代理反模式”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-24

claude "只围绕“子代理反模式”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

示例

下面的示例不是为了展示复杂代码，而是为了给 Claude Code 一个可以读取、运行或解释的最小对象。

#include <filesystem>

#include <iostream>

int main() {

std::filesystem::path target{"README.md"};std::cout << "Path: " << std::filesystem::absolute(target) << "

";std::cout << "Exists: " << std::filesystem::exists(target) << "

";

return 0;

}

可以把这段代码交给 Claude Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 子代理反模式 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 子代理反模式 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

常见坑与排查

常见问题

表现

处理方式

任务描述过宽Claude Code 一次读取过多文件或输出泛泛总结缩小范围，明确只处理一个小节或一个文件缺少验收标准看起来完成，但无法判断是否正确在提示词中加入测试、检查清单或输出格式忽略上下文边界模型引用无关资料或过期规则要求列出依据文件，并清理无关上下文没有记录结果下次还要重新解释同一规则将有效流程沉淀到 Markdown、命令或 Skill 中本章案例与练习

• 案例：创建 .claude/agents/code-reviewer.md。

• 练习：限制 code-reviewer 只读不改。

• 练习：用 log-analyzer 处理长日志。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• .claude/agents/code-reviewer.md

• .claude/agents/test-runner.md

• 子代理职责表

本章检查清单

• [ ] 我已经完成第 24 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“SubAgents 基础”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接下一章将进入“多 Agent 协作”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skills

