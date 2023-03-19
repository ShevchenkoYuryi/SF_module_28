from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


'''Открывем сайт в браузере Chrome'''
driver = webdriver.Chrome()
driver.implicitly_wait(5)


def test_1_login_phone():
    driver.get("https://b2c.passport.rt.ru")
    #Вводим телефон
    driver.find_element(By.ID, "username").send_keys("+79093632903")
    #Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.ID, "logout-btn").click()
    print("Test №1 Completed")


def test_2_login_phone():
    driver.get("https://b2c.passport.rt.ru")
    #Вводим телефон
    driver.find_element(By.ID, "username").send_keys("89093632903")
    #Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.ID, "logout-btn").click()

    print("Test №2 Completed")


def test_3_login_email():
    driver.get("https://b2c.passport.rt.ru")
    #Переходим на таб выбора "почта"
    driver.find_element(By.ID, "t-btn-tab-mail").click()
    #Вводим email
    driver.find_element(By.ID, "username").send_keys("cojiw31184@terkoer.com")
    # Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.ID, "logout-btn").click()

    print("Test №3 Completed")


def test_4_login_login():
    driver.get("https://b2c.passport.rt.ru")
    #Переходим на таб выбора "логин"
    driver.find_element(By.ID, "t-btn-tab-login").click()
    #Вводим логин
    driver.find_element(By.ID, "username").send_keys("rtkid_1678555358617")
    # Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.ID, "logout-btn").click()

    print("Test №4 Completed")

def test_5_user_agreement():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/a[1]").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.save_screenshot('foto_1.png')

    print("Test №5 Completed")


def test_6_forgot_pass():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "forgot_password").click()
    driver.find_element(By.ID, "username").send_keys("+79093632903")
    capcha = driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/img[1]").text
    driver.find_element(By.ID, "captcha").send_keys(capcha)
    driver.find_element(By.ID, "reset").click()

    print("Test №6 Completed")


def test_7_log_VK():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "oidc_vk").click()
    driver.find_element(By.XPATH, "//body/div[1]/div[1]/div[1]/div[1]/a[1]")
    driver.save_screenshot('foto_2.png')

    print("Test №7 Completed")


def test_8_log_OK():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "oidc_ok").click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Одноклассники')]")
    driver.save_screenshot('foto_3.png')

    print("Test №8 Completed")


def test_9_log_mail():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "oidc_mail").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Мой Мир@Mail.Ru')]")
    driver.save_screenshot('foto_4.png')

    print("Test №9 Completed")


def test_10_log_gmail():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.ID, "oidc_google").click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Войдите в аккаунт Google')]")
    driver.save_screenshot('foto_5.png')

    print("Test №10 Completed")


def test_11_log_ya():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.XPATH, "//a[@id='oidc_ya']").click()
    driver.find_element(By.XPATH, "//div[contains(text(),'Вход с помощью Яндекса')]")
    driver.save_screenshot('foto_6.png')

    print("Test №11 Completed")


def test_12_cookie():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.XPATH, "//span[contains(text(),'Cookies')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Мы используем Cookie')]")
    driver.save_screenshot('foto_7.png')

    print("Test №12 Completed")


def test_13_conf_pol():
    driver.get("https://b2c.passport.rt.ru")
    driver.find_element(By.XPATH, "//span[contains(text(),'Политикой конфиденциальности')]").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.save_screenshot('foto_8.png')

    print("Test №13 Completed")


def test_14_login_phone():
    driver.get("https://b2c.passport.rt.ru")
    #Негативное тестирование - поле ввода "мобильный телефон" пустое

    #Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Введите номер телефона')]")

    print("Test №14 Completed")


def test_15_login_phone():
    driver.get("https://b2c.passport.rt.ru")
    #Негативное тестирование - поле ввода "пароль" пустое
    driver.find_element(By.ID, "username").send_keys("+79093632903")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.ID, "password")

    print("Test №15 Completed")


def test_16_login_email():
    driver.get("https://b2c.passport.rt.ru")
    #Негативное тестирование - поле ввода "Электронная почта" пустое
    # Переходим на таб выбора "почта"
    driver.find_element(By.ID, "t-btn-tab-mail").click()
    # Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Введите адрес, указанный при регистрации')]")

    print("Test №16 Completed")


def test_17_login_login():
    driver.get("https://b2c.passport.rt.ru")
    #Переходим на таб выбора "логин"
    driver.find_element(By.ID, "t-btn-tab-login").click()
    #Негативное тестирование - поле ввода "Логин" пустое
    # Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Введите логин, указанный при регистрации')]")

    print("Test №18 Completed")


def test_18_login_personal_acc():
    driver.get("https://b2c.passport.rt.ru")
    #Переходим на таб выбора "Лицевой счет"
    driver.find_element(By.ID, "t-btn-tab-ls").click()
    #Негативное тестирование - поле ввода "Лицевой счет" пустое
    # Вводим пароль
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "kc-login").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Введите номер вашего лицевого счета')]")

    print("Test №18 Completed")


def test_19_registration():
    driver.get("https://b2c.passport.rt.ru")
    #Переходим на страницу регистрации
    driver.find_element(By.ID, "kc-register").click()
    # Вводим данные новго пользователя
    driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Лев")
    driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]").send_keys("Толстойй")
    driver.find_element(By.CSS_SELECTOR, "main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.rt-select.rt-select--search.register-form__dropdown:nth-child(3) div.rt-input-container.rt-select__input div.rt-input.rt-input--rounded.rt-input--orange.rt-input--actions > input.rt-input__input.rt-input__input--rounded.rt-input__input--orange").send_keys("Москва")
    driver.find_element(By.ID, "address").send_keys("portynar@mai.ru")
    driver.find_element(By.ID, "password").send_keys("Aa123Tt987")
    driver.find_element(By.ID, "password-confirm").send_keys("Aa123Tt987")
    driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/button[1]").click()
    driver.find_element(By.XPATH, "//h1[contains(text(),'Подтверждение email')]")

    print("Test №19 Completed")


def test_20_registration():
    driver.get("https://b2c.passport.rt.ru")
    #Негативное тестирование. Поле ввода "Имя не соответствует требованиям (см. файл "Документация для тестирования"
    #Переходим на страницу регистрации
    driver.find_element(By.ID, "kc-register").click()
    # Вводим данные новго пользователя
    driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys("")
    driver.find_element(By.ID, "address").send_keys("portynar@mai.ru")
    driver.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]")
    driver.close()
    driver.quit()
    print("Test №20 Completed")





