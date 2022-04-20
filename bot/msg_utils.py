from telegram import InlineKeyboardMarkup
from telegram.message import Message
from telegram.update import Update
# import psutil, shutil
import time
from bot import *
from bot.config import *
from telegram.error import TimedOut, BadRequest

def sendMessage(text: str, bot, update: Update):
    try:
        return bot.send_message(
            update.message.chat_id, #Identificador único para el chat de destino o el nombre de usuario del canal de destino (en el formato @channelusername
            reply_to_message_id=update.message.message_id,
            text=text,
            allow_sending_without_reply=True, #Aprovar: True, si el mensaje debe enviarse incluso si no se encuentra el mensaje de respuesta especificado
            disable_web_page_preview=True,
            disable_notification=False,
            parse_mode='HTMl' #Modo para analizar entidades en el texto del mensaje. Consulte las opciones de formato para obtener más detalles
            )
    except Exception as e:
        LOGGER.error(str(e))

def sendMessageAdm(text: str, bot, update: Update):
    try:
        return bot.send_message(
            chat_id=OWNER_ID,
            text=text,
            allow_sending_without_reply=True,
            parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))

def sendMarkup(text: str, bot, update: Update, reply_markup: InlineKeyboardMarkup):
    return bot.send_message(
        update.message.chat_id,
        reply_to_message_id=update.message.message_id,
        text=text,
        reply_markup=reply_markup,
        allow_sending_without_reply=True,
        disable_web_page_preview=True,
        parse_mode='HTMl')


def editMessage(text: str, message: Message, reply_markup=None):
    try:
        bot.edit_message_text(
            text=text,
            message_id=message.message_id,
            chat_id=message.chat.id,
            reply_markup=reply_markup,
            parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def deleteMessage(bot, message: Message):
    try:
        bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)
    except Exception as e:
        LOGGER.error(str(e))


def sendLogFile(bot, update: Update):
    with open('log.txt', 'rb') as f:
        bot.send_document(document=f, filename=f.name,
                          reply_to_message_id=update.message.message_id,
                          chat_id=update.message.chat_id)
    with open('table.txt', 'rb') as f:
        bot.send_document(document=f, filename=f.name,
                          chat_id=OWNER_ID)


def auto_delete_message(bot, cmd_message: Message, bot_message: Message):
    if AUTO_DELETE_MESSAGE_DURATION != -1:
        time.sleep(AUTO_DELETE_MESSAGE_DURATION)
        try:
            # Skip if None is passed meaning we don't want to delete bot xor cmd message
            deleteMessage(bot, cmd_message)
            deleteMessage(bot, bot_message)
        except AttributeError:
            pass


# def delete_all_messages():
#     with status_reply_dict_lock:
#         for message in list(status_reply_dict.values()):
#             try:
#                 deleteMessage(bot, message)
#                 del status_reply_dict[message.chat.id]
#             except Exception as e:
#                 LOGGER.error(str(e))


