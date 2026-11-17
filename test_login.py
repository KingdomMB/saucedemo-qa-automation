from selenium import webdriver
from login_page import LoginPage

def test_login_exitoso():
    driver = webdriver.Chrome()
    pagina_login = LoginPage(driver)  # Instanciamos tu objeto

    pagina_login.abrir()
    pagina_login.iniciar_sesion("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url
    driver.quit()

def test_login_fallido():
    driver = webdriver.Chrome()
    pagina_login = LoginPage(driver)

    pagina_login.abrir()
    pagina_login.iniciar_sesion("standard_user","clave_falsa")
    mensaje_error = pagina_login.obtener_error()
    assert "Username and password do not match" in mensaje_error
    driver.quit()