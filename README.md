# Django Weather Application

This project is a Django web application that allows users to search for weather forecasts by city and provides autocomplete suggestions. It also tracks search history.

## Features

- **City Weather Forecast**: Get weather forecasts for any city.
- **Autocomplete Search**: Auto-suggest city names as you type.
- **Search History**: View and access previously searched cities.
- **API Integration**: Uses OpenWeatherMap and Open-Meteo API for weather data.

## Requirements

- Python 3.8 or higher
- Django 4.x
- Requests 2.28.0
- Django Widget Tweaks 1.4.12
- Django Debug Toolbar 4.0.0

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/yourprojectname.git
   cd yourprojectname
   ```

2. **Create a Virtual Environment**

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```


3. **Install Dependencies**
   
    ```bash
    pip install -r requirements.txt
   ```

5. **Apply Migrations**

 ```bash
    python manage.py migrate
  ```
6. **Run the App**

```bash
    python manage.py runserver
  ```
## API endpoints

### City Autocomplete

- **Endpoint**: `GET api/city-autocomplete/`
- **Description**: Retrieve a list of city names and details matching the search term for autocomplete suggestions.
- **Parameters**:
  - `term` (string): The term to search for city names. Example: `London`.
 
### Weather Forecast

- **Endpoint**: `POST /api/weather/`
- **Description**: Weather forecast details for the specified city.
- **Parameters**:
  - city (string) - The name of the city for which to get the weather forecast.


## Acknowledgements

- **Django** - The web framework used.
- **OpenWeatherMap** - Provides weather data.
- **Open-Meteo** - Provides all cities data.
- **jQuery UI** - Used for autocomplete functionality.



