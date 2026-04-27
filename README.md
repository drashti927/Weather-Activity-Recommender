# Weather-Activity-Recommender System

## Project Overview
This system is a microservice-based REST system that provides personalized activity recommendations based on real-time weather data and user preferences. 

It demonstates distributed system design using REST APIs and JSON communication.

## Architecture
This system follows a microservice architecture where each component is independent and communicates via REST APIs.

- User Interface (CLI Client)
- Recommendation Service (Main Orchestrator)
- Weather Service (External API / Weather Data Provider)
- User Profile Service (User Preferences Storage)

All services communicate using HTTP requests and exchange data in JSON format.

## Architecture Diagram

```mermaid
flowchart LR

UI[User Interface (CLI)]
REC[Recommendation Service]
WEA[Weather Service]
USR[User Profile Service]

UI <--> REC
REC <--> WEA
REC <--> USR
```

## Communication
- REST API (HTTP)
- JSON format

## System Flow

1. User enters city and user ID in CLI
2. UI sends request to Recommendation Service
3. Recommendation Service calls:
   - Weather Service
   - User Profile Service
4. Services return JSON responses
5. Recommendation Service generates final output
6. Result is displayed in CLI

### Weather Service
- Fetches real-time weather using OpenWeatherMap API

Endpoint:
GET /weather?city=<city>

### User Profile Service
- Stores user preferences (indoor/outdoor + activities)

Endpoints:
GET /user/<id>
POST /user/<id>

### Recommendation Service
- Combines weather + user data
- Generates recommendations

Endpoint:
GET /recommend?userId=<id>&city=<city>

### 4. UI Client
- Simple CLI client to interact with system.
---

## How to Run
### Step 1: Install dependencies
```bash
pip install flask requests
```
### Step 2: Run Weather Service (in separate terminal)
Start Weather Service:
```bash
python src/weather_service.py
```
### Step 3: Run User Service (in separate terminal)
```bash
python src/user_service.py
```
### Step 4: Run Recommendation Service (in separate terminal)
```bash
python src/recommendation_service.py
```
### Step 5: Run UI Client (in separate terminal)
```bash
python src/ui.py
```
## Testing
The system was tested using:

- Manual CLI testing
- REST API testing via browser/Postman
- Service-to-service communication validation
