#!/usr/bin/python3
import os
import getpass
user = getpass.getuser()
User = user.capitalize()
print (" \n\n\n\n Hello %s ;) \n Welcome to your Music-Player"% User)
dir = input("\n\n\n [!] Wich Directory Do You Want ?\n\n ")

if dir.count("music") == 1 or dir.count("Music") == 1 :
    dir = "/home/"+user+"/Music"
os.system("clear")
endline = "\n" * 4
print(endline)
os.chdir(dir)
list = []
total_list = os.listdir(".")
for file in total_list :
    if os.path.isfile(file):
        list.append(file)
len = len(list)
print(" [S] Choose your target :\n")
for i in range (0,len):
    music = list[i]
    if music.count("-") > 0 or music.count("(") > 0 or music.count(")") > 0:
        alpha = music
        music = music.replace("-","_")
        music = music.replace("(","[")
        music = music.replace(")","]")
        os.rename(alpha,music)
    num = str(i+1)
    print(" [%s] %s"% (num, music))
choice = input("\n :")
music = list[int(choice)-1]
music = music.replace(" ","\ ")
#print(music,"\n",cmd)
print(endline)
os.system("clear")
times = input("\n [-] How Many Times Do You Want Play it\n\n [1] forever 'f'\n [2] one time 'o'\n [3] N times \n\n [*] For N times enter the N\n :")
if times.count("f") == 1 or times.count("F") == 1 :
    cmd = "mpv --no-audio-display --loop inf " + music
    os.system("clear")
    os.system(cmd)
elif times.count("o") == 1 or times.count("O") == 1 :
    cmd = "mpv --no-audio-display  " + music
    os.system("clear")
    os.system(cmd)
else :
    cmd = "mpv --no-audio-display --loop " + times + " " + music
    os.system("clear")
    os.system(cmd)

