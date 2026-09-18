---
name: "codex-add-models"
description: "Use when the user wants Codex Desktop to list extra proxy models (DeepSeek, GLM, Grok, Kimi, MiniMax, Qwen, GPT-5.6, etc.) in the model picker, add/update ~/.codex/ccai-catalog.json, set model_catalog_json, or fix a catalog that dumps Codex to the login page. Never change base_url or API keys."
---

# Codex 添加模型

把自定义模型写进 `~/.codex/ccai-catalog.json`，并在 `config.toml` 加上 `model_catalog_json`。桌面端下拉会读这份文件。

## 硬性约束

- 只改 catalog 和 `model_catalog_json` 这一行。
- **禁止**改 `base_url`、`experimental_bearer_token`、`auth.json`、其它 provider 字段。
- 不要把官方 `models_cache.json` 整份当自定义目录（字段多、含 null，会解析失败并跳登录页）。
- 不要写 JSON `null`。不要设 `wire_api = "chat"`（新版本会整份配置失败）。
- slug 必须和中转后台的 model id 完全一致。
- 跑完告诉用户：**完全退出再开 Codex**。

## 怎么跑

在 skill 目录执行：

```bash
python3 scripts/install_ccai_catalog.py
```

Windows 可用 `python` 或 `py -3`。脚本自己找 `~/.codex`（Windows 是 `%USERPROFILE%\.codex`）。

用户要加/删模型时：改 `scripts/install_ccai_catalog.py` 里的 `MODELS`，再跑一遍。不要手搓一份超大 cache。

## 推理深度

`default_reasoning_level` 必须出现在该条的 `supported_reasoning_levels` 里，否则界面不给调档。

- gpt / grok：low, medium, high, xhigh, max
- 偏推理：low, medium, high, xhigh
- 偏 flash：none, low, medium, high

## 协议

Codex 走 OpenAI Responses。中转需 OpenAI 兼容。纯 Anthropic `/v1/messages` 加进 catalog 也变不成 Claude 协议。
