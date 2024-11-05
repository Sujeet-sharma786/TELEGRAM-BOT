from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from nltk.chat.util import Chat, reflections
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your new Telegram bot. How can I help you?")

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm doing fine, thank you!", "Great! How can I help you?"]],
    ["what is your name?", ["I'm your chatbot!", "They call me Chatbot."]],
    ["bye|exit", ["Goodbye!", "Have a nice day!"]],
]
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can ask below mentioned dialogues, or let me know new one...")
    for i in pairs:
        await update.message.reply_text(i[0])


chatbot = Chat(pairs,reflections)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    response = chatbot.respond(text)
    await update.message.reply_text(response)

async def send_message_to_user(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hello,this is my bot!")
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("send_message",send_message_to_user))
    
   
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
  
    
  
    app.run_polling()

if __name__ == '__main__':
    main()
