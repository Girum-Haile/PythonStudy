from tkinter import *
import requests

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City:%s,\n Condition:%s,\n Temperature(F):%s' % (name, description, temp)
    except:
        final_str = "there was a problem retrieving the info"
    return final_str


def get_weather(city):
    weather_key = '8c8c4e3aed97502c53e85535a060a7c7'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_Image = PhotoImage(file='landscape.png')
background_Label = Label(root, image=background_Image)
background_Label.place(relheight=1, relwidth=1)
frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=40)
label.place(relwidth=1, relheight=1)

root.mainloop()
