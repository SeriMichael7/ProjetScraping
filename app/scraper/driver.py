from selenium import webdriver



def creer_navigateur():
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)
