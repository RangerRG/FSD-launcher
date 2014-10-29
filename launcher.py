# -*- coding: utf-8 -*-
from Tkinter import *
import Tkconstants
from tkFileDialog import *
import tkMessageBox
import os, sys

font = ("Curlz MT", 12, "bold")

try:
	lconfig = open("layncherconfig.txt", "r")
	#lconfigarray = text_file.read().split(',')
	lconfigarray = lconfig.read().split(',')
	#print "uspeshno prochitan"
	#print lconfigarray
	#lconfigarray = eval(lconfigarray)
	#global fsdpath
	#global tspath
	#global a3path
except:
	firstarr = "Ваша папка с аддонами FSD,Ваша папка с Тимспиком,Ваша папка с Армой"
	lconfigarray = firstarr.split(',')
	lconfig = open("layncherconfig.txt", "w")
	lconfig.write(firstarr)
	print "fail"

#print lconfigarray
#lconfig.close()
fsdpath = lconfigarray[0]
tspath = lconfigarray[1]
a3path = lconfigarray[2]
lconfig.close()

def searchfsd():
    # Get the file
	global fsdpath
	fsdpath = askdirectory()
	if fsdpath == "":
		tkMessageBox.showinfo('Title','Вы не указали папку с аддонами')
		fsdpath = ""
		return None
	var1.set(fsdpath) 
	lconfigarray[0] = str(fsdpath)
	#print lconfigarray[0]
	gogo = str(",".join(lconfigarray))
	#print gogo
	lconfig = open("layncherconfig.txt", "w") 
	lconfig.write(gogo)
	lconfig.close()
	root.update()





def searchteamspeak():
    # Get the file
	global tspath
	tspath = askdirectory()
	teamspeakpath = tspath + '/ts3client_win64.exe'
	teamspeakpath2 = tspath + '/ts3client_win32.exe'
	#print teamspeakpath2
	if not (os.path.exists(teamspeakpath) or os.path.exists(teamspeakpath2)):
		tkMessageBox.showinfo('Title','Вы указали неверную папку')
		tspath = ""
		return None
	var2.set(tspath)
	lconfigarray[1] = str(tspath)
	#print lconfigarray[0]
	gogo = str(",".join(lconfigarray))
	#print gogo
	lconfig = open("layncherconfig.txt", "w") 
	lconfig.write(gogo)
	lconfig.close()
	root.update()

	
def searcharma3():
	global a3path
    # Get the file
	a3path = askdirectory()
	arma3exepath = a3path + '/arma3.exe'
	#print arma3exepath
	if not os.path.exists(arma3exepath):
		tkMessageBox.showinfo('Title','Вы указали неверную папку')
		a3path = ""
		return None
	var3.set(a3path)
	lconfigarray[2] = str(a3path)
	#print lconfigarray[0]
	gogo = str(",".join(lconfigarray))
	#print gogo
	lconfig = open("layncherconfig.txt", "w") 
	lconfig.write(gogo)
	lconfig.close()
	root.update()

def updatetf():
	# ОБНОВЛЯЕМ ТИМСПИК
	try: 
		tfpath = tspath
	except:
		tkMessageBox.showinfo('Title','Укажите сначала папку с тимспиком')
		return None
	plugpath = lconfigarray[0] + '/TeamSpeak3/plugins'
	print plugpath
	plugpathbat = plugpath.replace("/","\\") 
	print plugpathbat
	installpath = lconfigarray[1] + '/plugins'
	installpathbat = installpath.replace("/","\\")
	fots = open("tfupdtae.bat", "w")
	S = 'S'
	fots.write('echo "All" | XCOPY "' + plugpathbat + '" "' + installpathbat + '" /' + S) #echo "Y" | XCOPY "E:\VBS\@fsd2\TeamSpeak3\plugins" "E:\VBS\@fsd4\plugins" /S
	fots.close()
	os.startfile('tfupdtae.bat')
	# ОБНОВЛЯЕМ ЮЗЕРКОНФИГ
	print "nachalo"
	userconfigpathfrom = lconfigarray[0] + '/userconfig'
	userconfigpathto = lconfigarray[2] + '/userconfig'
	if not (os.path.exists(userconfigpathto)):
		os.mkdir(userconfigpathto)
	userconfigpathfrombat = userconfigpathfrom.replace("/","\\")
	userconfigpathfromto = userconfigpathto.replace("/","\\")
	print "epered otkr"
	fouc = open("userconinst.bat", "w")
	S = 'S'
	fouc.write('echo "All" | XCOPY "' + userconfigpathfrombat + '" "' + userconfigpathfromto + '" /' + S) #echo "Y" | XCOPY "E:\VBS\@fsd2\TeamSpeak3\plugins" "E:\VBS\@fsd4\plugins" /S
	fouc.close()
	os.startfile('userconinst.bat')
	
		
	
