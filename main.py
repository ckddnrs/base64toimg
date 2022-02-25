import requests as rq
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import re
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

url = "https://genhan-report.aiak.or.kr:85/ClipReport5/report_hims.jsp?reportID=ka_s102_1&barcode=002309511932"



driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://genhan-report.aiak.or.kr:85/ClipReport5/report_hims.jsp?reportID=ka_s102_1&barcode=002309511932')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "report_menu_next_button")))
base64_image1 = driver.execute_script("return document.querySelector('canvas').toDataURL('image/png').substring(22);")

driver.get('https://genhan-report.aiak.or.kr:85/ClipReport5/report_hims.jsp?reportID=ka_s102_1&barcode=002309511932')
button = driver.find_element_by_id("report_menu_next_button")
button.click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "report_menu_next_button")))
base64_image2 = driver.execute_script("return document.querySelector('canvas').toDataURL('image/png').substring(22);")
print(base64_image2)

img = Image.open(BytesIO(base64.b64decode(base64_image2)))
plt.imshow(img)
