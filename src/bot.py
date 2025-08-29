from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class JobBot:
    def __init__(self, driver_path=None):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def search_jobs(self, site_url, cargo, cidade, max_pages = 1):
        self.driver.get(site_url)
        time.sleep(2)

        botao_dados = self.driver.find_element(By.ID, "didomi-notice-agree-button")
        time.sleep(2)
        botao_dados.click()
        time.sleep(5)

        keyword_cargo = self.driver.find_element(By.ID, "keywordsCombo")
        time.sleep(1)
        keyword_cargo.send_keys(cargo)
        time.sleep(1)

        keyword_cidade = self.driver.find_element(By.ID, "city")
        keyword_cidade.clear()
        keyword_cidade.send_keys(cidade)
        time.sleep(2)

        selecionar_cidade = self.driver.find_element(By.CLASS_NAME, "autocomplete-suggestion")
        selecionar_cidade.click()
        time.sleep(2)

        achar_vagas = self.driver.find_element(By.CLASS_NAME, "job-location-filter-btn")
        achar_vagas.click()
        time.sleep(3)

        jobs = []

        for page in range(1, max_pages + 1):
            time.sleep(2)
            print(f"Coletando página {page}...")

            cards = self.driver.find_elements(By.CSS_SELECTOR, "div.card.js_rowCard")
            print(f"Encontrados {len(cards)} cards na página {page}")

            for card in cards:
                try:
                    titulo = card.find_element(By.CSS_SELECTOR, "a h2").text
                    link = card.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                    try:
                        compania = card.find_element(By.CSS_SELECTOR, ".text-body a").text
                    except:
                        compania = "Não informado"

                    try:
                        localizacao = card.find_element(By.CSS_SELECTOR, ".mb-8").text
                    except:
                        localizacao = "Não informado"

                    try:
                        salario = card.find_element(By.XPATH, ".//*[contains(text(), 'R$')]").text
                    except:
                        salario = "Não informado"

                    try:
                        contrato = card.find_element(By.XPATH, ".//*[contains(text(), 'CLT') or contains(text(), 'PJ') or contains(text(), 'Estágio')]").text
                    except:
                        contrato = "Não informado"

                    try:
                        modalidade = card.find_element(By.XPATH, ".//*[contains(text(), 'Remoto') or contains(text(), 'Híbrido') or contains(text(), 'Presencial')]").text
                    except:
                        modalidade = "Não informado"

                    jobs.append([titulo, compania, localizacao, salario, contrato, modalidade, link])
                except:
                    pass

        return jobs

    def fechar(self):
        self.driver.quit()