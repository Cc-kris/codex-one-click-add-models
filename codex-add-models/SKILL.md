---
name: "codex-add-models"
description: "用户说「添加其他模型」，或要把 DeepSeek、GLM、Grok、Kimi、MiniMax、Qwen、GPT-5.6 等写进 Codex 桌面端模型列表时使用。写入 ~/.codex/ccai-catalog.json 并设置 model_catalog_json。不要改 base_url 和 API Key。"
metadata:
  short-description: "给 Codex 桌面端补上其他模型"
---

# Codex 添加模型

写入 `~/.codex/ccai-catalog.json`，并在 `config.toml` 里设置 `model_catalog_json`。桌面端下拉读的是这份文件。

## 约束

- 只做上面两件事。不要改 `base_url`、`experimental_bearer_token`、`auth.json` 或其他 provider 字段。
- 不要把官方 `models_cache.json` 整份当自定义目录（多余字段或 JSON null 会让 Codex 跳登录页）。
- 不要输出 JSON `null`。不要把 `wire_api` 改成 `"chat"`。
- catalog 里的 slug 必须和接口上的 model id 完全一致。
- 跑成功后提醒用户：完全退出再打开 Codex。

## 运行

在本 skill 目录下：

```bash
python3 scripts/install_ccai_catalog.py
```

Windows 可用 `python` 或 `py -3`。脚本会定位 `~/.codex` / `%USERPROFILE%\\.codex`。

要增删模型，改 `scripts/install_ccai_catalog.py` 里的 `MODELS` 再跑一遍。

## 推理深度

`default_reasoning_level` 必须出现在该条的 `supported_reasoning_levels` 里，否则界面不给调档。

- gpt / grok：low, medium, high, xhigh, max
- 偏推理：low, medium, high, xhigh
- 偏 flash：none, low, medium, high

## 协议

Codex 走 OpenAI Responses。原生 Anthropic `/v1/messages` 不会因为写进 catalog 就变成 Claude 协议。
