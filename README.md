# Student Record API

A simple and lightweight API built with Python and the Flask framework. This project serves as a basic starting point for creating a web API.

## 🚀 Features
- Provides a single GET endpoint to confirm the API is running.
- Easy to set up and run locally.
- Minimal dependencies.

## 🔧 Installation & Setup

To get a local copy up and running, follow these simple steps.

1.  *Clone the repository*
    sh
    git clone [https://github.com/bfarzinhaid/student-record-api.git](https://github.com/bfarzinhaid/student-record-api.git)
    

2.  *Navigate to the project directory*
    sh
    cd student-record-api
    

3.  *Install the required packages*
    *(First, make sure you have created a requirements.txt file by running pip freeze > requirements.txt in your local terminal and pushed it to GitHub).*
    sh
    pip install -r requirements.txt
    

4.  *Run the Flask application*
    sh
    python testenv.py
    
    The API will be running at http://127.0.0.1:5000/.

## ⚙ API Endpoints

### Get API Status

- *Method:* GET
- *Route:* /
- *Description:* Returns a success message to indicate that the API service is active.
- *Success Response:*
  - *Code:* 200 OK
  - *Content:*
    json
    {
      "message": "Student Record API working!"
    }
    