def start_arma():
	path_f = []
	# filename = str(filename)
	# os.path.normpath(filename)
	try:
		cc = fsdpath
	except:
		tkMessageBox.showinfo('Title','Вы не указали папку с аддонами')
		return None
	try:
		ccb = a3path
	except:
		tkMessageBox.showinfo('Title','Вы не указали папку c Армой')
		return None
	cc = fsdpath.replace("/","\\") 
	ccb = a3path.replace("/","\\") 
	filename = cc
	arma3filename = '"' + ccb + r'\arma3.exe' + '"'
	print arma3filename
	# path = os.path.join(a, filename)
	dirs = os.listdir(filename)
	for file in dirs:
		print file
		path_f.append(file)

	path_f2 = [i for i in range(len(path_f)) if path_f[i].startswith('@')]

	#print path_f2

	T = []
	for i in path_f2:
		T.append(path_f[i])

	mod = r'" -mod="' + filename +'\\'
	modfirst = r' -mod="' + filename +'\\'
	#list2 = ['-mod=filename\%s' % x for x in T]
	#print (list2)
	modlist = mod.join(T) + '"'
	#print T
	#print modlist
	modlist = modfirst + modlist
	arma3final = a3path + '/arma3.bat'
	# arma3final
	# arma3fibalbat = a3path.replace("/","\\")
	fo = open(arma3final, "w")
	fo.write('start "" ' + arma3filename + modlist)
	path = []
	path_f = []
	path_f2 = []
	root.update()
	tkMessageBox.showinfo('Title','Ярлык успешно создан')




	
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root = Tk()
center_window(350, 200)
root.columnconfigure(0,weight=1000)
root.columnconfigure(1,weight=1000)
#root.geometry("300x150")
var1 = StringVar()
try: 
	var1.set(fsdpath)
except:
	var1.set('Ваша папка с аддонами FSD:')
var2 = StringVar()
try: 
	var2.set(tspath)
except:
	var2.set('Ваша папка с Тимспиком:')
var3 = StringVar()
try: 
	var3.set(a3path)
except:
	var3.set('Ваша папка с Армой 3:')
#globalfsd = StringVar()
theLabel1 = Label(root, textvariable=var1, bg = 'grey').grid(row=0,column=0, padx = 1, pady = 2)
button1 = Button(root, text="Указать папку", command = searchfsd).grid(row=0,column=1, padx = 1, pady = 2)

theLabel2 = Label(root, textvariable=var2, bg = 'grey').grid(row=1,column=0, padx = 1, pady = 2)
button2 = Button(root, text="Указать папку", command = searchteamspeak).grid(row=1,column=1, padx = 1, pady = 2)

theLabel3 = Label(root, textvariable=var3, bg = 'grey').grid(row=2,column=0, padx = 1, pady = 2)
button3 = Button(root, text="Указать папку", command = searcharma3).grid(row=2,column=1, padx = 1, pady = 2)

button4 = Button(root, text="Установить(Обновить) Таскфорс и Userconfig",height=2, command = updatetf).grid(rowspan = 2, columnspan = 2, sticky='nsew', padx = 5, pady = 5)
button5 = Button(root, text="Cоздать Ярлык / Запустить Арму 3",height=2,font=font, command = start_arma).grid(rowspan = 2, columnspan = 2, sticky='nsew', padx = 5, pady = 0)






root.mainloop()
