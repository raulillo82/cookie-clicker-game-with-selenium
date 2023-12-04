from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

#Full timeout of game is 5 min
timeout = time() + 20
while True and time() <= timeout:
    #Step timeout is 5 min
    timeout2 = time() + 5
    while True and time() <= timeout2:
        cookie.click()

    #Check money:
    money = int(driver.find_element(
        By.CSS_SELECTOR, value="div#money").text.replace(",", ""))
    #Check all products that are enabled and unlocked:
    products = driver.find_elements(By.CSS_SELECTOR,
                                    value="div#rightPanel div#store div b")
    #Reverse the list, as the most expensive item is the one desired to buy
    products = products[::-1]
    product_bought = False
    i = 0
    #Loop the list till, exiting on the first affordable item
    while i < len(products) and not product_bought:
        #print(f"Money: {money}")
        if products[i].text != "":
            price = int(products[i].text.split(" - ")[1].strip().replace(",", ""))
            if price <= money:
                products[i].click()
                product_bought = True
            else:
                i += 1
        else:
            i += 1
    #Max value is for the last one:
    #Click on the product
    #product.click()

#Get cookies per second:
cookies_per_second = float(driver.find_element(By.CSS_SELECTOR,
                                               value="#cps").text.split(" : ")[1])
print(f"cookies/second: {cookies_per_second}")
driver.quit()
