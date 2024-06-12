# Ice Cream Parlor Application

## Description
A simple Python application for managing an ice cream parlor's seasonal flavor offerings, ingredient inventory, customer flavor suggestions, and allergy concerns.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Initialize the database:
    ```sh
    python database.py
    ```

3. Run the application:
    ```sh
    python views.py
    ```

4. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Docker

1. Build the Docker image:
    ```sh
    docker build -t ice_cream_parlor .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:5000 ice_cream_parlor
    ```

## Testing Steps

1. Verify the home page displays the list of seasonal flavors.
2. Use the search functionality to find specific flavors.
3. Add allergens and verify they are recorded correctly.
4. Check the cart functionality.

## SQL Query / ORM Abstraction
Implemented using raw SQL queries in `models.py`.

## Documentation
Inline comments provided in the code for clarity.
