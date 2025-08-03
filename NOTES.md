Project Overview:

This project implements a simple URL shortening service using Flask, supporting three main features:

Shorten URL Endpoint: Receives a long URL and returns a unique 6-character short code and corresponding short URL.

Redirect Endpoint: Redirects requests from short codes to the original URLs while incrementing click counts.

Analytics Endpoint: Provides access to click count, creation timestamp, and original URL by short code.

The application uses an in-memory data store for URL mappings with thread-safe access, validating URLs before shortening, and clean error handling with appropriate HTTP status codes.
_____________________________________________________________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________________________________________________

Implementation Approach:

Storage: Implemented as a Python dictionary wrapped with a threading.Lock to handle concurrent request safety.

Short Code Generation: Random 6-character alphanumeric strings generated with collision checks against existing codes.

URL Validation: Used Python’s built-in urllib.parse to ensure inputs are valid HTTP/HTTPS URLs.

API Design: Followed REST principles; all endpoints return consistent JSON responses and status codes.

Testing: Created 5+ tests covering core functionality and error conditions, using pytest with Flask’s test client.

Project Structure: Logic split into multiple modules for models, utilities, and API routes for clarity and maintainability.
____________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________

Tools and Libraries:

Python 3.13

Flask — Web framework for implementing API endpoints.

pytest — Testing framework used to write and run test cases.

Standard Python library modules (urllib.parse, threading, random, string, datetime).
____________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________

Used ChatGPT as a coding assistant to:

Help design the overall architecture of the URL shortener.

Generate initial code templates for endpoint implementations.

Write utility functions for URL validation and short code generation.

Draft unit tests covering core API flows and error cases.

All AI-generated code was carefully reviewed, modified, and integrated to fit project requirements and personal coding style.

No code was blindly accepted; all logic and structure decisions were validated independently.
____________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________
Limitations and Future Work:

The in-memory store means all data will be lost on server restart; persistent storage could be added for production.

Password or user authentication is not implemented as per assignment scope.

The short code generator uses random selection with collision checks; a more robust approach may be necessary at scale.

URL validation is basic and can be improved with specialized libraries.

Additional logging, monitoring, and error tracking are not included.
____________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________
Install dependencies with:

pip install -r requirements.txt

Run the Flask application:

python -m flask --app app.main run

Run tests with:

pytest
