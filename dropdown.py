from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver =  webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("enter website here")
driver.maximize_window()
# create the list which store options from dropdown
totl_values = []
sel = Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
for opt in sel.options:
    totl_values.append(opt.text)

# create the list which contains actual element from dropdown
originalList = []

for original in totl_values:
    # add elements to the originalList
    originalList.append(original)
print("The original list are")
print(originalList)
print("-----------------------------------------------------")
# Create the another list which store original values for temp purpose
tempList = []
for temp in originalList:
    tempList.append(temp)

print("Temp List are")
print(tempList)
print("-----------------------------------------------------")
print("After sorting the original list elements are")
# sort the original list
originalList.sort()
print("-----------------------------------------------------")
print(originalList)

print("-----------------------------------------------------")

# check the original list with temp list

if originalList == tempList:
    print("Test case pass dropdown lists are alphabetically sorted")
else:
    print("Test case fail dropdown lists are not alphabetically sorted")
