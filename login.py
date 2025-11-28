# login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import URL_LOGIN, USERNAME, PASSWORD

def login():
    # Initialisation du navigateur (Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    driver.get(URL_LOGIN)
    time.sleep(2)  # attendre le chargement

    # Remplir le formulaire
    driver.find_element(By.ID, "email").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

    time.sleep(3)  # attendre la connexion
    return driver
