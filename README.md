<div align="center">

# Codex 一键添加模型脚本

**让 Codex 桌面端下拉里出现 DeepSeek、GLM、Grok、Kimi、Qwen…**  
双击运行 · 不改 API Key · 不改中转地址 · 带推理深度

[![Release](https://img.shields.io/github/v/release/Cc-kris/codex-one-click-add-models?color=2ea44f)](https://github.com/Cc-kris/codex-one-click-add-models/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-informational)](#用法)
[![Python](https://img.shields.io/badge/python-3-yellow)](#用法)

[下载压缩包](https://github.com/Cc-kris/codex-one-click-add-models/releases/latest) · [查看源码](https://github.com/Cc-kris/codex-one-click-add-models)

</div>

---

OpenAI Codex 桌面端默认只能在模型列表里看到官方 GPT。  
很多人已经用了 **OpenAI 兼容中转**（GPT / Claude / Gemini / 国产模型），但 Codex 下拉里就是选不到 DeepSeek、GLM、Grok。

这个脚本只做一件事：给 `~/.codex/` 写一份合法的 **自定义模型目录**（`ccai-catalog.json`），并在 `config.toml` 里加上：

```toml
model_catalog_json = "ccai-catalog.json"
```

写完 **完全退出再打开 Codex**，下拉就能切模型，还能调 **low / medium / high / xhigh / max** 等推理深度。  
`base_url` 和 Key **一律不动**。

适合搜这些词的人：`Codex 添加模型`、`Codex 自定义模型列表`、`Codex DeepSeek`、`Codex GLM`、`Codex Grok`、`Codex 中转`、`model_catalog_json`。

---

## 推荐中转

脚本只管「列表能不能出现」。真正能不能打通，取决于中转是否提供 **OpenAI Responses 兼容** 接口。

| 名称 | 简介 | 链接 |
|:----:|:-----|:-----|
| **CCAI** | CCAI 是一站式多模型中转平台，支持 GPT、Claude、Gemini 和各种国模。稳定高效，随充随用。 | [https://cc-ai.xyz](https://cc-ai.xyz) |

> 先在中转后台确认 model id 和本脚本 slug **一字不差**，再在 Codex 里点选。

---

## 用法

需要已安装 **Python 3**。从 [Releases](https://github.com/Cc-kris/codex-one-click-add-models/releases/latest) 下载 zip，解压即可。

<table>
<tr>
<td width="50%" valign="top">

### Windows

1. 双击 `一键添加其他模型（windows）.bat`
2. 看到成功提示后关掉窗口
3. **完全退出** Codex 桌面端再打开

</td>
<td width="50%" valign="top">

### macOS

```bash
chmod +x "一键添加其他模型（mac）.command"
```

然后双击该文件。若系统拦截：  
**设置 → 隐私与安全性 → 仍要打开**

</td>
</tr>
</table>

<details>
<summary>不想双击？命令行一样能跑</summary>

```bash
python3 install_ccai_catalog.py
```

Windows 也可用 `py -3 install_ccai_catalog.py`。

</details>

---

## 内置模型与推理档

| 模型 slug | 推理深度 |
|:----------|:---------|
| `gpt-5.6-luna` · `gpt-5.6-terra` · `gpt-5.6-sol` · `gpt-6-astra` | low / medium / high / xhigh / **max** |
| `grok-4.5` · `grok-4.6` | low / medium / high / xhigh / **max** |
| `deepseek-v4-pro` · `glm-5.3` · `kimi-k3` · `qwen3.8-max` | low / medium / high / **xhigh** |
| `deepseek-v4-flash` · `deepseek-v4.1-flash` · `glm-5.3-flash` · `minimax-m3` | none / low / medium / high |

slug 必须和中转后台的 model id **完全一致**，否则下拉能选、请求会失败。

---

## 原理（为什么改 models_cache.json 没用）

Codex 下拉优先读 `model_catalog_json` 指向的 JSON。  
官方 `models_cache.json` 会被联网刷新覆盖，而且字段太杂，直接当自定义目录用会 **解析失败并跳登录页**。

本脚本按精简的 OpenAI **Responses** 模板生成条目（和 CC Switch 同类做法）。

> Codex 桌面端走 `wire_api = "responses"`。原生 Anthropic `/v1/messages` **不能**靠本脚本切换；Claude 只有中转做成 OpenAI 兼容时才能用。

---

## 许可

MIT
