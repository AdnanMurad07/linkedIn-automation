from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3796881607&f_AL=true&keywords=Python%20Developer&location=Indore&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

driver.get(url)
sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
email_input = driver.find_element(By.CSS_SELECTOR, value="#username")
email_input.send_keys("YOUR_MAIL_ID")
password_input = driver.find_element(By.CSS_SELECTOR, value="#password")
password_input.send_keys("YOUR_GMAIL_PASSWORD")
sign = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign.click()
time.sleep(8.0)
apply_button = driver.find_element(By.XPATH, value='//*[@id="ember325"]/span')
apply_button.click()
time.sleep(2.0)
phone_no = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3796881607-108373787-phoneNumber-nationalNumber"]')
phone_no.send_keys("YOUR_PHONE_NUMBER")