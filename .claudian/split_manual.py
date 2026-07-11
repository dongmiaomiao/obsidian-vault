#!/usr/bin/env python3
"""拆分 Claude Code 学习手册并修复格式"""

import re
import os

VAULT = "/Users/miaomaio/Library/Mobile Documents/iCloud~md~obsidian/Documents/小懂不懂知识库"
SRC = os.path.join(VAULT, "未命名 2.md")
OUT = os.path.join(VAULT, "10-知识管理/Claude Code 学习手册")

# ── 篇章映射 ──
PARTS = [
    (147, "第一篇：入门地图 - 从 AI Agent 到 Claude Code"),
    (2677, "第二篇：日常开发工作流 - 先把 Claude Code 用顺手"),
    (5785, "第三篇：Markdown、记忆和本地知识库"),
    (8915, "第四篇：提示词、Opus 4.7 和模型驾驭"),
    (11395, "第五篇：上下文、Token 和成本控制"),
    (13255, "第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins"),
    (19471, "第七篇：自动化、GitHub、CI 和可编程 Agent"),
    (22565, "第八篇：安全、权限、沙箱和风险控制"),
    (25037, "第九篇：高级驾驭工程 - 从会用到会设计 Agent 工作系统"),
    (26907, "第十篇：完整实战案例"),
]

# ── 章节行号 (start line, end line, filename) ──
CHAPTERS = [
    # 前言 / 目录 / 阅读说明 (1-146)
    (1, 146, "00-前言与目录"),
    # 第一章
    (147, 782, "第01章-为什么Claude Code不只是聊天机器人"),
    (783, 1428, "第02章-环境账号模型和第一个任务"),
    (1429, 2044, "第03章-Claude Code的文件读写和工具系统"),
    (2045, 2674, "第04章-学习用项目准备"),
    (2677, 3318, "第05章-代码理解与项目地图"),
    (3319, 3922, "第06章-Bug定位与修复"),
    (3923, 4538, "第07章-重构测试和文档"),
    (4539, 5172, "第08章-Git工作流与提交质量"),
    (5173, 5780, "第09章-从一次性问答到可复用工作流"),
    (5781, 6402, "第10章-Markdown不是文档格式而是Agent控制层"),
    (6403, 7046, "第11章-CLAUDE.md记忆系统"),
    (7047, 7656, "第12章-项目规则AGENTS.md和规则文件夹"),
    (7657, 8270, "第13章-本地知识库"),
    (8271, 8912, "第14章-记忆系统的反模式"),
    (8913, 9522, "第15章-Claude Code提示词基本功"),
    (9523, 10138, "第16章-计划模式与探索模式"),
    (10139, 10784, "第17章-驯服Opus 4.7"),
    (10785, 11392, "第18章-复杂工程任务的提示词编排"),
    (11393, 12010, "第19章-上下文窗口与文件选择"),
    (12011, 12644, "第20章-压缩恢复和长会话管理"),
    (12645, 13252, "第21章-Token节省与成本优化"),
    (13253, 13866, "第22章-Skills基础"),
    (13867, 14504, "第23章-自定义命令与任务型Skill"),
    (14505, 15108, "第24章-SubAgents基础"),
    (15109, 15724, "第25章-多Agent协作"),
    (15725, 16358, "第26章-Hooks事件驱动自动化"),
    (16359, 16964, "第27章-MCP基础与外部工具连接"),
    (16965, 17592, "第28章-Plugins插件系统"),
    (17593, 18240, "第29章-Tools与Rules体系"),
    (18241, 18854, "第30章-Skill Agent MCP Plugin的组合模式"),
    (18855, 19468, "第31章-扩展系统实战小项目"),
    (19469, 20104, "第32章-Headless模式与命令行自动化"),
    (20105, 20710, "第33章-Agent SDK入门"),
    (20711, 21324, "第34章-Routines定时任务和自动化工作流"),
    (21325, 21958, "第35章-GitHub PR CI工作流"),
    (21959, 22562, "第36章-IDE浏览器和外部开发工具集成"),
    (22563, 23176, "第37章-权限系统和安全工作模式"),
    (23177, 23810, "第38章-沙箱数据安全和提示注入"),
    (23811, 24414, "第39章-Git安全发布和回滚"),
    (24415, 25034, "第40章-生产级Claude Code使用规范"),
    (25035, 25676, "第41章-Claude Code内部工作机制导览"),
    (25677, 26280, "第42章-上下文工程缓存和成本工程"),
    (26281, 26902, "第43章-从个人能力到团队AI编码体系"),
    (26903, 27550, "第44章-实战一个人Python项目从Bug到PR"),
    (27551, 28164, "第45章-实战二团队Claude Code工具包"),
    # 附录
    (28165, 28212, "附录/附录A-Claude Code常用命令速查"),
    (28213, 28274, "附录/附录B-目录与文件速查"),
    (28275, 28328, "附录/附录C-Markdown写作模板"),
    (28329, 28362, "附录/附录D-提示词模板库"),
    (28363, 28414, "附录/附录E-Skill模板库"),
    (28415, 28452, "附录/附录F-SubAgent模板库"),
    (28453, 28488, "附录/附录G-MCP配置示例"),
    (28489, 28516, "附录/附录H-Hooks示例"),
    (28517, 28572, "附录/附录I-Token与成本清单"),
    (28573, 28610, "附录/附录J-安全清单"),
    (28611, 28678, "附录/附录K-术语表"),
]

