from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
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
email_input.send_keys("novousuario@dominio.com]")

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
email_input.send_keys("adesanya@teste.com")

password_input = driver.find_element(By.XPATH, '//input[@type="password" and @placeholder="••••••••"]')
password_input.send_keys("123123")

# Clica no botão de login
login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Entrar")]')
login_button.click()

# Verifica se houve erro no login
try:
    error_message = driver.find_element(By.CLASS_NAME, "error-message")
    print("❌ Falha no login: " + error_message.text)
    driver.quit()
    exit()
except NoSuchElementException:
    print("✅ Login efetuado com sucesso!")

# Aguarda o campo de IP e insere o valor
try:
    mikrotik_ip_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mikrotikIp"))
    )
    mikrotik_ip_input.clear()
    mikrotik_ip_input.send_keys("192.168.88.1")
    print("✅ IP inserido com sucesso!")
except:
    driver.quit()
    exit()

# Aguarda e clica no botão "Próximo"
try:
    proximo_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Próximo")]'))
    )
    proximo_button.click()
    print("✅ Botão 'Próximo' clicado com sucesso!")
except:
    print("❌ Não foi possível clicar no botão 'Próximo'.")
    driver.quit()
    exit()

time.sleep(2) 



try:
    # Espera o elemento select pelo ID
    select_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "selectedInterface"))
    )
    print("✔️ Campo select encontrado, tentando clicar...")

    # Usa ActionChains para clicar no campo do select
    actions = ActionChains(driver)
    actions.move_to_element(select_field).click().perform()
    print("✔️ Clique no select realizado.")

    # Espera o menu das opções aparecer
    menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//ul[@role="listbox"]'))
    )
    print("✔️ Menu das opções está visível.")

    # Seleciona a primeira opção do menu
    first_option = menu.find_element(By.XPATH, './/li[@role="option"]')
    print(f"✔️ Encontrada opção: {first_option.text}, tentando clicar...")

    # Clica na opção
    actions.move_to_element(first_option).click().perform()
    print("✅ Interface selecionada com sucesso!")

except Exception as e:
    import traceback
    print(f"❌ Não foi possível selecionar a interface: {e}")
    traceback.print_exc()

try:
    proximo_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Próximo")]'))
    )
    proximo_button.click()
    print("✅ Botão 'Próximo' clicado com sucesso!")
except:
    print("❌ Não foi possível clicar no botão 'Próximo'.")
    driver.quit()
    exit()



# Pequeno delay para garantir que o select já foi processado
time.sleep(1)

try:
    # Preenche o campo interfaceName
    interface_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "interfaceName"))
    )
    interface_name_input.clear()
    interface_name_input.send_keys("testando interface")
    print("✅ Campo interfaceName preenchido.")

    # Preenche o campo interfacePort
    interface_port_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "interfacePort"))
    )
    interface_port_input.clear()
    interface_port_input.send_keys("testando porta opcional")
    print("✅ Campo interfacePort preenchido.")

    # Clica no botão "Próximo" novamente
    proximo_button_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Próximo")]'))
    )
    proximo_button_2.click()
    print("✅ terceiro botão 'Próximo' clicado com sucesso!")

except Exception as e:
    print(f"❌ Erro ao preencher campos ou clicar em 'Próximo': {e}")

try:
    # Preenche o campo wireguardInterfaceOptional
    wireguard_interface_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wireguardInterfaceOptional"))
    )
    wireguard_interface_input.clear()
    wireguard_interface_input.send_keys("testando interface")
    print("✅ Campo wireguardInterfaceOptional preenchido.")

    # Preenche o campo wireguardComment
    wireguard_comment_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wireguardComment"))
    )
    wireguard_comment_input.clear()
    wireguard_comment_input.send_keys("comentário opcional teste")
    print("✅ Campo wireguardComment preenchido.")

    # Preenche o campo wireguardIp
    wireguard_ip_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wireguardIp"))
    )
    wireguard_ip_input.clear()
    wireguard_ip_input.send_keys("10.0.0.1")
    print("✅ Campo wireguardIp preenchido.")

except Exception as e:
    print(f"❌ Erro ao preencher campos wireguard: {e}")

try:
    next_or_finish_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, '//button[contains(text(), "Próximo") or contains(text(), "Finalizar")]'
        ))
    )
    next_or_finish_button.click()
    print("✅ Botão 'Próximo' ou 'Finalizar' clicado com sucesso!")
except Exception as e:
    print(f"❌ Não foi possível clicar no botão 'Próximo' ou 'Finalizar': {e}")
   
   
   # === LOGOUT ===

try:
    # Clica no botão de perfil - usando espera explícita e ActionChains para garantir
    profile_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'btt_persona'))
    )
    
    # Rolando a página para o elemento (se necessário)
    driver.execute_script("arguments[0].scrollIntoView();", profile_button)
    
    # Usando ActionChains para mover e clicar
    ActionChains(driver).move_to_element(profile_button).pause(0.5).click().perform()
    print("✅ Clique no botão de perfil efetuado com sucesso!")
    
    # Espera um pouco para o menu abrir
    time.sleep(1)  # Pode tentar reduzir esse tempo ou usar espera explícita
    
    # Localiza o botão de logout - verifique se o ID está correto
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btt_sair'))
    )
    
    # Clica usando JavaScript como fallback
    try:
        logout_button.click()
    except:
        driver.execute_script("arguments[0].click();", logout_button)
    
    print("✅ Logout efetuado com sucesso!")
    
except Exception as e:
    print(f"❌ Erro ao tentar fazer logout: {e}")
    driver.quit()
    exit()
# Fecha o navegador
driver.quit()
print("✅ Automação finalizada com sucesso!")