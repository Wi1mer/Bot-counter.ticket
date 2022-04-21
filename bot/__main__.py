from time import sleep
import time
import threading
from pyrogram import idle

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
from telegram import ChatAction, message, ParseMode

# from bot import bot, app

from bot import LOGGER, dp, updater, bot
from bot.decorators import is_authorised, is_owner
from bot.config import *
from bot.msg_utils import *

# $ cat zip_cap_dirs.py 
""" Zip 'cap_*' directories. """           
import os                                                                       
import zipfile as zf    

id_owner = OWNER_ID
id_channel = CHANNEL_ID
id_group = GROUP_ID


# @is_owner
def mesgs_hand(update, context): 
    # msg = update.message.text
    if update.message:
        id_received = update.message.chat_id
        id_msg_received=update.message.message_id
        if id_received <= 0:
            Es_grupo = True
            # print("Es grupo")
        else:
            Es_usuario = True
            # print("Es usuario")
        msg_text = update.message.text
        # print("Es grupo o usaurio")

    elif update.channel_post:
        id_received = update.channel_post.chat_id
        id_msg_received=update.channel_post.message_id
        msg_text = update.channel_post.text

        # print("Es canal")
    else:
        print("No es un usuario, grupo o canal")
        
    xvalor = ['100k', '50k', '20k', '10k', '5k', '2k', '1k']
        # print(xvalor[0])

    if(msg_text == "Hi"):
        # context.bot.send_message(
        #    chat_id=id_received,
        #    reply_to_message_id=update.message.message_id,
        #    text="Hello!")
        # this method forwards the message but without adding 'Hey there!'
        reply = sendMessage('Hello!', context.bot, update)
        time.sleep(4)
        editMessage(f'Estas <code>AhI</code>', reply)


    elif(msg_text == "Hello"):
        context.bot.send_message(chat_id=id_received, text="Hey there!"); 
        # this method just replies to the message without forwarding 
        
    elif('/' in msg_text and ' ' in msg_text):
        cantidad = int(msg_text.split(" ")[1])
        
        
        def cantxvalor(total_0, valor_0):
            # Escribir
            x = total_0
            x1 = f'Billetes/{valor_0}.txt'
            f = open (x1,'w') #a
            f.write(str(x))
            # f.write('\n')
            f.close()
            context.bot.send_message(chat_id=id_received, text=f'{valor_0}\n${total_0}'); 
            # print(f'{valorx} x {cantidadx} = {totalx}!')
            
            print(f'{valor_0}\n${total_0}!')
            
        if('all 0' in msg_text):
            time_0 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(time_0)
            context.bot.send_message(chat_id=id_received, text=time_0); 
            for root, dirs, files in sorted(os.walk('.')):
                if 'Billetes' in root:
                    print(f"Compressing: {root}")                                           
                    # Defining .zip name, according to Capítulo.                            
                    cap_dir_zip = '{}.zip'.format(root)                                     
                    # Opening zipfile context for current root dir.                         
                    with zf.ZipFile(cap_dir_zip, 'w', zf.ZIP_DEFLATED) as new_zip:          
                        # Iterating over os.walk list of files for the current root dir.    
                        for f in files:                                                     
                            # Defining relative path to files from current root dir.        
                            f_path = os.path.join(root, f)                                  
                            # Writing the file on the .zip file of the context              
                            new_zip.write(f_path) 
            # def sendLogFile(bot, update: Update):
            with open('Billetes.zip', 'rb') as f:
                bot.send_document(document=f, filename=f.name,
                          reply_to_message_id=update.message.message_id,
                          chat_id=update.message.chat_id)
                    
            for ival in xvalor:
                valor_0 = ival
                total_0 = 0
                cantxvalor(total_0, valor_0)
        
        if('100k' in msg_text):
            valor = 100000
            valor_0 = xvalor[0]
            # valor_0 = '100k'
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
            
        elif('50k' in msg_text):
            valor = 50000
            valor_0 = xvalor[1]
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
        
        elif('20k' in msg_text):
            valor = 20000
            valor_0 = xvalor[2]
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
            
        elif('10k' in msg_text):
            valor = 10000
            valor_0 = xvalor[3]
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
            
        elif('5k' in msg_text):
            valor = 5000
            valor_0 = xvalor[4]
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
            
        elif('2k' in msg_text):
            valor = 2000
            valor_0 = xvalor[5]
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
            
        elif('1k' in msg_text):
            valor = 1000
            valor_0 = xvalor[6]
            total_0 = cantidad*valor
            cantxvalor(total_0, valor_0)
            
    elif('sumar' in msg_text):
        
        
            
        # Leer
        # archivo-entrada.py
        f = open ('Billetes/100k.txt','r')
        total100k = int(f.read())
        # texttt = f'100k = ${total100k}\n'
        # print(f'100k = ${total100k}\n')
        f.close()
        
        f = open ('Billetes/50k.txt','r')
        total50k = int(f.read())
        # texttt = texttt + f'  50k = ${total50k}\n'
        # print(texttt)
        # print(total50k)
        f.close()
        
        f = open ('Billetes/20k.txt','r')
        total20k = int(f.read())
        # texttt = texttt + f'  50k = ${total50k}\n'
        # print(total20k)
        f.close()
        
        f = open ('Billetes/10k.txt','r')
        total10k = int(f.read())
        # print(total10k)
        f.close()
        
        f = open ('Billetes/5k.txt','r')
        total5k = int(f.read())
        # print(total5k)
        f.close()
        
        f = open ('Billetes/2k.txt','r')
        total2k = int(f.read())
        # print(total2k)
        f.close()
        
        f = open ('Billetes/1k.txt','r')
        total1k = int(f.read())
        # print(total1k)
        f.close()
        
        totalf = total100k+total50k+total20k+total10k+total5k+total2k+total1k
        
        texttf = f'Total = ${totalf}\n\n 100k = ${total100k}\n   50k = ${total50k}\n   20k = ${total20k}\n   10k = ${total10k}\n     5k = ${total5k}\n     2k = ${total2k}\n     1k = ${total1k}\n'
        # ----------------------------------------------
        print(f'100k = ${total100k}\n 50k = ${total50k}\n 20k = ${total20k}\n 10k = ${total10k}\n  5k = ${total5k}\n  2k = ${total2k}\n  1k = ${total1k}\n\nTotal = ${totalf}\n')
        # ----------------------
        context.bot.send_message(chat_id=id_received, text=f'{texttf}'); 
        # d = str(totalf)
        # print(d)
        # s = d.split("000")[0]
        # print(s)
        
        # print(totalf)
        
    # elif('reinicar' in msg_text):
    #     x = total_0
    #         x1 = f'Billetes/{valor_0}.txt'
    #         f = open (x1,'w') #a
    #         f.write(str(x))
    #         # f.write('\n')
    #         f.close()
        
        
    elif(msg_text == "Del"):
        message = "Este mensaje se borrara"
        reply_message = sendMessage(message, context.bot, update)
        threading.Thread(target=auto_delete_message, args=(bot, update.message, reply_message)).start()



    else:
        # context.bot.send_message(
        #    chat_id=id_received,
        #    reply_to_message_id=update.message.message_id,
        #    text=update.message.text)
        # print(msg)
        # print("FaLsE")
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        No_problem = True


def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('Bot Escuchando...')
    LOGGER.info("Bot Iniciado!")

    # updater = Updater(token=telegram_token, use_context=True);
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    messages_handler = MessageHandler(Filters.text, mesgs_hand)
    dispatcher.add_handler(messages_handler)

    updater.start_polling()
    
    updater.idle()


# app.start()
main()
idle()

# if __name__ == "__main__":
#     bot()
