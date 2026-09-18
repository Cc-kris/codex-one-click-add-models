<div align="center">

# Codex 添加模型 Skill

给 Codex 桌面端写入自定义模型列表。  
把仓库链接丢给 Codex 安装，再说一句触发即可。不改 API Key，不改中转地址。

[![Release](https://img.shields.io/github/v/release/Cc-kris/codex-one-click-add-models?color=2ea44f)](https://github.com/Cc-kris/codex-one-click-add-models/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/Cc-kris/codex-one-click-add-models/releases)

</div>

Codex 自带下拉只有官方那几个 GPT。中转上的 DeepSeek、GLM、Grok、Kimi、Qwen 默认出不来。  
这个 skill 会写 `~/.codex/ccai-catalog.json`，并加上：

```toml
model_catalog_json = "ccai-catalog.json"
```

---

## 推荐中转

| 名称 | 简介 | 链接 |
| --- | --- | --- |
| CCAI | CCAI是一站式多模型中转平台，支持GPT、Claude、Gemini和各种国模。稳定高效，随充随用。 | https://cc-ai.xyz |

---

## 用 Codex 安装这个 Skill

在 Codex 对话里发：

```text
帮我安装这个 skill：https://github.com/Cc-kris/codex-one-click-add-models/tree/main/codex-add-models
```

装好后（下一轮生效），再说：

```text
把中转模型加进下拉
```

然后 **完全退出再开 Codex**，下拉里才会出现新模型。

安装走官方 `skill-installer`（GitHub 链接 → `~/.codex/skills/codex-add-models`）。不要手工拷文件。

---

## 模型

| slug | 推理深度 |
| --- | --- |
| `gpt-5.6-luna` · `gpt-5.6-terra` · `gpt-5.6-sol` · `gpt-6-astra` · `grok-4.5` · `grok-4.6` | low / medium / high / xhigh / max |
| `deepseek-v4-pro` · `glm-5.3` · `kimi-k3` · `qwen3.8-max` | low / medium / high / xhigh |
| `deepseek-v4-flash` · `deepseek-v4.1-flash` · `glm-5.3-flash` · `minimax-m3` | none / low / medium / high |

---

## 格式

符合 OpenAI / Codex skill 布局：

```text
codex-add-models/
|-- SKILL.md
|-- agents/openai.yaml
`-- scripts/install_ccai_catalog.py
```

`SKILL.md` 需要 YAML：`name`、`description`。自定义 catalog 必须是精简字段，不能拿官方 `models_cache.json` 当目录。

---

## 一键脚本（不走 Codex 安装时）

[Release](https://github.com/Cc-kris/codex-one-click-add-models/releases) 下 zip，或 clone 本仓库。需要 Python 3。

| 系统 | 文件 |
| --- | --- |
| Windows | 双击 `一键添加其他模型（windows）.bat` |
| macOS | `chmod +x "一键添加其他模型（mac）.command"` 后双击 |

跑完同样要完全退出再开 Codex。

---

## 许可

MIT
