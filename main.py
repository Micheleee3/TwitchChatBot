import random
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

channel = input("Channel link:")

s = []
with open('text.csv', 'r',  encoding='utf-8') as text_file:
    reader = csv.reader(text_file)
    for row in reader:
        s.append(row[0])


options = webdriver.ChromeOptions()
#Chrome profile path
#options.add_argument(r"--user-data-dir=C:\Users\YourName\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Default')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(channel)
time.sleep(5)
input_box = driver.find_element("xpath", "//*[@data-a-target='chat-input']")
while True:
    message = random.choice(s)
    #s.remove(message)
    print(message)
    input_box.send_keys(message)
    time.sleep(random.uniform(5, 30))
    input_box.send_keys(Keys.ENTER)

#driver.quit()
