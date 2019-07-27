import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

#API Key: INSERT_YOUR_OPENWEATHER_API_KEY_HERE
#API Call: api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#WWW: https://openweathermap.org/appid


def fnGetWeatherForecast(cityName):
    #print(cityName)
    weather_key = '2451625f3b60fcc125e9b7024c451096'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': cityName, 'units': 'Metric'}
    response = requests.get(url, params=params)
    print(response.json())

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving the information.'
    return final_str

def fnGetWeatherCurrent(cityName):
    weather_key = '2451625f3b60fcc125e9b7024c451096'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': cityName, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


app = tk.Tk()

canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#Top Frame to type city
topFrame = tk.Frame(app, bg='#3498db', bd=5)
topFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = tk.Entry(topFrame, font=('Arial', 18))
entry.place(relwidth=0.65, relheight=1)
button1 = tk.Button(topFrame, text="Get Weather", bg="#2c3e50", fg="white",  font=('Arial', 12), command=lambda: fnGetWeatherCurrent(entry.get()))
button1.place(relx=0.7, relwidth=0.3, relheight=1)

#Bottom Frame where results will be printed
lowerFrame = tk.Frame(app, bg='#3498db', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lowerFrame, text="", bg='white', font=('Arial', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

#print(tk.font.families())

app.mainloop()

#To make EXE:
#pip install pyinstaller
#pyinstaller.exe --onefile --icon=sun_icon.ico weatherapp.py
#Check that required images etc are also in the folder
