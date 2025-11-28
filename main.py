# main.py
from login import login
from download import download_invoice

def main():
    driver = login()
    download_invoice(driver)
    driver.quit()

if __name__ == "__main__":
    main()
