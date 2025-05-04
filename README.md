# FastAPI MySQL CRUD Application

A simple CRUD application with Users and Tasks management using FastAPI and MySQL.

## Features
- Create, Read, Update, Delete Users
- Create, Read, Update, Delete Tasks
- Automatic task cleanup when deleting users (cascade delete)
- List all tasks with associated user information
- MySQL database integration with SQLAlchemy ORM
- Input validation using Pydantic schemas

## Prerequisites
- Python 3.11+ (recommended)
- MySQL Server 8.0+
- Git (optional)
- VS Code (recommended)

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/tstazbid/fastapi-crud.git
cd fastapi-crud
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Database Setup
1. Start MySQL Server (XAMPP/WAMP or MySQL Service)
2. Create database:

    ```sql
    CREATE DATABASE fastapi_crud;
    ```
3. Tables will be automatically created when you run the application


### 5. Configure Environment
Create .env file in project root:

```env
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/fastapi_crud
```

### 6. Run Application
```bash
uvicorn app.main:app --reload
```
The API will be available at: http://localhost:8000

## API Endpoints

| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| POST   | `/users/`               | Create new user              |
| GET    | `/users/{user_id}`      | Get user details             |
| PUT    | `/users/{user_id}`      | Update user details          |
| DELETE | `/users/{user_id}`      | Delete user and their tasks  |
| POST   | `/users/{user_id}/tasks/` | Create task for user       |
| GET    | `/tasks/`               | List all tasks with users    |
| PUT    | `/tasks/{task_id}`      | Update task                  |
| DELETE | `/tasks/{task_id}`      | Delete task                  |

## Project Structure

```text
fastapi-crud/
├── app/
│   ├── __init__.py
│   ├── main.py       # FastAPI routes and endpoints
│   ├── database.py   # Database connection setup
│   ├── models.py     # SQLAlchemy database models
│   ├── schemas.py    # Pydantic schemas for data validation
│   └── crud.py       # CRUD operations implementation
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## Troubleshooting

### Common Issues

**MySQL Connection Error:**
- Verify MySQL service is running
- Check credentials in `.env` file
- Confirm database `fastapi_crud` exists

**Module Not Found:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**Python Version Issues:**
- Use Python 3.11 if encountering SQLAlchemy errors

**Port Conflicts:**
```bash
# Check port usage
netstat -ano | findstr :8000
netstat -ano | findstr :3306
```

## Development

- **Auto-reload:** Use `--reload` flag for live code updates during development
- **Testing:** Utilize Swagger UI at `/docs` for endpoint testing
- **Logs:** Monitor terminal output for real-time error tracking


> **Note:** Replace `yourpassword` in `.env` with your actual MySQL root password.  
