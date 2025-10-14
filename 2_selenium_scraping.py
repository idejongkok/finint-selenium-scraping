"""
Web Scraping Sederhana dengan Selenium + BeautifulSoup
Target: https://testapp.idejongkok.com
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# ===========================================
# BAGIAN 1: SETUP BROWSER
# ===========================================
print("Membuka browser...")
driver = webdriver.Chrome()
driver.maximize_window()

# ===========================================
# BAGIAN 2: LOGIN DENGAN SELENIUM
# ===========================================
print("\n=== PROSES LOGIN ===")

# Buka halaman login
url_login = "https://testapp.idejongkok.com"
driver.get(url_login)
time.sleep(2)

# Isi email
print("Mengisi email...")
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("uno.testing3@gmail.com")

# Isi password
print("Mengisi password...")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("123456789")

# Klik tombol login
print("Klik tombol login...")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Tunggu sampai login berhasil
time.sleep(3)
print("Login berhasil!\n")

# ===========================================
# BAGIAN 3: SCRAPING DATA DENGAN BEAUTIFULSOUP
# ===========================================
print("=== MULAI SCRAPING DATA ===\n")

# Ambil page source dari halaman setelah login
page_source = driver.page_source

# Parse HTML dengan BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# print(soup.prettify()[:7000])  # Print sebagian karakter pertama dari HTML yang di-scrape

rows = soup.find('tbody').find_all('tr')

for i, row in enumerate(rows, 1):

    cells = row.find_all('td')
    nama_product = cells[0].find('div', class_='font-medium').get_text(strip=True)
    
    harga = cells[2].get_text(strip=True)
    
    print(f"{i}. {nama_product} - Harga: {harga}")
    # print(f"   Harga: {harga}")
