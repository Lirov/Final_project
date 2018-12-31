from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\selenium\chromeDriver_selenium\chromedriver.exe")
driver.get("http://192.168.99.100:5000")
x = driver.find_element_by_xpath("//html/body")
print(x.text)

