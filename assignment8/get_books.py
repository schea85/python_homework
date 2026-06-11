from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import csv
import json

# TASK 1:
# reviewed robots.txt 

# TASK 2:
# collect information:

# first item <li>:
## search_result_item = <class = "row cp-search-result-item" >

# title <span>:
## result_book_title = class = "title-content"

# author(s): <span class ="cp-author-link">
## <a target="_parent" class="author-link">

# book format/year:
## <span class="display-info-primary">

# TASK 3:
# enable headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

results = []

# web scrape
try:
    
    # build url
    base_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart&page="
    
    for i in range(1, 16):
        get_page_url = base_url + str(i)
    
        driver.get(get_page_url)
        
        book_search_results = driver.find_elements(By.CSS_SELECTOR, "li[class='row cp-search-result-item']")
            
        # create loop to find book info
        for result in book_search_results:
            # get title
            book_title = result.find_element(By.CSS_SELECTOR, "span[class='title-content']").text
                
            # get author(s)
            book_authors = result.find_elements(By.CLASS_NAME, "author-link")
            authors_list = [author.text for author in book_authors]
            book_authors = "; ".join(authors_list)
                
            # get format and year
            book_format_year = result.find_element(By.CLASS_NAME, "display-info-primary").text
                
            results.append({
                "Title": book_title,
                "Author(s)": book_authors,
                "Format-Year": book_format_year
            })        
            
        sleep(5)
            
except Exception as e:
    print(f"Couldn't get data. {e}")
finally:
    # no more pages
    driver.quit()
    
# create DF and print
books_df = pd.DataFrame(results)
print(books_df)

# TASK 4:
# create csv
df_to_csv = books_df.to_csv("assignment8/get_books.csv", index=False)

# # create json
with open("assignment8/get_books.json", "w") as file:
    json.dump(results, file, indent=4)
    

