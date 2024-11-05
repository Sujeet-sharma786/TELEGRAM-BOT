from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from nltk.chat.util import Chat, reflections
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


tasks = ["I will take a small session for calming yourself and mind and then I'll move forward so just write /done",
'I am going to provide an audio clip for 1 min please try to listen it by sitting comfortably and back staright.Then write /done',
'send_audio_file','now just feel relaxed by releasing your body free and sit in asaan as i have provided in below image','send_aasan_image',
'Now inahale and exhale for 2-3 min and after each inhale and exhale just hold your breath for some seconds...,after competion write /done',
'i hope now you are feeling better a bit now we will move fwd']



global index
index = 0
async def calming_session(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if tasks[index]=='send_audio_file':
        audio_file_path = './song.mp3'
        with open(audio_file_path,'rb') as audio:
            await context.bot.send_audio(chat_id=update.effective_chat.id,audio=audio)
            
        await context.bot.send_message("write done")

        index+=1
        

    elif tasks[index]=='send_aasan_image':
        image_path = './aasan.jpg'
        with open(image_path,'rb') as image:
            await context.bot.send_photo(update.effective_chat.id,photo=image)


    else:
        await context.bot.send_message(tasks[index])
        index+=1
        if index==len(tasks)-1:
            index==0






async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello sir/mam😀")
    await update.message.reply_text("i'll provide some task after each step just write /done...")
    await update.message.reply_text('So, just start this session by writting /done...')

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
    app.add_handler(CommandHandler("done",calming_session))
    
   
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
  
    
  
    app.run_polling()

if __name__ == '__main__':
    main()
