import selenium
from selenium import webdriver

driver = webdriver.Chrome()

class Auth():
    def __init__(self, mail, password) -> str:
        self.user_mail = mail
        self.user_pasword = password

    def user_data(self):
        self.mail = input("Введите свою почту: ")
        self.password = input("Введите свой пароль: ")

    def auth(self):
        driver.get()