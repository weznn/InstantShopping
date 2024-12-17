
pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Tarayıcı ayarları
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Arka planda çalıştırmak için
driver = webdriver.Chrome(options=options)

# Ürün linki
product_url = "https://www.zara.com/tr/tr/ornek-urun-linki"

# Otomasyonun ana işlevi
def check_and_add_to_cart(url):
    try:
        driver.get(url)
        time.sleep(2)  # Sayfanın tamamen yüklenmesi için bekle

        # Stok kontrolü: Butonun metnini kontrol ediyoruz
        try:
            stock_button = driver.find_element(By.CLASS_NAME, "add-to-cart-button-class")  # Düğme sınıfını doğru gir
            if stock_button.text.lower() in ["sepete ekle", "add to cart"]:
                stock_button.click()
                print("Ürün sepete eklendi!")
            else:
                print("Ürün stokta yok.")
        except Exception as e:
            print("Stok kontrolünde hata:", e)

    except Exception as e:
        print("Bir hata oluştu:", e)

# Belirli aralıklarla kontrol etme
while True:
    check_and_add_to_cart(product_url)
    print("Tekrar kontrol ediliyor...")
    time.sleep(60)  # 60 saniye sonra tekrar kontrol

# İşlem tamamlandıktan sonra tarayıcıyı kapat
driver.quit()





