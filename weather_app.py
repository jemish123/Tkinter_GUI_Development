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
    city_data_label = Label(frame, text=city)
    city_data_label.grid(row=0, column=1)

    air_quality = api[0]['AQI']
    air_quality_label = Label(frame, text=air_quality)
    air_quality_label.grid(row=1, column=1)

    category = api[0]['Category']['Name']
    cat_label = Label(frame, text=category)
    cat_label.grid(row=2, column=1)

    if category == "Good":
        frame.configure(background="")
except Exception as e:
    api = "Error..."

city_label = Label(frame, text="City")
city_label.grid(row=0, column=0)
aqi_label = Label(frame, text="Air Quality")
aqi_label.grid(row=1, column=0)
category_label = Label(frame, text="Category")
category_label.grid(row=2, column=0)


root.mainloop()
