#!/bin/bash

# Set a key-value pair
echo "Setting key 'name' with value 'John'..."
curl -X POST http://localhost:5000/api/store/set -H "Content-Type: application/json" -d "{\"key\": \"name\", \"value\": \"John\"}"

# Get the key-value pair
echo "Getting value for key 'name'..."
curl curl http://localhost:5000/api/store/get?key=name

# Increment the value of a key (if applicable)
echo "Incrementing key 'counter' by 5..."
curl -X POST http://localhost:5000/api/store/incrby -H "Content-Type: application/json" -d "{\"key\": \"counter\", \"increment\": 5}"

# Delete keys
echo "Deleting key 'name'..."
curl -X DELETE http://localhost:5000/api/store/delete -H "Content-Type: application/json" -d "{\"keys\": [\"name\"]}"

# Check if keys exist
echo "Checking if 'name' and 'counter' exist..."
curl "http://localhost:5000/api/store/exists?keys=name,counter"