from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

print('telegram')

def start(update,context):
    user = update.message.from_user
    user = update.message.chat_id
    try:filee = open('list_Telegram_Id.txt').readlines()
    except:filee= [None]
    if str(user)+'\n' not in filee:
            with open('list_Telegram_Id.txt','a')as listTele:
                listTele.write(str(update.message.chat_id)+'\n')
            update.message.reply_text('مرحبا تم اضافتك وسيتم ارسال الاذكار قريبا')
    else:
        update.message.reply_text('مرحبا تم اضافتك مسبقا')
update = Updater(here your token bot)
update.dispatcher.add_handler(CommandHandler('startA',start))
update.start_polling()