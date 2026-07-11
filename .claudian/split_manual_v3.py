#!/usr/bin/env python3
"""拆分 Claude Code 学习手册 - v3: 段落级智能合并"""

import re
import os

VAULT = "/Users/miaomaio/Library/Mobile Documents/iCloud~md~obsidian/Documents/小懂不懂知识库"
SRC = os.path.join(VAULT, "未命名 2.md")
OUT = os.path.join(VAULT, "10-知识管理/Claude Code 学习手册")

PART_STARTS = {1:147, 2:2677, 3:5785, 4:8915, 5:11395, 6:13255, 7:19471, 8:22565, 9:25037, 10:26907}
PART_NAMES = {
    1:"第一篇：入门地图 - 从 AI Agent 到 Claude Code",
    2:"第二篇：日常开发工作流 - 先把 Claude Code 用顺手",
    3:"第三篇：Markdown、记忆和本地知识库",
    4:"第四篇：提示词、Opus 4.7 和模型驾驭",
    5:"第五篇：上下文、Token 和成本控制",
    6:"第六篇：扩展系统 - Skills、Commands、SubAgents、Hooks、MCP、Plugins",
    7:"第七篇：自动化、GitHub、CI 和可编程 Agent",
    8:"第八篇：安全、权限、沙箱和风险控制",
    9:"第九篇：高级驾驭工程 - 从会用到会设计 Agent 工作系统",
    10:"第十篇：完整实战案例",
}

CHAPTERS = [
    (1,146,"00-前言与目录",None),
    (147,782,"第01章-为什么Claude Code不只是聊天机器人",1),
    (783,1428,"第02章-环境账号模型和第一个任务",1),
    (1429,2044,"第03章-Claude Code的文件读写和工具系统",1),
    (2045,2674,"第04章-学习用项目准备",1),
    (2677,3318,"第05章-代码理解与项目地图",2),
    (3319,3922,"第06章-Bug定位与修复",2),
    (3923,4538,"第07章-重构测试和文档",2),
    (4539,5172,"第08章-Git工作流与提交质量",2),
    (5173,5780,"第09章-从一次性问答到可复用工作流",2),
    (5781,6402,"第10章-Markdown不是文档格式而是Agent控制层",3),
    (6403,7046,"第11章-CLAUDE.md记忆系统",3),
    (7047,7656,"第12章-项目规则AGENTS.md和规则文件夹",3),
    (7657,8270,"第13章-本地知识库",3),
    (8271,8912,"第14章-记忆系统的反模式",3),
    (8913,9522,"第15章-Claude Code提示词基本功",4),
    (9523,10138,"第16章-计划模式与探索模式",4),
    (10139,10784,"第17章-驯服Opus 4.7",4),
    (10785,11392,"第18章-复杂工程任务的提示词编排",4),
    (11393,12010,"第19章-上下文窗口与文件选择",5),
    (12011,12644,"第20章-压缩恢复和长会话管理",5),
    (12645,13252,"第21章-Token节省与成本优化",5),
    (13253,13866,"第22章-Skills基础",6),
    (13867,14504,"第23章-自定义命令与任务型Skill",6),
    (14505,15108,"第24章-SubAgents基础",6),
    (15109,15724,"第25章-多Agent协作",6),
    (15725,16358,"第26章-Hooks事件驱动自动化",6),
    (16359,16964,"第27章-MCP基础与外部工具连接",6),
    (16965,17592,"第28章-Plugins插件系统",6),
    (17593,18240,"第29章-Tools与Rules体系",6),
    (18241,18854,"第30章-Skill Agent MCP Plugin的组合模式",6),
    (18855,19468,"第31章-扩展系统实战小项目",6),
    (19469,20104,"第32章-Headless模式与命令行自动化",7),
    (20105,20710,"第33章-Agent SDK入门",7),
    (20711,21324,"第34章-Routines定时任务和自动化工作流",7),
    (21325,21958,"第35章-GitHub PR CI工作流",7),
    (21959,22562,"第36章-IDE浏览器和外部开发工具集成",7),
    (22563,23176,"第37章-权限系统和安全工作模式",8),
    (23177,23810,"第38章-沙箱数据安全和提示注入",8),
    (23811,24414,"第39章-Git安全发布和回滚",8),
    (24415,25034,"第40章-生产级Claude Code使用规范",8),
    (25035,25676,"第41章-Claude Code内部工作机制导览",9),
    (25677,26280,"第42章-上下文工程缓存和成本工程",9),
    (26281,26902,"第43章-从个人能力到团队AI编码体系",9),
    (26903,27550,"第44章-实战一个人Python项目从Bug到PR",10),
    (27551,28164,"第45章-实战二团队Claude Code工具包",10),
    (28165,28212,"附录/附录A-Claude Code常用命令速查",None),
    (28213,28274,"附录/附录B-目录与文件速查",None),
    (28275,28328,"附录/附录C-Markdown写作模板",None),
    (28329,28362,"附录/附录D-提示词模板库",None),
    (28363,28414,"附录/附录E-Skill模板库",None),
    (28415,28452,"附录/附录F-SubAgent模板库",None),
    (28453,28488,"附录/附录G-MCP配置示例",None),
    (28489,28516,"附录/附录H-Hooks示例",None),
    (28517,28572,"附录/附录I-Token与成本清单",None),
    (28573,28610,"附录/附录J-安全清单",None),
    (28611,28678,"附录/附录K-术语表",None),
]

