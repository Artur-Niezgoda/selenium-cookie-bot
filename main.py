from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime


def click_update():
    """
    Finds and clicks the next upgrade in the store
    """
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    new_upgrade = None
    for item in store:
        if item.get_attribute("class") == "":
            new_upgrade = item
        if item.get_attribute("class") == "grayed":
            break
    new_upgrade.click()


# Install and set up Chromedriver
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

# Open the Cookie Clicker game website
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

# Start clicking the cookie and checking for upgrades
game_on = True
start_time = datetime.now()
check_time = start_time

while game_on:
    cookie.click()
    now_time = datetime.now()
    
    # Click the next upgrade every 5 seconds
    if (now_time - check_time).seconds > 5:
        check_time = now_time
        click_update()
        print(driver.find_element(By.ID, "cps").text)
        
    # End the game after 5 minutes
    if (now_time - start_time).seconds > 60*5:
        game_on = False

# Close the browser window
driver.quit()
