#!/usr/bin/env python3
"""Sync 프로그래머스 push to Notion DB - mark as DONE."""
import os
import re
import subprocess
import sys
import urllib.parse
from datetime import datetime, timezone, timedelta

import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATA_SOURCE_ID = os.environ["NOTION_DATA_SOURCE_ID"]
GITHUB_REPO = os.environ["GITHUB_REPO"]

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2025-09-03",
    "Content-Type": "application/json",
}


def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True, text=True, check=True
    )
    return [f for f in result.stdout.strip().split("\n") if f]


def extract_problems(files):
    """Pattern: 프로그래머스/{level}/{number}. {name}/..."""
    problems = {}
    pattern = re.compile(r"프로그래머스/(\d+)/(\d+)\.\s+(.+?)/")
    for f in files:
        m = pattern.match(f)
        if m:
            level, number, name = m.group(1), m.group(2), m.group(3)
            if number not in problems:
                problems[number] = {
                    "level": level,
                    "name": name,
                    "folder": f"{number}. {name}",
                }
    return problems


def find_notion_page(problem_number):
    url = f"https://api.notion.com/v1/data_sources/{DATA_SOURCE_ID}/query"
    body = {
        "filter": {
            "property": "문제번호",
            "rich_text": {"equals": problem_number}
        }
    }
    resp = requests.post(url, headers=HEADERS, json=body, timeout=30)
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return results[0]["id"] if results else None


def update_page(page_id, level, folder):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    kst = timezone(timedelta(hours=9))
    today = datetime.now(kst).strftime("%Y-%m-%d")
    encoded_folder = urllib.parse.quote(folder)
    encoded_prgms = urllib.parse.quote("프로그래머스")
    github_url = (
        f"https://github.com/{GITHUB_REPO}/tree/main/"
        f"{encoded_prgms}/{level}/{encoded_folder}"
    )
    body = {
        "properties": {
            "상태": {"status": {"name": "DONE"}},
            "풀이일": {"date": {"start": today}},
            "github": {"url": github_url},
        }
    }
    resp = requests.patch(url, headers=HEADERS, json=body, timeout=30)
    if resp.status_code == 200:
        return True
    print(f"  Update failed: {resp.status_code} {resp.text}", file=sys.stderr)
    return False


def main():
    files = get_changed_files()
    print(f"Changed files: {len(files)}")
    problems = extract_problems(files)
    if not problems:
        print("No 프로그래머스 problems in changes")
        return 0
    print(f"Detected {len(problems)} problem(s): {sorted(problems.keys())}")
    success = 0
    for number, info in problems.items():
        print(f"\n-> Problem {number} ({info['name']}, Lv.{info['level']})")
        page_id = find_notion_page(number)
        if not page_id:
            print(f"  Not in Notion DB, skipping")
            continue
        if update_page(page_id, info["level"], info["folder"]):
            print(f"  Marked DONE")
            success += 1
    print(f"\n=== Done: {success}/{len(problems)} updated ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
