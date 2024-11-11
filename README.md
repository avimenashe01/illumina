# Store API

This is a simple key-value store API that provides basic operations like setting, getting, deleting, and checking for keys. It is built using Flask for the backend and supports interaction through RESTful HTTP methods.


## Features

- **Set a key-value pair**: `POST /api/store/set`
- **Get the value of a key**: `GET /api/store/get?key=<key>`
- **Delete keys**: `DELETE /api/store/delete`
- **Check if keys exist**: `GET /api/store/exists`
- **Increment a key value**: `POST /api/store/incrby`


## Architecture

The application is built using a Service-Oriented Architecture (SOA), with clear separation between different components:

- **Controller Layer**: Handles HTTP requests and routes them to the appropriate service. (Located in `/svc/controllers/`)
- **Service Layer**: Contains the business logic for handling operations like set, get, delete, and increment. (Located in `/svc/services/`)
- **Core Layer**: Manages data storage and retrieval (in-memory store). (Located in `/svc/core/`)


## Setup and Usage

### Requirements

- Python 3.9+
- Docker (for containerization)

### Running the application

You can run the application either using Docker or locally.

#### With Docker Compose:

```bash
# Build the app and start the services (including Flask app)
docker-compose up --build
```


## Example API calls
Set a key-value pair

```bash
curl -X POST http://localhost:5000/api/store/set -H "Content-Type: application/json" -d "{\"key\": \"name\", \"value\": \"John\"}"
```

Get a key-value pair
```bash
curl curl http://localhost:5000/api/store/get?key=name
```

Increment value of key
```bash
curl -X POST http://localhost:5000/api/store/incrby -H "Content-Type: application/json" -d "{\"key\": \"counter\", \"increment\": 5}"
```

Delete keys
```bash
curl -X DELETE http://localhost:5000/api/store/delete -H "Content-Type: application/json" -d "{\"keys\": [\"name\"]}"
```

Check if keys exist
```bash
curl "http://localhost:5000/api/store/exists?keys=name,counter"
```



## Feedback

- **Time Spent**: It took me approximately 2 hours in total to complete the exercise:
  - **API implementation (1 hour)**: Developing the core functionality of the API.
  - **Testing and debugging (30 minutes)**: Writing test cases and resolving issues.
  - **Docker setup and final adjustments (30 minutes)**: Setting up Docker for the application and writing the necessary configuration.

- **Comments**: The exercise is well-structured and provides a clear set of tasks to be completed. The documentation was helpful, and the implementation itself is simple yet effective for learning the process of building APIs and managing a basic key-value store.