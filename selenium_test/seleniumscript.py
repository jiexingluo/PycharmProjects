from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\jluo\\PycharmProjects\\browser_driver\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get('http://www.ni.com')
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element_by_id('n33_autoCompleteInput').send_keys("6556")
driver.find_element_by_class_name("search search-icon").click()
