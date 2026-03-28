def search_hotels(city: str, check_in: str, check_out: str, budget_category: str = "mid-range") -> list[dict]:
    """Searches for hotels in a city for specified dates and budget.
    
    Args:
        city: Destination city name.
        check_in: Check-in date (YYYY-MM-DD).
        check_out: Check-out date (YYYY-MM-DD).
        budget_category: One of 'budget', 'mid-range', or 'luxury'.
        
    Returns:
        A list of dictionaries representing hotel options.
    """
    # Mock data for demonstration purposes
    if budget_category == "budget":
        return [
            {"hotel_id": "HTL-001", "name": "Backpackers Haven", "price_per_night": "$45", "rating": "3.5/5"},
            {"hotel_id": "HTL-002", "name": "Cozy Hostel", "price_per_night": "$55", "rating": "3.8/5"}
        ]
    elif budget_category == "luxury":
         return [
            {"hotel_id": "HTL-101", "name": "Grand Palace Hotel", "price_per_night": "$450", "rating": "4.9/5"},
            {"hotel_id": "HTL-102", "name": "Royal Suite Residences", "price_per_night": "$550", "rating": "5.0/5"}
        ]
    else:
        return [
            {"hotel_id": "HTL-201", "name": "Park View Inn", "price_per_night": "$120", "rating": "4.2/5"},
            {"hotel_id": "HTL-202", "name": "Traveler's Den", "price_per_night": "$140", "rating": "4.1/5"}
        ]
