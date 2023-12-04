from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#import locale
#locale.setlocale(locale.LC_ALL, '')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#url_wikipedia = "https://en.wikipedia.org/wiki/Main_Page"
#driver.get(url_wikipedia)

#Getting a value:
#articles_count_link = driver.find_element(By.CSS_SELECTOR,
#                                          value="div#articlecount a")
#articles_number = int(articles.text.replace(",", ""))
#print(f"{articles:n}")
#articles_count_link.click()

#Clicking on a link
#all_portals = driver.find_element(By.LINK_TEXT, value="Community portal")
#all_portals.click()

##Typing in a searchbox
#driver.maximize_window()
#sleep(1)
#search_box = driver.find_element(By.NAME, value="search")
#search_box.send_keys("Python")
#search_box.send_keys(Keys.ENTER)
#sleep(3)

#Register in a dummy website
url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)
fname_input = driver.find_element(By.NAME, value="fName")
fname_input.send_keys("My First Name") 
lname_input = driver.find_element(By.NAME, value="lName")
lname_input.send_keys("My Last Name") 
email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("santa@northpole.com")
signup_button = driver.find_element(By.CSS_SELECTOR, value="button.btn")
signup_button.click()
sleep(3)

driver.quit()
