from .client import fetch_weather

def get_weather(city: str) -> dict:
    """Retrieves current weather and forecast for a given city.
    
    Args:
        city: The name of the city (e.g., 'New York', 'Tokyo').
        
    Returns:
        A dictionary containing the current status, weather report, and forecast.
    """
    return fetch_weather(city)
