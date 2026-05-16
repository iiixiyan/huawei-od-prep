#!/usr/bin/env python3
"""华为OD每日学习推送 — 读取当天课程文件，生成邮件发送"""

import os, sys, re, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_DIR = "/tmp/huawei-od-prep"
START_DATE = date(2026, 5, 11)  # 第1天 = 5月11日（周一）

# SMTP配置
SMTP = {
    "host": "smtp.163.com",
    "port": 465,
    "user": "ClawGirl@163.com",
    "pass": "GXQUv37QVZiP3XaY",
    "to": "suijiong@huawei.com",
}

# day_number → file_glob mapping (base on REPO_DIR)
# Files use inconsistent naming: day-NN-*.md, DNN-*.md, DNN-*.md
def find_day_file(day_num: int) -> str | None:
    """Find the .md file for a given day number"""
    patterns = [
        f"day-{day_num:02d}*.md",
        f"day-{day_num}*.md",
        f"D{day_num:02d}*.md",
        f"D{day_num}*.md",
    ]
    for pat in patterns:
        matches = list(Path(REPO_DIR).rglob(pat))
        if matches:
            # Exclude curriculum.md and README
            for m in matches:
                if "curriculum" not in m.name.lower() and "readme" not in m.name.lower():
                    return str(m)
    return None

def get_week_name(day_num: int) -> str:
    """Week number and name based on day"""
    weeks = [
        (1, 7, "第1周 — 数组 & 哈希表"),
        (8, 14, "第2周 — 字符串 & 双指针"),
        (15, 21, "第3周 — 栈、队列、链表"),
        (22, 28, "第4周 — 二叉树、图"),
        (29, 35, "第5周 — OD 100分·字符串/数组类"),
        (36, 42, "第6周 — OD 100分·树/图/矩阵类"),
        (43, 49, "第7周 — OD 200分题"),
        (50, 56, "第8周 — 模拟考冲刺"),
    ]
    for start, end, name in weeks:
        if start <= day_num <= end:
            return f"第{(start-1)//7+1}周"
    return "未知"

def extract_content(md_path: str) -> str:
    """Read markdown file and extract key content"""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return f"❌ 读取失败: {e}"

    # Remove frontmatter if present
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Convert markdown headings to HTML-ish format for email
    lines = content.split('\n')
    html_lines = []
    in_code = False
    
    for line in lines:
        if line.startswith('```'):
            in_code = not in_code
            if in_code:
                html_lines.append('<pre style="background:#1e1e1e;color:#d4d4d4;padding:10px;border-radius:4px;overflow-x:auto;font-size:13px">')
            else:
                html_lines.append('</pre>')
            continue
        
        if in_code:
            html_lines.append(line)
            continue
        
        if line.startswith('# '):
            html_lines.append(f'<h2 style="color:#c62828;border-bottom:2px solid #c62828;padding-bottom:5px">{line[2:]}</h2>')
        elif line.startswith('## '):
            html_lines.append(f'<h3 style="color:#1565c0">{line[3:]}</h3>')
        elif line.startswith('### '):
            html_lines.append(f'<h4 style="color:#2e7d32">{line[4:]}</h4>')
        elif line.startswith('- '):
            html_lines.append(f'<li>{line[2:]}</li>')
        elif line.startswith('**') and line.endswith('**'):
            html_lines.append(f'<p><strong>{line[2:-2]}</strong></p>')
        elif line.strip():
            html_lines.append(f'<p>{line}</p>')
        else:
            html_lines.append('<br>')
    
    return '\n'.join(html_lines)

def send_email(html_body: str, subject: str):
    """Send email via 163 SMTP"""
    msg = MIMEMultipart("alternative")
    msg["From"] = SMTP["user"]
    msg["To"] = SMTP["to"]
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL(SMTP["host"], SMTP["port"]) as server:
        server.login(SMTP["user"], SMTP["pass"])
        server.sendmail(SMTP["user"], [SMTP["to"]], msg.as_string())
    print(f"✅ 邮件已发送 → {SMTP['to']}")

def main():
    today = date.today()
    day_num = (today - START_DATE).days + 1
    
    if day_num < 1:
        print(f"📅 课程尚未开始（{today}，距开始还有{-day_num+1}天）")
        sys.exit(0)
    if day_num > 56:
        print(f"🎉 课程已结束！共56天，今天第{day_num}天")
        sys.exit(0)
    
    print(f"📅 今天 {today} | 课程 Day {day_num} | {get_week_name(day_num)}")
    
    filepath = find_day_file(day_num)
    if not filepath:
        print(f"❌ 未找到 Day {day_num} 的课程文件")
        print("尝试的模式: day-{:02d}*.md / D{:02d}*.md".format(day_num, day_num))
        # List all day files for debugging
        all_md = sorted(Path(REPO_DIR).rglob("day-*.md")) + sorted(Path(REPO_DIR).rglob("D*.md"))
        print("可用文件:", [p.name for p in all_md if 'curriculum' not in p.name.lower()][:10])
        sys.exit(1)
    
    print(f"📄 课程文件: {filepath}")
    
    content_html = extract_content(filepath)
    
    # Build full HTML email
    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:700px;margin:0 auto;padding:20px;background:#f5f5f5">
<div style="background:white;border-radius:8px;padding:24px;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
    
    <div style="background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:20px;border-radius:8px;margin-bottom:20px">
        <h1 style="margin:0 0 8px 0;font-size:24px">🎯 华为OD · Day {day_num}</h1>
        <p style="margin:0;opacity:0.85">📅 {today.strftime('%Y年%m月%d日')} | {get_week_name(day_num)} | 总进度 {day_num}/56 ({day_num*100//56}%)</p>
    </div>
    
    {content_html}
    
    <hr style="border:none;border-top:1px solid #e0e0e0;margin:24px 0">
    
    <div style="background:#e8f5e9;padding:16px;border-radius:8px">
        <h4 style="margin:0 0 8px 0;color:#2e7d32">📝 今日学习建议</h4>
        <ul style="margin:0;padding-left:20px">
            <li>📖 先看知识点速览（15min）</li>
            <li>🧩 逐题练习，先思考再对答案（75min）</li>
            <li>✅ 对照代码理解错题（15min）</li>
            <li>📝 记录易错点（5min）</li>
        </ul>
    </div>
    
    <p style="color:#999;font-size:12px;text-align:center;margin-top:20px">📬 自动推送 | ClawBot · 华为OD备考助手</p>
</div>
</body>
</html>"""
    
    subject = f"🎯 华为OD Day{day_num} | {today.strftime('%m/%d')} {get_week_name(day_num)}"
    send_email(html, subject)

if __name__ == "__main__":
    main()
