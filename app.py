import requests

def get_users():
    """Fetches users from a public API and returns the JSON response."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def get_user_names():
    """Extracts user names from the fetched users."""
    try:
        users = get_users()
        return [user['name'] for user in users]
    except Exception as e:
        return str(e)
        
def get_user_count():
    """Returns the count of users."""
    try:
        users = get_users()
        return len(users)
    except Exception as e:
        return str(e)

# Main function for testing
if __name__ == "__main__":
    print("User Names:", get_user_names())
    print("User Count:", get_user_count())

