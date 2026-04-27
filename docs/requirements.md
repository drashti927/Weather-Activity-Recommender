# 🌦️ Weather & Activity Recommender System

**Course:** Software Engineering
**Project Type:** Individual Project
**Author:** Drashti Shah
**Date:** February 17, 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines the software requirements for the Weather & Activity Recommender System, a microservice-based application that retrieves live weather data from an external REST API and generates personalized activity recommendations based on user preferences.

## 1.2 Scope

The system will:

* Fetch real-time weather data from an external API
* Store user activity preferences (indoor/outdoor, favorite activities)
* Generate daily activity recommendations
* Display weather information and recommendations via a user interface

The system uses REST APIs and JSON for inter-service communication.

## 1.3 System Overview

The system follows a microservice architecture consisting of:

* Weather Service
* User Profile Service
* Recommendation Service
* User Interface (Web UI or CLI)

Each service communicates via REST endpoints using JSON. The Weather Service integrates with an external weather provider (e.g., OpenWeatherMap).

## 1.4 Assumptions and Dependencies

### Assumptions

* Users provide valid city names
* External weather API is available
* Internet connection is stable

### Dependencies

* External Weather API
* Database system
* HTTP/REST infrastructure

---

# 2. Functional Requirements

## 2.1 Weather Service Requirements

* [WRS-1] Retrieve current weather data from an external API
* [WRS-2] Normalize weather data into temperature and condition fields
* [WRS-3] Return weather data in JSON format
* [WRS-4] Handle external API errors gracefully

### Example Response

```json
{
  "location": "Pittsburgh, PA",
  "tempC": 18,
  "condition": "rain"
}
```

---

## 2.2 User Profile Service Requirements

* [URS-1] Create a user profile
* [URS-2] Store indoor/outdoor preference
* [URS-3] Store a list of preferred activities
* [URS-4] Update user preferences
* [URS-5] Retrieve user preferences by user ID

### Example

```json
{
  "userId": "1",
  "indoorPreferred": true,
  "activities": ["museum", "board_games"]
}
```

---

## 2.3 Recommendation Service Requirements

* [RS-1] Accept user ID and city as input
* [RS-2] Retrieve weather data from Weather Service
* [RS-3] Retrieve user preferences from User Profile Service
* [RS-4] Generate activity recommendations based on weather condition and preferences
* [RS-5] Return recommendations in JSON format

### Example Response

```json
{
  "userId": "1",
  "location": "Pittsburgh, PA",
  "recommendation": "Visit the science museum (rainy + indoor preference)"
}
```

---

## 2.4 User Interface Requirements

* [UI-1] Allow users to enter a city name
* [UI-2] Display temperature and weather condition
* [UI-3] Display generated recommendation
* [UI-4] Allow users to update their activity preferences

---

# 3. Non-Functional Requirements

## 3.1 Usability

* [NFR-1] Interface shall be simple and intuitive
* [NFR-2] Display clear error messages

## 3.2 Performance

* [NFR-3] Weather data shall be retrieved within 3 seconds
* [NFR-4] Recommendation generation shall complete within 2 seconds

## 3.3 Reliability

* [NFR-5] Handle external API failures without crashing
* [NFR-6] Validate user input before processing

## 3.4 Data Storage

The system shall store user data with:

* userId (Primary Key)
* indoorPreferred (Boolean)
* activities (List/Array)

---

# 4. System Architecture Diagram

A diagram of weather service

![My Diagram](images/SystemArchitectureDiagram.png)

---

# 5. Verification

The system will be verified through:

* Unit testing of each microservice
* API testing using Postman
* Integration testing between services
* Manual UI testing

### Test Cases Will Validate:

* Weather retrieval
* Preference storage
* Recommendation logic correctness
* Error handling
