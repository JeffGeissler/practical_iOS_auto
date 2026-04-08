def log_meal(payload):
    meal = payload.get("meal", "unknown")

    return {
        "status": "success",
        "message": f"Logged meal: {meal}"
    }
