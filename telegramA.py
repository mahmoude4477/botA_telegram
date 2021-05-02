from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

print('telegram')

def start(update,context):
    user = update.message.from_user
    user = update.message.chat_id
    try:filee = open('list_Telegram_Id.txt').readlines()
    except:filee= [None]
    if str(user)+'\n' not in filee:#str(user['id'])+'\n' not in filee:
            with open('list_Telegram_Id.txt','a')as listTele:
                listTele.write(str(update.message.chat_id)+'\n')
            update.message.reply_text('مرحبا تم اضافتك وسيتم ارسال الاذكار قريبا')
    else:
        update.message.reply_text('مرحبا تم اضافتك مسبقا')
update = Updater('1630827457:AAHxyYsnRfUIM7XMcU3cvV8_EkE6pB2mWi8')
update.dispatcher.add_handler(CommandHandler('startA',start))
update.start_polling()