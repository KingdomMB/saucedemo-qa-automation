from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver= driver
        self.input_usuario = (By.ID, "user-name")
        self.input_password= (By.ID, "password")
        self.boton_login = (By.ID, "login-button")
        self.mensaje_error = (By.CSS_SELECTOR, "[data-test='error']")


    def abrir(self):
        self.driver.get("https://www.saucedemo.com/")

    def iniciar_sesion(self,usuario, password):
        self.driver.find_element(*self.input_usuario).send_keys(usuario)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.boton_login).click()

    def obtener_error(self):
        return self.driver.find_element(*self.mensaje_error).text
    
        