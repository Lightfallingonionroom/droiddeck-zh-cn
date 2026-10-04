---
name: steam-l10n
description: >
  Steam 与 DroidDeck 界面本地化术语表。用于将 DroidDeck / Steam / Proton /
  Gamescope 界面的英文文案翻译为简体中文，或校对任何涉及 Steam 生态专有名词
  （Proton、DXVK、VKD3D、FEX、Gamescope、Turnip、LSFG、MangoHud、Decky、
  Steam Input、Big Picture、Wine、Proot、Flatpak、AppImage、Flathub 等）的翻译。
  翻译 DroidDeck 汉化包（values-zh-rCN/strings.xml）时必须先阅读本技能。
keywords:
  - steam
  - droiddeck
  - 汉化
  - 本地化
  - l10n
  - 翻译
  - proton
  - dxvk
  - vkd3d
  - fex
  - gamescope
  - turnip
  - lsfg
  - mangohud
  - decky
  - steam input
  - big picture
  - wine
  - proot
  - flatpak
  - appimage
  - flathub
  - strings.xml
  - values-zh
packageType: instruction-skill
instructionOnly: true
metadata:
  version: 1.0.0
  openclaw:
    requiresNetwork: false
    dataClassification: none
---

# Steam / DroidDeck 本地化术语表（简体中文）

本技能为 DroidDeck（及 Steam 生态）界面汉化提供**唯一术语真源**。翻译 `values-zh-rCN/strings.xml` 时必须遵循本文档，禁止凭个人感觉选词、禁止一词多译、禁止中英混杂（专有名词除外）。

## 文件结构

- `SKILL.md` — 本文件：硬规则 + 术语表索引
- `terms-core.md` — 核心术语表（通用界面 + Steam 专有名词）
- `terms-session.md` — 会话/性能/组件术语表
- `terms-store.md` — 商店/应用/更新术语表
- `terms-setup.md` — 设置/调试/控制术语表
- `terms-game.md` — 游戏/存档/桌面应用术语表

翻译时先读 `SKILL.md`（硬规则），再按需查阅对应术语文件。

## 一、硬规则（必须先读）

1. **专有名词一律保留原文，不得音译或意译**：Proton、DXVK、VKD3D、FEX、Gamescope、Turnip、LSFG、MangoHud、Decky、Steam Input、Big Picture、Flatpak、Flathub、AppImage、Wine、Winlator、GameHub、Bannerlator、RetroArch、LXQt、Mesa、PulseAudio、Adreno、DroidDeck、Steam、Valve。
2. **固定译名必须全文一致**：例如 `session` 一律译「会话」，不得出现「进程/时段/一次运行」等变体。
3. **占位符必须保留**：`%1$s`、`%2$d`、`%1$d×`、`%1$.1f` 等，位置按中文语序调整但不可丢失；带 `formatted="false"` 的字符串保持属性。
4. **复数（plurals）项**：中文无复数形态，`quantity="one"` 与 `quantity="other"` 都输出同一译文，保留 `<item>` 结构。
5. **XML 转义**：`&amp;`（&）、`\'`（'）、`…`（…）等在中文中按语义输出；`&amp;` 在中文里多数情况直接写「和/与」。
6. **界面按钮与标题词性**：按钮译动词短语（「添加」「安装」「继续」），设置项标题译名词短语（「游戏环境」「会话行为」）。
7. **帮助文本、提示、说明（hint/note/detail/description 结尾的 key）**：译成完整通顺的中文短句，保持克制、不过度口语化，保留原文技术含义；字数以短于或等于原文为宜。
8. **游戏专用名词按 Steam 国区官方译法**：如 "picture in picture" 译「画中画」、「Quick Access」译「快捷访问」，「online/offline mode」译「在线/离线模式」。
9. **同一英文词在上下文不同时以 DroidDeck 语境为准**：例如 `library` 在「游戏库」义项固定译「库」，`store` 译「商店」，`runtime` 译「运行时」。
10. **禁止把 key 名（如 `lsfg_needs_steam`）当作文案翻译**，只翻译 `<string>` 标签内的英文内容。
11. **术语查表顺序**：先查 `terms-core.md`，未命中查 `terms-session.md`，再 `terms-store.md` → `terms-setup.md` → `terms-game.md`。全部未命中时，按硬规则自行翻译，并在译文旁加 `<!-- TBD -->` 注释供复核。
12. **翻译输出格式**：直接输出 `values-zh-rCN/strings.xml` 完整文件，保持与英文 `strings.xml` 相同的 key 顺序与 XML 结构。