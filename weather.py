#! /usr/bin/env python3
#Ran Thawonmas, 2600180396-3, Distributed Systems Project

#How to run
#cd Desktop/DSProject >> python3 -m http.server --cgi 8000 using your Terminal
#http://localhost:8000/cgi-bin/weather.py using your browser

import datetime
import requests
import json
import cgi

#Current date and time can be obtained as a string value by the following code.
datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#The weather information for a specified city can be obtained with the following code.
form = cgi.FieldStorage()
city_name = form.getvalue('city','Shiga')

API_KEY = "d01ed74f13d285ba9f785fb49335bf3a"
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
url = api.format(city = city_name, key = API_KEY)
response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)

#Content of the JSON data can be extracted with the following code.
city = data["name"]
country = data["sys"]["country"]
icon = data["weather"][0]["icon"]
iconurl = "http://openweathermap.org/img/w/" + icon + ".png"
description = data["weather"][0]["description"]
weather = data["weather"][0]["main"]
temp = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
hum = data["main"]["humidity"]
wind = data["wind"]["speed"]

#An input form can be shown with the following HTML elements.
print("Content-type: text/html\n")
print("""
<html>
    <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>
    
    
    <tr><td align="center">JST: %s</tr></td>
    
    <body style="background-color:#ffff00;" text=#000080>
        <table>
            <h1>Ran's Weather Forecast</h1>
            
        <form name="city_name" action="/cgi-bin/weather.py" method="POST">
              City:
              <input type="text" name="city" />
              <button type="submit" name="submit">Show</button>
            </form>
                
              </td></tr>
              
              <tr><td align="center">%s</tr></td>
              
              <tr><td align="center">Country: %s</tr></td>
              
              <tr><td align="center"><img src= %s></td></tr>

            <tr><td align="center">Description: %s</tr></td>
              
              <tr><td align="center">Weather: %s</tr></td>
              
              <tr><td align="center">Temperature (in Celsius): %s </tr></td
              
              <tr><td align="center">Temperature Min (in Celsius): %s </tr></td
              
              <tr><td align="center">Temperature Max (in Celsius): %s </tr></td
              
            <tr><td align="center">Temperature (in Fahrenheit): %s </tr></td
            
            <tr><td align="center">Temperature Min (in Fahrenheit): %s </tr></td
            
            <tr><td align="center">Temperature Max (in Fahrenheit): %s </tr></td
            
            
            
              
              <tr><td align="center">Humidity (in percentage): %s </tr></td>
              
              <tr><td align="center">Wind (in m/s): %s </tr></td>
              
              

        </table>
        
    </body>
    
</html>"""%(datetime, city, country, iconurl, description, weather, temp, temp_min, temp_max, round(temp *  (9/5) + 32,2),round(temp_min *  (9/5) + 32,2), round(temp_max *  (9/5) + 32,2), hum, round(wind)))





# Print JSON text with <pre> tags
print("<html> ")
print("<pre>")
print(jsonText)
print("</pre>")
print("</html>")
