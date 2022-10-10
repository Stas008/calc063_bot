

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
actions=["+","-","*","/","к","ст"]

def act_str(input_string):
    for item in actions:
        if item in input_string:
            print(item)
            main_act=item
            elems=input_string.split(main_act)
            if item == "+":
                result=int(elems[0])+int(elems[1])
            if item == "-":
                result=int(elems[0])-int(elems[1])
            if item == "*":
                result=int(elems[0])+int(elems[1])
            if item == "/":
                result=int(elems[0])+int(elems[1])
            if item == "к":
                result=pow(int(elems[0]),1/int(elems[1]))
            if item == "ст":
                result=(int(elems[0]) ** int(elems[1]))

    return result

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Для того чтобы узнать погоду введите /weather Город')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    primer=msg[6:]

    await update.message.reply_text(f"результат: {primer}={act_str(primer)}")
    
    
    

    