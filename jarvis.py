import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyautogui
import time
import math
from sympy import symbols, Eq, solve

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def takeScreenshot():
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"screenshot_{timestamp}.png"  # Save to current directory
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print(f"Screenshot taken and saved to {screenshot_path}")
        speak("Screenshot saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't take the screenshot.")

def solveMath(query):
    operators = {'plus': '+', 'minus': '-', 'times': '*', 'divided': '/'}
    query = query.lower()

    for word, symbol in operators.items():
        if word in query:
            parts = query.split(word)
            num1 = int(parts[0].strip())
            num2 = int(parts[1].strip())
            if symbol == '+':
                result = num1 + num2
            elif symbol == '-':
                result = num1 - num2
            elif symbol == '*':
                result = num1 * num2
            elif symbol == '/':
                result = num1 / num2
            speak(f"The answer is {result}")
            return
    speak("Sorry, I couldn't understand the math problem.")

def solveEquation(query):
    try:
        if 'solve' in query and '=' in query:
            equation = query.replace("solve", "").replace("=", "-(") + ")"
            x = symbols('x')
            eq = Eq(eval(equation), 0)
            solution = solve(eq, x)
            speak(f"The solution is {solution[0]}")
    except Exception as e:
        speak("Sorry, I couldn't solve the equation.")

def funFact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3000 years old!",
        "Bananas are berries, but strawberries are not!",
        "Octopuses have three hearts and blue blood.",
        "There are more stars in the universe than grains of sand on all the Earth’s beaches.",
    ]
    fact = random.choice(facts)
    speak(fact)

def tellQuote():
    quotes = [
        "Believe you can and you're halfway there. — Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
        "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
        "The only way to do great work is to love what you do. — Steve Jobs"
    ]
    quote = random.choice(quotes)
    speak(quote)

def openPaint():
    try:
        os.system("start mspaint")
        speak("Opening Microsoft Paint")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry sir, I couldn't open Paint.")

def drawRectangle():
    speak("Drawing rectangle now.")
    time.sleep(2)
    pyautogui.moveTo(300, 300, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(500, 300, duration=0.5)
    pyautogui.moveTo(500, 500, duration=0.5)
    pyautogui.moveTo(300, 500, duration=0.5)
    pyautogui.moveTo(300, 300, duration=0.5)
    pyautogui.mouseUp()
    speak("Rectangle drawn.")

def drawCircle():
    speak("Preparing to draw a circle in Paint.")
    time.sleep(2)
    pyautogui.moveTo(150, 70, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)
    center_x, center_y = 600, 400
    radius = 100
    pyautogui.moveTo(center_x + radius, center_y)
    pyautogui.mouseDown()
    for angle in range(0, 361, 5):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        pyautogui.moveTo(x, y, duration=0.01)
    pyautogui.mouseUp()
    speak("Circle drawn.")

def drawTriangle():
    pyautogui.moveTo(500, 600)
    pyautogui.mouseDown()
    pyautogui.moveTo(700, 600)
    pyautogui.moveTo(600, 400)
    pyautogui.moveTo(500, 600)
    pyautogui.mouseUp()
    speak("Triangle drawn")

def drawFreehand():
    pyautogui.moveTo(600, 600)
    pyautogui.mouseDown()
    for _ in range(100):
        x_offset = random.randint(-50, 50)
        y_offset = random.randint(-50, 50)
        pyautogui.moveTo(600 + x_offset, 600 + y_offset)
        time.sleep(0.05)
    pyautogui.mouseUp()
    speak("Freehand drawing complete")

def refreshLaptop():
    pyautogui.press('f5')
    speak("Refreshing the laptop")

def dragVSCode():
    start_x, start_y = 100, 100
    end_x = 800
    end_y = start_y
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(end_x, end_y, duration=2)
    pyautogui.mouseUp()
    speak("VS Code window has been dragged from left to right.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find any result on Wikipedia.")

        elif 'take screenshot' in query:
            takeScreenshot()

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            try:
                os.system("code")  # VS Code must be in PATH
            except:
                speak("Sorry sir, I couldn't open Visual Studio Code.")

        elif 'open calculator' in query:
            os.system('calc')

        elif 'open brave' in query:
            try:
                os.system("start brave")  # Brave must be in PATH
            except:
                speak("Sorry sir, Brave browser is not installed or not found.")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com")

        elif 'open games' in query or 'play games' in query:
            webbrowser.open("https://www.crazygames.com/")

        elif 'fun fact' in query:
            funFact()

        elif 'tell me a quote' in query or 'motivate me' in query:
            tellQuote()

        elif 'how to close jarvis' in query:
            speak("To close me, just say 'Jarvis stop' or 'exit'.")

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            speak("Goodbye sir, shutting down.")
            break

        elif 'open paint' in query:
            openPaint()

        elif 'draw rectangle' in query:
            drawRectangle()

        elif 'draw circle' in query:
            drawCircle()

        elif 'draw triangle' in query:
            drawTriangle()

        elif 'draw freehand' in query:
            drawFreehand()

        elif 'refresh laptop' in query:
            refreshLaptop()

        elif 'drag vscode' in query:
            dragVSCode()

        elif 'solve math' in query:
            solveMath(query)

        elif 'solve equation' in query:
            solveEquation(query)
