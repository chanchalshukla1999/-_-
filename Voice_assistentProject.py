import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import wolframalpha
from selenium import webdriver

num = 1
def assistant_speaks(output):
    global num
    num += 1
    print("Assistent:",output)

    toSpeak = gTTS(text=output,lang="en",slow=False)
    file = str(num)+".mp3" 
    toSpeak.save(file)
    playsound.playsound(file,True)
    os.remove(file)

def get_audio():
    r_object = sr.Recognizer()
    audio = ""
    with sr.Microphone() as source:
        print("Speak...")

        audio = r_object.listen(source,phrase_time_limit=5)
    print("Stop.")

    try:
        text = r_object.recognize_google(audio,language="en-US")
        print("You:",text)
        return text
    
    except:
        assistant_speaks("Could not understand your command,Please try again!")
        return 0

def process_text(input):
    try:
        if "search" in input or "play" in input:
            search_web(input)
            return
        
        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return
        
        elif "who created you" in input and "made you" in input:
            speak = "I have been created by Chanchal Shukla."
            assistant_speaks(speak)
            return
        
        elif "calculate" in input.lower():

            app_id  = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)
            indx = input.lower().split().index("calculate")
            query = input.split()[indx+1:]
            res = client.query("".join(query))
            answer  = next(res.results).text
            assistant_speaks("The answer is" + answer)
            return
        
        elif "open" in input:
            open_application(input.lower())
            return
        
        else:
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if "yes" in str(ans) or "yeah" in str(ans):
                search_web(input)
            else:
                return
    except:
        assistant_speaks("I do not understand,I can search the web for you,Do you want to continue?")
        ans = get_audio()
        if "yes" in str(ans) or "yeah" in str(ans):
            search_web(input)

def search_web(input):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.minimize_window()

    if "youtube" in input.lower():
        assistant_speaks("opening in youtube for you")
        indx = input.lower().split().index("youtube")
        query = input.split()[indx+1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
    
    elif "wikipedia" in input.lower():
        assistant_speaks("opening wikipedia for you")
        indx = input.lower()[indx+1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    
    else:
        
        if "google" in input:
            indx = input.lower().split().index("google")
            query = input.split()[indx+1:]
            driver.get("https://www.google.com/search?q =" + "+".join(query))
        elif "search" in input:
            indx = input.lower().split().index("google")
            query = input.split()[indx+1:]
            driver.get("https://www.google.com/search?q =" + "+".join(query))
        else:
            driver.get("https://www.google.com/search?q =" + "+".join(input.split()))
        return
    
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files\Google\Chrome\Application')
        return
    elif "microsoft edge" in input or "microsoft search engine" in input:
        assistant_speaks("Opening Microsoft edge for you")
        os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application')
        return
    elif "word" in input:
        assistant_speaks("Opening microsoft word for you")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
        return
    elif "excel" in input:
        assistant_speaks("Opening microsoft excel for you")
        os.startfile('C:\Program Files (x86)\Microsoft Office\root\Office16')
        return
    else:
        assistant_speaks("Application not available")
        return
if __name__ == "__main__":
    assistant_speaks("Whats your name,User?")
    name = "User"
    name = get_audio()
    assistant_speaks("Hello"+ name +'.')

    while(1):
        assistant_speaks("what can i do for you?")
        text = get_audio().lower()
        
        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
          assistant_speaks("Ok bye,"+ name   +".")
          break

        process_text(text)












