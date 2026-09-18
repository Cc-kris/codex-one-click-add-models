#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write ~/.codex/ccai-catalog.json and set model_catalog_json. Never touch URL/key."""
from __future__ import annotations
import json, os, re, sys
from pathlib import Path

CATALOG_NAME = "ccai-catalog.json"
CONFIG_KEY = "model_catalog_json"
BASE_INSTRUCTIONS = (
    "You are Codex, a coding agent. You and the user share the same workspace "
    "and collaborate to achieve the user's goals."
)
LEVELS_GPT = [
    {"effort": "low", "description": "Fast responses with lighter reasoning"},
    {"effort": "medium", "description": "Balances speed and reasoning depth for everyday tasks"},
    {"effort": "high", "description": "Greater reasoning depth for complex problems"},
    {"effort": "xhigh", "description": "Extra high reasoning depth for complex problems"},
    {"effort": "max", "description": "Maximum reasoning depth for the hardest problems"},
]
LEVELS_REASONER = [
    {"effort": "low", "description": "Lighter reasoning"},
    {"effort": "medium", "description": "Balanced reasoning"},
    {"effort": "high", "description": "Greater reasoning depth"},
    {"effort": "xhigh", "description": "Extra high reasoning"},
]
LEVELS_CHAT = [
    {"effort": "none", "description": "Disable Thinking"},
    {"effort": "low", "description": "Lighter reasoning"},
    {"effort": "medium", "description": "Balanced reasoning"},
    {"effort": "high", "description": "Greater reasoning depth"},
]
# slug, display, vision, ctx, parallel, kind, default
MODELS = [
    ("gpt-5.6-luna", "GPT-5.6 Luna", True, 272000, True, "gpt", "medium"),
    ("gpt-5.6-terra", "GPT-5.6 Terra", True, 272000, True, "gpt", "medium"),
    ("gpt-5.6-sol", "GPT-5.6 Sol", True, 1050000, True, "gpt", "medium"),
    ("gpt-6-astra", "GPT-6 Astra", True, 1050000, True, "gpt", "medium"),
    ("grok-4.5", "Grok 4.5", True, 256000, True, "gpt", "high"),
    ("grok-4.6", "Grok 4.6", True, 256000, True, "gpt", "high"),
    ("deepseek-v4-flash", "DeepSeek V4 Flash", True, 128000, True, "chat", "medium"),
    ("deepseek-v4-pro", "DeepSeek V4 Pro", True, 128000, True, "reasoner", "high"),
    ("deepseek-v4.1-flash", "DeepSeek V4.1 Flash", True, 128000, True, "chat", "medium"),
    ("glm-5.3", "GLM-5.3", False, 128000, False, "reasoner", "high"),
    ("glm-5.3-flash", "GLM-5.3 Flash", False, 128000, False, "chat", "medium"),
    ("kimi-k3", "Kimi K3", True, 256000, True, "reasoner", "high"),
    ("minimax-m3", "MiniMax M3", True, 200000, True, "chat", "medium"),
    ("qwen3.8-max", "Qwen 3.8 Max", True, 256000, True, "reasoner", "high"),
]

def levels_for(kind):
    return {"gpt": LEVELS_GPT, "reasoner": LEVELS_REASONER}.get(kind, LEVELS_CHAT)

def codex_dir() -> Path:
    d = Path.home() / ".codex"
    d.mkdir(parents=True, exist_ok=True)
    return d

def build_entry(priority, spec):
    slug, name, vision, ctx, parallel, kind, default = spec
    return {
        "slug": slug,
        "display_name": name,
        "description": name,
        "base_instructions": BASE_INSTRUCTIONS,
        "default_reasoning_level": default,
        "supported_reasoning_levels": levels_for(kind),
        "shell_type": "shell_command",
        "visibility": "list",
        "supported_in_api": True,
        "priority": priority,
        "supports_reasoning_summaries": True,
        "default_reasoning_summary": "none",
        "support_verbosity": kind == "gpt",
        "truncation_policy": {"mode": "bytes", "limit": 10000},
        "supports_parallel_tool_calls": bool(parallel),
        "supports_image_detail_original": bool(vision),
        "context_window": int(ctx),
        "max_context_window": int(ctx),
        "effective_context_window_percent": 95,
        "experimental_supported_tools": [],
        "input_modalities": ["text", "image"] if vision else ["text"],
        "supports_search_tool": False,
    }

def patch_config(config_path: Path) -> str:
    line = f'{CONFIG_KEY} = "{CATALOG_NAME}"'
    if not config_path.exists():
        config_path.write_text(line + "\n", encoding="utf-8")
        return "created_config"
    text = config_path.read_text(encoding="utf-8")
    pattern = re.compile(r'(?m)^[ \t]*model_catalog_json[ \t]*=[ \t]*["\'][^"\']*["\'][ \t]*')
    if pattern.search(text):
        new_text, n = pattern.subn(line, text, count=1)
        if n:
            if new_text != text:
                config_path.write_text(new_text, encoding="utf-8")
                return "updated_existing_key"
            return "already_set"
    lines = text.splitlines(keepends=True)
    insert_at = 0
    for i, ln in enumerate(lines):
        if re.match(r"^[ \t]*model_provider[ \t]*=", ln):
            insert_at = i + 1
            break
    else:
        for i, ln in enumerate(lines):
            if ln.strip() and not ln.lstrip().startswith("#"):
                insert_at = i + 1
                break
    insert = line if line.endswith("\n") else line + "\n"
    lines.insert(insert_at, insert)
    config_path.write_text("".join(lines), encoding="utf-8")
    return "inserted_key"

def main() -> int:
    d = codex_dir()
    catalog = d / CATALOG_NAME
    models = [build_entry(i + 1, spec) for i, spec in enumerate(MODELS)]
    catalog.write_text(json.dumps({"models": models}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    action = patch_config(d / "config.toml")
    print("Codex dir :", d)
    print("Catalog   :", catalog, f"({catalog.stat().st_size} bytes)")
    print("Models    :")
    for spec in MODELS:
        print(f"  - {spec[0]:24s}  {spec[5]} ({len(levels_for(spec[5]))} levels)")
    print("Config    :", d / "config.toml", f"[{action}]")
    print("URL/key   : not modified")
    print("Fully quit Codex Desktop and reopen.")
    return 0

if __name__ == "__main__":
    try:
        code = main()
    except Exception as e:
        print("FAILED:", e, file=sys.stderr)
        code = 1
    try:
        input("\nPress Enter to close...")
    except EOFError:
        pass
    sys.exit(code)
