# -*- coding: utf-8 -*-
from Tkinter import *
from _winreg import *
import Tkconstants
from tkFileDialog import *
import tkMessageBox
from urllib import *
import os, sys

font = ("Curlz MT", 8, "bold")

userhome = os.path.expanduser('~')

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size



def autosearch(autoway, reg_value):
	aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
	aKey = OpenKey(aReg, autoway,0 ,KEY_READ | KEY_WOW64_64KEY)
	val = QueryValueEx(aKey, reg_value)
	val = str(val)
	CloseKey(aReg)
	line = val.translate(None, "(),u'")
	line = line[:-2]
	#print line
	return line

regtsway = r"SOFTWARE\TeamSpeak 3 Client"
rega3way = r"SOFTWARE\Wow6432Node\bohemia interactive\arma 3"
reg_value_ts = None
reg_value_a3 = "main"


try:
	way_to_a3 = autosearch(rega3way, reg_value_a3)
	print way_to_a3
except:
	print "autoa3path fail"
	
try:
	way_to_ts = autosearch(regtsway, reg_value_ts )
	print way_to_ts
except:
	print "autotspath fail"


way_to_fsd1 = way_to_a3 + "\\@fsd"
way_to_fsd2 = way_to_a3 + "\\fsd"
if os.path.isdir(way_to_fsd1):
	print way_to_fsd1
	way_to_fsd = way_to_fsd1
elif os.path.isdir(way_to_fsd2):
	print way_to_fsd2
	way_to_fsd = way_to_fsd2
else:
	print "notfound"
	tkMessageBox.showinfo('Title','Папка с аддонами FSD не найдена, укажите ее вручную')
	way_to_fsd = askdirectory()
	way_to_fsd = way_to_fsd.replace("/","\\")
	print way_to_fsd

def norm_fucking_path(fuckingpath):
	fuckingpath = fuckingpath.replace("\\","/")
	fuckingpath = os.path.normpath(fuckingpath)
	return fuckingpath
	

def updateall():
	tkMessageBox.showinfo('Title','Закройте тимспик, если он открыт')
	# ОБНОВЛЯЕМ ТИМСПИК
	way_to_addons_plugins = way_to_fsd + "\\TeamSpeak3\\plugins"
	way_to_addons_plugins = norm_fucking_path(way_to_addons_plugins)
	way_to_ts_plugins = way_to_ts + "\\plugins"
	way_to_ts_plugins = norm_fucking_path(way_to_ts_plugins)
	if not (os.path.isdir(way_to_addons_plugins)):
		tkMessageBox.showinfo('Title','Папка с плагинами FSD для тимспика не найдена')
		return
	S = 'S'
	# ОБНОВЛЯЕМ ЮЗЕРКОНФИГ
	way_to_addons_userconfig = way_to_fsd + "\\userconfig"
	way_to_addons_userconfig = norm_fucking_path(way_to_addons_userconfig)
	way_to_arma3 = way_to_a3 + "\\userconfig"
	way_to_arma3 = norm_fucking_path(way_to_arma3)
	if not (os.path.isdir(way_to_addons_userconfig)):
		tkMessageBox.showinfo('Title','Папка с userconfig в папке с аддонами FSD не найдена')
		return
	if not (os.path.isdir(way_to_arma3)):
		os.mkdir(way_to_arma3)
	desktop_update_path = userhome + "\\Desktop\\" + "\\UPDATE_ALL.bat"
	desktop_update_path = norm_fucking_path(desktop_update_path)
	all_installer = open(desktop_update_path, "w")
	all_installer.write('echo "All" | XCOPY "' + way_to_addons_userconfig + '" "' + way_to_arma3 + '" /' + S + '\n') #echo "Y" | XCOPY "E:\VBS\@fsd2\TeamSpeak3\plugins" "E:\VBS\@fsd4\plugins" /S
	all_installer.write('echo "All" | XCOPY "' + way_to_addons_plugins + '" "' + way_to_ts_plugins + '" /' + S)
	all_installer.close()
	os.startfile(desktop_update_path)
	tkMessageBox.showinfo('ВНИМАНИЕ','Windows Не всегда позволяет обновлять файлы, находящтеся на диске C,поэтому на рабочем столе создан файл UPDATE_ALL.bat , запустите его от имени администратора, если обновление через лаунчер не удалось')
	
