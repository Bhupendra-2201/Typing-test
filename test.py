from time import *
import random as r
import keyboard



def mistake(paratest,  usertest):
    error = 0
    para = paratest.split()
    user = usertest.split()
    for i in range(len(para)):
        if para[i] != user[i]:
            error += 1
    return error
    


def speed(t1, t2, userinput):
    time_delay = t2 - t1
    time_R = round(time_delay, 2)
    speed = count_words(userinput) / (time_R  /60)
    return round(speed)
     
       
def count_words(text):
    words = text.split()
    return len(words)


def start_time(event):
    global t1
    if t1 is None:
        t1 = time()
    return
        
         
        
t1 = None        

test = ["For developing the GUI, we'll use the Tkinter module. The player must enter ten words in this box, which are presented one after another. The English words module will be used to obtain the words. Moreover, the screen will display how many times have passed."]
test1 = r.choice(test)
print("-----------Typing speed test-----------")
print(test1)
print()
print()

keyboard.on_press(start_time)

testInput= input("Enter: ")
t2 = time()
keyboard.unhook_all()

print(count_words(test1))
print('Speed:', speed(t1, t2, testInput), "wpm")
print('Error: ', mistake(test1, testInput))