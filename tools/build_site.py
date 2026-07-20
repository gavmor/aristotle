#!/usr/bin/env python3
"""Preprocess the Aristotle wiki's Obsidian wikilinks into mdsite-compatible
relative markdown links, then stage a src/ tree for mdsite to build."""
import os
import re
import shutil

VAULT = "/home/user/Documents/aristotle"
SRC = "/tmp/mdsite-check/site/src"

# Categories to publish -- internal bookkeeping (hot.md, log.md, .manifest.json,
# .obsidian/) is excluded on purpose; it's session notes, not wiki content.
CATEGORIES = ["concepts", "synthesis", "entities", "references"]

WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def target_rel_html(src_file_dir, target_path):
    """target_path is like 'concepts/hexis' (root-relative, no extension).
    Compute the path relative to src_file_dir, pointing at target_path + .html"""
    target_dir = os.path.dirname(target_path)
    target_base = os.path.basename(target_path)
    rel_dir = os.path.relpath(target_dir or ".", src_file_dir or ".")
    if rel_dir == ".":
        return f"{target_base}.html"
    return f"{rel_dir}/{target_base}.html"


def strip_frontmatter(text):
    """mdsite doesn't parse YAML frontmatter -- it renders the raw block as
    garbled markdown. Strip the leading --- ... --- fence entirely."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :].lstrip("\n")
    return text


def rewrite_wikilinks(text, file_dir):
    def repl(m):
        target = m.group(1).strip()
        display = (m.group(2) or target).strip()
        href = target_rel_html(file_dir, target)
        return f"[{display}]({href})"

    return WIKILINK.sub(repl, text)


def main():
    if os.path.exists(SRC):
        shutil.rmtree(SRC)
    os.makedirs(SRC)

    copied = 0
    for cat in CATEGORIES:
        src_cat_dir = os.path.join(VAULT, cat)
        if not os.path.isdir(src_cat_dir):
            continue
        out_cat_dir = os.path.join(SRC, cat)
        os.makedirs(out_cat_dir, exist_ok=True)
        for fname in sorted(os.listdir(src_cat_dir)):
            if not fname.endswith(".md"):
                continue
            with open(os.path.join(src_cat_dir, fname), encoding="utf-8") as f:
                text = f.read()
            text = strip_frontmatter(text)
            text = rewrite_wikilinks(text, cat)
            with open(os.path.join(out_cat_dir, fname), "w", encoding="utf-8") as f:
                f.write(text)
            copied += 1

    # Homepage from index.md, rewritten from the root's perspective ("")
    with open(os.path.join(VAULT, "index.md"), encoding="utf-8") as f:
        idx = f.read()
    idx = strip_frontmatter(idx)
    idx = rewrite_wikilinks(idx, "")
    with open(os.path.join(SRC, "index.md"), "w", encoding="utf-8") as f:
        f.write(idx)

    print(f"Staged {copied} pages + homepage into {SRC}")


if __name__ == "__main__":
    main()
