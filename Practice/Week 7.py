# 1 A complex class with attributes, constructors and getters/setters

class Complex():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def setValue(self,a,b):
        self.a = a
        self.b = b

    def getValue(self):
        x = str(self.a) + "+" + str(self.b) + "i"
        return x

a = int(input("Give value to a: "))
b = int(input("Give value b: "))

myValue = Complex(a,b)
print (myValue.getValue())

a = int(input("Give value to a: "))
b = int(input("Give value b: "))

myValue.setValue(a,b)
print (myValue.getValue())
print ()
        
# 2 Class clock

import time

class Clock():

    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def setTime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def ticking(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    def timedisplayed(self):
        return "%2d:%2d:%2d" % (self.hours,self.minutes, self.seconds)
           

class AlarmClock(Clock):

    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        super().__init__(hours,minutes,seconds)

    def setAlarm(self, alarmh, alarmm, alarms):
        self.alarmh = alarmh
        self.alarmm = alarmm
        self.alarms = alarms

    def isItAlarmTime(self):
        x = "%2d:%2d:%2d" % (self.alarmh,self.alarmm, self.alarms)
        if x == super().timedisplayed():
            print ("Alarm!")
        

print ("Set time")

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
    timenow = AlarmClock(hours,minutes,seconds)

alarmh = int(input("Alarm hours: "))
alarmm = int(input("Alarm minutes: "))
alarms = int(input("Alarm seconds: "))
timenow.setAlarm(alarmh,alarmm,alarms)

while True:
    print (timenow.timedisplayed())
    timenow.isItAlarmTime()
    time.sleep(1)
    timenow.ticking()
    

 
