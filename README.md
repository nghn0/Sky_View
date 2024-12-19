# Sky_View - Weather web application
- **Description**: A weather forecasting web application built using Flask that allows users to fetch real-time weather data. The app integrates with the WeatherAPI to provide current weather information, such as temperature, wind speed, humidity, and more. Users can input a city name or geographic coordinates (latitude and longitude) to get weather details, which can be saved or deleted from a SQLite database.
- **Tech Stack**: Python, Flask, SQLite, Requests
- **Key Features**:
  - **Weather Data Fetching**: Users can get current weather for any location using city name or geographic coordinates.
  - **Data Display**: Displays various weather details including temperature, wind speed, humidity, and more.
  - **Database Integration**: Allows saving frequently used locations (with latitude and longitude) into a SQLite database and retrieving them easily.
  - **City Name Links**: Users can click on city names to quickly fetch weather info for that specific location.
  - **Location Management**: Users can save or delete cities from their saved list for quick access to their weather information.

- **Future Improvements**:
  - Enhance the user interface with modern design elements for better user experience.
  - Add forecast features to provide weather predictions for multiple days.
  - Allow users to customize the units of measurement (e.g., Celsius to Fahrenheit).
  - Provide option for users to set their preferred unit system for all future queries (e.g., metric, imperial).