# ── 句子结束标点 ──
SENTENCE_END = set('。！？…—）」》”’')
CODE_INDICATORS = re.compile(r'^(\s{4,}|\t|```|# |## |### |\d+\. |[-*•] |\||>)')

def is_broken_end(line: str) -> bool:
    """判断行尾是否是「断裂」的（不应该在此处换行）"""
    if not line:
        return False
    last = line.rstrip()[-1]
    # 如果以句子结束标点结尾，则不认为断裂
    if last in SENTENCE_END:
        return False
    # 英文冒号结尾且下一行不是列表 → 可能是断裂
    if last == '：':
        return True
    # 中文或英文字母结尾 → 可能是断裂
    if '一' <= last <= '鿿' or last.isalpha():
        return True
    # 逗号、分号结尾 → 断裂
    if last in '，、；,;':
        return True
    return False

def should_join(current: str, next_line: str) -> bool:
    """判断当前行和下一行是否应该合并"""
    cur = current.rstrip()
    nxt = next_line.strip()

    if not cur or not nxt:
        return False

    # 如果下一行是代码/列表/标题/表格，不合并
    if CODE_INDICATORS.match(nxt):
        return False

    # 当前行以代码标记开头，不合并
    if CODE_INDICATORS.match(cur):
        return False

    # 当前行是单独的数字（页码），跳过
    if re.match(r'^\d{1,4}$', cur):
        return False

    # 行尾断裂 + 下一行是中文或小写字母开头
    if is_broken_end(cur):
        return True

    return False

def fix_line_wrapping(lines: list) -> list:
    """修复断行——智能合并被截断的行"""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # 跳过空白页码行
        stripped = line.strip()
        if re.match(r'^\d{1,4}$', stripped) and (i > 0 and lines[i-1].strip() == ''):
            i += 1
            continue

        # 尝试与后续行合并
        merged = line.rstrip('\n')
        j = i + 1
        while j < len(lines):
            next_line = lines[j]
            if should_join(merged, next_line):
                # 判断是否需要空格分隔
                nxt_stripped = next_line.strip()
                if merged and merged[-1] in '一-鿿' and nxt_stripped and nxt_stripped[0] in '一-鿿':
                    merged += nxt_stripped  # 中文之间不加空格
                elif merged and merged[-1].isalpha() and nxt_stripped and nxt_stripped[0].isalpha():
                    merged += ' ' + nxt_stripped  # 英文单词之间加空格
                elif merged[-1] in '：:,':
                    merged += nxt_stripped  # 标点后不加空格
                else:
                    merged += nxt_stripped
                j += 1
            else:
                break

        result.append(merged + '\n')
        i = j

    return result

def clean_content(lines: list) -> str:
    """清理内容"""
    # 移除「Claude Code 学习手册」独立行（页码标记）
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped == 'Claude Code 学习手册':
            continue
        if re.match(r'^\d{1,4}$', stripped):
            # 单独的页码，检查上下文
            continue
        cleaned.append(line)

    # 合并连续的空白行
    result = []
    prev_empty = False
    for line in cleaned:
        is_empty = line.strip() == ''
        if is_empty and prev_empty:
            continue
        result.append(line)
        prev_empty = is_empty

    return ''.join(result)

def get_part_name(line_num: int) -> str:
    """根据行号获取所属篇章名"""
    part_name = ""
    for start, name in reversed(PARTS):
        if line_num >= start:
            part_name = name
            break
    return part_name

def extract_title(lines: list) -> str:
    """从内容中提取标题"""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# ') or stripped.startswith('第 ') and '章' in stripped:
            return stripped
    return ""

def main():
    # 读取源文件
    with open(SRC, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    total = len(CHAPTERS)

    for idx, (start, end, filename) in enumerate(CHAPTERS):
        # 提取行（行号从1开始）
        lines = all_lines[start-1:end]

        # 修复断行
        fixed = fix_line_wrapping(lines)

        # 清理
        content = clean_content(fixed)

        # 提取标题
        title = extract_title(fixed)
        if not title:
            title = filename

        # 获取所属篇章
        part_name = get_part_name(start)

        # 构造 frontmatter
        # 判断是否为附录
        is_appendix = '附录' in filename

        frontmatter = f"""---
title: "{title}"
type: {"appendix" if is_appendix else "chapter"}
part: "{part_name}"
source: "Claude Code 学习手册"
aliases:
---

"""

        # 完整内容
        full_content = frontmatter + content

        # 写入
        out_path = os.path.join(OUT, filename + '.md')
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"[{idx+1}/{total}] {filename}.md ({len(content)} chars)")

    print(f"\n✅ 完成！共生成 {total} 个文件")

if __name__ == '__main__':
    main()
