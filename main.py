#voice recongnition
import pyttsx3
#computer can listen to speacking
import speech_recognition as sr
#
import webbrowser
#
import time
#deal with time in computer
import datetime
#deal with os operating system
import os
#
import simpleaudio as sa
#
import pyautogui

import tkinter as tk
from tkinter import filedialog

#voice recongnition
wel= pyttsx3.init()
voices= wel.getProperty('voices')
wel.setProperty('voice',voices[0].id)

#waiting for him to speake
def Speak(audio):
    wel.say(audio)
    wel.runAndWait()

# داله لاعطاء الاوامر
def Takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
        print('say command sir ..........')
        #دقه الاستماع الى الصوت كل ما ازود فى الرقم لى بعد العامه كان ادق
        command.phrase_threshold = 0.4
        #استمع للصوت الى انا مدخله من المايك
        audio=command.listen(mic)
        try:
            print('Recording ....')# اكتبها عشان اعرف انك بتسجل
            query= command.recognize_google(audio,language='en')
            print(f'you said : {query}')
        except Exception as Error:
            print(Error)
            return None
        return query.lower()

#play this to welcome
filename = "E:/marwa 's project/sound/welcome1.wav"
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done() 

# take rest for 1 second
time.sleep(1)

#
filename = "E:/marwa 's project/sound/welcome2.wav"
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done() 

while True:
#
    query = Takecommand()
    
    if "good morning" in query:
        filename = "E:/marwa 's project/sound/good morning.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if 'good evening ' in query:
         filename = "E:/marwa 's project/sound/good evening.wav"
         wave_obj = sa.WaveObject.from_wave_file(filename)
         play_obj = wave_obj.play()
         play_obj.wait_done()

    if 'open google 'in query:
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/open google.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
          
         # سيفتح لك جوجل عن طريق اللينك بتاعه وهنا اقدر انسخ اى رابط انا عوزاه
        time.sleep(2)
        webbrowser.open_new_tab('https://www.google.com')
    
    if 'dates' in query:
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/Schedule.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    
    if 'close pc' in query:
        filename ="C:/Users/MaKaNaK/Desktop/marwa 's project/sound/closepc.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        #os.system("shutdown /s /t 1")
    
#ده عاوز تغيير ريكورد
    if  'program' in query:
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/program (2).wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()

        cpath = "C:\\Users\\MaKaNaK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(cpath)

    if 'facebook' in query:
         filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/post in facebook.wav"
         wave_obj = sa.WaveObject.from_wave_file(filename)
         play_obj = wave_obj.play()
         play_obj.wait_done()
         #post = input('enter your post : ')
         
         #webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
         
         #pyautogui.hotkey('ctrl','t')
         
         link = "https://www.facebook.com/profile.php?id=61554264623126"
         #webbrowser.open_new_tab(link)
         webbrowser.open_new_tab(link)  
         #pyautogui.hotkey('ctrl','f')
         
        # webbrowser.get('chrome').open_new(link)
         
        #pyautogui.hotkey('ctrl','f')
         '''
         time.sleep(10)
         pyautogui.typewrite("what's on your mind?")
         pyautogui.press('enter')
         pyautogui.press('escape')
         pyautogui.press('enter')
         time.sleep(4)
         pyautogui.typewrite(post)
         pyautogui.click(670,585)
         '''

    if 'youtube'in query:
        
        # play this alarm then enter the diserd time  It tells you that it agrees to alert you
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/open youtube.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 
        link = "https://www.youtube.com/watch?"
        webbrowser.open_new_tab(link)

    if 'friend'in query:
        
        # play this alarm then enter the diserd time  It tells you that it agrees to alert you
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/open watsapp.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 
        link = "https://web.whatsapp.com/"
        webbrowser.open_new_tab(link)

    if 'chat'in query:
        
        # play this alarm then enter the diserd time  It tells you that it agrees to alert you
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/open gpt.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 
        link = "https://chat.openai.com/"
        webbrowser.open_new_tab(link)

    
    if 'thank you'in query:
        
        # play this alarm then enter the diserd time  It tells you that it agrees to alert you
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/you are welcome.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 
    
    if 'file'in query:
        
        # play this alarm then enter the diserd time  It tells you that it agrees to alert you
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/open file.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 
        import tkinter as tk
        from tkinter import filedialog

        def choose_file():
            file_path = filedialog.askopenfilename()
    
          # Check if the path is not empty
            if file_path:
              with open(file_path, 'r') as file:
            # Read the content
                content = file.read()
            # Display the content in a new window
                show_text_window(content)

        def show_text_window(text):
            text_window = tk.Toplevel(root)
            text_window.title("File Content Display")
    
            text_display = tk.Text(text_window)
            text_display.insert(tk.END, text)
            text_display.pack()

        # Set up the Tkinter window
        root = tk.Tk()
        root.title("Read File")

        # File choose button
        choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
        choose_file_button.pack(pady=20)

        root.mainloop()

    


    if 'alarm' in query:
        # enter the disered time
        time=input("Enter the alarm: ")

        # play this alarm then enter the diserd time  It tells you that it agrees to alert you
        filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/set alarm.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 

        # Make current time always equal to the time in your city
        while True:
            timo= datetime.datetime.now()

        # Specify the hour, time and minutes
            now=timo.strftime("%H:%M:%S")

        #If the clock is now like the user wrote it, we will do the following
            if now==time:
              # play that alarm 
              filename = "C:/Users/MaKaNaK/Desktop/marwa 's project/sound/time of action.wav"
              wave_obj = sa.WaveObject.from_wave_file(filename)
              play_obj = wave_obj.play()
              play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing
 
            #The computer's current time has exceeded the required time. Take a break
              if now > time: 
                  break  
         


          
























            

