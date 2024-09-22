from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Defina o token do seu bot
TELEGRAM_BOT_TOKEN = '7043396784:AAHXOehN26QhzSlddvzDJ9riyxSNtgjmIaw'
WHATSAPP_NUMBER = '+55085985533178'  # Inclua o código do país

# Função para lidar com o comando /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Fazer Pedido", callback_data='fazer_pedido')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Use 'await' para enviar a mensagem
    await update.message.reply_text('Bem-vindo à nossa loja virtual! O que você gostaria de fazer?', reply_markup=reply_markup)

# Função para lidar com os botões inline
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Use 'await' para chamar a função assíncrona

    if query.data == 'fazer_pedido':
        whatsapp_url = f"https://wa.me/{'+55085985533178' }"
        message = f'Para fazer um pedido, por favor, entre em contato conosco pelo WhatsApp: [Clique aqui]({whatsapp_url})'
        
        # Use 'await' para editar a mensagem com o link do WhatsApp
        await query.edit_message_text(text=message, parse_mode='Markdown')

# Função principal que inicializa o bot
def main() -> None:
    # Crie o Application e passe o token do bot.
    application = Application.builder().token('7043396784:AAHXOehN26QhzSlddvzDJ9riyxSNtgjmIaw').build()

    # Adicione os handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    # Inicie o bot usando run_polling
    application.run_polling()

# Ponto de entrada para executar o bot
if __name__ == '__main__':
    main()