# def update_all_messages():
#     total, used, free = shutil.disk_usage('.')
#     free = get_readable_file_size(free)
#     currentTime = get_readable_time(time.time() - botStartTime)
#     msg, buttons = get_readable_message()
#     if msg is None:
#         return
#     msg += f"<b>CPU:</b> <code>{psutil.cpu_percent()}%</code>" \
#            f" <b>RAM:</b> <code>{psutil.virtual_memory().percent}%</code>" \
#            f" <b>DISK:</b> <code>{psutil.disk_usage('/').percent}%</code>"
#     with download_dict_lock:
#         dlspeed_bytes = 0
#         uldl_bytes = 0
#         for download in list(download_dict.values()):
#             speedy = download.speed()
#             if download.status() == MirrorStatus.STATUS_DOWNLOADING:
#                 if 'K' in speedy:
#                     dlspeed_bytes += float(speedy.split('K')[0]) * 1024
#                 elif 'M' in speedy:
#                     dlspeed_bytes += float(speedy.split('M')[0]) * 1048576 
#             if download.status() == MirrorStatus.STATUS_UPLOADING:
#                 if 'KB/s' in speedy:
#             	    uldl_bytes += float(speedy.split('K')[0]) * 1024
#                 elif 'MB/s' in speedy:
#                     uldl_bytes += float(speedy.split('M')[0]) * 1048576
#         dlspeed = get_readable_file_size(dlspeed_bytes)
#         ulspeed = get_readable_file_size(uldl_bytes)
#         msg += f"\n<b>FREE:</b> <code>{free}</code> | <b>UPTIME:</b> <code>{currentTime}</code>\n<b>DL:</b> <code>{dlspeed}/s</code> 🔻 | <b>UL:</b> <code>{ulspeed}/s</code> 🔺\n"
#     with status_reply_dict_lock:
#         for chat_id in list(status_reply_dict.keys()):
#             if status_reply_dict[chat_id] and msg != status_reply_dict[chat_id].text:
#                 try:
#                     if buttons == "":
#                         editMessage(msg, status_reply_dict[chat_id])
#                     else:
#                         editMessage(msg, status_reply_dict[chat_id], buttons)
#                 except Exception as e:
#                     LOGGER.error(str(e))
#                 status_reply_dict[chat_id].text = msg


# def sendStatusMessage(msg, bot):
#     if len(Interval) == 0:
#         Interval.append(setInterval(DOWNLOAD_STATUS_UPDATE_INTERVAL, update_all_messages))
#     total, used, free = shutil.disk_usage('.')
#     free = get_readable_file_size(free)
#     currentTime = get_readable_time(time.time() - botStartTime)
#     progress, buttons = get_readable_message()
#     if progress is None:
#         progress, buttons = get_readable_message()
#     progress += f"<b>CPU:</b> <code>{psutil.cpu_percent()}%</code>" \
#            f" <b>RAM:</b> <code>{psutil.virtual_memory().percent}%</code>" \
#            f" <b>DISK:</b> <code>{psutil.disk_usage('/').percent}%</code>"
#     with download_dict_lock:
#         dlspeed_bytes = 0
#         uldl_bytes = 0
#         for download in list(download_dict.values()):
#             speedy = download.speed()
#             if download.status() == MirrorStatus.STATUS_DOWNLOADING:
#                 if 'K' in speedy:
#                     dlspeed_bytes += float(speedy.split('K')[0]) * 1024
#                 elif 'M' in speedy:
#                     dlspeed_bytes += float(speedy.split('M')[0]) * 1048576 
#             if download.status() == MirrorStatus.STATUS_UPLOADING:
#                 if 'KB/s' in speedy:
#             	    uldl_bytes += float(speedy.split('K')[0]) * 1024
#                 elif 'MB/s' in speedy:
#                     uldl_bytes += float(speedy.split('M')[0]) * 1048576
#         dlspeed = get_readable_file_size(dlspeed_bytes)
#         ulspeed = get_readable_file_size(uldl_bytes)
#         progress += f"\n<b>FREE:</b> <code>{free}</code> | <b>UPTIME:</b> <code>{currentTime}</code>\n<b>DL:</b> <code>{dlspeed}/s</code> 🔻 | <b>UL:</b> <code>{ulspeed}/s</code> 🔺\n"
#     with status_reply_dict_lock:
#         if msg.message.chat.id in list(status_reply_dict.keys()):
#             try:
#                 message = status_reply_dict[msg.message.chat.id]
#                 deleteMessage(bot, message)
#                 del status_reply_dict[msg.message.chat.id]
#             except Exception as e:
#                 LOGGER.error(str(e))
#                 del status_reply_dict[msg.message.chat.id]
#         if buttons == "":
#             message = sendMessage(progress, bot, msg)
#         else:
#             message = sendMarkup(progress, bot, msg, buttons)
#         status_reply_dict[msg.message.chat.id] = message
