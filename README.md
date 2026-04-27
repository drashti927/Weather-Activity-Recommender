# Weather-Activity-Recommender System

## Project Overview
This system is a microservice-based REST application that provides personalized activity recommendations based on real-time weather data and user preferences.

## Architecture
- User Interface (CLI)
- Recommendation Service (Main Controller)
- Weather Service (External API integration)
- User Profile Service (Database simulation)

## Communication
- REST API (HTTP)
- JSON format

## Services

### Weather Service
- Fetches real-time weather using OpenWeatherMap API

### User Profile Service
- Stores user preferences (indoor/outdoor + activities)

### Recommendation Service
- Combines weather + user data
- Generates recommendations

---

## How to Run
### Step 1: Install dependencies
```bash
pip install flask requests