# Chinese/CJK sentence-ending punctuation
SENTENCE_END = set('。！？…—）」》”\'）')
# Chinese/CJK mid-sentence punctuation (line probably continues)
MID_PUNCT = set('，、；：,;:')

# Short phrases that indicate section headers (not to be merged with body)
SECTION_HEADERS = {
    '本章导读', '学习目标', '核心概念', '操作步骤', '示例', '练习', '检查清单',
    '常见坑与排查', '常见问题', '本章小结', '阅读说明', '总目录', '附录目录',
    '先做一个小案例', '参考资料', '术语', '说明', '处理方式', '表现',
}

# Lines starting with these are metadata and should stay separate
METADATA_PREFIXES = ('所属篇章：', '主案例语言：', '命令示例：')

# Code-indicating patterns (Python-heavy)
CODE_PATTERNS = [
    re.compile(r'^(from\s+\w+\s+import|import\s+\w+)'),
    re.compile(r'^(def\s+|class\s+|if\s+__name__)'),
    re.compile(r'^[A-Z_]+\s*=\s*'),
    re.compile(r'^(try:|except|finally:|with\s+|for\s+|while\s+|return\s|yield\s)'),
    re.compile(r'^(\s{4,}|\t)'),
    re.compile(r'^(Set-Location|cd\s+|mkdir\s+|python|pip\s+|npm\s+|git\s+|claude\s+)'),
]

def is_page_artifact(s):
    """检测页眉、页脚、页码"""
    if s == 'Claude Code 学习手册':
        return True
    if re.match(r'^\d{1,4}$', s):
        return True
    if re.match(r'^\d{1,4}Claude Code 学习手册$', s):
        return True
    return False

def is_structural(s):
    """检测结构性行（不参与文本合并）"""
    if not s:
        return True
    if s.startswith('```') or s == '---':
        return True
    if s.startswith('#'):
        return True
    if s.startswith('|'):
        return True
    if re.match(r'^(\s{4,}|\t)', s):
        return True
    if re.match(r'^[-*•]\s', s):
        return True
    if re.match(r'^\d+\.\s', s):
        return True
    if re.match(r'^\d+\.\d+', s):
        return True
    if re.match(r'^\[.\]\s', s):
        return True
    return False

def is_code_line(s):
    """检测是否是代码行"""
    for pat in CODE_PATTERNS:
        if pat.match(s):
            return True
    return False

def is_section_header(s):
    """检测是否是章节内部的小标题（如'本章导读'、'学习目标'等）"""
    if s in SECTION_HEADERS:
        return True
    # 元数据行
    if s.startswith(METADATA_PREFIXES):
        return True
    return False

def ends_with_mid_punct(s):
    """行尾是否是句中标点（说明句子没结束，应该合并下一行）"""
    if not s:
        return False
    last = s[-1]
    if last in MID_PUNCT:
        return True
    # 以中文字符结尾（说明在词中截断）
    if '一' <= last <= '鿿':
        return True
    # 以英文字母结尾（说明在词中截断）
    if last.isalpha():
        return True
    return False

def classify_line(line):
    """将行分类"""
    s = line.strip()
    if not s:
        return 'empty'
    if is_page_artifact(s):
        return 'page'
    if s in ('竖版电子书优化版', '目录'):
        return 'page'
    # 目录+书名残留 (e.g. "目录Claude Code 学习手册")
    if s.startswith('目录') and 'Claude Code' in s:
        return 'page'
    if is_structural(s):
        return 'structural'
    if is_code_line(s):
        return 'code'
    if is_section_header(s):
        return 'header'
    # 检测 Generated 日期行
    if re.match(r'^Generated \d{4}-\d{2}-\d{2}', s):
        return 'page'
    return 'text'

def join_text_block(lines):
    """将多行文本合并为一个段落"""
    if not lines:
        return ''
    result = lines[0].rstrip('\n')
    for line in lines[1:]:
        nxt = line.strip()
        if not nxt:
            continue
        if result and nxt:
            last_c = result[-1]
            first_c = nxt[0]
            # 中文之间不加空格
            if '一' <= last_c <= '鿿' or last_c in '：，。！？、；：“”（）《》—…':
                result += nxt
            elif last_c.isalpha() and first_c.isalpha():
                result += ' ' + nxt
            elif last_c in ':,;':
                result += nxt
            else:
                result += nxt
    return result + '\n'

