from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- CONFIG ---
LINKEDIN_POST_URL = "https://www.linkedin.com/feed/update/urn:li:activity:7351403666169315329/"

# --- SETUP ---
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# --- LOGIN ---
driver.get("https://www.linkedin.com/login")
input("Log in manually, then press Enter here to continue...\n")
print("✅ Login complete")

# --- GO TO POST ---
driver.get(LINKEDIN_POST_URL)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "article")))
print("✅ Post loaded")
time.sleep(2)

# --- OPEN DROPDOWN ---
try:
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "comments-sort-order-toggle__trigger"))
    )
    dropdown_button.click()
    print("✅ Dropdown opened")

    input("👋 Manually select 'Most recent' from dropdown, then press Enter to continue...\n")

except Exception as e:
    print("❌ Could not open dropdown")
    print("Error:", e)
