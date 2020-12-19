from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
import time
from random import randint

SEARCH = "_ACCOUNT_YOU_WANT_TO_GET_FOLLOWERS_FROM_"
WEB_PAGE = "https://www.instagram.com/accounts/login/"
DRIVER_PATH = "_YOUR_DRIVER_PATH_"
EMAIL = "_ACCOUNT_EMAIL_LOGIN_"
PASSWORD = "_ACCOUNT_PASSWORD_"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(WEB_PAGE)
print(">>> Connected to webpage")

time.sleep(randint(2, 4))
insta_email = driver.find_element_by_class_name("_9GP1n")
insta_email.click()

insta_email_entry = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
insta_email_entry.send_keys(EMAIL)

insta_email_entry.send_keys(Keys.TAB)
insta_pass = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
insta_pass.send_keys(PASSWORD)
insta_pass.send_keys(Keys.ENTER)
time.sleep(4)
print(">>> Logged in")


insta_dismiss = driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > "
                                                    "button.aOOlW.HoLwm")
insta_dismiss.click()
print(">>> Dismiss notification success")


insta_search_click = driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div "
                                                         "> div.LWmhU._0aCwM > div")
insta_search_click.click()

begin_search = driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > "
                                                   "div.LWmhU._0aCwM > input")
begin_search.send_keys(SEARCH)
begin_search.send_keys(Keys.ENTER)
print(">>> Search Success")

time.sleep(randint(2, 4))
selection_click = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
selection_click.click()

time.sleep(randint(1, 3))
follower_link = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
follower_link.click()
time.sleep(randint(1, 3))

follower_popup = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
scroll = 0
while scroll < 10:  # determines how many scrolls
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)
    time.sleep(randint(2, 3))
    follow_btns = driver.find_elements_by_css_selector("li button")
    for button in follow_btns:
        try:
            button.click()
            time.sleep(randint(1, 2))
        except ElementClickInterceptedException:
            cancel_button = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            cancel_button.click()
            time.sleep(randint(1, 2))
        except StaleElementReferenceException:
            pass


