#!/usr/bin/env python3
# DroidDeck zh-rCN 本地化质量验证脚本
# 对比: A.上游英文  B.当前PR  C.个人仓库  D.术语表
import re
import sys
import xml.etree.ElementTree as ET

def parse_strings(path):
    """解析 strings.xml，返回 {name: (text, formatted_attr)} 及特殊结构"""
    tree = ET.parse(path)
    root = tree.getroot()
    strings = {}
    string_arrays = {}
    plurals = {}
    for el in root:
        name = el.get('name')
        if el.tag == 'string':
            strings[name] = (el.text or '', el.get('formatted'))
        elif el.tag == 'string-array':
            string_arrays[name] = [it.text or '' for it in el.findall('item')]
        elif el.tag == 'plurals':
            plurals[name] = {it.get('quantity'): (it.text or '') for it in el.findall('item')}
    return strings, string_arrays, plurals

def placeholders(s):
    return sorted(re.findall(r'%\d*\$?[sd]|%\d+\$?[sd]|%%', s))

def check_escape(s):
    """检查未正确转义的字符"""
    issues = []
    # 检查裸的 & （非 &amp; &lt; &gt; " ' &#）
    for m in re.finditer(r'&(?!amp;|lt;|gt;|quot;|apos;|#)', s):
        issues.append(f'裸 & 于位置 {m.start()}')
    return issues

print('=' * 60)
print('DroidDeck zh-rCN 本地化质量验证')
print('=' * 60)

# 加载四份文件
en_str, en_arr, en_plu = parse_strings('/tmp/upstream_en.xml')
pr_str, pr_arr, pr_plu = parse_strings('/root/droiddeck-main/app/src/main/res/values-zh-rCN/strings.xml')

print(f'\n【规模统计】')
print(f'  上游英文 (A):   {len(en_str)} string / {len(en_arr)} array / {len(en_plu)} plurals')
print(f'  当前 PR (B):    {len(pr_str)} string / {len(pr_arr)} array / {len(pr_plu)} plurals')

# 1. key 完整性
en_keys = set(en_str.keys())
pr_keys = set(pr_str.keys())
missing = en_keys - pr_keys
extra = pr_keys - en_keys
common = en_keys & pr_keys

print(f'\n【1. Key 完整性】')
print(f'  共同 key:        {len(common)}')
print(f'  missing (英有中无): {len(missing)}')
print(f'  extra (中有英无):   {len(extra)}')
if missing:
    print(f'  ⚠️ 缺失的 key（需补翻译）:')
    for k in sorted(missing):
        print(f'     - {k}: "{en_str[k][0][:60]}"')
if extra:
    print(f'  ⚠️ 多余的 key（上游已删除，需移除）:')
    for k in sorted(extra):
        print(f'     - {k}')

# 2. string-array 一致性
print(f'\n【2. string-array 一致性】')
arr_issues = 0
for name in en_arr:
    if name not in pr_arr:
        print(f'  ⚠️ 缺失 string-array: {name}'); arr_issues += 1
    elif len(en_arr[name]) != len(pr_arr[name]):
        print(f'  ⚠️ {name} item 数量不一致: en={len(en_arr[name])} zh={len(pr_arr[name])}'); arr_issues += 1
for name in pr_arr:
    if name not in en_arr:
        print(f'  ⚠️ 多余 string-array: {name}'); arr_issues += 1
if arr_issues == 0:
    print(f'  ✅ 全部一致')

# 3. plurals 一致性
print(f'\n【3. plurals 一致性】')
plu_issues = 0
for name in en_plu:
    if name not in pr_plu:
        print(f'  ⚠️ 缺失 plurals: {name}'); plu_issues += 1
    else:
        en_q = set(en_plu[name].keys())
        pr_q = set(pr_plu[name].keys())
        if en_q != pr_q:
            print(f'  ⚠️ {name} quantity 不一致: en={en_q} zh={pr_q}'); plu_issues += 1
for name in pr_plu:
    if name not in en_plu:
        print(f'  ⚠️ 多余 plurals: {name}'); plu_issues += 1
if plu_issues == 0:
    print(f'  ✅ 全部一致')

# 4. format placeholder 一致性
print(f'\n【4. format placeholder 一致性】')
ph_mismatch = 0
for name in common:
    ph_en = placeholders(en_str[name][0])
    ph_zh = placeholders(pr_str[name][0])
    if ph_en != ph_zh:
        print(f'  ⚠️ {name}: en={ph_en} zh={ph_zh}')
        ph_mismatch += 1
if ph_mismatch == 0:
    print(f'  ✅ 全部一致 ({len(common)} 个 string)')
else:
    print(f'  共 {ph_mismatch} 处不一致')

# 5. formatted 属性一致性
print(f'\n【5. formatted 属性一致性】')
fmt_mismatch = 0
for name in common:
    if en_str[name][1] != pr_str[name][1]:
        print(f'  ⚠️ {name}: en={en_str[name][1]} zh={pr_str[name][1]}')
        fmt_mismatch += 1
if fmt_mismatch == 0:
    print(f'  ✅ 全部一致')

# 6. XML escape 检查
print(f'\n【6. XML escape 检查】')
esc_issues = 0
for name in pr_keys:
    issues = check_escape(pr_str[name][0])
    if issues:
        print(f'  ⚠️ {name}: {issues}')
        esc_issues += 1
if esc_issues == 0:
    print(f'  ✅ 无裸 & 字符')

