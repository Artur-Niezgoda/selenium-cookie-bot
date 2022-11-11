from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)


# 1
# driver.get("https://a.co/d/5iUKt2H")
# name = driver.find_element(By.ID, 'productTitle')
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(name.text)
# print(price.get_attribute('innerHTML'))


# # 2
# driver.get("https://python.org")
# dates = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time")
# names = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > a")
# events = {i: {"time": dates[i].get_attribute("datetime").split("T")[0], "name": names[i].text} for i in range(len(names))}
# print(events)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number = driver.find_element(By.CSS_SELECTOR, "#articlecount > a")
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

driver.quit()