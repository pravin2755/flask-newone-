import time
from configparser import ConfigParser
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path= r"C:\Users\pravinsinh.gohil\Desktop\chromedriver.exe")
# driver.get("https://www.geeksforgeeks.org/interacting-with-webpage-selenium-python/")
# time.sleep(2)
# title_data = driver.find_element_by_xpath('//div[@class="article-title"]//h1')
# title_data = driver.find_element(By.XPATH, '//li[@id="userProfileId"]//a')
# title_data.get_attribute("@href")
# title_data.get_attribute("@img")
# title_data.get_attribute("@src")
# print()
# print(driver.page_source)


# driver = webdriver.Chrome(executable_path=r"C:\Users\pravinsinh.gohil\Desktop\chromedriver.exe")
# driver.get("https://www.oclc.org/en/worldcat/library100/top500.html")
# time.sleep(2)
#
# data_lot = driver.find_elements(By.XPATH, '//table[@class="wcf500 tablesorter"]//td')
# a1 = []

# for data in data_lot:
#     db_data = data.text
#     print(db_data)

# ab = [data.text for data in data_lot]
# for i in range(len(ab)):
#     if i % 3 == 0:
#         c = ab[i]
#     elif i==1  or :
#         title = ab[i]
#     else:
#         author = ab[i]

# data_details = psycopg2.connect(database="script_db", user="postgres", password="postgres", host="127.0.0.1",
#                                 port="5432")
# ri = 0
# ti = 1
# ai = 2
# for i in range(int(len(ab) / 3)):
#     num1 = ab[ri].strip(".")
#     print(num1)
#     rank1 = int(num1)
#     title1 = ab[ti]
#     author1 = ab[ai]
#     print("Rank : ", rank1, "\n", "Title : ", title1, "\n", "Author : ", author1)
#     ri = ri + 3
#     ti = ti + 3
#     ai = ai + 3
#
#     data_details = psycopg2.connect(database="script_db", user="postgres", password="postgres", host="127.0.0.1",
#                                     port="5432")
#     cur = data_details.cursor()
#     print(rank1)
#     cur.execute("INSERT INTO scrap_db (rank ,title,author) VALUES ((%s), (%s), (%s));", (rank1, title1, author1))
#
#     data_details.commit()
#
# data_details.close()

# config = configparser.ConfigParser()
# config.read("resources.properties")
#
# # driver = webdriver.Chrome(executable_path=r"C:\Users\pravinsinh.gohil\Desktop\chromedriver.exe")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.cowin.gov.in/")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
# time.sleep(2)
# abc=driver.find_element(By.XPATH, '//div[@id="mat-select-value-5"]').click()
# time.sleep(2)
#
# state_list = driver.find_element(By.XPATH, '//mat-option[@id="mat-option-24"]').click()
# print("state:", state_list)
# driver.find_element(By.XPATH, '//div[@id="mat-select-value-7"]').click()
# time.sleep(1)
# dist_list = driver.find_element(By.XPATH, "(//mat-option[contains(@id,'mat-option-')])[1]")
# print("dist:",dist_list.text)
# dist_list.click()


# for list of state

# dist = driver.find_elements(By.XPATH, '//div[@id="mat-select-value-7"]')
# search = driver.find_elements(By.XPATH, '//div[@class="searchBtn pin-search-btn district-search accessibility-plugin-ac"]')
#
#
# print(dist)
# print(search)


# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# if__name__="__main__":
#     app.run(debug=True)