import json

FILENAME = "data.json"

def load_all_users():
    """Return a dict mapping usernames -> streaks.
    Accept the old single-user format {"username":..., "streak":...} for backward compatibility.
    """
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            # handle legacy single-user file
            if isinstance(data, dict) and "username" in data and "streak" in data and len(data) == 2:
                return {data["username"]: data["streak"]}
            # assume file is already a mapping username->streak
            if isinstance(data, dict):
                return data
            return {}
    except FileNotFoundError:
        return {}

def save_all_users(users):
    """Write the full users mapping to disk."""
    with open(FILENAME, "w") as f:
        json.dump(users, f, indent=2)

def save_data(username, streak):
    """Add or update a user's streak in the file (creates file if missing)."""
    users = load_all_users()
    users[username] = streak
    save_all_users(users)

def get_user_streak(username, default=0):
    """Get a single user's streak; returns default if user not present."""
    users = load_all_users()
    return users.get(username, default)


save_data("gkik", 7)