📚 Student Record Management API (Python Flask + HTML)
A simple web application built with Python Flask for managing student records.
Designed for learning DevOps, containerization, and cloud deployment practices.

🚀 Features
✅ Add student records via a web interface

✅ View all student records

✅ Update student information

✅ Delete student records

✅ Lightweight – uses in-memory storage (no database)

✅ Fully containerized with Docker

✅ Deployment-ready for AWS ECR & EKS

✅ Compatible with CI/CD pipelines

✅ Prerequisites
To build and deploy this project, you should have basic knowledge of:

🐍 Python — for backend development

🌐 Flask — lightweight web framework

🐳 Docker — for containerizing the application

🗃️ Git & GitHub — version control and source code management

⚙️ GitHub Actions — CI/CD pipeline automation (used instead of Jenkins)

☸️ Kubernetes — for container orchestration on EKS

🐧 Linux Basics — working with CLI, Docker, and Kubernetes tools

☁️ AWS (ECR, EKS) — for container registry and managed Kubernetes cluster


## 🗂️ Project Structure  

```
student-record-app/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build configuration
├── README.md            # Project documentation
└── templates/
    └── index.html       # HTML interface for managing records
```

🔧 Local Setup Instructions:
1️⃣ Clone the Repository:
[git clone https://github.com/Ishansinhaid/student-record-api.git
cd student-record-api]
2️⃣ Create Virtual Environment & Install Dependencies:
[python -m venv venv]
3️⃣ Run the Flask Application:
[python app.py ,Visit http://localhost:5000 in your browser].

🐳 Docker Usage->
🛠️ Build Docker Image:
[docker build -t student-record-api ]
🚀 Run Docker Container:
[docker run -p 5000:5000 student-record-api]

☁️ Push Docker Image to Amazon ECR:
1️⃣ Authenticate Docker with AWS ECR
[aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com].
2️⃣ Create ECR Repository
[aws ecr create-repository --repository-name student-record-api]
3️⃣ Tag Your Docker Image
[docker tag student-record-api:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/student-record-record-api:latest].
4️⃣ Push the Image to ECR
[docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/student-record-api:latest]

☁️ AWS Deployment Workflow:
✅ Build & Push Docker image to Amazon ECR
✅ Create and configure EKS Cluster
✅ Apply Kubernetes Manifests (Deployment, Service, Ingress)
✅ Expose application using LoadBalancer / Ingress Controller
✅ Automate CI/CD with GitHub Actions.

#ARCHITECTURE DIAGRAM:  <img width="1536" height="1024" alt="ChatGPT Image Jun 26, 2025, 03_20_59 PM" src="https://github.com/user-attachments/assets/6f860034-e33f-4cb6-8ce4-6c70219ec2e1" />

🛠️ CI/CD Pipeline Architecture
This project uses a CI/CD pipeline powered by GitHub Actions, which automates the Docker image build, push to Amazon ECR, and deployment to EKS.


🔥 How It Works:
✅ Step 1: Code is pushed to GitHub Repository
✅ Step 2: GitHub Actions workflow triggers
✅ Step 3: Docker image is built and pushed to Amazon ECR
✅ Step 4: Deployment to Amazon EKS happens via GitHub Actions
✅ Step 5: Ingress + Load Balancer expose the app to end-users
✅ Step 6: User interacts with the app running inside Kubernetes Pods

#FLOW CHART OF CI/CD PIPELINE: <img width="1536" height="1024" alt="flowchartBEST" src="https://github.com/user-attachments/assets/c8a8e10f-4b97-48a5-949d-b7bcfbb0f430" />
#CLOUD SHELL :  <img width="1920" height="1080" alt="Screenshot (27)" src="https://github.com/user-attachments/assets/89eabd71-3604-4785-8754-69a79a871e26" />

📝 Conclusion
In this project, we successfully built a complete CI/CD pipeline using GitHub Actions, Docker, Amazon ECR, and Amazon EKS to deploy a simple Flask-based Student Record Management API.

This project demonstrated:
Automating Docker image builds and deployments using GitHub Actions
Managing container images with Amazon ECR
Deploying scalable applications on Amazon EKS with Kubernetes manifests
Exposing applications via Ingress and Load Balancer for public access
This setup is designed for learning and DevOps practice purposes.
For production-grade pipelines.
