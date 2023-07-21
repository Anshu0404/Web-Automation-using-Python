reg = input("Enter your college id")
password  =  input("Enter your password:")
from selenium import webdriver
import time
# Download and paste the path of your browser
path = "C:\Program Files (x86)\msedgedriver"
# Example: 
driver = webdriver.Edge(path)
driver.get("college login portal")
driver.maximize_window()
user = driver.find_element_by_xpath('//*[@id = "txtusername"]')
user.send_keys(reg)
pwd = driver.find_element_by_xpath('//*[@id = "password"]')
pwd.send_keys(password)
lgn = driver.find_element_by_xpath('//*[@id = "Submit"]')
lgn.click()
glrn = driver.find_element_by_xpath('//*[@id = "MainContent_studentg"]/div[12]/a/h5')
glrn.click()
class1 = driver.find_element_by_xpath('/html/body/form/div[3]/section/div/div/div[2]/div[4]/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/a/div')
# time.sleep(5)
class1.click()



# Note: Update web drivers everytime your browser is updated for error free working
