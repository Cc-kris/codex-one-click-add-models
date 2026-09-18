---
name: "codex-add-models"
description: "Use when the user says 添加其他模型, or wants extra models (DeepSeek, GLM, Grok, Kimi, MiniMax, Qwen, GPT-5.6) in the Codex Desktop picker, or to write ~/.codex/ccai-catalog.json and model_catalog_json. Do not change base_url or API keys."
metadata:
  short-description: "Add extra models to the Codex Desktop picker"
---

# Codex 添加模型

Write `~/.codex/ccai-catalog.json` and set `model_catalog_json` in `config.toml`. The Desktop picker reads that file.

## Constraints

- Only those two things. Never edit `base_url`, `experimental_bearer_token`, `auth.json`, or other provider fields.
- Do not copy official `models_cache.json` as the custom catalog (extra fields / JSON null send Codex to the login page).
- Do not emit JSON `null`. Do not set `wire_api = "chat"`.
- Catalog slugs must match the proxy model ids exactly.
- After a successful run, tell the user to fully quit and reopen Codex.

## Run

From this skill folder:

```bash
python3 scripts/install_ccai_catalog.py
```

On Windows: `python` or `py -3`. The script resolves `~/.codex` / `%USERPROFILE%\.codex`.

To add or remove models, edit `MODELS` in `scripts/install_ccai_catalog.py` and run again.

## Reasoning levels

`default_reasoning_level` must be one of `supported_reasoning_levels` or the UI hides the control.

- gpt / grok: low, medium, high, xhigh, max
- reasoner: low, medium, high, xhigh
- flash: none, low, medium, high

## Protocol

Codex uses OpenAI Responses. A native Anthropic `/v1/messages` endpoint will not become Claude protocol just because the slug is in the catalog.
