from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://iscc-system.org/certification/valid-certificates/")

# ==========================
# Accept All 쿠키 클릭
# ==========================

try:
    accept_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Accept') or contains(., 'Accept All')]")
        )
    )

    driver.execute_script("arguments[0].click();", accept_btn)

    print("쿠키 허용 완료!")

except:
    print("쿠키 팝업 없음")

# ==========================
# CSV 다운로드
# ==========================

link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href,'export.php')]")
    )
)

driver.execute_script("arguments[0].click();", link)

print("CSV 버튼 클릭 성공!")

time.sleep(10)

driver.quit()