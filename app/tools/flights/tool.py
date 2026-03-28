def search_flights(origin: str, destination: str, date: str) -> list[dict]:
    """Searches for flights between origin and destination on a given date.
    
    Args:
        origin: The departure city.
        destination: The arrival city.
        date: The date of travel in YYYY-MM-DD format.
        
    Returns:
        A list of dictionaries representing flight options.
    """
    # Mock data for demonstration purposes
    return [
      {"flight_number": "BA101", "origin": origin, "destination": destination, "price": "$1250", "duration": "14h 30m"},
      {"flight_number": "JAL202", "origin": origin, "destination": destination, "price": "$1100", "duration": "15h 05m"},
      {"flight_number": "DL303", "origin": origin, "destination": destination, "price": "$1350", "duration": "13h 45m"}
    ]
