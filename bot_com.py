

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pathlib import Path
import action

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Для того чтобы узнать погоду введите /weather Город')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    primer=msg[6:]

    await update.message.reply_text(f"результат: {action.act_str(primer)}")
    
    
    

    