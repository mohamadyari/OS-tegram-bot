import telebot
from telebot import types
import os
import random
from PIL import ImageGrab
from winsound import Beep
from datetime import datetime
import webbrowser
import sys


class data:
    today = datetime.now()
    nowtime = today.strftime("%H%M%S")
    runtime = nowtime
    user_want_to_restart = 0
    user_want_to_shutdown = 0


os.system("cls")
print("Bot is ready !")
print("\n")
#---------------#
TOKEN = "your token"
bot = telebot.TeleBot(TOKEN)
#---------------#


def getfile(filename):
    myfile = open(filename, "r+")
    return myfile.read()
    myfile.close()


def putfile(filename, filedata):
    myfile = open(filename, "w+")
    return myfile.write(filedata)
    myfile.close()
#--------------#


def poweroptions(user):
    userchatid = user.chat.id
    # ---------
    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton("🖲Shutdown")
    dokme2 = types.KeyboardButton("🔄Restart")
    dokme3 = types.KeyboardButton("🏘Home")
    dokmeha.add(dokme1, dokme2, dokme3)
    bot.send_message(userchatid, "😀Welcome to Power options",
                     reply_markup=dokmeha)


def takescreenshot(user):
    userchatid = user.chat.id

    bot.send_message(userchatid, "🙂Taking a screen shot...")
    ThisIsPhoto = ImageGrab.grab()
    ThisIsPhoto.save("screenshot.png")
    bot.send_message(
        userchatid, "😊Hooray! Screenshot was taked :)\n◼️ Sending...")
    photo = open("screenshot.png", "rb")
    bot.send_photo(userchatid, photo, caption="This is your computer")
    photo.close()
    os.remove("screenshot.png")
    startcmd(user, 1)


def startcmd(user, check):
    userchatid = user.chat.id

    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton("📸Take a screen shot")
    dokme2 = types.KeyboardButton("🔋Power options")
    dokme3 = types.KeyboardButton("🔊Play Sound")
    dokme4 = types.KeyboardButton("🗃File Manager")
    dokme5 = types.KeyboardButton("🌐 WebBrowser")
    dokme6 = types.KeyboardButton("💾 Open a program")
    dokmeha.add(dokme1, dokme2, dokme3, dokme4, dokme5, dokme6)

    bot.send_message(
        userchatid, """😎Hello, Welcome To My OS Remoter Bot

👨🏻‍💻Coded By mohamad yari
""", reply_markup=dokmeha)
    today = datetime.now()
    nowtime = today.strftime("%H%M%S")
    runningtime = int(nowtime)-int(data.runtime)

    if(runningtime > 60):
        runningtime2 = runningtime/60
        runningtime2 = round(runningtime2)
        runningtime = str(runningtime2)+" Minutes"
        if(runningtime2 > 3600):
            runningtime2 = runningtime2/3600
            runningtime2 = round(runningtime2)
            runningtime = str(runningtime2)+" Hours"
    else:
        runningtime = str(runningtime)+" Seconds"

    my_pc_user = os.getlogin()

    cpuusage = os.popen("wmic cpu get loadpercentage").read()
    cpuusage = cpuusage.replace("LoadPercentage", "")
    bot.send_message(userchatid, "👀Running Time : "+str(runningtime) +
                     "\n💻User : "+str(my_pc_user) + "\n📍CPU : %"+str(eval(cpuusage)))
    if(check == 1):
        print("User "+str(userchatid)+" Backed to home")
    else:
        print("User "+str(userchatid)+" Started The Bot")
#--------------#


def savetodb(user):
    usertext = user.text
    userchatid = user.chat.id
    #---------#
    thetext = usertext.replace("/save ", "")
    #----#
    randomnumber = random.randint(11111, 99999)
    putfile("database/data_"+str(randomnumber)+".txt", str(thetext))
    bot.send_message(userchatid, "Payame Shoma Ba ID " +
                     str(randomnumber)+" Zakhire Shod.")


def dbsavelist(user):
    userchatid = user.chat.id
    #---------#
    listfiles = ""
    for r, d, f in os.walk("database"):
        for file in f:
            listfiles = listfiles+"\n"+str(file)
    bot.send_message(userchatid, "Your save list :\n"+str(listfiles))


#--------------#

def playsound_btn(user):
    userchatid = user.chat.id
    #-----------#
    bot.send_message(userchatid, "Playing...")
    for x in range(1, 5):
        Beep(1000*x, 200)
        Beep(1000*x, 200-(x*50))
    bot.send_message(userchatid, "Done!")

#--------------#

def filemanager(user):
    userchatid = user.chat.id
    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton("🏘Home")
    dokme2 = types.KeyboardButton("📥 Download")
    dokme3 = types.KeyboardButton("🗂 File List")
    dokmeha.add(dokme2, dokme3, dokme1)
    bot.send_message(userchatid,"Welcome to filemanager",reply_markup=dokmeha)

def downloadfile(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,"Usage :\n/download [file name/file adress]")


#--------------#


def shutdown_btn(user):
    data.user_want_to_restart = 0
    data.user_want_to_shutdown = 1
    userchatid = user.chat.id
    #==========#
    bot.send_message(
        userchatid, "Are you sure to shutdown your computer ?\nSend /yes to shutdown or send /no to")


def restart_btn(user):
    data.user_want_to_restart = 1
    data.user_want_to_shutdown = 0
    userchatid = user.chat.id
    #==========#
    bot.send_message(
        userchatid, "Are you sure to restart your computer ?\nSend /yes to restart or send /no to")