def process_lines(raw_lines):
    """主处理函数：分类→合并→输出"""

    # 预处理：strip "Claude Code 学习手册" suffix from lines
    def clean_line(line):
        s = line.rstrip('\n')
        # 去除行尾的 "Claude Code 学习手册" 残留
        if s.endswith('Claude Code 学习手册'):
            s = s[:-len('Claude Code 学习手册')].rstrip()
            return s + '\n'
        # 去除行尾的 "Claude Code 学习手册" 前面有数字的情况
        s = re.sub(r'\d{1,4}Claude Code 学习手册$', '', s).rstrip()
        if s:
            return s + '\n'
        return '\n'
    raw_lines = [clean_line(line) for line in raw_lines]
    # 第一步：分类每一行
    classified = [(classify_line(line), line) for line in raw_lines]

    # 第二步：分组处理
    # 将连续的 'text' 行分组，遇到 non-text 时结束当前组
    # 但也要处理一个特殊情况: 'text' → 'empty' → 'text' 可能是页面断行，应该跨空行合并
    # 策略: 收集连续的 text+empty 块，直到遇到 structural/header/page，然后合并 text 行

    groups = []  # list of (type, content)
    i = 0
    while i < len(classified):
        typ, line = classified[i]

        if typ == 'page':
            i += 1
            continue

        if typ in ('structural', 'header', 'code'):
            groups.append((typ, line))
            i += 1
            continue

        if typ == 'empty':
            # 收集连续空行，压缩为一个
            while i < len(classified) and classified[i][0] == 'empty':
                i += 1
            # 只有当后面有内容且不是 structural/page 时才保留空行
            if i < len(classified) and classified[i][0] in ('text', 'header', 'structural', 'code'):
                groups.append(('empty', '\n'))
            continue

        if typ == 'text':
            # 收集连续的 text 行（可能被 empty 行分隔）
            text_lines = [line]
            j = i + 1
            while j < len(classified):
                next_typ, next_line = classified[j]
                if next_typ == 'text':
                    text_lines.append(next_line)
                    j += 1
                elif next_typ == 'empty':
                    # 跳过单个空行，检查后面是否还是 text
                    k = j + 1
                    while k < len(classified) and classified[k][0] == 'empty':
                        k += 1
                    if k < len(classified) and classified[k][0] == 'text':
                        # 空行后面还是 text，且当前行以句中标点结尾 → 跨空行合并
                        if text_lines and ends_with_mid_punct(text_lines[-1].strip()):
                            text_lines.append(next_line)  # 加入空行（会被 join 忽略）
                            j = k  # 跳到空行后面的位置继续
                            continue
                    # 否则空行是真正的段落分隔
                    break
                elif next_typ in ('page', 'empty'):
                    # 跳过页眉页脚，继续检查后面
                    k = j + 1
                    while k < len(classified) and classified[k][0] in ('page', 'empty'):
                        k += 1
                    if k < len(classified) and classified[k][0] == 'text':
                        if text_lines and ends_with_mid_punct(text_lines[-1].strip()):
                            j = k  # 跳过 page artifacts，继续合并
                            continue
                    break
                else:
                    break

            merged = join_text_block(text_lines)
            groups.append(('text', merged))
            i = j
            continue

        i += 1

    # 第三步：输出，合并连续空行
    result = []
    prev_was_empty = False
    for typ, content in groups:
        if typ == 'empty':
            if not prev_was_empty:
                result.append('\n')
            prev_was_empty = True
        else:
            result.append(content)
            prev_was_empty = False

    # 清理首尾空行
    while result and result[0].strip() == '':
        result.pop(0)
    while result and result[-1].strip() == '':
        result.pop(-1)

    return ''.join(result)

def extract_title(processed_lines):
    """从处理后的内容中提取标题"""
    for line in processed_lines:
        s = line.strip()
        if re.match(r'^第 \d+ 章', s):
            return s
        if s.startswith('附录 ') and '：' in s:
            return s
    return ""

def process_section(lines, filename, start_line, explicit_part=None):
    content = process_lines(lines)

    # 提取标题
    title = extract_title(content.split('\n'))
    if not title:
        title = filename

    # 确定篇章
    is_appendix = filename.startswith('附录')
    if is_appendix:
        part_name = "附录"
    elif explicit_part is not None:
        part_name = PART_NAMES.get(explicit_part, "")
    else:
        part_num = 0
        for num, start in sorted(PART_STARTS.items()):
            if start_line >= start:
                part_num = num
        part_name = PART_NAMES.get(part_num, "") if part_num else ""

    frontmatter = f"""---
title: "{title}"
type: {"appendix" if is_appendix else "chapter"}
part: "{part_name}"
source: "Claude Code 学习手册"
aliases:
---

"""
    full_content = frontmatter + content + '\n'

    out_path = os.path.join(OUT, filename + '.md')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

    return len(content)

def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    total = len(CHAPTERS)
    for idx, (start, end, filename, explicit_part) in enumerate(CHAPTERS):
        lines = all_lines[start-1:end]
        size = process_section(lines, filename, start, explicit_part)
        print(f"[{idx+1:02d}/{total}] {filename}.md — {size} chars")

    print(f"\n✅ 完成！共生成 {total} 个文件")

if __name__ == '__main__':
    main()
