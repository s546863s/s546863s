from datetime import date

# ✅ এখানে শুধু START_DATE পরিবর্তন করুন
START_DATE = date(2025, 4, 18)

# Phase গুলো
PHASES = [
    ("JavaScript Fundamentals", 1,  14),
    ("JavaScript Advanced",     15, 28),
    ("Node.js + Express",       29, 42),
    ("MongoDB + Mongoose",      43, 56),
    ("React",                   57, 77),
    ("Socket.io + WebRTC",      78, 98),
    ("Final Project + Deploy",  99, 120),
]

def get_current_day():
    delta = (date.today() - START_DATE).days + 1
    return max(1, min(120, delta))

def get_phase(day):
    for i, (name, start, end) in enumerate(PHASES):
        if start <= day <= end:
            return i + 1, name
    return 7, PHASES[-1][0]

def get_progress_bar(day, total=120, length=20):
    filled = int((day / total) * length)
    bar = "█" * filled + "░" * (length - filled)
    pct = round((day / total) * 100)
    return bar, pct

def get_phase_table(current_day):
    icons = ["🟡","🟢","🟢","🟢","🟢","🟢","🟢"]
    rows = ""
    for i, (name, start, end) in enumerate(PHASES):
        if current_day < start:
            status = "⏳ Upcoming"
            icon = "⚪"
        elif current_day > end:
            status = "✅ Done"
            icon = "🟢"
        else:
            status = "🔄 In Progress"
            icon = "🟡"
        rows += f"| {icon} Phase {i+1} | {name} | Day {start}–{end} | {status} |\n"
    return rows

# README আপডেট
day = get_current_day()
phase_num, phase_name = get_phase(day)
bar, pct = get_progress_bar(day)
table = get_phase_table(day)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

import re

# Day badge
content = re.sub(
    r"Challenge-Day%20\d+%20of%20120",
    f"Challenge-Day%20{day}%20of%20120",
    content
)

# Phase badge
content = re.sub(
    r"Phase-\d+%20of%207",
    f"Phase-{phase_num}%20of%207",
    content
)

# Progress bar
content = re.sub(
    r"Progress ━+.*?\(\d+%\)",
    f"Progress ━━━━━━━━━━━━━━━━━━━━━━━━  Day {day} / 120  ({pct}%)",
    content
)

# Phase table
content = re.sub(
    r"(\| Phase \| Topic \| Days \| Status \|\n\|[-|]+\|\n)([\s\S]*?)(\n📌)",
    rf"\1{table}\3",
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ README updated — Day {day}, Phase {phase_num}: {phase_name} ({pct}%)")