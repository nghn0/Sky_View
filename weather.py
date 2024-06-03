from flask import Flask, render_template, request, redirect, url_for
import requests
import sqlite3

app = Flask(__name__)

key = "7a552e6d485b4d08947134558243105"



def sql():
    con = sqlite3.connect("saved_weather.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS location(location_name TEXT, lat REAL, lon REAL)")
    return con


@app.route('/')
def index():
    con = sql()
    cur = con.cursor()
    cur.execute("SELECT * FROM location")
    rows = cur.fetchall()
    details = {}
    if rows:
        for i in rows:
            point = i[0]
            url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={point}"
            response = requests.get(url)
            data = response.json()
            location = data['location']['name']
            country = data['location']['country']
            temperature_c = data['current']['temp_c']
            humidity = data['current']['humidity']
            wind = data['current']['wind_kph']
            wind_dir = data['current']['wind_dir']
            wind_de = data['current']['wind_degree']
            perp = data['current']['precip_mm']
            details[location] = (location, country, temperature_c, wind, humidity, wind_dir, wind_de, perp)

    con.close()
    return render_template('index1.html', details=details)


@app.route('/weather', methods=['POST'])
def get_weather():
    try:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        point = f"{latitude},{longitude}"
    except:
        point = request.form['cityname']
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={point}"
    response = requests.get(url)
    data = response.json()

    lat = data['location']['lat']
    lon = data['location']['lon']
    tz = data['location']['tz_id']
    location = data['location']['name']
    country = data['location']['country']
    condition = data['current']['condition']['text']
    temperature_c = data['current']['temp_c']
    temperature_f = data['current']['temp_f']
    humidity = data['current']['humidity']
    wind = data['current']['wind_mph']
    wind_dir = data['current']['wind_dir']
    wind_de = data['current']['wind_degree']
    perp = data['current']['precip_mm']
    pre = data['current']['pressure_mb']
    visibility = data['current']['vis_km']
    gust = data['current']['gust_mph']

    weather_info = (location, country, lat, lon, tz, temperature_c, temperature_f, condition, wind, wind_dir, wind_de, pre, perp, humidity, visibility, gust)
    return render_template('index2.html', weather_info=weather_info)


@app.route('/link/<name>') 
def cityname(name):
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={name}"
    response = requests.get(url)
    data = response.json()

    lat = data['location']['lat']
    lon = data['location']['lon']
    tz = data['location']['tz_id']
    location = data['location']['name']
    country = data['location']['country']
    condition = data['current']['condition']['text']
    temperature_c = data['current']['temp_c']
    temperature_f = data['current']['temp_f']
    humidity = data['current']['humidity']
    wind = data['current']['wind_mph']
    wind_dir = data['current']['wind_dir']
    wind_de = data['current']['wind_degree']
    perp = data['current']['precip_mm']
    pre = data['current']['pressure_mb']
    visibility = data['current']['vis_km']
    gust = data['current']['gust_mph']

    weather_info = (
    location, country, lat, lon, tz, temperature_c, temperature_f, condition, wind, wind_dir, wind_de, pre, perp,
    humidity, visibility, gust)
    return render_template('index2.html', weather_info=weather_info)

@app.route('/save/<loc>/<lat>/<lon>')
def save(loc, lat, lon):
    con = sql()
    cur = con.cursor()
    cur.execute("select location_name from location")
    rows = cur.fetchall()
    for i in rows:
        if loc in i:
            return redirect(url_for('index'))
    cur.execute('insert into location values(?,?,?)', (loc, lat, lon))
    con.commit()
    con.close()
    return redirect(url_for('index'))

@app.route('/delete/<loc>')
def delete(loc):
    con = sql()
    cur = con.cursor()
    cur.execute("delete from location where location_name=?", (loc,))
    con.commit()
    con.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
