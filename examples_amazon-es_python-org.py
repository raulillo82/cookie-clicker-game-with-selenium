from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#url_amazon = "https://www.amazon.es/Instant-Pot-IP-DUO60-el%C3%A9ctrica-programable/dp/B08Z4HCGDH/"
#driver.get(url_amazon)
#price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#print(f"The price is {price_euro.text},{price_cents.text}€")

#url_python = "https://www.python.org/"
#driver.get(url_python)
#search_bar = driver.find_element(By.NAME, value="q")
#print(search_bar.get_attribute("placeholder"))
#button = driver.find_element(By.ID, value="submit")
#print(button.size)
#doc_link = driver.find_element(By.CSS_SELECTOR,
#                               value=".documentation-widget a")
#print(doc_link.text)
#link_submit_web_bug = driver.find_element(By.XPATH, 
#                                          value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
#print(link_submit_web_bug.text)
##also as a list with "find_elementS"

#Scrap the next python events into a dictionary and print it:
url_python = "https://www.python.org/"
driver.get(url_python)
css_dates = ".event-widget.last time"
css_names = ".event-widget.last li a"
events_dates = [element.get_attribute("datetime").split("T")[0]
                for element
                in driver.find_elements(By.CSS_SELECTOR, value=css_dates)]
events_names = [element.text
                for element
                in driver.find_elements(By.CSS_SELECTOR, value=css_names)]
events_dict = {i: {"time": events_dates[i], "name": events_names[i]}
               for i in range(len(events_dates))
               }
print(events_dict)

#driver.close()
driver.quit()
