## Setup Instructions

1. Clone the repository.
2. Copy `.env.example` to `.env` and add your database credentials

## Deployed Version

You can view and interact with the API documentation at:

[Pereval REST API Documentation](https://pereval-rest-api.onrender.com/docs)



This API allows users to interact with the Pereval platform by submitting data about mountain passes.

Base URL
Base URL: https://pereval-rest-api.onrender.com/

You can access the interactive Swagger documentation here: Pereval REST API Docs
Endpoints Overview:
1. Get Perevals by User ID
Endpoint: /users/{user_id}/perevals/
Method: GET
Description: Retrieves all perevals (mountain passes) submitted by a specific user.
Path Parameters:
user_id (int): ID of the user.
Response Example:
{
  "state": 1,
  "perevals": [
    {
      "id": 1,
      "name": "Pereval Name",
      "coordinates": {
        "latitude": 45.0,
        "longitude": 7.0,
        "height": 2000
      }
    },
    ...
  ]
}

2. Submit New Pereval
Endpoint: /perevals/
Method: POST
Description: Submit a new pereval to the database.
Request Body Example:
{
  "user_id": 1,
  "name": "New Pereval",
  "latitude": 45.0,
  "longitude": 7.0,
  "height": 2000
}
Response Example:
{
  "state": 1,
  "message": "Pereval submitted successfully."
}

3. Get Perevals by User email
Endpoint: /users/{email}/perevals/
Method: GET
Description: Retrieves all perevals (mountain passes) submitted by a specific user.
Path Parameters:
email (str): Email of the user.
Response Example:

4. Update Pereval (Partial Update)
Endpoint: /perevals/{pereval_id}/
Method: PATCH
Description: Updates an existing pereval entry with partial data. Only the fields provided in the request body will be updated, leaving the rest unchanged.
Path Parameters:
pereval_id (int): The ID of the pereval to update.
Request Body Example:
{
  "name": "Updated Pereval Name",
  "latitude": 46.0
}
You can include any of the following fields in the request:
name (string): New name of the pereval.
latitude (float): Updated latitude of the pereval.
longitude (float): Updated longitude of the pereval.
height (int): Updated height of the pereval.
Response Example:
{
  "state": 1,
  "message": "Pereval updated successfully."
}
Error Response Example:
{
  "state": 0,
  "error": "Pereval not found."
}
Rules for PATCH requests:
Only the fields that need updating should be included in the request body.
If an invalid pereval_id is provided, the server will return an error.