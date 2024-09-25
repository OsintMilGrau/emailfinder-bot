import discord
import subprocess
import re
import asyncio
import io

# Define os intents do bot
intents = discord.Intents.default()
intents.message_content = True

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        self.is_processing = False

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()

# Comando de ajuda
@bot.tree.command(name="ajuda", description="Mostra as instruções de uso do bot")
async def ajuda(interaction: discord.Interaction):
    help_text = """
    **📘 Bot Emailfinder By OSINTMILGRAU - Help**

    **Comandos disponíveis:**

    1. **`/emailfinder [domínio]`**
       - **Descrição**: Realiza uma busca de emails associados ao domínio fornecido.
       - **Exemplo**: `/emailfinder exemple.com`

    **Observações importantes:**
    - Caso o número de emails encontrados seja muito grande, eles serão enviados como um arquivo para evitar problemas de limite de caracteres.
    - O bot pode demorar alguns segundos para processar a busca, dependendo do tamanho do domínio e da quantidade de emails encontrados.
    """
    await interaction.response.send_message(help_text, ephemeral=True)

# Função para filtrar os emails indesejados
def filter_emails(email_list):
    return [email for email in email_list if not (email.startswith('u0027@') or email.startswith('22@'))]

async def loading_bar(interaction):
    stages = [
        "🔄 Buscando emails [▒▒▒▒▒▒▒▒▒▒] 0%",
        "🔄 Buscando emails [█▒▒▒▒▒▒▒▒▒] 10%",
        "🔄 Buscando emails [██▒▒▒▒▒▒▒▒] 20%",
        "🔄 Buscando emails [███▒▒▒▒▒▒▒] 30%",
        "🔄 Buscando emails [████▒▒▒▒▒▒] 40%",
        "🔄 Buscando emails [█████▒▒▒▒▒] 50%",
        "🔄 Buscando emails [██████▒▒▒▒] 60%",
        "🔄 Buscando emails [███████▒▒▒] 70%",
        "🔄 Buscando emails [████████▒▒] 80%",
        "🔄 Buscando emails [█████████▒] 90%",
        "🔄 Buscando emails [██████████] 100%",
    ]
    for stage in stages:
        await interaction.edit_original_response(content=stage)
        await asyncio.sleep(1)

# Comando principal /emailfinder
@bot.tree.command(name="emailfinder", description="Realiza busca de emails associados a um domínio")
async def emailfinder(interaction: discord.Interaction, domain: str):
    if bot.is_processing:
        await interaction.response.send_message("O bot está processando um comando. Por favor, aguarde.", ephemeral=True)
        return

    bot.is_processing = True  # Ativa o bloqueio

    try:
        await interaction.response.defer()
        await loading_bar(interaction)

        # Executa o comando emailfinder e captura o resultado
        result = subprocess.run(['emailfinder', '-d', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', result.stdout)
            filtered_emails = filter_emails(emails)

            if filtered_emails:
                total_emails = len(filtered_emails)
                email_list_message = '\n'.join(filtered_emails)
                final_message = f'**Total de emails encontrados (filtrados): {total_emails}**'

                if len(email_list_message) > 2000:
                    file = io.StringIO(email_list_message)
                    await interaction.edit_original_response(content=f'{final_message}\nOs emails foram enviados em um arquivo.', allowed_mentions=discord.AllowedMentions.none())
                    await interaction.followup.send(file=discord.File(file, filename='emails.txt'))
                else:
                    await interaction.edit_original_response(content=f'{final_message}\n{email_list_message}')
            else:
                await interaction.edit_original_response(content='Nenhum email válido encontrado.')
        else:
            await interaction.edit_original_response(content=f'Erro ao executar a busca: {result.stderr}')
    
    except Exception as e:
        await interaction.edit_original_response(content=f'Ocorreu um erro ao executar a busca: {str(e)}')

    finally:
        await interaction.followup.send(f"Resultados da busca para o domínio `{domain}`.", allowed_mentions=discord.AllowedMentions(users=True))  # Menciona o usuário
        bot.is_processing = False

# Insira o token do bot aqui
bot.run('SEU_TOKEN_AQUI')
