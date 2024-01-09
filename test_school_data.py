from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import pandas as pd
from io import BytesIO
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://emis.moeys.gov.kh/?#/pages/school-report-card")

#WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH,

dict_data ={}
list_data = []

# change lang -> eng
driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div/div/div/button[2]").click()

#choose academic year
list_year = ['2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019']

# select year
for enum_year, i_year in enumerate(list_year):
    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/main/div/div/div/div[1]/div/div/div[2]/div/div/div[1]"))).click() #select button
    # dir(driver.find_element(By.XPATH,'//*[@id="list-49"]')).text # select button
    driver.find_element(By.XPATH, '//*[@id="list-item-83-'+ str(enum_year) +'"]').click()

    # click on advance search
    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/form/div/div/div/div/div/div[1]/div/div[2]/div/div[4]"))).click()

    # list province by academic year
    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/form/div/div/div/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[1]"))).click() #select bar
    driver.sleep(5)
    list_province = driver.find_element(By.XPATH, "/html/body/div/div[3]/div").text.split("\n")
    for enum_prov, i_prov in enumerate(list_province):
        driver.find_element(By.XPATH, '//*[@id="list-item-105-'+ str(enum_prov)+ '"]').click()

        # search button
        WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/form/div/div/div/div/div/div[3]/div/button[1]"))).click()
        driver.sleep(5)

        #expand list to all
        WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/main/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div"))).click()
        WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list-item-174-3"]'))).click()
        driver.sleep(5)
        
        #Data Table
        
        # ele_table = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div[2]/div[2]/div/div[1]")
        # ele_tr = ele_table.find
        
        #thead
        driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div[2]/div[2]/div/div[1]/table/thead")

        ele_table = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div[2]/div[2]/div/div[1]/table/tbody")
        ele_tr = ele_table.find_elements(By.TAG_NAME, "tr")

# WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/span/svg'))).click()

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
canvas_element = driver.find_element(By.ID, 'chart3')

# Get the location and size of the canvas
location = canvas_element.location
size = canvas_element.size

# Take a screenshot of the entire webpage
screenshot = driver.get_screenshot_as_png()
screenshot = Image.open(BytesIO(screenshot))

# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
canvas_image = screenshot.crop((left, top, right, bottom))

# Use Tesseract OCR to extract text from the canvas image
extracted_text = pytesseract.image_to_string(canvas_image)