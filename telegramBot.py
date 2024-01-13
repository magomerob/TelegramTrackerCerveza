from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from addtosheet import addRow

async def cana(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    addRow("Caña")
    await update.message.reply_text(f'Que aproveche, {update.effective_user.first_name}!')

async def litrona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    addRow("Litrona")
    await update.message.reply_text(f'Que aproveche, {update.effective_user.first_name}!')

async def pinta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    addRow("Pinta")
    await update.message.reply_text(f'Que aproveche, {update.effective_user.first_name}!')

async def corto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    addRow("Corto")
    await update.message.reply_text(f'Que aproveche, {update.effective_user.first_name}!')

async def lata(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    addRow("Lata")
    await update.message.reply_text(f'Que aproveche, {update.effective_user.first_name}!')

async def botellin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    addRow("Botellin")
    await update.message.reply_text(f'Que aproveche, {update.effective_user.first_name}!')

def main():
    with open('Clave/telegramApi.txt', 'r') as file:
        TOKEN = file.read().strip()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("cana", cana))
    app.add_handler(CommandHandler("litrona", litrona))
    app.add_handler(CommandHandler("pinta", pinta))
    app.add_handler(CommandHandler("corto", corto))
    app.add_handler(CommandHandler("lata", lata))
    app.add_handler(CommandHandler("botellin", botellin))

    app.add_handler(CommandHandler("help", help))


    app.run_polling()

if __name__ == '__main__':
    main()
