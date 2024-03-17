## API Documentation

This document provides an overview of the endpoints available in the API.

### Users

#### Create User
- **Endpoint:** `POST /users/`
- **Description:** Creates a new user.
- **Request Body:** JSON object representing user details.
- **Response:** JSON object representing the created user.
- **Example:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "hobby": "Reading"
  }
  ```

#### Read User
- **Endpoint:** `GET /users/{user_id}`
- **Description:** Retrieves a user by their ID.
- **Response:** JSON object representing the user.
- **Example Response:**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "hobby": "Reading"
  }
  ```

#### Get Users
- **Endpoint:** `GET /users/`
- **Description:** Retrieves a list of users. Can be filtered by hobby.
- **Query Parameters:**
  - `by_hobby` (optional): Filter users by hobby.
- **Response:** List of JSON objects representing users.
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "age": 30,
      "hobby": "Reading"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane@example.com",
      "age": 25,
      "hobby": "Gardening"
    }
  ]
  ```

### Activities

#### Create Activity
- **Endpoint:** `POST /activities/`
- **Description:** Creates a new activity.
- **Request Body:** JSON object representing activity details.
- **Response:** JSON object representing the created activity.
- **Example:**
  ```json
  {
    "name": "Running",
    "description": "Morning run in the park",
    "date": "2024-03-17T08:00:00",
    "location": "Central Park"
  }
  ```

#### Get Activities
- **Endpoint:** `GET /activities/`
- **Description:** Retrieves a list of activities.
- **Query Parameters:**
  - `skip` (optional): Number of records to skip.
  - `limit` (optional): Maximum number of records to return.
- **Response:** List of JSON objects representing activities.
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Running",
      "description": "Morning run in the park",
      "date": "2024-03-17T08:00:00",
      "location": "Central Park"
    },
    {
      "id": 2,
      "name": "Hiking",
      "description": "Exploring the mountains",
      "date": "2024-03-18T10:00:00",
      "location": "Mountain Range"
    }
  ]
  ```

#### Get Activity by ID
- **Endpoint:** `GET /activities/{activity_id}`
- **Description:** Retrieves an activity by its ID.
- **Response:** JSON object representing the activity.
- **Example Response:**
  ```json
  {
    "id": 1,
    "name": "Running",
    "description": "Morning run in the park",
    "date": "2024-03-17T08:00:00",
    "location": "Central Park"
  }
  ```

#### Get Recent Activities
- **Endpoint:** `GET /recent_activities/`
- **Description:** Retrieves a list of recent activities (within one week).
- **Response:** List of JSON objects representing recent activities.
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Running",
      "description": "Morning run in the park",
      "date": "2024-03-17T08:00:00",
      "location": "Central Park"
    },
    {
      "id": 2,
      "name": "Cycling",
      "description": "Evening bike ride",
      "date": "2024-03-16T18:00:00",
      "location": "City Streets"
    }
  ]
  ```
