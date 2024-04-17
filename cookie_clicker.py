
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

chromedriver_path = r"C:\Users\USER\Dev\chromedriver-win64\chromedriver.exe"
service=Service(executable_path=chromedriver_path)
options=webdriver.ChromeOptions()
# options.timeouts=
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

language = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language.click()

cookie = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "bigCookie")))
highest_price=0
most_expensive_product=None

timeout=time.time()+60*5
time_in=time.time()+5

while time.time()<timeout:
    cookie.click()
    no_of_cookies=int(driver.find_element(By.ID,"cookies").text.split()[0])
    # Find affordable products and click on most expensive product after 5 seconds
    if time.time()>time_in:
        affordable_products=driver.find_elements(By.CSS_SELECTOR,".product.unlocked.enabled")
        if affordable_products:
            for product in affordable_products:
                product_price=int(product.find_element(By.CLASS_NAME,"price").text)
                if product_price>highest_price:
                    highest_price=product_price
                    most_expensive_product=product
        while no_of_cookies>highest_price:
            most_expensive_product.click()


cookies_per_sec=int(driver.find_element(By.ID,"cookiesPerSecond").text.split(":")[1])
print(cookies_per_sec)


