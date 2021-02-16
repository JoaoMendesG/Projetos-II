from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('Selenium is running...')
drive = webdriver.Chrome(executable_path=r'C:\Users\joaop\Desktop\Drivers\chromedriver')
drive.get('https://www.google.com/')
drive.find_element_by_name('q').send_keys('selenium cheat sheet' + Keys.RETURN)
drive.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div[1]/a/h3').click()
time.sleep(5)
drive.find_element_by_xpath('//*[@id="MainNav"]/div/div[4]/span/span[3]/a').click()
time.sleep(5)
drive.find_element_by_xpath('//*[@id="Cyber-security"]/li/a').click()