import requests, json


def getWeather(location):
    api_key = "MY_TOKEN_ID"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = location

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = str(round(y["temp"]-273.15, 2))

        min = str(round(y["temp_min"]-273.15, 2))
        max = str(round(y["temp_max"]-273.15, 2))
        name = x["name"]

        current_humidiy = str(y["humidity"])

        z = x["weather"]

        weather_description = z[0]["description"]

        weather = (str(name) + "\n" + "\n" +
                   str("Temperatura: " + current_temperature + "°C" + "\n") +
                   str("Mínima: " + min + "°C" + "\n") +
                   str("Máxima: " + max + "°C" + "\n") +
                   str("Umidade do ar: " + current_humidiy + "%" + "\n"))

    else:
        weather = "CIDADE NÃO ENCONTRADA. TENTE NOVAMENTE"

    return weather
