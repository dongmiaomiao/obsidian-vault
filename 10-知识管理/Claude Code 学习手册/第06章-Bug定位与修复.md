---
title: "第 6 章：Bug 定位与修复"
type: chapter
part: "第二篇：日常开发工作流 - 先把 Claude Code 用顺手"
source: "Claude Code 学习手册"
aliases:
---

第 6 章：Bug 定位与修复

所属篇章：第二篇：日常开发工作流 - 先把 Claude Code 用顺手

主案例语言：C++

命令示例：Windows PowerShell 为主，macOS/Linux 对照。

本章导读

建立 Claude Code 修 Bug 的标准流程：先根据证据提出假设，再最小修改，最后用测试验证。

本章围绕“测试失败日志”展开。先让 Claude Code 读取错误、定位相关文件、提出多个假设，再要求它给

出验证方法。修复阶段强调小步修改和测试先行。最后输出修复报告，为后续 Git 和 PR 工作流打基础。

学习目标

• 理解“Bug 定位与修复”在 Claude Code 学习路线中的位置。

• 能把本章知识转化为一个可交给 Claude Code 执行的小任务。

• 能使用 PowerShell 命令完成主流程，并能读懂 macOS/Linux 对照命令。

• 能用 C++ 示例完成本章案例，并知道如何迁移到其他语言项目。

• 能根据检查清单判断任务是否真正完成。

先做一个小案例

本章先使用 C++ 项目做一个最小案例。目标不是一次性完成复杂工程，而是训练“提出明确任务 -> 让

Claude Code 探索 -> 获取可验证输出 -> 记录结果”的闭环。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-06"

claude "基于本章主题“Bug 定位与修复”，设计一个最小可执行案例，并给出验证清单。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-06

claude "基于本章主题“Bug 定位与修复”，设计一个最小可执行案例，并给出验证清单。"

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

• 6.1 从报错到假设

• 6.1.1 如何提供错误日志

• 6.1.2 要求模型列出可能原因Claude Code 学习手册

• 6.1.3 为每个假设设计验证方法

• 6.2 最小修改原则

• 6.2.1 不借 Bug 修复做大重构

• 6.2.2 修改范围控制

• 6.2.3 diff 审查

• 6.3 回归测试

• 6.3.1 先写失败测试

• 6.3.2 修复后重跑测试

• 6.3.3 防止只修表面现象

• 6.4 修复报告

• 6.4.1 Bug 原因

• 6.4.2 修改点

• 6.4.3 验证结果和风险

6.1 从报错到假设

学习目标

• 理解 从报错到假设 在本章主题中的具体作用。

• 能把 从报错到假设 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：如何提供错误日志、要求模型列出可能原因、为每个假设设计验证方法。

核心概念

从报错到假设 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 6.1.1 如何提供错误日志：先解释它解决的问题，再给出一个可观察的操作。

• 6.1.2 要求模型列出可能原因：先解释它解决的问题，再给出一个可观察的操作。

• 6.1.3 为每个假设设计验证方法：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。Claude Code 学习手册

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-06"

claude "只围绕“从报错到假设”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-06

claude "只围绕“从报错到假设”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 从报错到假设 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 从报错到假设 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

6.2 最小修改原则

学习目标

• 理解 最小修改原则 在本章主题中的具体作用。

• 能把 最小修改原则 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：不借 Bug 修复做大重构、修改范围控制、diff 审查。

核心概念

最小修改原则 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：Claude Code 学习手册

• 6.2.1 不借 Bug 修复做大重构：先解释它解决的问题，再给出一个可观察的操作。

• 6.2.2 修改范围控制：先解释它解决的问题，再给出一个可观察的操作。

• 6.2.3 diff 审查：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-06"

claude "只围绕“最小修改原则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-06

claude "只围绕“最小修改原则”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

• 练习 1：把 最小修改原则 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 最小修改原则 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。Claude Code 学习手册

6.3 回归测试

学习目标

• 理解 回归测试 在本章主题中的具体作用。

• 能把 回归测试 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：先写失败测试、修复后重跑测试、防止只修表面现象。

核心概念

回归测试 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 6.3.1 先写失败测试：先解释它解决的问题，再给出一个可观察的操作。

