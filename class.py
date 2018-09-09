from selenium import webdriver
driver = webdriver.Firefox()
driver.get("file:///C:/Users/pgandhi/Documents/Selenium/Ex_Files_Python_Automation_Testing/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html")
content= driver.find_element_by_class_name('content')

print("My class element is: ")
print(content)

driver.close()
