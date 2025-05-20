# Documentação do Script Selenium

## Visão Geral
Este documento descreve um script Python que utiliza o Selenium WebDriver para automatizar o cadastro, login, configuração de uma interface de rede e logout em uma aplicação web local (`http://localhost:5173/login`). O script simula interações do usuário para testar funcionalidades de autenticação e configuração de rede.

## Objetivo do Script
O script automatiza o seguinte fluxo:
1. Acessa a página de login.
2. Realiza o cadastro de um novo usuário.
3. Faz login com credenciais específicas.
4. Configura uma interface de rede (ex.: Mikrotik com Wireguard), incluindo IP, seleção de interface e parâmetros adicionais.
5. Acessa o perfil e realiza logout.
6. Finaliza fechando o navegador.

## Análise Passo a Passo
### 1. Configuração Inicial
- **Importações**: Inclui `ActionChains` para interações avançadas (ex.: cliques em menus dropdown).
- **WebDriver**: Configura o Chrome com log reduzido (`--log-level=3`).
- **Acesso**: Navega para `http://localhost:5173/login`.

### 2. Processo de Cadastro
- Clica no link `cadastro_link` (ID).
- Preenche os campos:
  - Email: `"novousuario@dominio.com]"` (**Nota**: Contém um erro; corrigir para `"novousuario@dominio.com"`).
  - Nome: `"João"`.
  - Sobrenome: `"Silva"`.
  - Senha e confirmação: `"senhaForte123"`.
- Clica no botão `"Cadastrar"` (XPath).
- Aguarda 3 segundos.

### 3. Processo de Login
- Navega de volta para a página de login.
- Preenche:
  - Email: `"adesanya@teste.com"` (**Nota**: Diferente do cadastro; alinhar se necessário).
  - Senha: `"123123"`.
- Clica no botão `"Entrar"` (XPath).
- Verifica se há mensagem de erro (`error-message`). Se não houver, prossegue.

### 4. Configuração de Interface de Rede
- **IP do Mikrotik**: Insere `"192.168.88.1"` no campo `mikrotikIp`.
- **Botão "Próximo"**: Clica no botão com texto `"Próximo"`.
- **Seleção de Interface**:
  - Usa `ActionChains` para clicar no `<select>` (`selectedInterface`).
  - Seleciona a primeira opção do menu dropdown (`//ul[@role="listbox"]//li[@role="option"]`).
- **Campos de Interface**:
  - `interfaceName`: `"testando interface"`.
  - `interfacePort`: `"testando porta opcional"`.
  - Clica novamente em `"Próximo"`.
- **Campos Wireguard**:
  - `wireguardInterfaceOptional`: `"testando interface"`.
  - `wireguardComment`: `"comentário opcional teste"`.
  - `wireguardIp`: `"10.0.0.1"`.
- **Botão Final**:
  - Clica em `"Próximo"` ou `"Finalizar"` (XPath condicional).

### 5. Processo de Logout
- Localiza o botão `btt_persona` (ID) com espera de 15 segundos.
- Rola a página até o elemento via JavaScript.
- Usa `ActionChains` para clicar no botão de perfil.
- Aguarda 1 segundo e clica no botão `btt_sair` (ID), com fallback via JavaScript.

### 6. Finalização
- Fecha o navegador com `driver.quit()`.
- Exibe: `"✅ Automação finalizada com sucesso!"`.
