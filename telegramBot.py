#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

from addtosheet import addRow

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Caña", callback_data="Caña"),
            InlineKeyboardButton("Litrona", callback_data="Litrona"),
        ],
        [
            InlineKeyboardButton("Pinta", callback_data="Pinta"),
            InlineKeyboardButton("Corto", callback_data="Corto"),
        ],
        [
            InlineKeyboardButton("Lata", callback_data="Lata"),
            InlineKeyboardButton("Botellín", callback_data="Botellín"),
        ],
        
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Que vas a beber?:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    keyboard = [
    [
        InlineKeyboardButton("Caña", callback_data="Caña"),
        InlineKeyboardButton("Litrona", callback_data="Litrona"),
    ],
    [
        InlineKeyboardButton("Pinta", callback_data="Pinta"),
        InlineKeyboardButton("Corto", callback_data="Corto"),
    ],
    [
        InlineKeyboardButton("Lata", callback_data="Lata"),
        InlineKeyboardButton("Botellín", callback_data="Botellín"),
    ],]

    reply_markup = InlineKeyboardMarkup(keyboard)


    await query.edit_message_text(text=f"Que aproveche tu: {query.data}", reply_markup=reply_markup)

    print(f"added {query.data}")
    addRow(str(query.data))
    start(update, context)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""

    with open('Clave/telegramApi.txt', 'r') as file:
        TOKEN = file.read().strip()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()