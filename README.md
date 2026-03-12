# Weather API (FastAPI)


This project is a **FastAPI-based backend service** that retrieves weather data from an external API and improves performance using **database caching**. The API checks whether weather information for a city already exists in the database and returns cached data if it is still valid. If the cache has expired or does not exist, the service fetches fresh data from the external weather provider and stores it in the database.

## Features

* Asynchronous API built with FastAPI
* Integration with a third-party weather service
* Database caching to reduce external API calls
* Cache expiration using timestamp logic
* HTTPS support for secure communication
* Clean modular project structure
* Environment-based configuration for API keys

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* HTTPX (async HTTP requests)

## How It Works

1. A client requests weather data for a specific city.
2. The API checks the database for cached weather data.
3. If cached data exists and is still valid, it returns the cached result.
4. If no valid cache exists, the API fetches data from the external weather service.
5. The new data is stored in the database and returned to the client.

## Example Endpoint

GET /weather/{city}

Example:

GET /weather/London

## Running the Project


Start the server:

uvicorn main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs

## Project Structure

weather/
├── main.py
├── weather_service.py
├── models.py
├── database.py
├── config.py


## Future Improvements

* Redis-based caching
* Background cache refresh
* API monitoring and metrics
* Deployment using Docker and Nginx
