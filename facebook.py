from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.facebook.com')

userName = browser.find_element_by_id('email')
userName.send_keys('your email')
passWord = browser.find_element_by_id('pass')
passWord.send_keys('yourpass')
passWord.submit()
