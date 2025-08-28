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
                    title = card.find_element(By.CSS_SELECTOR, "h2").text
                    link = card.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                    try:
                        company = card.find_element(By.CSS_SELECTOR, "div.text-body a").text
                    except:
                        company = "Não informado"

                    try:
                        location = card.find_element(By.CSS_SELECTOR, "div.mb-8").text
                    except:
                        location = "Não informado"

                    jobs.append([title, company, location, link])
                except Exception as e:
                    print("Erro ao coletar vaga:", e)

            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, "a[title='Próxima']")
                next_button.click()
                time.sleep(3)
            except:
                print("Não há mais páginas disponíveis.")
                break
        return jobs

    def fechar(self):
        self.driver.quit()