from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + zipcode + ',&appid=e842d2443f05cf49e2e6c4f0a140e355')

    json_object = response.json()
    temp_k = float(json_object['main']['temp'])
    city_name = zipcode
    print(city_name)
    temp_f=temp_k/10
    wind_speed=float(json_object['wind']['speed'])
    Pressure = float(json_object['main']['pressure'])
    temp_l=int(str(temp_f)[:2])

   # temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('index.html', temp=temp_l, city_name=city_name, wind_speed=wind_speed,Pressure=Pressure)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
