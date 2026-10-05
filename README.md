# droiddeck-zh-cn

**中文** | [English](README.en.md)

> **📌 本仓库已完成历史使命。**
> DroidDeck 官方已内置完整中文（含简体、台湾繁体、香港繁体）和中文字体。
> 想用中文版，请直接下载 **[官方 Releases](https://github.com/Droid-Deck/DroidDeck/releases)**，无需再使用本仓库的汉化包。

---

## 这个仓库现在是什么

一个 **DroidDeck 中文本地化的存档与参考资料库**。

故事是这样的：2026 年 10 月，DroidDeck 只有英文和西班牙语，中文界面显示为 □□□（缺字体）。我做了这套汉化，并把 62 条上游缺失的翻译通过 [PR #232](https://github.com/Droid-Deck/DroidDeck/pull/232) 提交给了官方，已被合并。随后官方团队推出了更完整的多语言方案，中文正式进入官方版本。

所以本仓库现在保留两样**仍然有用**的东西：

| 内容 | 用途 |
|---|---|
| `steam-l10n-terms.md` | Steam / Proton / DXVK / Gamescope 等 **1200+ 条术语表**，翻译 Steam 生态任何东西都能用 |
| `screenshots/` | 中文界面的效果参考图 |
| `strings-zhCN.xml` | 完整的简体中文资源文件（历史版本，供参考） |

## 关于旧汉化包

`DroidDeck-0.3.0-zhCN-font.apk`（见 Releases）是**基于 0.3.0 的旧汉化包**，请**仅作存档参考**：

- 基于 0.3.0，**不含官方后续版本的新功能**
- 使用 debug 签名，安装前必须先卸载官方版
- 官方新版已内置中文与字体，**没有任何理由再用它**

## 官方中文化进展

| 项目 | 状态 |
|---|---|
| [PR #232](https://github.com/Droid-Deck/DroidDeck/pull/232)（62 条翻译） | ✅ 已合并进 `main` |
| 官方多语言方案（zh-rCN / zh-rTW / zh-rHK + 语言设置） | 上游开发中 |
| 中文字体（共享 Android 系统 Noto，无需下载） | 上游开发中 |

## 致谢

- 原版：[Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck)（GPL-3.0）
- 字体：[Noto Sans CJK](https://github.com/notofonts/noto-cjk)（SIL Open Font License）
- 术语参考：[steam-l10n](steam-l10n-terms.md)