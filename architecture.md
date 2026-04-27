# System Architecture Design

## Overview
This system uses a microservice architecture where all services communicate via REST APIs using JSON.

## Architecture Diagram

```mermaid
flowchart LR

UI["User Interface (CLI)"]
REC["Recommendation Service"]
WEA["Weather Service"]
USR["User Profile Service"]
API["External Weather API"]
DB[("Database")]

UI --> REC
REC --> WEA
REC --> USR
WEA --> API
USR --> DB

```


## System Flow

UI sends request to Recommendation Service
Recommendation Service calls:
Weather Service
User Profile Service
Weather Service calls external API
User Profile Service accesses database
Recommendation Service returns result to UI

## Key Design Choice

Bidirectional communication ensures request/response flow across all services
