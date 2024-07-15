from tkinter import *
import requests
import json


root = Tk()
root.title("Frames Demo")
root.geometry("500x250")

frame = Frame(root, width=400, height=200,)
frame.pack(pady=25)

try:
    api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=F394104A-04A4-492D-B3E3-20B8B4C8BFE6"
    )
    api = json.loads(api_request.content)

    city = api[0]['ReportingArea']
    air_quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

label = Label(frame, text="City")
label.grid(row=0, column=0)
label = Label(frame, text=city)
label.grid(row=0, column=1)
label = Label(frame, text="Air Quality")
label.grid(row=1, column=0)
label = Label(frame, text=air_quality)
label.grid(row=1, column=1)
label = Label(frame, text="Category")
label.grid(row=2, column=0)
label = Label(frame, text=category)
label.grid(row=2, column=1)


root.mainloop()
