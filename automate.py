from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

browser = Chrome()
# browser.maximize_window()
browser.get("http://127.0.0.1:5500/index.html")

website = browser.find_element_by_id("fname")
website.send_keys("Rugved")

website = browser.find_element_by_id("lname")
website.send_keys("Koshiya")

website = browser.find_element_by_id("email")
website.send_keys("myemail@gmail.com")

website = browser.find_element_by_id("mobnumber")
website.send_keys("0123456789")

browser.find_element_by_xpath("/html/body/div/form/div[4]/input").click()
browser.find_element_by_xpath('//*[@id="reading"]').click()
browser.find_element_by_xpath('//*[@id="coding"]').click()
browser.find_element_by_xpath('//*[@id="gaming"]').click()

# browser.find_element_by_xpath('//*[@id="areyou"]]').click()
browser.find_element_by_xpath('//*[@id="areyou"]/option[2]').click()

website = browser.find_element_by_xpath('//*[@id="comment"]')
website.send_keys("Like Share & Subscribe :)")

website.submit()
browser.close()