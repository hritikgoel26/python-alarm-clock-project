import datetime
import winsound

alarmHour=int(input("what hour do you want to wake up:"))
alarmMinute=int(input("what minute do you want to wake up:"))
ampm=str(input("am or pm:"))

if(ampm == "pm" and alarmHour == 12):
    alarmHour= 12

elif(ampm == "pm"):
    alarmHour = alarmHour + 12


while True:
    if(alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute):
        print("wake up")
        break
print("existed")    
f=5000
d=7000
winsound.Beep(f,d)

