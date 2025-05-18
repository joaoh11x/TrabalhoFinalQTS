from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:5173/login")  # URL local da aplicação

# === CADASTRO ===

# Clica no link de cadastro
try:
    cadastro_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'cadastro_link'))
    )
    cadastro_link.click()
    print("✅ Clique no link de cadastro efetuado com sucesso!")
except:
    print("❌ Não foi possível encontrar o link de cadastro.")

# Espera um pouco para garantir que a página de cadastro carregou
time.sleep(2)

# Limpa os campos de email e senha antes de preencher com novos dados
email_input = driver.find_element(By.ID, "email_input")
email_input.clear()
email_input.send_keys("novousuario@dominio.com")

first_name_input = driver.find_element(By.ID, "first_name_input")
first_name_input.send_keys("João")

last_name_input = driver.find_element(By.ID, "last_name_input")
last_name_input.send_keys("Silva")

# Limpa o campo de senha antes de preenchê-lo
password_input = driver.find_element(By.ID, "password_input")
password_input.clear()
password_input.send_keys("senhaForte123")

# Limpa o campo de confirmar senha antes de preenchê-lo
confirm_password_input = driver.find_element(By.ID, "confirm_password_input")
confirm_password_input.clear()
confirm_password_input.send_keys("senhaForte123")

# Clica no botão de cadastrar
register_button = driver.find_element(By.XPATH, '//button[contains(text(), "Cadastrar")]')
register_button.click()

# Aguarda um pouco para ver o resultado do cadastro
time.sleep(3)

# === LOGIN COM O MESMO EMAIL E SENHA ===

# Agora, tenta fazer login com o email e senha cadastrados
driver.get("http://localhost:5173/login")  # Volta para a página de login

# Preenche os campos de login
email_input = driver.find_element(By.XPATH, '//input[@type="email" and @placeholder="seu@email.com"]')
email_input.send_keys("novousuario@dominio.com")

password_input = driver.find_element(By.XPATH, '//input[@type="password" and @placeholder="••••••••"]')
password_input.send_keys("senhaForte123")

# Clica no botão de login
login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Entrar")]')
login_button.click()

# Aguarda botão de perfil
profile_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'btt_persona'))
)

try:
    error_message = driver.find_element(By.CLASS_NAME, "error-message")
    print("❌ Falha no login: " + error_message.text)
except NoSuchElementException:
    print("✅ Login efetuado com sucesso!")

    profile_button.click()
    print("✅ Clique no botão de perfil efetuado com sucesso!")

    time.sleep(4)  # Delay antes de sair

    logout_button = driver.find_element(By.ID, 'btt_sair')
    logout_button.click()
    print("✅ Logout efetuado com sucesso!")

# Finaliza a automação
driver.quit()
