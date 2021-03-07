from selenium import webdriver
import time

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://store.hp.com/us/en/pdp/hp-laptop-15t-dy200-2j130av-1/")
time.sleep(10)
privacy_accept_ele = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(1)
review_ele = driver.find_element_by_id("tab_5").click()
time.sleep(5)
reqd_comment_title = driver.find_element_by_xpath('//*[@id="BVRRContainer"]/div/div/div/div/ol/li[1]/div/div[1]/div/div[1]/div/div[3]/h3').text
print(reqd_comment_title)
driver.close()

