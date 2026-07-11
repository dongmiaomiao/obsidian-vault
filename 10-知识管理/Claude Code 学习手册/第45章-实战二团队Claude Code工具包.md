---
title: "第 45 章：实战二 - 团队 Claude Code 工具包"
type: chapter
part: "第十篇：完整实战案例"
source: "Claude Code 学习手册"
aliases:
---

第 45 章：实战二 - 团队 Claude Code 工具包

所属篇章：第十篇：完整实战案例

主案例语言：C++

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

通过团队工具包项目，把 Skill、SubAgent、Hook、MCP、CI 和插件化分发串成一个完整系统。

本章是团队级综合案例。读者需要先设计需求，不直接堆功能。工具包要能回答：谁使用、解决什么问题

、包含哪些能力、如何安装、如何验证、如何维护。

学习目标

• 理解“实战二 - 团队 Claude Code 工具包”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C++ 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C++ 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-45"

claude "基于本章主题“实战二 - 团队 Claude Code 工具包”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-45

claude "基于本章主题“实战二 - 团队 Claude Code 工具包”，设计一个最小可执行案例，并给出验证清单。"

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

• 45.1 需求设计

• 45.1.1 团队角色和使用场景

• 45.1.2 review、test、docs、security 四类能力Claude Code 学习手册

• 45.1.3 工具包边界

• 45.2 构建 Skill 与 SubAgents

• 45.2.1 code-review Skill

• 45.2.2 test-runner Agent

• 45.2.3 doc-writer Agent

• 45.2.4 security-scanner Agent

• 45.3 加入 Hooks、MCP 和 CI

• 45.3.1 安全和质量 Hook

• 45.3.2 本地知识库 MCP

• 45.3.3 CI 失败分析流程

• 45.4 插件化分发

• 45.4.1 插件目录结构

• 45.4.2 安装说明

• 45.4.3 版本和升级策略

45.1 需求设计

学习目标

• 理解 需求设计 在本章主题中的具体作用。

• 能把 需求设计 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：团队角色和使用场景、review、test、docs、security 四类能力、工具包边界。

核心概念

需求设计 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 45.1.1 团队角色和使用场景：先解释它解决的问题，再给出一个可观察的操作。

• 45.1.2 review、test、docs、security 四类能力：先解释它解决的问题，再给出一个可观察的操作。

• 45.1.3 工具包边界：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。Claude Code 学习手册

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-45"

claude "只围绕“需求设计”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-45

claude "只围绕“需求设计”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 需求设计 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 需求设计 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

45.2 构建 Skill 与 SubAgents

学习目标

• 理解 构建 Skill 与 SubAgents 在本章主题中的具体作用。

• 能把 构建 Skill 与 SubAgents 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：code-review Skill、test-runner Agent、doc-writer Agent。

核心概念

构建 Skill 与 SubAgents 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。Claude Code 学习手册

本节可以按下面的顺序理解：

• 45.2.1 code-review Skill：先解释它解决的问题，再给出一个可观察的操作。

• 45.2.2 test-runner Agent：先解释它解决的问题，再给出一个可观察的操作。

• 45.2.3 doc-writer Agent：先解释它解决的问题，再给出一个可观察的操作。

• 45.2.4 security-scanner Agent：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-45"

claude "只围绕“构建 Skill 与 SubAgents”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-45

claude "只围绕“构建 Skill 与 SubAgents”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 构建 Skill 与 SubAgents 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 构建 Skill 与 SubAgents 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。Claude Code 学习手册

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

45.3 加入 Hooks、MCP 和 CI

学习目标

• 理解 加入 Hooks、MCP 和 CI 在本章主题中的具体作用。

• 能把 加入 Hooks、MCP 和 CI 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：安全和质量 Hook、本地知识库 MCP、CI 失败分析流程。

核心概念

加入 Hooks、MCP 和 CI 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 45.3.1 安全和质量 Hook：先解释它解决的问题，再给出一个可观察的操作。

• 45.3.2 本地知识库 MCP：先解释它解决的问题，再给出一个可观察的操作。

• 45.3.3 CI 失败分析流程：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-45"

claude "只围绕“加入 Hooks、MCP 和 CI”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-45

claude "只围绕“加入 Hooks、MCP 和 CI”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

}Claude Code 学习手册

可以把这段代码交给 Claude

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。

练习

• 练习 1：把 加入 Hooks、MCP 和 CI 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 加入 Hooks、MCP 和 CI 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

45.4 插件化分发

学习目标

• 理解 插件化分发 在本章主题中的具体作用。

• 能把 插件化分发 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：插件目录结构、安装说明、版本和升级策略。

核心概念

插件化分发 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 45.4.1 插件目录结构：先解释它解决的问题，再给出一个可观察的操作。

• 45.4.2 安装说明：先解释它解决的问题，再给出一个可观察的操作。

• 45.4.3 版本和升级策略：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-45"

claude "只围绕“插件化分发”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"Claude Code 学习手册

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-45

claude "只围绕“插件化分发”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 插件化分发 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 插件化分发 解决什么问题。

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

• 案例：构建团队 Claude Code toolkit 插件。

• 练习：用一个真实 diff 验证 reviewer、tester、doc-writer 是否工作。

• 练习：写插件发布说明和升级说明。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物Claude Code 学习手册

• team-claude-toolkit/

• team-claude-toolkit/README.md

• team-claude-toolkit/CHANGELOG.md

• 团队安装与使用手册

本章检查清单

• [ ] 我已经完成第 45 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“实战二 - 团队 Claude Code

工具包”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude Code

在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

到这里，全书正文已经完成。后续应结合附录、模板和工具清单持续打磨个人或团队的 Claude Code

工作系统。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

410Claude Code 学习手册

