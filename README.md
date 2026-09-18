# Codex 一键添加模型脚本

给 **Codex 桌面端** 写入自定义模型目录（`~/.codex/ccai-catalog.json`），让下拉列表出现中转上的 GPT / Grok / DeepSeek / GLM / Kimi / MiniMax / Qwen 等模型，并带可选推理深度。

**不修改** `config.toml` 里的 `base_url` 和 API Key，只增加或更新：

```toml
model_catalog_json = "ccai-catalog.json"
```

> Codex 客户端走 OpenAI **Responses**（`wire_api = "responses"`）。模型能否真正调用，取决于中转是否用 OpenAI 兼容协议暴露这些 slug。原生 Anthropic `/v1/messages` 不能靠本脚本切换。

## 用法

需要已安装 **Python 3**。

### Windows

双击 `一键添加其他模型（windows）.bat`

### macOS

```bash
chmod +x "一键添加其他模型（mac）.command"
```

然后双击该文件。若提示无法打开：系统设置 → 隐私与安全性 → 仍要打开。

跑完后 **完全退出再打开 Codex 桌面端**。

## 内置模型与推理档

| slug | 推理档 |
|---|---|
| `gpt-5.6-luna` / `gpt-5.6-terra` / `gpt-5.6-sol` / `gpt-6-astra` | low / medium / high / xhigh / max |
| `grok-4.5` / `grok-4.6` | 同上 |
| `deepseek-v4-pro` / `glm-5.3` / `kimi-k3` / `qwen3.8-max` | low / medium / high / xhigh |
| `deepseek-v4-flash` / `deepseek-v4.1-flash` / `glm-5.3-flash` / `minimax-m3` | none / low / medium / high |

slug 必须和中转后台的 model id **完全一致**，否则下拉能选但请求会失败。

## 原理

Codex 桌面端下拉读取 `model_catalog_json` 指向的 JSON（精简 schema，不能照搬官方 `models_cache.json`）。本脚本按 CC Switch 使用的 native Responses 模板生成条目。

## 许可

MIT
