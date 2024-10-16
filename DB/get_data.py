from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 

company_list = ['2330 - 台積電', '3711 - 日月光投控', '2454 - 聯發科', '2303 - 聯電', '2379 - 瑞昱']
download_dir = 'C:\\Users\\Anna_Chen\\Desktop\\NCU\\Lab\\ESG\\DB\\org_csv'

# 設置 Chrome 選項
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
chrome_options.add_experimental_option("prefs", prefs)  # 正確設置偏好選項

# 添加無頭模式參數
chrome_options.add_argument("--headless")  # 在這裡添加無頭模式
chrome_options.add_argument("--disable-gpu")  # 在某些情況下可以禁用 GPU
chrome_options.add_argument("--no-sandbox")  # 禁用沙盒模式
chrome_options.add_argument("--disable-dev-shm-usage")  # 避免資源限制

# 初始化 Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)  # 在這裡傳遞 chrome_options

# 進入目標網址
driver.get('https://esggenplus.twse.com.tw/inquiry/info/individual')

for company in company_list:
    try:
        input_field_company = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='公司代號/股票代號*']"))
        )
        input_field_company.click()  # 點擊輸入框以顯示下拉選單

        # 使用 CSS 選擇器選擇所有 option-item 元素
        company_options = driver.find_elements(By.CSS_SELECTOR, "div.option-item")

        # 遍歷選項以找到所需的
        for option in company_options:
            if option.text == company:
                option.click()  # 點擊該選項
                print("已成功選擇" + company)
                break  # 找到後退出循環

        # Input year
        input_field_year = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='報告年度*']"))
        )
        input_field_year.clear()
        input_field_year.click()
        year_options = driver.find_elements(By.CSS_SELECTOR, "div.option-item")
        
        for option in year_options:
            if option.text == "2023":
                option.click()  # 點擊該選項
                print("已成功選擇 2023")
                break  # 找到後退出循環

        # 點擊搜索按鈕
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.default:not(.disabled)"))
        )
        search_button.click()

        time.sleep(2)  # 等待結果加載
        
        # 使用 XPath 點擊下載按鈕
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='另存CSV']"))
        )
        download_button.click()  # 點擊按鈕
        
        # 等待文件下載完成
        time.sleep(3)  # 這裡的時間可能需要根據下載速度進行調整

        # 確保文件已經下載
        downloaded_file = os.path.join(download_dir, "個別公司查詢.csv")
        if os.path.exists(downloaded_file):
            new_filename = os.path.join(download_dir, company + ".csv")
            os.rename(downloaded_file, new_filename)
            print(f"已將文件重命名為: {new_filename}")
        else:
            print(f"下載的文件未找到: {downloaded_file}")

    except Exception as e:
        print(f"未找到 {company}: {e}")

# 關閉瀏覽器
driver.quit()
