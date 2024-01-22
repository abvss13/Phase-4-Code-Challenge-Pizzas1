# Flask PROJECT- Superheroes

## Project Description

The Flask Code Challenge - Superheroes is an API for tracking heroes and their superpowers. This project provides a Flask-based backend application with a React frontend to facilitate testing the API's functionality. The goal is to implement various features within the Flask API as outlined in the deliverables section below.

## Author

- Author: Daniel Mararo

## License

This project is licensed under the [MIT License](LICENSE.md).

## Setup

To get started with this project, follow the setup instructions below:

### Backend Setup

1. Install backend dependencies using Pipenv:


   pipenv install 

2. Run database migrations:

   flask db upgrade

3. Seed the database with initial data:


   python app/seed.py

4. Run the Flask API on localhost:5555:

   python app.py

### Frontend Setup

   1. Install frontend dependencies using npm:

    npm install --prefix client

   2. Run the React app on localhost:4000:

    npm start --prefix client

### Testing

You can test your progress using one of the following methods:


    Interact with the API using the React frontend application. 
    
    Use Postman to make requests to the Flask API.

### Models

The project requires creating the following relationships:

    A Hero has many Powers through HeroPower.
    A Power has many Heros through HeroPower.
    A HeroPower belongs to a Hero and belongs to a Power.


### Validations

The project includes the following validations:
HeroPower Model

    strength must be one of the following values: 'Strong', 'Weak', 'Average'.

Power Model

    description must be present and at least 20 characters long.

### Routes

The following routes have been set up in the project. JSON data should be returned in the specified format along with the appropriate HTTP verb.

### GET /heroes

Returns JSON data with hero information in the format:

json

[
  { "id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "id": 3, "name": "Gwen Stacy", "super_name": "Spider-Gwen" }
]

### GET /heroes/:id

    If the Hero exists, returns JSON data in the format below:

json

{
  "id": 1,<br>
  "name": "Kamala Khan",<br>
  "super_name": "Ms. Marvel", <br>
  "powers": [<br>
    {<br>
      "id": 1,<br>
      "name": "super strength",<br>
      "description": "gives the wielder <br>super-human strengths"
    },<br>
 
  ]<br>
}<br>

### GET /powers

Returns JSON data with power information in the format:

json

[
  {
    "id": 1,<br>
    "name": "super strength",<br>
    "description": "gives the wielder super-human strengths"<br>
  },<br>
  {<br>
    "id": 2,<br>
    "name": "flight",<br>
    "description": "gives the wielder the ability to fly through the skies at supersonic speed"<br>
  }<br>
]<br>

### GET /powers/:id

    If the Power exists, returns JSON data in the format below:

json

{
  "id": 1,<br>
  "name": "super strength",<br>
  "description": "gives the wielder super-human strengths"<br>
}<br>

    If the Power does not exist, returns JSON data with an error message and the appropriate HTTP status code.

### PATCH /powers/:id

    This route updates an existing Power. It accepts an object with the following properties in the body of the request:

json

{
  "description": "Updated description"<br>
}

    If the Power exists and is updated successfully (passes validations), it updates the description and returns JSON data in the format below:

json

{
  "id": 1,<br>
  "name": "super strength",<br>
  "description": "Updated description"<br>
}

    If the Power does not exist, returns JSON data with an error message and the appropriate HTTP status code.

    If the Power is not updated successfully (does not pass validations), returns JSON data with an error message and the appropriate HTTP status code.

### POST /hero_powers

    This route creates a new HeroPower associated with an existing Power and Hero. It accepts an object with the following properties in the body of the request:

json

{
  "strength": "Average",<br>
  "power_id": 1,<br>
  "hero_id": 3<br>
}

    If the HeroPower is created successfully, it sends back a response with data related to the Hero.

json

{
  "id": 1,<br>
  "name": "Kamala Khan",<br>
  "super_name": "Ms. Marvel",<br>
  "powers": [<br>
    {<br>
      "id": 1,<br>
      "name": "super strength",<br>
      "description": "gives the wielder super-human strengths"<br>
    },<br>
    {<br>
      "id": 2,<br>
      "name": "flight",<br>
      "description": "gives the wielder the ability to fly through the skies at supersonic speed"<br>
    }<br>
  ]<br>
}<br>

### contact
You can reach me via email <danielmararo1@gmail.com>
