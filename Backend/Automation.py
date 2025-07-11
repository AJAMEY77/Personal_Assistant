from AppOpener import close, open as appopen 
from webbrowser import open as webopen 
from pywhatkit import search, playonyt
from dotenv import dotenv_values 
from bs4 import BeautifulSoup 
from rich import print 
from groq import Groq 
import webbrowser 
import subprocess 
import requests
import keyboard 
import asyncio 
import os 

# Load environment variables from the env file.
env_vars = dotenv_values(".env")
GroqAPIKey =env_vars.get("GroqAPIKey") # Retrieve the Groq API key.


# Define CSS classes for parsing specific elements in HTML content.
classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table", "dDoNo ikb4Bb gsrt", "sXLaOe",
"LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]


#Define a user-agent for making web requests.
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'


# Initialize the Groq client with the API key.
client = Groq(api_key=GroqAPIKey)




professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

#List to store chatbot messages.
messages = []



SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ ['Username']}, You're a content writer. You have to write content like letters, essays, and articles. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."}]


def GoogleSearch(Topic):
    search(Topic) # Use pywhatkit's search function to perform a Google search.
    return True # Indicate success.


def Content(Topic):
    #Nested function to open a file in Notepad.
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe' # Default text editor.
        subprocess.Popen([default_text_editor, File]) # Open the file in Note

    #Nested function to generate content using the AI chatbot.
    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            # Specify the AI
            messages=SystemChatBot + messages, # Include s
            max_tokens=2048, # Limit the maximum tokens in
            temperature=0.7, # Adjust response randomness.
            top_p=1, # Use nucleus sampling for response c
            stream=True,
            # Enable streaming response.
            stop=None # Allow the model to determine stopp
        )
        
        Answer = "" # Initialize an empty string to store the AI's response.
        
        # Process streamed response chunks.
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content #Append th
                
        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer}) #
        return Answer
    
    Topic: str = Topic.replace("Content ", "")
    ContentByAI = ContentWriterAI(Topic) 
    
    
    with open(rf"Data\{Topic.lower().replace(' ','')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI) # Write the content to the file.
        file.close()
    
    OpenNotepad(rf"Data\{Topic.lower().replace(' ','')}.txt") # Open the file in Notepad.
    return True # Indicate success.
#Content("application to sick leave") # Example usage of Content function.

def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}" # Construct the YouTu
    webbrowser.open(Url4Search) # Open the search URL in a web browser.
    return True # Indicate success.


def PlayYoutube(query):
    playonyt(query) # Use pywhatkit's playonyt function to play the video
    return True # Indicate success.
# PlayYoutube("Tere Pyaar main by Kavish")



def OpenApp(app, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True) #
        return True # Indicate success.
    except:
        #Nested function to extract links from HTML content.
        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', {'jsname': 'UWckNb'})
            return [link.get('href') for link in links]
        
        def search_google(query):
            url = f"https://www.google.com/search?q={query}" #
            headers = {"User-Agent": useragent} # Use the prede
            response = sess.get(url, headers=headers) # Perform
            if response.status_code == 200:
                return response.text # Return the HTML content.
            
            else:
                print("Failed to retrieve search results.") # F
            return None
        
        html = search_google(app) 

        if html:
            link = extract_links(html) [0]
            webopen(link) # Open the link in a web browser.
            
        return True # Indicate success.
    

def CloseApp(app):
    if "chrome" in app:
        pass # Skip if the app is Chrome.
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True # Indicate success.
        except:
            return False # Indicate failure.    


def System(command):
    # Nested function to mute the system volume.
    def mute():
        keyboard.press_and_release("volume mute")

    # Nested function to unmute the system volume.
    def unmute():
        keyboard.press_and_release("volume mute") # S
    
    # Nested function to increase the system volume.
    def volume_up():
        keyboard.press_and_release("volume up")

    # Nested function to decrease the system volume.
    def volume_down():
        keyboard.press_and_release("volume down") # Simulate volume down key press.
        
        
    if command == "mute":
        mute()
        
    elif command == "unmute":
        unmute()
    elif command == "volume up":
        volume_up()
    elif command == "volume down":
        volume_down()
        
    return True 
   
async def TranslateAndExecute(commands: list [str]):
    funcs = []
    # List to store asynchronous tasks.
    for command in commands:
        if command.startswith("open "):
            if "open it" in command: #
                pass

            if "open file"== command: # 
                pass
            
            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open ")) #
                funcs.append(fun)
        elif command.startswith("general "):
            # Placeholder for general commands.
            pass
        
        elif command.startswith("realtime "): #
            pass
    
        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close ")) # Sc
            funcs.append(fun)

        
        elif command.startswith("play "): # Handle "play" commands.
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play ")) # Schedule 
            funcs.append(fun)
        
        elif command.startswith("content "):
            fun = asyncio.to_thread (Content, command.removeprefix("content ")) # Schedule c 
            funcs.append(fun)

        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search ")) 
            funcs.append(fun)
            
        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search "))
            funcs.append(fun)

        
        elif command.startswith("system "): # Handle system commands.
            fun = asyncio.to_thread(System, command.removeprefix("system ")) # S
            funcs.append(fun)
        else:
            print(f"No Function Found. For {command}") 
            
    results = await asyncio.gather(*funcs) # Execute all tasks concurrently.

    for result in results: # Process the results.
        if isinstance(result, str):
            yield result
        else:
            yield result

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands): 
        pass
    return True
