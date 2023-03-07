# FastAPI Auth Template

This is a template project for building a RESTful API with FastAPI, Postgres, SQLAlchemy and JWT token-based authentication.

Requirements
The following dependencies are required to run this project:

1. Python 3.7 or above
2. Postgres
3. pip

You can install Python and pip from [python.org](https://python.org) and Postgres from [postgres.org](https://postgres.org).

### Installation

#### Clone this repository:

```
git clone https://github.com/olsihoxha/fastapi-auth-template.git`
cd fastapi-auth-template
```


#### Install the required Python packages:

`pip install -r requirements.txt`


#### Create a .env file in the root directory of the project and add the following environment variables:

```
DATABASE_URL=postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
JWT_SECRET={SECRET_KEY}
```
___Replace {DB_USER}, {DB_PASSWORD}, {DB_HOST}, {DB_PORT}, {DB_NAME} and {SECRET_KEY} with your own values.___

#### Create the database tables:
`python app/services.py`

#### Running the Server

**To start the server, run the following command:**

```
uvicorn app.main:app --reload
This will start the server at http://localhost:8000.
```



# License
This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.
