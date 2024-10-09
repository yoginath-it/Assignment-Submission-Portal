# Assignment Submission Portal

The Assignment Submission Portal is a web-based application designed to facilitate the submission and review of assignments. Users can register, log in, and upload assignments, while admins can review and manage these assignments.
## Technologies Used

- Flask: A micro web framework for Python.
- MongoDB: A NoSQL database for storing user and assignment data.
- Python 3.13.0: The programming language used for development.
- Flask-PyMongo: An extension that simplifies working with MongoDB in Flask.
## Prerequisites

- Python 3.13.0 or higher
- MongoDB installed and running
- Flask and other dependencies installed (see `requirements.txt`)

## Installation

Clone the repository:


```bash
git clone https://github.com/yoginath-it/Assignment-Submission-Portal.git
cd Assignment-Submission-Portal

```
Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate

```
Install the dependencies:

```bash
pip install -r requirements.txt

```
Start the Flask application:
```bash
python app.py

```
## User API Endpoints

## Register User

- URL: ```/user/register```

- Method: ```POST```

- Request Body:
```bash
{
  "username": "string",
  "password": "string"
}
```

- CURL:
```bash
curl -X POST http://127.0.0.1:5000/user/register -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass123"}'
```

- Responses:
    
    201 Created: User registered successfully.

    400 Bad Request: Invalid input.

## Login User

- URL: ```/user/login```

- Method: ```POST```
- CURL:
```bash
curl -X POST http://127.0.0.1:5000/user/login -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass123"}'

```
- Request Body:
```bash
{
  "username": "string",
  "password": "string"
}
```
- Responses:
    
    200 OK: Login successful.

    401 Unauthorized: Invalid credentials.

## Upload Assignment

- URL: ```/user/upload```

- Method: ```POST```

- Request Body:
```bash
{
  "userId": "string",
  "task": "string",
  "admin": "string"
}

```
- CURL:
```bash
curl -X POST http://127.0.0.1:5000/user/upload -H "Content-Type: application/json" -d '{"userId": "user1", "task": "Hello World", "admin": "admin1"}'

```
- Responses:
    
    201 Created: Assignment uploaded successfully.

    400 Bad Request: Invalid input.

## Fetch Admins


- URL: ```/user/admins```

- Method: ```GET```
- CURL:
```bash
curl -X GET http://127.0.0.1:5000/user/admins -H "Content-Type: application/json"

```
- Responses:
    
    201 Created: Returns a list of all admins.

    400 Bad Request: No admins found.

## Admin Endpoints
## Upload Assignment


- URL: ```/admin/register```

- Method: ```POST```

- Request Body:
```bash
{
  "username": "string",
  "password": "string"
}

```
- CURL:
```bash
curl -X POST http://127.0.0.1:5000/admin/register -H "Content-Type: application/json" -d '{"username": "admin1", "password": "pass123"}'

```
- Responses: 
    201 Created: Admin registered successfully.

    400 Bad Request: Invalid input.

## Login Admin

- URL: ```/admin/login```

- Method: ```POST```

- Request Body:
```bash
{
  "username": "string",
  "password": "string"
}
```
- CURL:
```bash
curl -X POST http://127.0.0.1:5000/admin/login -H "Content-Type: application/json" -d '{"username": "admin1", "password": "pass123"}'

```
- Responses:
    
    200 OK: Login successful.

    401 Unauthorized: Invalid credentials.

## View Assignments

- URL: ```/admin/assignments```

- Method: ```GET```
- CURL:
```bash
curl -X GET http://127.0.0.1:5000/admin/assignments -H "Content-Type: application/json"

```
- Responses:

    200 OK: Returns a list of assignments tagged to the admin.

    404 Not Found: No assignments found.

## Accept Assignment

- URL: ```/admin/assignments/<assignment_id>/accept```

- Method: ```POST```
- CURL:
```bash
curl -X POST http://127.0.0.1:5000/admin/assignments/<assignment_id>/accept

```
- Responses:

    200 OK: Assignment accepted successfully.

    404 Not Found: Assignment not found.

## Accept Assignment

- URL: ```/admin/assignments/<assignment_id>/reject```

- Method: ```POST```
- CURL:
```bash
curl -X POST http://127.0.0.1:5000/admin/assignments/<assignment_id>/reject

```
- Responses:

    200 OK: Assignment rejected successfully.

    404 Not Found: Assignment not found.


## Database Structure
## Users Collection

- username: String

- password: String (hashed)

- role: String (either "user" or "admin")

## Assignments Collection

- userId: String (ID of the user)
- task: String (assignment task)
- admin: String (admin assigned to the task)
- status: String (e.g., "pending", "accepted", "rejected")
## Error Handling
- 400 Bad Request: Indicates a problem with the request data.
- 401 Unauthorized: Invalid credentials provided during login.
- 404 Not Found: The resource requested was not found.
- 500 Internal Server Error: An unexpected error occurred on the server.
## Conclusion
This documentation provides a detailed overview of the Assignment Submission Portal project, including functionality, setup instructions, API endpoints, and error handling. Feel free to extend or modify the documentation as needed.
