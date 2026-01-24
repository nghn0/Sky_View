# 🌦️ Sky View: Weather Forecast Web App (Flask + WeatherAPI)
<p align="left">
  <img src="https://img.shields.io/badge/Framework-Flask-FF2D20?style=flat-square" alt="Flask">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/Database-SQLite-44D62C?style=flat-square" alt="SQLite">
  <img src="https://img.shields.io/badge/API-WeatherAPI-FFD700?style=flat-square" alt="WeatherAPI">
</p>

A simple and interactive **Flask-based Weather Forecast Application** that allows users to:
- Search weather using **City Name** or **Latitude & Longitude**
- View detailed real-time weather conditions
- **Save** locations to a SQLite database for quick access
- **Delete** saved locations anytime

---

## ✨ Features

- 🌍 Search weather by **City Name**
- 📍 Search weather using **Latitude & Longitude**
- 💾 Save favorite locations (stored in **SQLite**)
- 🗑️ Delete saved locations
- 📊 Displays temperature, humidity, wind, pressure, visibility, etc.
- ⚡ Real-time weather data using **WeatherAPI**

---

## 📂 Project Structure

```text
Weather-App/
│
├── weather.py                 # Main Flask application
├── saved_weather.db           # SQLite database (auto-created on first run)
├── requirements.txt           # Python dependencies
│
├── templates/                 # HTML pages
│   ├── index1.html            # Saved locations + overview
│   └── index2.html            # Detailed weather result page
│
└── static/                    # CSS / images (optional)
    └── style.css
```

---

## ⚙️ Installation & Setup

### 1) Create and Activate Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2) Install Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

✅ Required libraries:
- Flask
- requests  
*(sqlite3 comes built-in with Python, so no need to install it separately)*

---

## 🔑 Get WeatherAPI Key

This project uses **WeatherAPI** for real-time weather data.

🔗 Website: https://www.weatherapi.com/

Create an account and copy your API key from the dashboard.

---

## 🛠️ Update API Key in Code

Open `weather.py` and replace:

```python
key = "your-api-key"
```

With your actual key:

```python
key = "YOUR_REAL_API_KEY_HERE"
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python weather.py
```

Then open in browser:

✅ **http://127.0.0.1:5000/**

---

## 🖼️ Results / Output Screenshots

<p align="center"> <img src="images/homepage.png" width="48%" alt="Homepage - Saved Locations" /> <img src="images/weatherpage.png" width="48%" alt="Weather Page - Detailed Forecast" /> </p>

<p align="center"> <strong>🏠 Dashboard & Saved Locations</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>🌤️ Detailed Weather Insights</strong> </p>

<p align="center"> <em>The homepage manages your persistent locations, while the weather page provides a deep dive into temperature, humidity, and wind metrics.</em> </p>

---

## 👨‍💻 Author

**Nithish Gowda H N**  
B.Tech (Hons.) CSE – AI & ML Major

**Nandan**  
B.Tech (Hons.) CSE – Cloud & Full Stack Major

**Pratham Rajesh Vernekar**  
B.Tech (Hons.) CSE – Cloud & Full Stack Major
