---
title: "# Stop Hook Checklist"
type: appendix
part: "第十篇：完整实战案例"
source: "Claude Code 学习手册"
aliases:
---

附录 H：Hooks 示例

Hooks 用于在工具调用前后加入安全和质量控制。

安全 Hook 设计

• 阻止删除关键目录。

• 阻止读取 .env、密钥、token。

• 阻止未经确认的发布命令。

Stop Hook 检查项

# Stop Hook Checklist

- 是否说明修改了哪些文件？

- 是否运行了测试？

- 是否说明测试结果？

- 是否列出剩余风险？Claude Code 学习手册

426Claude Code 学习手册

