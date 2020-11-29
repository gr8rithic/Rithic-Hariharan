from selenium import webdriver

from selenium.webdriver.common.keys import Keys 

browser = webdriver.Firefox()

browser.get("https://www.google.com/")

elem = browser.find_element_by_name("q")

elem.send_keys("What is python ")

elem.send_keys(Keys.RETURN)

inp = input("press q to quit")

if inp == "q":
	browser.quit()