📚 Student Record Management API (Flask + HTML)
This is a simple Student Record Management application built using Python Flask. It allows users to create, read, update, and delete (CRUD) student records via a web interface. Data is stored in an in-memory Python dictionary, making it ideal for learning, prototyping, or small-scale usage.

🚀 Features
✅ Add a student via HTML form
✅ View all student records
✅ Update student name
✅ Delete a student record
✅ Lightweight, no external DB used
✅ Fully containerized with Docker
✅ Deployment-ready for AWS ECR and EKS

🛠 Technologies Used
🐍 Python 3.9

🌐 Flask (Web framework)

🧾 HTML with Jinja2 templates

🐳 Docker (for containerization)

☁️ AWS ECR & EKS (for deployment)

🗂 Project Structure
bash
Copy
Edit
student-record-app/
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build configuration
├── README.md               # Project documentation
│
└── templates/              # HTML templates (Jinja2)
    └── index.html          # UI for managing student records
🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
2. Create a Virtual Environment & Install Dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
3. Run the Flask App
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

🐳 Docker Usage
Build Docker Image
bash
Copy
Edit
docker build -t student-record-api .
Run Docker Container
bash
Copy
Edit
docker run -p 5000:5000 student-record-api
☁️ AWS Deployment (ECR + EKS)
Push image to Amazon ECR

Create and configure EKS cluster

Use Kubernetes manifests to deploy container

Expose via LoadBalancer or Ingress

This project is compatible with CI/CD pipelines and cloud-native deployments.

📸 Screenshot

Add, update, and delete student records using a clean HTML interface.

🙋‍♂️ Author
Ishan Sinha
Feel free to connect on LinkedIn or GitHub.

📄 License
