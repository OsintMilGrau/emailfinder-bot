<h1 align="center">
  <b>Emailfinder Bot</b>
  <br>
</h1>
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square&logo=python"> 
  </a>
  <a href="https://github.com/OsintMilGrau/emailfinder-bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg?style=square&logo=mit">
  </a>
  <a href="https://github.com/OsintMilGrau">
    <img src="https://img.shields.io/badge/author-@OsintMilGrau-orange.svg?style=square&logo=github">
  </a>
</p>

<p align="center">
O Emailfinder Bot é uma ferramenta para buscar emails associados a um domínio, focado em testes de OSINT. Ele processa os resultados de forma eficiente e envia os emails encontrados diretamente no chat do Discord.
</p>
<br/>
<p align="center">
  <img src="https://github.com/user-attachments/assets/9ee2d0f9-c944-4a13-a1df-553a2ca8c080" alt="emailfinder" width="300">
</p>


<a href="https://discord.gg/dQ4sbCHPbK">
  <img src="https://img.shields.io/badge/Discord-OSINTMILGRAU-blue">
</a>

O **Emailfinder Bot** é uma ferramenta desenvolvida para testes de OSINT, focada na busca de endereços de email associados a um domínio. Utilizando o bot no Discord, você pode rapidamente extrair emails e receber os resultados diretamente no chat, com uma interface fácil e rápida de usar.

## Funcionalidades

- **Busca de emails relacionados a um domínio**: Forneça um domínio, e o bot executa uma busca por emails associados.
- **Filtragem de emails inválidos**: Emails indesejados, como aqueles com caracteres não usuais, são automaticamente filtrados.
- **Envio de resultados extensos em arquivo**: Caso o número de emails seja grande, o bot envia um arquivo `.txt` com todos os resultados para evitar ultrapassar o limite de caracteres do Discord.
- **Simulação de barra de carregamento**: O bot apresenta uma barra de carregamento enquanto processa a busca, mantendo o usuário informado sobre o progresso.

## Comandos

### `/emailfinder [domínio]`
Realiza a busca de emails associados ao domínio fornecido.

**Exemplo:**
### /emailfinder `fbi.gov`

![image](https://github.com/user-attachments/assets/a6875a97-9dd0-4e34-937f-484467038441)

### `/ajuda` Mostra as instruções de uso do bot.
![image](https://github.com/user-attachments/assets/00a2a916-e643-4a9f-bf8a-11156a29f654)

## Requisitos

- Python 3.8+
- Ferramenta [emailfinder](https://github.com/Josue87/EmailFinder) instalada e configurada no seu sistema (necessária para realizar as buscas).
- Bibliotecas Python necessárias:
  - `discord.py`
  - `asyncio`

## Como Instalar

1. Clone este repositório:

  
   - `git clone https://github.com/OsintMilGrau/emailfinder-bot.git`
   - `cd emailfinder-bot`
   - `pip3 install -r requirements.txt`
   - Substitua `SEU_TOKEN_AQUI` no arquivo `emailfinder-bot.py` pelo token do seu bot do Discord.
   - `python3 emailfinder-bot.py`

- Além de instalar o `requirements.txt`, o usuário deve garantir que a ferramenta **emailfinder** esteja instalada e disponível no sistema.
