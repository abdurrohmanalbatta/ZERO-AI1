from ast import parse
import telebot
from test import speech_to_text
from translate import translate_uz
from time import sleep
from text_to_speech import text_to_speech, text_to_speech2
import os
token ="5061846231:AAGgoVVaiNFOxIgXutyQ7dyky5spDUUZBxA"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(chat_id=message.chat.id,text=f"<b>Assalomu alaykum</b> <b>{message.chat.first_name}</b>\n\n🤖AI Intelligence siz bilan!\n\n@thegoldenjet_uzb",parse_mode="HTML")
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    msg = bot.reply_to(message,"<i>Qabul qildim biroz kuting</i>",parse_mode="HTML")
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('new_file.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    tarjima,til = map(str,translate_uz(speech_to_text("new_file.ogg")))
    text_to_speech(tarjima)
    file = open("movie.wav","rb")
    bot.send_voice(message.chat.id,file,caption="🤖@ai_intelligencebot")
    bot.delete_message(message.chat.id, msg.message_id)
    bot.reply_to(message=message,text= f"<i>✅Tarjima tayyor. Marhamat qabul qiling({til})</i>\n\n <b>{tarjima.title()}</b> \n\n<b>🤖@ai_intelligencebot | @thegoldenjet_uzb</b>",parse_mode="html")
    os.remove("new_file.ogg")
    file.close()
@bot.message_handler(content_types=['audio'])
def voice_processing(message):
    msg = bot.reply_to(message,"<i>Qabul qildim biroz kuting</i>",parse_mode="html")
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('new_file.wav', 'wb') as new_file:
        new_file.write(downloaded_file)
    tarjima,til = map(str,translate_uz(speech_to_text("new_file.wav")))
    text_to_speech(tarjima)
    file = open("movie.wav","rb")
    bot.send_voice(message.chat.id,file,caption="🤖@AI_Intelligencebot")
    bot.delete_message(message.chat.id, msg.message_id)
    bot.reply_to(message=message,text= f"<i>✅Tarjima tayyor. Marhamat qabul qiling({til})</i>\n\n <b>{tarjima.title()}</b>\n\n<b>🤖@AI_Intelligencebot | @thegoldenjet_uzb</b>",parse_mode="HTML")
    os.remove("new_file.mp3")
    file.close()
@bot.message_handler(content_types=['text'])
def text_proccesing(message):
    tarjima,til = map(str,translate_uz(message.text))
    msg = bot.reply_to(message,f"<i>✅Tarjima tayyor. Marhamat qabul qiling({til})</i>\n\n<b>{tarjima}</b>\n\n<b>🤖@AI_Intelligencebot | @thegoldenjet_uzb</b>",parse_mode="HTML")
    if til=="en-uz":
        text_to_speech(tarjima)
    elif til=="uz-en":
        text_to_speech2(tarjima)
    sleep(1)
    file = open("movie.wav","rb")
    bot.send_voice(message.chat.id,file,caption="🤖@AI_Intelligencebot",)
    os.remove("movie.wav")
bot.polling()