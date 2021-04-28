"""
Importing necessary modules.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import mysql.connector
import pandas as pd
import time
import re

"""
Defining required data structure.
"""
underlying_urls = []
products = []
product_names = []
brands = []
registrants = []
addresses = []
producers = []


"""
Utility functions
"""
def replaceTextBetween(originalText, delimeterA, delimterB, replacementText):
    leadingText = originalText.split(delimeterA)[0]
    trailingText = originalText.split(delimterB)[1]

    return leadingText + delimeterA + replacementText + delimterB + trailingText

"""
Setting some optional arguments for driver object.
"""
options = webdriver.ChromeOptions()
options.add_argument("incognito")
options.add_argument("--disable-notifications")
options.add_argument("--headless")
options.add_argument("--start-maximized")

"""
Initializing the driver object.
"""
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
time.sleep(1)

"""
Hitting the base url.
"""
base_url = "https://cekbpom.pom.go.id/"
driver.get(base_url)
time.sleep(3)

REGISTRANT_NAME_KEYWORD = "mandiri"


"""
Selecting the desired option.
"""
Select(driver.find_element_by_id("tb_keycari")).select_by_value("6")

input_keyword = driver.find_element_by_id("tb_search")
input_keyword.clear()
input_keyword.send_keys(REGISTRANT_NAME_KEYWORD)

search = driver.find_element_by_name("cari")
driver.execute_script("arguments[0].click();", search)
time.sleep(5)


"""
Calculating the total no of records.
"""
soup = BeautifulSoup(driver.page_source, "html.parser")
total_records = re.search("Dari ([0-9]+) Data", soup.find("tr", {"class": "title mbottom"}).get_text().strip()).group(1)

"""
Making target url to get all the products in one page by combining current url and the total no of records.
"""
main_url = driver.current_url
url_to_target = replaceTextBetween(main_url, "row/", "/page", total_records)
driver.get(url_to_target)
time.sleep(6)


"""
Fetching all the underlying urls.
"""
soup = BeautifulSoup(driver.page_source, "html.parser")
unique_key = re.search("/produk/(.*)/all", main_url).group(1)

links = soup.find_all("tr", {"title": "Klik untuk menampilkan detil data"})
for link in links:
    urldetil = link.get("urldetil")
    underlying_urls.append(f"https://cekbpom.pom.go.id/index.php/home/detil/{unique_key}/produk{urldetil}")
    
print(f"Urls Found: {len(underlying_urls)}")


"""
Fetching data from the underlying urls.
"""
index = 0
for url in underlying_urls[:1000]:
    
    index += 1
    print(f"Url: {index}")
    
    driver.get(url)
    time.sleep(1.5)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    try:
        product = soup.find("table", {"class": "normal"}).find_all("tbody")[1].find(lambda tag:tag.name=="td" and "Produk" in tag.text).find_next().get_text().strip()
        # print(product)
        products.append(product)
    except:
        products.append("")
    
    try:
        product_name = soup.find("table", {"class": "normal"}).find_all("tbody")[2].find(lambda tag:tag.name=="td" and "Nama Produk" in tag.text).find_next().get_text().strip()
        # print(product_name)
        product_names.append(product_name)
    except:
        product_names.append("")
    
    try:
        brand = soup.find("table", {"class": "normal"}).find_all("tbody")[2].find(lambda tag:tag.name=="td" and "Merk" in tag.text).find_next().get_text().strip()
        # print(brand)
        brands.append(brand)
    except:
        brands.append(brand)
    
    try:
        registrant = soup.find("table", {"class": "normal"}).find_all("tbody")[2].find(lambda tag:tag.name=="td" and "Pendaftar" in tag.text).find_next().get_text().strip().split(",")[0]
        # print(registrant)
        registrants.append(registrant)
    except:
        registrants.append("")
    
    try:
        address = soup.find("table", {"class": "normal"}).find_all("tbody")[2].find(lambda tag:tag.name=="td" and "Pendaftar" in tag.text).find_next().get_text().split(",")[1].strip()
        # print(address)
        addresses.append(address)
    except:
        addresses.append("")
    
    try:
        producer = soup.find("table", {"class": "normal"}).find_all("tbody")[2].find(lambda tag:tag.name=="td" and "Diproduksi Oleh" in tag.text).find_next().get_text().strip().split(",")[0]
        # print(producer)
        producers.append(producer)
    except:
        producers.append("")
        
        
"""
Making connection and inserting data into database.
"""       
connection = mysql.connector.connect(host='localhost',database='License',user='root', password='********')
cursor = connection.cursor()

for product, product_name, brand, registrant, producer, address in zip(products, product_names, brands, registrants, producers, addresses):
    
    mySql_insert_query = """INSERT INTO ProductsData (Product, ProductName, Brand, Registrant, Company, Address) 
                                VALUES (%s, %s, %s, %s, %s, %s) """

    record = (product, product_name, brand, registrant, producer, address)
    cursor.execute(mySql_insert_query, record)

connection.commit()
connection.close()