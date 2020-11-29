from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://www.youtube.com/")

elem = browser.find_element_by_name("search_query")

elem.send_keys("Dhoni")

elem1 = browser.find_elemement_by_link_text("search")
elem1.click()

