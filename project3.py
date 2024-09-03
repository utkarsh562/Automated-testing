from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

service = Service(r'C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.implicitly_wait(10)
#1. Selecting the radio button

driver.find_element(By.XPATH, '//*[@id="product_549"]').click()

#2. Filling the passengers details

driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Utkarsh")
driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Pathak")

#3. Choosing date of birth..

driver.find_element(By.XPATH, "//input[@id='dob']").click()

month = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
month.select_by_visible_text("Nov")

yr = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yr.select_by_visible_text("2001")

date_pick = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for d in date_pick:
    if d.text == "12":
        d.click()
        break

#4. Choosing the gender

driver.find_element(By.XPATH, "//input[@id='sex_1']").click()

#5 Choosing trip type and details

driver.find_element(By.XPATH, "//input[@id='traveltype_1']").click()

driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("New Delhi")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Mirzapur")

#6 Selecting the departure date
driver.find_element(By.XPATH, "//input[@id='departon']").click()
month_picker = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
month_picker.select_by_visible_text("Aug")
yr_picker = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yr_picker.select_by_visible_text("2024")

date_picker = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td')
for da in date_picker:
    if da.text == "29":
        da.click()
        break

#7. Selecting the delivery options

driver.find_element(By.XPATH, "//span[@id='select2-reasondummy-container']").click()

driver.find_element(By.XPATH, "//li[text()='Visa application']").click()

driver.find_element(By.XPATH, "//input[@id='deliverymethod_3']").click()

#8. Billing address

driver.find_element(By.XPATH, "//input[@id='billname']").send_keys("Medoc")
driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("8303271019")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("nicks.thebrand@gmail.com")
driver.find_element(By.XPATH, '//*[@id="select2-billing_country-container"]').click()
driver.find_element(By.XPATH, "//li[text()='India']").click()

driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("235")
driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Mirzapur")
driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']").click()
driver.find_element(By.XPATH, "//li[text()='Uttar Pradesh']").click()
driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("231001")

time.sleep(2)

# driver.find_element(By.XPATH, "//button[@id='place_order']").click()

place_order_button = driver.find_element(By.XPATH, "//button[@id='place_order']")
driver.execute_script("arguments[0].scrollIntoView();", place_order_button)
place_order_button.click()

confirmation_message = driver.find_element(By.XPATH, "/html/body").text

print("Confirmation Message: ", confirmation_message)

with open("confirmation_message.txt", "w", encoding="utf-8") as file:
    file.write(confirmation_message)

print("Confirmation message saved to confirmation_message.txt")

print("!!..............Successfully placed Order............!!")

input("Enter to quit..!!")
driver.close()
