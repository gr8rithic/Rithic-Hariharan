from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("https://docs.python.org/3/")

elem = browser.find_element_by_name("q")

inp_find = input("Enter the doc search")
elem.send_keys(inp_find)

elem.send_keys(Keys.RETURN)


inp = input()

if inp =="q":
	browser.quit()
