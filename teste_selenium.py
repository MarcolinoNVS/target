from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Caminho para o ChromeDriver
chrome_driver_path = "/Users/marcolino/Downloads/chromedriver-mac-x64"

# Configuração das opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abre o Chrome maximizado

# Configuração do serviço do ChromeDriver
service = Service(chrome_driver_path)

# Inicializa o WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Acessa o Google
    driver.get("https://www.google.com")

    # Encontra a barra de pesquisa e insere o termo "teste"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("teste")
    search_box.send_keys(Keys.RETURN)  # Simula o pressionamento da tecla Enter

finally:
    # Fecha o navegador após alguns segundos
    import time

    time.sleep(5)  # Aguarda 5 segundos para visualizar o resultado
    driver.quit()
