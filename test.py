from tkinter.filedialog import askdirectory
import os
import os.path
from PIL import Image
import pytesseract
import csv
import re
import pdb
#import tkinter as tk
#from tkinter import filedialog
#root = tk.Tk()
#root.withdraw()
#file_path = filedialog.askopenfilenames()
print('Please input the floder with all raw pictures...')
Dpath = askdirectory()
Dresult = Dpath + '/Result'
Dcsv = Dresult + '/result.csv'
if not(os.path.exists(Dresult)):
	os.mkdir(Dresult)
DQRCode = Dresult+ '/QRCode'
if not(os.path.exists(DQRCode)):
	os.mkdir(DQRCode)
DOrderNum = Dresult+'/OrderNum'
if not(os.path.exists(DOrderNum)):
	os.mkdir(DOrderNum)
DAssistantCode = Dresult+ '/AssistantCode'
if not(os.path.exists(DAssistantCode)):
	os.mkdir(DAssistantCode)
DWeChatCode = Dresult+'/WeChatCode'
if not(os.path.exists(DWeChatCode)):
	os.mkdir(DWeChatCode)

files = os.listdir(Dpath)
index = 0
Hander_row = ['Index','OrderNum','AssistantCode','WechatCode']
with open (Dcsv,'w',newline = '') as f:
	writer = csv.writer(f)
	writer.writerow(Hander_row)
print('The Code is working, please witing..')
for file in files:
	if '.jpg' in file:
		index = index+1;
		temp_arr=[]
		temp_arr.append(index)
		pic_path = Dpath + '/' + file;
		Raw_img = Image.open(pic_path)
		# Crop QRCode
		QR_img = Raw_img.crop((0,164,1080,1436))
		QR_dir = DQRCode + '/' + str(index) + '.jpg'
		QR_img.save(QR_dir)
		# Crop Order Number
		OrderNum_img = Raw_img.crop((391,1252,760,1302))
		OrderNum_dir = DOrderNum + '/' + str(index) + '.jpg'
		Temp_text = pytesseract.image_to_string(OrderNum_img,lang='eng')
		text_used = Temp_text.replace(" ","")
		#text_used= text_used.encode("utf8")
		#print(text_used)
		text_used = 'M'+text_used 
		temp_arr.append(text_used)
		# pdb.set_trace()
		OrderNum_img.save(OrderNum_dir)
		# Crop Assistant Code
		AssistantCode_img = Raw_img.crop((391,1302,578,1355))
		AssistantCode_dir = DAssistantCode + '/' + str(index) + '.jpg'
		Temp_text = pytesseract.image_to_string(AssistantCode_img,lang='eng')
		text_used = Temp_text.replace(" ","")
		temp_arr.append(text_used)
		AssistantCode_img.save(AssistantCode_dir)
		# Crop WeChat Code
		WeChatCode_img = Raw_img.crop((225,1734,616,1784))
		WeChatCode_dir = DWeChatCode + '/' + str(index) + '.jpg'
		Temp_text = pytesseract.image_to_string(WeChatCode_img,lang='eng')
		text_used = Temp_text.replace(" ","")
		temp_arr.append(text_used)
		WeChatCode_img.save(WeChatCode_dir)
		with open (Dcsv,'a',newline = '') as f:
			writer = csv.writer(f)
			writer.writerow(temp_arr)

