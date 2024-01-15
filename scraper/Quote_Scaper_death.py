from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the Chrome driver (make sure to download the appropriate version of ChromeDriver)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Define the number of pages to scrape
total_pages = 100

quote_data = []

# Iterate over pages
for page_number in range(1, total_pages + 1):
    # Navigate to the Goodreads quotes page
    url = f"https://www.goodreads.com/quotes/tag/death?page={page_number}"
    driver.get(url)

    
    # Extract quotes and tags
    quotes_elements = driver.find_elements(By.CLASS_NAME, "quoteText")
    tags_elements = driver.find_elements(By.CLASS_NAME, "greyText.smallText.left")

    # Iterate through each quote on the page
    for quote, tag in zip(quotes_elements, tags_elements):
        author, quote_text = quote.text.split("\n―")
        quote_data.append({
            'Quote': author.strip(),
            'Author': quote_text.strip('“”'),
            'Tags': tag.text.replace("tags:", "").strip()
        })

# Create a pandas DataFrame
df = pd.DataFrame(quote_data)

# Save the DataFrame to a CSV file
df.to_csv("Quote_data_death.csv", index=False)

# Close the browser window
driver.quit()

