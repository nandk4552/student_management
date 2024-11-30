
```
# Student Management System (Backend API)

This is a **Student Management System Backend API** built using **FastAPI** and **MongoDB Atlas**. It allows you to create, read, update, and delete student records, with filtering capabilities based on country and age. The project is deployed and accessible via Render.

---

## Features

- Create a student with name, age, and address (city and country).
- List students with optional filters (`country`, `age`).
- Fetch details of a student by their unique ID.
- Update a student's details by their ID.
- Delete a student by their ID.

---

## Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB Atlas (M0 Free Cluster)
- **Deployment**: Render

---

## Installation

### Prerequisites

- Python 3.9 or higher
- MongoDB Atlas account
- Docker (optional, for containerized setup)

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nandk4552/student_management
   cd student_management
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On macOS/Linux
   venv\Scripts\activate       # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB Atlas**:
   - Create a free cluster on MongoDB Atlas.
   - Create a database named `student_management` and a collection named `students`.
   - Whitelist your IP or use `0.0.0.0/0` for testing purposes.
   - Get the connection string and add it to a `.env` file:
     ```
     MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority
     ```

5. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Deployment on Render

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Render**:
   - Go to [Render](https://render.com).
   - Create a new **Web Service** and connect your GitHub repository.
   - Set the build command:
     ```bash
     pip install -r requirements.txt
     ```
   - Set the start command:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```
   - Add environment variables like `MONGO_URI`.

---

## API Endpoints

### Base URL
- Local: `http://127.0.0.1:8000`
- Deployed: `https://student-management-q5q3.onrender.com`

### Endpoints

1. **Create Student**
   - **Method**: `POST`
   - **Endpoint**: `/students`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "age": 21,
       "address": {
         "city": "New York",
         "country": "USA"
       }
     }
     ```
   - **Response**:
     ```json
     {
       "id": "63f1d7e2f19c8a9c1b234567"
     }
     ```

2. **List Students**
   - **Method**: `GET`
   - **Endpoint**: `/students`
   - **Query Parameters**:
     - `country` (optional): Filter by country.
     - `age` (optional): Filter by age greater than or equal to the value.
   - **Response**:
     ```json
     {
       "data": [
         {
           "id": "63f1d7e2f19c8a9c1b234567",
           "name": "John Doe",
           "age": 21,
           "address": {
             "city": "New York",
             "country": "USA"
           }
         }
       ]
     }
     ```

3. **Fetch Student by ID**
   - **Method**: `GET`
   - **Endpoint**: `/students/{id}`
   - **Response**:
     ```json
     {
       "id": "63f1d7e2f19c8a9c1b234567",
       "name": "John Doe",
       "age": 21,
       "address": {
         "city": "New York",
         "country": "USA"
       }
     }
     ```

4. **Update Student**
   - **Method**: `PATCH`
   - **Endpoint**: `/students/{id}`
   - **Request Body**:
     ```json
     {
       "name": "Jane Doe",
       "address": {
         "city": "Los Angeles"
       }
     }
     ```
   - **Response**: Status `204 No Content`.

5. **Delete Student**
   - **Method**: `DELETE`
   - **Endpoint**: `/students/{id}`
   - **Response**:
     ```json
     {
       "message": "Student deleted successfully"
     }
     ```

---

## Future Enhancements

- Add user authentication and authorization.
- Implement pagination for listing students.
- Add validation for country and city fields (e.g., predefined list).

---

## License

This project is licensed under the MIT License.

---

## Author

- **Nand Kishore Devarla**
- [GitHub](https://github.com/nandk4552)
- [Render Deployment](https://student-management-q5q3.onrender.com)
```