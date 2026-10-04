# DroidDeck 简体中文汉化版

> 基于 [DroidDeck](https://github.com/Droid-Deck/DroidDeck) 0.3.0 的完整中文本地化版本，内置中文字体，开箱即用。

## 与原版对比

| 特性 | 原版 | 本汉化版 |
|------|------|----------|
| 界面语言 | 仅英文/西语 | ✅ 完整简体中文（928 条字符串） |
| 中文字体 | 无（显示 □□□） | ✅ 内置 Noto Sans CJK（16MB） |
| 字体部署 | 需手动安装 | ✅ 会话启动时自动部署 |
| 术语一致性 | 无统一标准 | ✅ 基于 steam-l10n 术语表（1200+ 条） |
| 中文语言匹配 | 无 | ✅ zh-rCN / zh-rTW / zh 全覆盖 |

## 安装

1. 下载 `DroidDeck-0.3.0-zhCN-font.apk`
2. **卸载原版 DroidDeck**（签名不同，必须先卸载）
3. 安装汉化版 APK
4. 首次启动后：设置 → 开发者选项 → 关闭「限制子进程」（或用应用内的「帮我修复」）

## 汉化范围

- **928 条界面字符串**：主界面、设置、组件、商店、更新、会话、控制、游戏管理等全部界面
- **术语统一**：遵循 steam-l10n 术语表（Steam/Proton/DXVK/Gamescope/Turnip/LSFG 等专有名词统一译名）
- **中文语言支持**：values-zh-rCN / values-zh-rTW / values-zh（覆盖简中、繁中及所有中文设备）

## 技术细节

- **资源合并**：1011 条字符串（928 条界面 + 83 条 Material Components 库翻译）
- **字体注入**：smali 代码在 `SessionActivity.surfaceCreated()` 中自动部署字体到 `linuxfs/usr/share/fonts/`
- **Android 16 适配**：修复 `File(File, String)` 构造函数在 API 36 的兼容性问题（API 36 已移除该构造函数）
- **签名**：debug.keystore（与原版签名不同，需卸载原版后安装）

## 文件说明

- `DroidDeck-0.3.0-zhCN-font.apk` — 汉化版 APK（45.4MB，含中文字体）
- `strings-zhCN.xml` — 完整中文资源文件（928 条，可直接用于从源码构建）
- `steam-l10n-terms.md` — Steam/DroidDeck 术语表（1200+ 条，翻译用）

## 从源码构建

将 `strings-zhCN.xml` 复制到源码的 `app/src/main/res/values-zh-rCN/strings.xml`，然后按官方流程构建即可。

## 声明

- 本项目为 DroidDeck 的社区本地化衍生版，遵循 **GPL-3.0** 许可证
- 原版版权归 [Droid-Deck](https://github.com/Droid-Deck/DroidDeck) 团队所有
- 汉化部分（翻译字符串、术语表、字体注入补丁）由社区贡献

## 致谢

- 原版：[Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck)
- 翻译术语：[steam-l10n](steam-l10n-terms.md) 自建术语表
- 字体：[Noto Sans CJK SC](https://github.com/notofonts/noto-cjk) (SIL Open Font License)

---

# DroidDeck Simplified Chinese Localization

> A complete Chinese localization of [DroidDeck](https://github.com/Droid-Deck/DroidDeck) 0.3.0, with built-in CJK fonts.

## Differences from Upstream

| Feature | Upstream | This Build |
|---------|----------|------------|
| UI Language | English/Spanish only | ✅ Full Simplified Chinese (928 strings) |
| CJK Fonts | None (shows □□□) | ✅ Bundled Noto Sans CJK (16MB) |
| Font Deploy | Manual install | ✅ Auto-deployed on session start |
| Terminology | No standard | ✅ steam-l10n glossary (1200+ entries) |
| Chinese Locale | None | ✅ zh-rCN / zh-rTW / zh coverage |

## Install

1. Download `DroidDeck-0.3.0-zhCN-font.apk`
2. **Uninstall upstream DroidDeck first** (different signature)
3. Install this APK
4. After first launch: Developer options → Disable "Restrict child processes"

## Technical Notes

- **Resource merge**: 1011 strings (928 UI + 83 Material Components library)
- **Font injection**: smali patch in `SessionActivity.surfaceCreated()` auto-deploys fonts to `linuxfs/usr/share/fonts/`
- **Android 16 fix**: `File(File, String)` constructor removed in API 36 — patched to use `File(String, String)`

## License

GPL-3.0. Original work © [Droid-Deck](https://github.com/Droid-Deck/DroidDeck).