def start_arma():
	addons_list = []
	ask_site = tkMessageBox.askyesno("Title", "Запросить список аддонов с сайта FSD? ")
	if ask_site == True:
		try:
			url_addons_link = "http://rangertesting.esy.es/urlmodpath.txt"
			for line in urlopen(url_addons_link):
				#print line
				addons_list.append(line)
				addons_list[:] = [line.rstrip('\n') for line in addons_list]
			print addons_list
			#lconfig = open("layncherconfig.txt", "r")
			#lconfigarray = text_file.read().split(',')
		except:
			tkMessageBox.showinfo('Title','Не получилось запросить список аддонов из инета')
			addons_list = [i for i in os.listdir(way_to_fsd) if i.startswith('@') if os.path.isdir(os.path.join(way_to_fsd, i))]
	else:
		addons_list = [i for i in os.listdir(way_to_fsd) if i.startswith('@') if os.path.isdir(os.path.join(way_to_fsd, i))]
	#print addons_list
	modfirst = 'start "" "' + way_to_a3 + r'\\arma3.exe"' + r' -mod="' + way_to_fsd +'\\'
	mod = r'" -mod="' + way_to_fsd +'\\'
	list2 = modfirst + mod.join(addons_list) + '"'
	#list2 = ['-mod=filename\%s' % x for x in addons_list]
	aga = str(list2)
	list3 = aga.translate(None, "()[],u'")
	list4 = norm_fucking_path(list2) + " -nosplash -world=empty -skipIntro"
	print list4
	fo = open("kaka.bat", "w")
	fo.write(list4)
	fo.close()
	arma3_install_path = way_to_a3 + "\\FSD.bat"
	arma3_install_path = norm_fucking_path(arma3_install_path)
	#print arma3_install_path
	fo_arma3 = open(arma3_install_path, "w")
	fo_arma3.write(list4)
	fo_arma3.close()
	#userhome = os.path.expanduser('~')
	desktop_icon_path = userhome + "\\Desktop\\" + "\\FSD.bat"
	desktop_icon_path = norm_fucking_path(desktop_icon_path)
	#print desktop_icon_path
	fo_desktop = open(desktop_icon_path, "w")
	fo_desktop.write(list4)
	fo_desktop.close()
	ask_launch = tkMessageBox.askyesno("Title", "Ярлык создан,  запустить арму с аддонами FSD?")
	if ask_launch == True:
		os.startfile('kaka.bat')
		quit()
	else:
		return
		
		
def diagnos():
	# ДИАГНОСТИКА
	#addons_list_diagnosis = [i for i in os.listdir(way_to_fsd) if i.endswith('.pbo')]
	#print addons_list_diagnosis
	sizelist = []
	silzelist_names = []
	for dirpath, dirnames, filenames in os.walk(way_to_fsd):
		dirnames[:] = [d for d in dirnames if not d.startswith('.')]
		for filename in [f for f in filenames if f.endswith(".pbo")]:
			sizelist.append(dirpath + "\\" + filename)
			silzelist_names.append(filename)
	numberss = [ norm_fucking_path(x) for x in sizelist ]
	#print numberss
	sizelist_new = []
	for i in range(len(numberss)):
		sizelist_new.append(str(silzelist_names[i]) + " size: " + (str(os.path.getsize(numberss[i]))))
	print sizelist_new
	fo_compare = open("addons_list.txt", "w")
	for item in sizelist_new:
		fo_compare.write("%s\n" % item)
	fo_compare.close()
	"""
	ask_d_list = tkMessageBox.askyesno("Title", "ВЫ КАПИТАН ГАЛАКТИКА?, Отвечайте честно, от этого зависит работа диагностической утилиты!")
	if ask_d_list == True:
		fo_compare_admin = open("addons_list_admin.txt", "w")
		for item in sizelist_new:
			fo_compare_admin.write("%s\n" % item)
		fo_compare_admin.close()
	else:
		return
	"""
	try:
		fo_compare_admin_new = open("addons_list_admin.txt", "r")
		sizelist_admin = fo_compare_admin_new.read().split('\n')
		del sizelist_admin[-1]

		subset=set(sizelist_new).difference(sizelist_admin)

		print u"НЕСОВПАДЕНИЕ НАЙДЕНЫ В СЛЕДУЮЩИХ ПАПКАХ " + str(subset)
		if str(subset) == "set([])":
			tkMessageBox.showinfo('Title',u"НЕСОВПАДЕНИЯ НЕ НАЙДЕНЫ")
		else:
			tkMessageBox.showinfo('Title',u"НЕСОВПАДЕНИЕ НАЙДЕНЫ В СЛЕДУЮЩИХ ПАПКАХ " + str(subset))
		fo_compare_admin_new.close()
	except:
		tkMessageBox.showinfo('Title',"Файл со сверочным листом аддонов не найден")
	
	

	
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root = Tk()
root.title("Ranger FSD launcher")
center_window(270, 200)

button4 = Button(root, text="Установить(Обновить) Таскфорс и Userconfig",height=3, command = updateall).grid(rowspan = 1, sticky='nsew', padx = 5, pady = 5)
button5 = Button(root, text="Cоздать Ярлык / Запустить Арму 3",height=3, font = font, command = start_arma).grid(rowspan = 2, sticky='nsew', padx = 5, pady = 5)
button5 = Button(root, text="Диагностика",height=3, command =diagnos).grid(rowspan = 3, sticky='nsew', padx = 5, pady = 5)
root.mainloop()