• 6.3.2 修复后重跑测试：先解释它解决的问题，再给出一个可观察的操作。

• 6.3.3 防止只修表面现象：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-06"

claude "只围绕“回归测试”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-06

claude "只围绕“回归测试”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

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

Code，并要求它只完成一个小目标：解释入口、指出潜在问题、补一个测试，或者生成一段文档。Claude Code 学习手册

练习

• 练习 1：把 回归测试 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 回归测试 解决什么问题。

• [ ] 我能写出一个不会让 Claude Code 误解的任务说明。

• [ ] 我能指出本节任务的输入、输出、风险和验证方式。

• [ ] 我能判断 Claude Code 的回答是否基于真实证据。

6.4 修复报告

学习目标

• 理解 修复报告 在本章主题中的具体作用。

• 能把 修复报告 转化为一个可执行、可验证的 Claude Code 任务。

• 能识别这一节常见的误用场景，并知道如何修正。

• 能说明本节三个重点：Bug 原因、修改点、验证结果和风险。

核心概念

修复报告 的重点不是记住术语，而是把它放回真实工程动作里理解。对于 Claude Code

来说，一个好的任务必须同时说明目标、边界、可用资料、允许执行的动作和验收方式。

本节可以按下面的顺序理解：

• 6.4.1 Bug 原因：先解释它解决的问题，再给出一个可观察的操作。

• 6.4.2 修改点：先解释它解决的问题，再给出一个可观察的操作。

• 6.4.3 验证结果和风险：先解释它解决的问题，再给出一个可观察的操作。

本节主案例语言是 C++。用一个 C++

命令行或库项目作为观察对象，重点展示构建、边界条件和跨平台命令差异。

操作步骤

1. 明确当前任务只覆盖本节范围，不把后续章节内容提前展开。

2. 让 Claude Code 先读取或搜索与任务相关的最小资料集。

3. 要求 Claude Code 输出它基于哪些文件、命令或文档得出结论。

4. 让 Claude Code 给出可执行步骤，并在执行前说明风险。

5. 完成后用检查清单验证结果，而不是只看回答是否流畅。

# Windows PowerShell

Set-Location "D:\AI\claude code学习手册\book\examples\chapter-06"

claude "只围绕“修复报告”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"

# macOS / Linux

cd ~/claude-code-handbook/book/examples/chapter-06

claude "只围绕“修复报告”做一次可验证的小任务：先说明计划，再给出操作步骤、验证方式和风险。"Claude Code 学习手册

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

• 练习 1：把 修复报告 改写成一个包含目标、范围、限制、输出格式的提示词。

• 练习 2：要求 Claude Code 先列计划，不直接修改文件。

• 练习 3：让 Claude Code 给出验证命令，并记录验证结果。

检查清单

• [ ] 我能用自己的话解释 修复报告 解决什么问题。

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

• 案例：修复一个空值、边界条件或类型转换 Bug。

• 练习：要求 Claude Code 在修复前添加失败测试。

• 练习：根据 diff 写修复报告。

练习答案不要求唯一，但必须满足三个条件：任务边界清楚、输出可验证、结果能沉淀。

本章交付物

• 一个带测试的 Bug 修复提交Claude Code 学习手册

• notes/bugfix-report-template.md

• Bug 定位提示词模板

本章检查清单

• [ ] 我已经完成第 6 章的先导案例。

• [ ] 我已经记录本章至少 3 条可复用经验。

• [ ] 我能解释本章每个小节解决的问题。

• [ ] 我能把本章方法迁移到 Python、C# 或 C++ 项目。

• [ ] 我知道本章方法什么时候不适用。

本章小结

本章围绕“Bug 定位与修复”建立了一套可执行学习流程。真正的掌握标准不是记住概念，而是能让 Claude

Code 在明确边界内完成任务，并通过证据、测试或检查清单验证结果。

下一章衔接

下一章将进入“重构、测试和文档”，继续把本章方法扩展到新的 Claude Code 使用场景。

本章参考

• 官方总览：https://code.claude.com/docs/zh-CN/overview

• 记忆系统：https://code.claude.com/docs/zh-CN/memory

• Skills：https://code.claude.com/docs/zh-CN/skillsClaude Code 学习手册

58Claude Code 学习手册

