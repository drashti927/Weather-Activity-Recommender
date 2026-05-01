import requests

def main():

    user_id = input("Enter user ID: ")
    city = input("Enter city: ")

    # auto-create user for simplicity
    requests.post("http://localhost:5001/user", json={
        "userId": user_id,
        "indoorPreferred": True,
        "activities": ["museum", "movies"]
    })

    res = requests.get(
        f"http://localhost:5002/recommend?userId={user_id}&city={city}"
    ).json()

    print("\n--- RESULT ---")
    print("Location:", res["location"])
    print("Recommendation:", res["recommendation"])

if __name__ == "__main__":
    main()
