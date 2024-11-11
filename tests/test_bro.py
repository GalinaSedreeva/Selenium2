import time
import random
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


USER = "user"
PASSWORD = "bitnami"

# Тест проверяющий элементарное наличие элементов на главной странице приложения opencart
def test_elements_main(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 3)  # Ожидание до 3 секунд

    assert wait.until(EC.presence_of_element_located((By.ID, 'menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'top')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'alert')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'form-currency')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'wishlist-total')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'logo')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'search')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'header-cart')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'category')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'narbar-menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'common-home')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'content')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'carousel-banner-0')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'carousel-banner-1')))

    assert wait.until(EC.presence_of_element_located((By.NAME, 'viewport')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'description')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'code')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'redirect')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'search')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'product_id')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'quantity')))


# Тест проверяющий элементарное наличие элементов на странице каталога приложения opencart
def test_elements_catalog(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 3)  # Ожидание до 3 секунд

    assert wait.until(EC.presence_of_element_located((By.ID, 'product-list')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-limit')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-sort')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'button-grid')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'button-list')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'compare-total')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'display-control')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'product-category')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'top')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'alert')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'form-currency')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'wishlist-total')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'logo')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'search')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'header-cart')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'category')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'narbar-menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'content')))
 
    assert wait.until(EC.presence_of_element_located((By.NAME, 'code')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'redirect')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'search')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'quantity')))

# Тест проверяющий элементарное наличие элементов на странице логина в админку приложения opencart
def test_elements_admin(browser):
    browser.get(f"{browser.base_url}/administration")
    wait = WebDriverWait(browser, 3)  # Ожидание до 3 секунд
    assert wait.until(EC.presence_of_element_located((By.ID, 'container')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'alert')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'header')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'content')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'footer')))

    assert wait.until(EC.presence_of_element_located((By.NAME, 'viewport')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'password')))

	
# Тест проверяющий элементарное наличие элементов на странице карточки товара приложения opencart
def test_elements_card(browser):
    browser.get(f"{browser.base_url}/en-gb/product/apple-cinema")
    wait = WebDriverWait(browser, 3)  # Ожидание до 3 секунд
    assert wait.until(EC.presence_of_element_located((By.ID, 'menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'top')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'alert')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'form-currency')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'wishlist-total')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'logo')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'search')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'header-cart')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'category')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'narbar-menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'content')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'product')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'form-product')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'product-info')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-option-223')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'error-option-218')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-option-value-7')))

    assert wait.until(EC.presence_of_element_located((By.NAME, 'option[220]')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'text')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'code')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'redirect')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'name')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'product_id')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'quantity')))
	

# Тест проверяющий элементарное наличие элементов на странице регистрации пользователя приложения opencart
def test_elements_reg(browser):
    browser.get(f"{browser.base_url}/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)  # Ожидание до 3 секунд

    assert wait.until(EC.presence_of_element_located((By.ID, 'menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'top')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'alert')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'form-currency')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'wishlist-total')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'logo')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'search')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'header-cart')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'category')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'narbar-menu')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'content')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'account-register')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'form-register')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'account')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-firstname')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-email')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-password')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'input-newsletter')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'error-firstname')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'error-lastname')))
    assert wait.until(EC.presence_of_element_located((By.ID, 'error-email')))
    
    assert wait.until(EC.presence_of_element_located((By.NAME, 'firstname')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'lastname')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'code')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'redirect')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'search')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'newsletter')))
    assert wait.until(EC.presence_of_element_located((By.NAME, 'agree')))


# Tест логина-разлогина в админку с проверкой, что логин был выполнен
def test_check_login(browser: WebDriver | WebDriver | WebDriver | None):
    browser.get(f"{browser.base_url}/administration")

    browser.find_element(By.NAME, "username").send_keys(USER)
    browser.find_element(By.NAME, "password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(2)
    assert "Dashboard" in browser.title


#Добавить в корзину случайный товар с главной страницы и проверить что он появился в корзине
def test_ware(browser: WebDriver | WebDriver | WebDriver | None):
    browser.get(browser.base_url)
    i= random.randint(1,2)

    match i:
        case 1:
            browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div/button[1]").click()
            time.sleep(2)

            button_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-bs-toggle="dropdown"]')))
        
            # Проверяем содержимое текста кнопки
            assert button_element.text == "1 item(s) - $602.00"


        case 2:
            browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[2]/div/div[2]/form/div/button[1]").click()
            time.sleep(2)

            button_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-bs-toggle="dropdown"]')))
        
            # Проверяем содержимое текста кнопки
            assert button_element.text == "1 item(s) - $123.20"


#Проверить, что при переключении валют цены на товары меняются на главной       
def test_currency_main(browser):
    browser.get(browser.base_url) 
    browser.find_element(By.TAG_NAME, 'ul').click()
    
    #Выбираю первый элемент из списка валют - евро
    browser.find_element(By.CSS_SELECTOR, '.dropdown-menu li:first-child').click()
    # Проверяю что на главной странице в карточке товара теперь цена указывается со значком евро
    assert "€" in browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/span[1]").text
    
    #Выбираю второй элемент из списка валют - фунты
    browser.get(browser.base_url) 
    browser.find_element(By.TAG_NAME, 'ul').click()   
    browser.find_element(By.CSS_SELECTOR, '.dropdown-menu li:nth-child(2)').click()
    # Проверяю что на главной странице в карточке товара теперь цена указывается со значком фунта
    assert "£" in browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/span[1]").text

#Проверить, что при переключении валют цены на товары меняются в каталоге  
def test_currency_catalog(browser):
    browser.get(browser.base_url) 
    browser.find_element(By.TAG_NAME, 'ul').click()
    
    #Выбираю первый элемент из списка валют - евро
    browser.find_element(By.CSS_SELECTOR, '.dropdown-menu li:first-child').click()

    # Проверяю что в каталоге в карточке товара теперь цена указывается со значком евро
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    assert "€" in browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/span[1]").text