def shutdown_or_restart(user):
    userchatid = user.chat.id
    if(data.user_want_to_shutdown == 1 and data.user_want_to_restart == 0):
        bot.send_message(userchatid, "Your Computer Is Shutting Down...")
        data.user_want_to_shutdown = 0
        data.user_want_to_restart = 0
        os.system("shutdown /s /t 1")
    elif(data.user_want_to_restart == 1 and data.user_want_to_shutdown == 0):
        data.user_want_to_shutdown = 0
        data.user_want_to_restart = 0
        bot.send_message(userchatid, "Your Computer Is Restarting...")
        os.system("shutdown /r /t 1") 
    else:
        bot.send_message(userchatid, "!!! ERROR To Process !!!")


def no_to_shutdown(user):
    userchatid = user.chat.id
    data.user_want_to_restart = 0
    data.user_want_to_shutdown = 0
    bot.send_message(userchatid, "Done !")


#--------------#

def download_this_file(user):
    userchatid = user.chat.id
    usertext = user.text
    filename_or_fileadress = usertext.replace("/download ","")
    if(os.path.isdir(str(filename_or_fileadress))):
        bot.send_message(userchatid,"This is folder :)")
    else:
        if(os.path.isfile(str(filename_or_fileadress))):
            bot.send_message(userchatid,"Downloading "+str(filename_or_fileadress)+"...")
            thefile = open(filename_or_fileadress,"rb")
            bot.send_document(userchatid,thefile,caption="This is your file")
        else:
            bot.send_message(userchatid,"Not Found")
            pass

def justfilelist(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,"Usage:\n/filemanager [dir]")

def filemanagerlist(user):
    userchatid = user.chat.id
    usertext = user.text

    directory = usertext.replace("/filemanager ","")

    if(os.path.isdir(directory)):
        bot.send_message(userchatid,"🔎 Scanning....")

        foldercount = 0
        folderlist = ""

        filecount = 0
        filelist = ""

        for r, d, f in os.walk(directory):
            for folder in d:
                if(foldercount > 30 or foldercount == 30):
                    break
                else:
                    if("\\" in r):
                        pass
                    else:
                        foldercount += 1
                        folderlist = folderlist+"\n"+"📁 "+r+"/"+folder
            for file in f:
                if(filecount > 30 or filecount == 30):
                    break
                else:
                    filecount += 1
                    filelist = filelist+"\n"+"🧾 "+r+"/"+file
        bot.send_message(userchatid,"🗂 30 First Folders In "+directory+" : \n\n"+str(folderlist))
        bot.send_message(userchatid,"🗃 30 First File In "+directory+" : \n\n"+str(filelist))
    else:
        bot.send_message(userchatid,"I can't find this directory  :(")


#--------------#

def webbrowser_btn(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "Usage:\n/web [address]")

#--------------#

def openprogram_btn(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "Usage:\n/openprogram [name]")

#--------------#

def openweb(user):
    userchatid = user.chat.id
    usertext = user.text
    web_adress = usertext.replace("/web ","")
    bot.send_message(userchatid, "Opening "+web_adress+" ...")
    webbrowser.open(web_adress, new=1)
    bot.send_message(userchatid, "Done !")

def openprogram(user):
    userchatid = user.chat.id
    usertext = user.text
    programname = usertext.replace("/openprogram ","")
    bot.send_message(userchatid, "Opening "+programname+" ....")
    try:
        responde = os.system("start "+programname)
        if(responde == 0):
            bot.send_message(userchatid, "Done !")
        else:
            bot.send_message(userchatid, "Error To Start")
    except:
        bot.send_message(userchatid, "Error To Try Start")


#--------------#


@bot.message_handler(content_types=['text'])
def botmain(user):
    admin = "mohamad_yari"
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    #------------------------------------#
    if(userusername == admin):
        #-------------#
        if(usertext == "/start" or usertext == "🏘Home"):
            if(usertext == "🏘Home"):
                check = 1
            else:
                check = 2

            startcmd(user, check)

        if(usertext == "/save"):
            bot.send_message(userchatid, "Tarze Estefade :\n/save [message]")
        if(usertext.startswith("/save ")):
            savetodb(user)

        if(usertext == "/savelist"):
            dbsavelist(user)

        if(usertext == "🔋Power options"):
            poweroptions(user)

        if(usertext == "📸Take a screen shot"):
            takescreenshot(user)

        if(usertext == "🔊Play Sound"):
            playsound_btn(user)

        if(usertext == "🖲Shutdown"):
            shutdown_btn(user)

        if(usertext == "🔄Restart"):
            restart_btn(user)

        if(usertext == "/yes"):
            shutdown_or_restart(user)

        if(usertext == "/no"):
            no_to_shutdown(user)

        if(usertext == "🗃File Manager"):
            filemanager(user)
        
        if(usertext == "📥 Download"):
            downloadfile(user)
        
        if(usertext.startswith("/download ")):
            download_this_file(user)
        
        if(usertext == "/download"):
            downloadfile(user)

        if(usertext == "🗂 File List" or usertext == "/filemanager"):
            justfilelist(user)

        if(usertext.startswith("/filemanager ")):
            filemanagerlist(user)

        if(usertext == "🌐 WebBrowser" or usertext == "/web"):
            webbrowser_btn(user)

        if(usertext.startswith("/web ")):
            openweb(user)

        if(usertext == "💾 Open a program" or usertext == "/openprogram"):
            openprogram_btn(user)
        
        if(usertext.startswith("/openprogram ")):
            openprogram(user)


    #-------------#
    else:
         bot.send_message(userchatid, "shoma dastrasi nadarid")


#---------------#
bot.polling(True)