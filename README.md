## API Endpoints

- `GET /api/v1/brands`: Retrieve all brands
- `GET /api/v1/brands/<id>`: Retrieve a specific brand by ID
- `GET /api/v1/manufacturers`: Retrieve all manufacturers
- `GET /api/v1/manufacturers/<id>`: Retrieve a specific manufacturer by ID

## Admin Panel

The admin panel is accessible at:

- `/client/brands`: View and add brands
- `/client/manufacturers`: View and add manufacturers

## Install the required packages:
- `pip install -r requirements.txt`

## Initialize the database:
- `flask --app run:app db init` 
- `flask --app run:app db migrate `
- `flask --app run:app db upgrade`

## Run the app
- `flask --app run:app run --debug`