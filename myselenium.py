from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///home/ja/PycharmProjects/txt_to_gpx/nazwa_mapy.html")
driver.save_screenshot('nazwa_mapy.png')
#print(driver.title)
#search_bar = driver.find_element_by_name("q")
#search_bar.clear()
#search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)
while True:
    print("xx")
#print(driver.current_url)
#driver.close()