# download.py
from selenium.webdriver.common.by import By
import os
import time

def download_invoice(driver):
    # Aller à la page des factures
    driver.get("https://example.com/mes-factures")
    time.sleep(2)

    # Cliquer sur le bouton de téléchargement du dernier PDF
    download_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Télécharger')]")
    download_button.click()
    
    # Attendre que le téléchargement se fasse
    time.sleep(5)

    # Vérifier le dossier de téléchargement
    if not os.path.exists("data"):
        os.makedirs("data")
    
    print("Facture téléchargée dans le dossier data/")
