import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from secret import EMAIL,PASSWORD

options = webdriver.ChromeOptions()
options.add_argument("window-size=2000,1000")
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver= webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://www.linkedin.com/home")

sleep(2)

signButton = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
signButton.click()

sleep(1)

emailId = driver.find_element_by_id("username")
emailId.send_keys(EMAIL)

passBox = driver.find_element_by_id("password")
passBox.send_keys(PASSWORD)

signClick = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button")
signClick.click()

sleep(1)


driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

sleep(2)

acceptBtn  = driver.find_elements_by_css_selector('.invitation-card__action-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view')
                                                   
print(acceptBtn)
print(type(acceptBtn))
print()

for i in acceptBtn:
    i.click()
    sleep(3)

'''
driver.execute_script(""" 
let acceptBtns = document.querySelectorAll('.invitation-card__action-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view');
for (const btn of acceptBtns){
    btn.click();
}
""") 

'''  