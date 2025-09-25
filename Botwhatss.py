from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path

from time import sleep


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def abrir_janela_whatsapp():
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver,timeout=60)
    barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="side"]')))
    driver.implicitly_wait(2)

def abrir_janela_de_conversa(nome_contato):
    wait = WebDriverWait(driver,timeout=2)
    barra_pesquisa = driver.find_element(By.XPATH, value='//div[contains(@aria-label, "Caixa de texto de pesquisa")]')
    barra_pesquisa.send_keys(Keys.CONTROL +'A')
    barra_pesquisa.send_keys(Keys.DELETE)

    # barra_pesquisa = driver.find_element(By.XPATH, value='//div[contains(@aria-label, "Caixa de texto de pesquisa")]')
    barra_pesquisa.send_keys(nome_contato)

    conversa_lateral = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, f"//span[contains(text(), '{nome_contato}')]")
    ))

    conversa_lateral.send_keys(Keys.ENTER)
    conversa_lateral.click()

def sai_das_conversa():
    barra_pesquisa = driver.find_element(By.XPATH, value='//div[contains(@aria-label, "Caixa de texto de pesquisa")]')
    barra_pesquisa.send_keys(Keys.CONTROL +'A')
    barra_pesquisa.send_keys(Keys.DELETE)
    barra_pesquisa.send_keys(Keys.ESCAPE)

def enviar_mensagem(mensagem):
    barra_de_mensagem = driver.find_element(By.XPATH, value='//div[contains(@aria-placeholder,"Digite uma mensagem")]')
    barra_de_mensagem.send_keys(Keys.CONTROL + 'A')
    barra_de_mensagem.send_keys(mensagem)
    barra_de_mensagem.send_keys(Keys.RETURN)

def envia_documento(caminho_do_documento):
    botao_anexos = driver.find_element(By.XPATH,value='//span[@data-icon="plus-rounded"]')
    botao_anexos.click()
    botao_imagens = driver.find_element(By.XPATH, value='//span[contains(text(), "Fotos e vídeos")]/../input')
    botao_imagens.send_keys(caminho_do_documento)
    botao_enviar = driver.find_element(By.XPATH,value='//div[@aria-label="Enviar"]')
    botao_enviar.click()
     
if __name__ =='__main__':

    contatos = ['Cliente 1','Cliente 2','Cliente 3' ]
    caminho_catalogo = str(Path(__file__).parent/'Screenshot_3.png')
    print (caminho_catalogo)        
    mensagem="""
    Olá{}!
    Foi um prazer conhece-lo.
    Envio um catalogo dos nossos produtos, para que voce possa explorá-lo.
    Um Abraco!
    """;

    abrir_janela_whatsapp()
    
    for contato in contatos:
        abrir_janela_de_conversa(contato)
        sleep(1)
        enviar_mensagem(mensagem.format(contato))
        sleep(1)
        envia_documento(caminho_catalogo)
        sleep(1)
        sai_das_conversa()


