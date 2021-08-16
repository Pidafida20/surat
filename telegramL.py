import telebot
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'aplikasi.settings' 
django.setup()

#from .models import *
from telegram.ext import *
from surat.models import*

api = '1817619498:AAESj3i69z5Q6mcW27GPaYUE1l7GYHsR1_k'
bot = telebot.TeleBot(api)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Selamat Datang Di Aplikasi Layanan Surat')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	#list_penduduk = Penduduk.objects.order_by('-no_kk')
	bot.reply_to(message, 'Informasi Data Layanan Surat')

#@bot.message_handler(commands=['data'])
def isValidPinCode(pinCode):
	regex = "^[1-9]{1}[0-9]{2}\\S{0,1}[0-9]{3}$";
	p = re.compile(regex)
	if (pinCode == ''):
		return False;
	m = re.match(p, pinCode)
	if m is None:
		return False
	else:
		return True

def here(S):
	return any(i.isdigit() for i in S)

def tampildata(update, context):
	text = str(update.message.text).lower()
	
	data_surat = Masyarakat.objects.all()
	message = f""" Total {data_surat.count()} Data """
			
	for data in data_surat:				
				message += f"""Daftar Data Layanan Surat	

							Nama Lengkap = {data.nama_lengkap}																		
							NIK = {data.nik} 
							Jenis Surat = {data.jenis_surat}
							Keterangan = {data.keterangan} 
							catatan = {data.catatan} 							
							No Hp = {data.no_telp} \n \n 

							"""


	update.message.reply_text(f"{message}")	
	return	
	#print(update)
	update.message.reply_text(f"Hi, {update['message']['chat']['first_name']} Informasi Layanan (Surat) Enter NIK")



print('bot Success Running')
print(Surat.objects.first())
#bot.polling()


if __name__== '__main__':
	updater = Updater(api, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(MessageHandler(Filters.text, tampildata))

	updater.start_polling(1.0)
	updater.idle()