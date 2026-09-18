<div align="center">

# Codex 添加模型 Skill

给 Codex 桌面端写入自定义模型列表。对话里让 Agent 跑，或自己双击脚本。  
不改 API Key，不改中转地址。

[![Release](https://img.shields.io/github/v/release/Cc-kris/codex-one-click-add-models?color=2ea44f)](https://github.com/Cc-kris/codex-one-click-add-models/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/Cc-kris/codex-one-click-add-models/releases)

</div>

Codex 自带下拉只有官方那几个 GPT。中转上的 DeepSeek、GLM、Grok、Kimi、Qwen 默认出不来。  
这个 skill 会在 `~/.codex` 写一份 `ccai-catalog.json`，并加上：

```toml
model_catalog_json = "ccai-catalog.json"
```

---
<img width="1171" height="947" alt="image" src="https://github.com/user-attachments/assets/3f0e1c33-15d3-4fff-95b0-22708984e3cf" />


## 推荐中转

| 名称 | 简介 | 链接 |
| --- | --- | --- |
| CCAI | CCAI是一站式多模型中转平台，支持GPT、Claude、Gemini和各种国模。稳定高效，随充随用。 | https://cc-ai.xyz |

---

## 当 Skill 用

1. 把本仓库拷到 `~/.codex/skills/codex-add-models/`（Windows：`%USERPROFILE%\.codex\skills\codex-add-models\`）。
2. 需要 `SKILL.md` 和 `scripts/install_ccai_catalog.py`。
3. 打开 Codex，说「把中转模型加进下拉」即可。
4. **完全退出再开 Codex**，下拉里才会出现新模型。

Agent 只会改 catalog 和 `model_catalog_json`，不会动你的地址和 Key。

---

## 模型

| slug | 推理深度 |
| --- | --- |
| `gpt-5.6-luna` · `gpt-5.6-terra` · `gpt-5.6-sol` · `gpt-6-astra` · `grok-4.5` · `grok-4.6` | low / medium / high / xhigh / max |
| `deepseek-v4-pro` · `glm-5.3` · `kimi-k3` · `qwen3.8-max` | low / medium / high / xhigh |
| `deepseek-v4-flash` · `deepseek-v4.1-flash` · `glm-5.3-flash` · `minimax-m3` | none / low / medium / high |

slug 必须和中转后台的 model id 一致。

---

## 说明

自定义目录必须是精简字段。把官方 `models_cache.json` 整份拷进去，容易解析失败，打开直接进登录页。

客户端走 OpenAI Responses。中转如果只提供 Anthropic 原生接口，加进列表也不是 Claude 协议。

---

## 一键脚本（不用 skill 时）

[Release](https://github.com/Cc-kris/codex-one-click-add-models/releases) 里下 zip，或 clone 本仓库。需要已安装 Python 3。

| 系统 | 文件 |
| --- | --- |
| Windows | 双击 `一键添加其他模型（windows）.bat` |
| macOS | 终端执行 `chmod +x "一键添加其他模型（mac）.command"`，再双击 |

跑完同样要完全退出再开 Codex。

---

## 许可

MIT
