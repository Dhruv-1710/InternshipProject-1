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

# Setup speech engine
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

def closeApp(process_name, app_name):
    try:
        os.system(f"taskkill /f /im {process_name}")
        speak(f"Closing {app_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't close {app_name}")

def takeScreenshot():
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(os.getcwd(), f"{timestamp}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        speak(f"Screenshot saved successfully.")
    except Exception as e:
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
        "Honey never spoils.",
        "Bananas are berries, but strawberries are not!",
        "Octopuses have three hearts and blue blood.",
        "There are more stars in the universe than grains of sand on all the Earth’s beaches."
    ]
    speak(random.choice(facts))

def tellQuote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Success is not final, failure is not fatal.",
        "Don't watch the clock; do what it does. Keep going.",
        "The only way to do great work is to love what you do."
    ]
    speak(random.choice(quotes))

def openPaint():
    try:
        os.system("start mspaint")
        speak("Opening Microsoft Paint")
    except Exception as e:
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
    # Step 1: Open Paint
    os.system("start mspaint")
    time.sleep(3)  # Wait for Paint to fully open

    # Step 2: Select the Brush tool
    brush_x, brush_y = 260, 90  # Adjust if needed
    pyautogui.moveTo(brush_x, brush_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    # Step 3: Activate the canvas by clicking once in it
    canvas_click_x, canvas_click_y = 700, 400
    pyautogui.click(canvas_click_x, canvas_click_y)
    time.sleep(0.5)

    # Step 4: Draw a circle
    center_x, center_y = canvas_click_x, canvas_click_y
    radius = 100

    pyautogui.moveTo(center_x + radius, center_y, duration=0.2)
    pyautogui.mouseDown()

    for angle in range(0, 361, 3):  # smooth curve
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        pyautogui.moveTo(x, y, duration=0.01)

    pyautogui.mouseUp()
    print("Circle drawn.")

def drawTriangle():
    speak("Drawing triangle now.")
    time.sleep(2)
    pyautogui.moveTo(500, 600, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(700, 600, duration=0.5)
    pyautogui.moveTo(600, 400, duration=0.5)
    pyautogui.moveTo(500, 600, duration=0.5)
    pyautogui.mouseUp()
    speak("Triangle drawn.")

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
    end_x, end_y = 800, 100
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(end_x, end_y, duration=2)
    pyautogui.mouseUp()
    speak("VS Code window has been dragged.")

# Main loop
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
            codePath = "Microsoft VS Code.exe"
            try:
                os.startfile(codePath)
            except FileNotFoundError:
                speak("Sorry sir, I couldn't find Visual Studio Code.")

        elif 'open calculator' in query:
            os.system('calc')

        elif 'open brave' in query:
            bravePath = "Brave-Browser.exe"
            try:
                os.startfile(bravePath)
            except FileNotFoundError:
                speak("Sorry sir, Brave browser is not installed or the path is incorrect.")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com")

        elif 'open game' in query or 'play games' in query:
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

        elif 'draw free hand' in query:
            drawFreehand()

        elif 'refresh laptop' in query:
            refreshLaptop()

        elif 'change position vscode' in query:
            dragVSCode()

        elif 'solve math' in query:
            solveMath(query)

        elif 'solve equation' in query:
            solveEquation(query)

        elif 'close paint' in query:
            closeApp("mspaint.exe", "Paint")

        elif 'close brave' in query:
            closeApp("brave.exe", "Brave Browser")

        elif 'close google' in query or 'close chrome' in query:
            closeApp("chrome.exe", "Google Chrome")

        elif 'close youtube' in query:
            closeApp("brave.exe", "YouTube on Brave")

        elif 'close code' in query or 'close vs code' in query:
            closeApp("Code.exe", "Visual Studio Code")

        elif 'close calculator' in query:
            closeApp("Calculator.exe", "Calculator")
