import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
# nOt0r5Le5LhYZjrmZ6DpW4QvvXBXTCyG670NB1H02zr1ik9Zwh
username = "prashantsharma"
accessToken = "RlEUtZdSXJkl3iEtXNx6eWFSyLBfDJlkYRYG1igfb1OjpXfXRp"
build = os.getenv('LT_BUILD_NAME')
os.environ[“LT_GRID_URL”] = “https://prashantsharma:{AQAAABAAAABAvJUzCmhyN6piWVOFEIEF+Q7bPcDsSafuiRJN3pqDwq1ZY7IIJm6RlgnD3xpV1isd0njjE5sfVtr1PXpjVfpd9h6ZLAv+BKBZL8pClZlGv20=}@hub.lambdatest.com/wd/hub”
gridUrl = "hub.lambdatest.com/wd/hub"
options = ChromeOptions()
options.browser_version = "112.0"
options.platform_name = "Windows 11"
lt_options = {}
lt_options["project"] = "selenium test"
lt_options["name"] = "selenium"
lt_options["build"] = build
lt_options["network"] = True
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
# lt_options["tunnel"] = True
# lt_options["tunnelName"] = "LT-LP-156"
options.set_capability('LT:Options', lt_options)

# "http://hub.lambdatest.com/wd/hub"
url = "https://"+username+":"+accessToken+"@"+gridUrl

driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

Username = "prashantsharma@lambdatest.com"
pd = "aARUSH@123"
Url = "https://accounts.lambdatest.com/login"

# driver = webdriver.Chrome()
driver.get(Url)

uname = driver.find_element("id", "email")
uname.send_keys(Username)
password = driver.find_element("id", "password")
password.send_keys(pd)
driver.find_element("id", "login-button").click()
time.sleep(1)

# drp = driver.find_element(By.XPATH, "//*[@id=profile__dropdown]")
# drp.click()
# org = driver.find_element("id", "item__manage__team")
# org.click()
# exp = driver.find_element(By.XPATH, "//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]")
# exp.click()
# inv = driver.find_element(By.XPATH, "//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]")
# inv.click()
# # driver = webdriver.Chrome()
# driver.get("https://cgi-lib.berkeley.edu/ex/perl5/fup.html")
# time.sleep(1)
# upl = driver.find_element(By.XPATH, "/html/body/form/input[1]")
# upl.send_keys("C:/Users/prashantsharma/Downloads/Invited Users.csv")
# sub = driver.find_element(By.XPATH, "/html/body/form/input[3]")
# sub.click()
# time.sleep(1)
# # //*[@id="profile__dropdown"]
# # //*[@id="app"]/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div
# # driver.quit()
driver.quit()
