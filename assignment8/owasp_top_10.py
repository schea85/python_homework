from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import csv
import json

# TASK 6:
# enable headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://owasp.org/www-project-top-ten/")
    find_link = driver.find_element(By.LINK_TEXT, "OWASP Top Ten 2025")
    find_link.click()
    
    top_ten_h3 = driver.find_element(By.CSS_SELECTOR, "h3[id='top-102025-list']")
    links = []
    if (top_ten_h3):
        siblings = top_ten_h3.find_element(By.XPATH, "./following::ol")
        if siblings:
            look_for_li = siblings.find_elements(By.XPATH, "./li")
            for li in look_for_li:
                link = li.find_element(By.TAG_NAME, "a")
                title = link.text.strip()
                url = link.get_attribute("href")
                if title and url:
                    links.append({"title": title, "url": url})
            print(links)

except Exception as e:
    print(f"Unable to get data. {e}")
finally:
    driver.quit()
    
# create csv
owasp_df = pd.DataFrame(links)
owasp_csv = owasp_df.to_csv("owasp_top_10.csv", index=False)
