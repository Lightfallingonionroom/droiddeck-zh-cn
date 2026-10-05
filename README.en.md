# droiddeck-zh-cn

[中文](README.md) | **English**

> **📌 This repository has served its purpose.**
> DroidDeck now ships with full Chinese (Simplified, Taiwan Traditional, Hong Kong Traditional) and CJK fonts built in.
> For a Chinese build, download the **[official Releases](https://github.com/Droid-Deck/DroidDeck/releases)** — you no longer need the patched APK here.

---

## What this repository is now

An **archive and reference for DroidDeck's Chinese localization**.

The story: in October 2026 DroidDeck shipped in English and Spanish only, and Chinese text rendered as □□□ (no CJK font). I built this localization and submitted the 62 strings upstream was missing via [PR #232](https://github.com/Droid-Deck/DroidDeck/pull/232), which was merged. The team then landed a more complete multilingual scheme, so Chinese became an official, first-class language.

What is **still useful** here:

| Content | Use |
|---|---|
| `steam-l10n-terms.md` | A **1200+ entry glossary** for Steam / Proton / DXVK / Gamescope and friends — handy for translating anything in the Steam ecosystem |
| `screenshots/` | Reference images of the Chinese UI |
| `strings-zhCN.xml` | The full Simplified Chinese resource file (historical, for reference) |

## About the old patched APK

`DroidDeck-0.3.0-zhCN-font.apk` (see Releases) is the **old 0.3.0-based patch** and should be treated as **archive material only**:

- Based on 0.3.0 — **missing later upstream features**
- Uses a debug signature; the official app must be uninstalled first
- The official build now includes Chinese and fonts, so **there is no reason to use it**

## Upstream localization status

| Item | Status |
|---|---|
| [PR #232](https://github.com/Droid-Deck/DroidDeck/pull/232) (62 strings) | ✅ Merged into `main` |
| Official multilingual scheme (zh-rCN / zh-rTW / zh-rHK + language setting) | In progress upstream |
| CJK fonts (shared from Android's system Noto, nothing downloaded) | In progress upstream |

## Credits

- Upstream: [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) (GPL-3.0)
- Fonts: [Noto Sans CJK](https://github.com/notofonts/noto-cjk) (SIL Open Font License)
- Terminology: [steam-l10n](steam-l10n-terms.md)