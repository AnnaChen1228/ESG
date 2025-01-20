
# ESG 報告生成系統 :robot:

## 🎉 進入2024中技社AI創意競賽決賽
## 🖍 介紹

本專案是一個基於 **AI** 技術的 **ESG 報告生成系統**，旨在幫助企業簡化 ESG (環境、社會、治理) 報告的生成過程。系統提供數據爬取、數據存儲、報告生成等功能，能夠自動化整合 ESG 資料並根據最新的規範生成高質量報告。

## 🎯 功能概覽

### 💾 資料庫管理與數據整合
提供一套完整的資料庫管理功能，包括資料庫建立、數據比對、爬取目標公司 ESG 數據並進行資料表建構與數據存儲。

### 📡 數據爬取與處理
自動化爬取目標公司的 ESG 數據並將其處理後存儲到資料庫，支持 CSV 格式的數據文件。

### 📈 自動化報告生成
透過 Web 應用提供報告生成與檢查功能，使用戶能夠快速生成符合規範的 ESG 報告，並提供報告編寫指導。

## 🖥️ 系統架構

### 1. 資料庫管理與數據整合
- 創建與管理 ESG 數據資料庫。
- 進行數據比對與資料插入操作。
- 依據爬取的數據生成相應的資料表。
  
### 2. 數據爬取與處理
- 設計爬蟲自動化爬取 ESG 相關數據。
- 支持多公司、多議題、多指標的爬取。
- 存儲爬取結果為 CSV 格式，便於後續處理。

### 3. 報告生成與檢查
- Web 應用自動生成符合 ESG 標準的報告。
- 提供報告內容的檢查與修正功能。
- 使用報告編寫規則幫助用戶撰寫高質量的 ESG 報告。

## 🚀 如何使用

### 1. 安裝所需的依賴：
```bash
pip install -r requirements.txt
```

### 2. 執行爬取數據的腳本：
```bash
python get_data.py
```

### 3. 創建資料庫並將爬取的數據插入：
```bash
python insert_data.py
```

### 4. 生成並檢查 ESG 報告：
- 使用 Web 應用生成報告
- 訪問報告檢查頁面，核對內容

### 5. 執行網頁
```
python app.py
```
## 📁 檔案結構

```
/ESG_Report_Generation_System
├── /data
│   ├── company_data.csv         # 存儲爬取的公司資料
│   └── esg_report_template.csv  # 報告範本數據
├── /scripts
│   ├── get_data.py              # 數據爬取腳本
│   ├── insert_data.py           # 數據插入資料庫
│   ├── build_DB.py              # 創建資料庫
│   ├── check_data.py            # 比較數據異同
│   └── build_table.py           # 創建資料表
├── /web
│   ├── index.html               # 系統主頁
│   ├── check_reporter.html      # 報告檢查頁面
│   ├── generator_reporter.html  # 報告生成頁面
│   └── write_rule.html          # 報告編寫規則頁面
├── requirements.txt             # 依賴的 Python 包
└── README.md                    # 專案介紹文件
```