from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tinder_info as info

username = info.user()
password = info.passw()

driver = webdriver.chrom()
driver.get('https://www.tinder.com')