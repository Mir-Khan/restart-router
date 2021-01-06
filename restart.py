from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_is

def router_restart(routerIp, password):
    # if you wanted to use another browser, download the driver for it and just change Firefox to Chrome or whatever below
    driver = webdriver.Firefox()
    driver.get(routerIp)
    # enters whatever password you set it as
    driver.find_element(By.ID, 'http_passwd').send_keys(password + Keys.ENTER)
    # navigating the Linksys Router Web Interface until the reset button is reached
    WebDriverWait(driver, 10).until(title_is('Router'))
    driver.find_elements_by_tag_name('a')[6].click()
    WebDriverWait(driver, 10).until(title_is('Basic Setup'))
    driver.find_elements_by_tag_name('a')[23].click()
    WebDriverWait(driver, 10).until(title_is('Language'))
    driver.find_elements_by_tag_name('a')[24].click()
    WebDriverWait(driver, 10).until(title_is('Device Reset'))
    # the reset button is pressed and the following alert is accepted
    driver.find_element_by_name('btn_reboot').click()
    alert = driver.switch_to_alert()
    alert.accept()
# can set it to your current Linksys router webpage interface and enters whatever password you have for the interface
router_restart('LOGIN PAGE', 'PASSWORD')
