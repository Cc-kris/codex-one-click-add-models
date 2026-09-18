<div align="center">

# Codex 一键添加模型脚本

双击运行，给 Codex 桌面端补上自定义模型列表。  
不改 API Key，不改中转地址，可选推理深度。

[![Release](https://img.shields.io/github/v/release/Cc-kris/codex-one-click-add-models?color=2ea44f)](https://github.com/Cc-kris/codex-one-click-add-models/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-informational)](#用法)
[![Python](https://img.shields.io/badge/python-3-yellow)](#用法)

[下载压缩包](https://github.com/Cc-kris/codex-one-click-add-models/releases/latest) · [查看源码](https://github.com/Cc-kris/codex-one-click-add-models)

</div>

---

Codex 桌面端自带的模型下拉只有官方那几个 GPT。中转里明明有 DeepSeek、GLM、Grok、Kimi、Qwen，界面上就是选不到。

跑这个脚本会在 `~/.codex/` 生成 `ccai-catalog.json`，并在 `config.toml` 写入：

```toml
model_catalog_json = "ccai-catalog.json"
```

然后 **完全退出再打开 Codex**，下拉里就会出现这些模型，推理深度也能调。中转的地址和 Key 不会被改。

---

## 推荐中转

| 名称 | 简介 | 链接 |
|:----:|:-----|:-----|
| **CCAI** | CCAI 是一站式多模型中转平台，支持 GPT、Claude、Gemini 和各种国模。稳定高效，随充随用。 | [https://cc-ai.xyz](https://cc-ai.xyz) |

中转后台里的模型名要和下面表格里的 slug 一致，否则列表能点、请求会失败。

---

## 用法

需要 Python 3。从 [Releases](https://github.com/Cc-kris/codex-one-click-add-models/releases/latest) 下 zip，解压。

<table>
<tr>
<td width="50%" valign="top">

### Windows

双击 `一键添加其他模型（windows）.bat`，跑完后关掉窗口，再 **完全退出** Codex 重新打开。

</td>
<td width="50%" valign="top">

### macOS

```bash
chmod +x "一键添加其他模型（mac）.command"
```

双击运行。如果被拦截：系统设置 → 隐私与安全性 → 仍要打开。

</td>
</tr>
</table>

<details>
<summary>命令行</summary>

```bash
python3 install_ccai_catalog.py
```

Windows 也可以：`py -3 install_ccai_catalog.py`

</details>

---

## 内置模型

| slug | 推理深度 |
|:-----|:---------|
| `gpt-5.6-luna` · `gpt-5.6-terra` · `gpt-5.6-sol` · `gpt-6-astra` | low / medium / high / xhigh / max |
| `grok-4.5` · `grok-4.6` | low / medium / high / xhigh / max |
| `deepseek-v4-pro` · `glm-5.3` · `kimi-k3` · `qwen3.8-max` | low / medium / high / xhigh |
| `deepseek-v4-flash` · `deepseek-v4.1-flash` · `glm-5.3-flash` · `minimax-m3` | none / low / medium / high |

---

## 说明

Codex 读的是 `model_catalog_json` 指向的文件，不是去改会被覆盖的 `models_cache.json`。自定义目录必须是精简字段；把官方缓存整份拷进去，容易解析失败，打开直接进登录页。

客户端走 OpenAI Responses（`wire_api = "responses"`）。中转如果只提供 Anthropic 原生接口，这个脚本加不出真正的 Claude 协议。

---

## 许可

MIT