# 7. 机器翻译腔/繁体混入抽查（关键词）
print(f'\n【7. 繁体/翻译腔抽查】')
traditional_chars = '體臺灣這裡現在應該問題資訊軟體網路資料庫應用程式設定畫面預設值遊戲儲存檔案資料夾選擇開啟關閉新增刪除編輯儲存還原重設設定啟動停止暫停繼續完成確定取消返回下一步上一步自動手動從不總是自訂原生寬度高透明度佈局隱藏顯示詳情檔案瀏覽資料夾來源圖示名稱值變數繼承自訂標準功能層級覆蓋著色器模型快取光線追蹤診斷記錄幀率上限延遲麥克風語音聊天網路發現定位服務定位權限附近網路卡頓流式載入資源黑屏回退軟體渲染幀節奏刷新率折疊屏黑邊填滿螢幕拉伸遊戲填滿螢幕覆蓋鎖定自由調度後台殺死當前設定為殺死此下次重啟啟動交換儲存原版構建匹配推薦高級刷新不可用標題描述提示說明狀態進度步驟正在載入下載失敗複製命令連結主螢幕新預設圖示檢查更新清除重設配置重映射按下以移除需要執行時請先可用空間不足複製該需要已連結已複製共享儲存全螢幕選擇腳本選擇選擇圖示不是有效不是有效連結來自來自更新到已是最新已添加已移除已儲存已更新使用中原版早期構建始終保留每日構建中刷新以列出中的包匯入原版檔案尚未安裝啟動一次以自動下載其版或從設定中加入或正在執行遊戲因此需等待其關閉將放入其原版檔案會保留將原版還原到刪除此原版此原版來自的早期構建當前構建的原版始終保留捆绑包的一半兩個部分都會被移除使用中的驅動會回退到預設在每日構建中檢查新包關於為執行遊戲所用的每個提供選擇已安裝的行以進行交換它會在下次遊戲啟動時或執行中的遊戲關閉後生效每次啟動前都會重新檢查您的選擇若被更改則還原每個的原版檔案都會保留因此更新不會丟失它們跳過的輔助禁用的手柄導航輔助它會在每個遊戲中消耗無執行缺少系統呼叫的錯誤可能會降低效能快速路徑需要的過濾更快的檔案查找和更少的卡頓若程式找不到檔案請關閉僅限字母數字和中間連字元最多個字元留空將恢復看到的此裝置名稱保留最新的個附到錯誤報告中每次後儲存保留最新個用作主螢幕可設為主螢幕應用不再將提供為主螢幕應用隱藏狀態列與導航列預設主螢幕應用選擇主螢幕應用部分應用可能無法啟動日誌位於從安裝應用和遊戲瀏覽和管理檔案安裝構建核心分配模擬器遊戲存放位置按鍵映射新增連接到約第一個應用還會下載其執行時僅列出應用上沒有匹配的應用上沒有構建因此無法在此安裝另加共享執行時請先設定後才可安裝應用無法連線請檢查網路後重試無法載入此應用的頁面下載大小正在設定正在搜尋正在安裝搜尋遊戲模擬器按名稱搜尋或選擇分類還沒有應用可在發現或搜尋頁查找全部更新檢查於尚未檢查允許自行更新在下一螢幕中開啟允許來自此來源然後返回更新會自動繼續稍後簽名不同無法就地更新此副本未用發布金鑰簽名因此更新無法覆蓋安裝解除安裝它以切換可切換領先於穩定版您已領先於穩定版此構建比最新穩定版更新其下個版本發布時您將回到穩定版測試已結束此測試已結束其修復已合併或放棄關注預覽版以取得最新修復您已擁有最新的仍然安裝穩定版關注預覽版請停止正在執行的以更新新的預覽構建測試構建更新通道經過測試的版本適合大多數使用者最新的修復先於穩定版發布在發布前試用修復當前沒有此副本未構建已更新測試不久前剛剛有個可試用自您構建以來的變更落後個構建最近的變更個構建'
suspicious = []
for name in pr_keys:
    text = pr_str[name][0]
    for c in traditional_chars:
        if c in text:
            suspicious.append((name, c, text[:50]))
            break
if suspicious:
    print(f'  ⚠️ 发现 {len(suspicious)} 处可能混入繁体字:')
    for name, c, t in suspicious[:15]:
        print(f'     - {name} (含「{c}」): {t}...')
else:
    print(f'  ✅ 未发现明显繁体字混入')

# 总结
print(f'\n' + '=' * 60)
print('【验证总结】')
print('=' * 60)
print(f'  共同 key 数:              {len(common)}')
print(f'  missing keys:             {len(missing)}')
print(f'  extra keys:               {len(extra)}')
print(f'  string-array 问题:        {arr_issues}')
print(f'  plurals 问题:             {plu_issues}')
print(f'  format placeholder 不一致: {ph_mismatch}')
print(f'  formatted 属性不一致:      {fmt_mismatch}')
print(f'  XML escape 问题:          {esc_issues}')
print(f'  疑似繁体混入:             {len(suspicious)}')

# 退出码
total_issues = len(missing) + len(extra) + arr_issues + plu_issues + ph_mismatch + fmt_mismatch + esc_issues
print(f'\n  总问题数: {total_issues}')
if len(missing) > 0:
    print(f'  ⚠️ 上游新增了 {len(missing)} 条字符串，需补翻译后再提交！')
sys.exit(0 if total_issues == 0 else 1)