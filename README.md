# ❤️ HeartCare AI – Heart Disease Prediction System

## 📌 Overview

HeartCare AI is a full-stack Machine Learning-powered healthcare application that predicts the likelihood of heart disease based on clinical parameters. The system integrates a trained Random Forest model with a modern MERN stack architecture to provide real-time predictions, secure user authentication, prediction history tracking, and health analytics.

The application helps users perform an initial heart disease risk assessment by entering medical information and receiving instant AI-powered results.

---

## 🚀 Features

### 🔐 Authentication

* User Registration
* User Login
* JWT Authentication
* Protected Routes
* Secure Password Hashing

### ❤️ Heart Disease Prediction

* Real-time disease prediction
* AI-powered risk assessment
* Instant results
* Clinical parameter validation

### 📊 Dashboard

* Total Predictions
* High Risk Cases
* Low Risk Cases
* Recent Prediction History
* Personalized User Dashboard

### 📈 Data Insights

* Prediction Analytics
* Risk Distribution
* Health Statistics
* Dynamic Charts

### 🕒 Prediction History

* View Previous Predictions
* Search History
* Delete Records
* MongoDB Storage

### 📩 Contact System

* Contact Form
* Message Storage
* User Feedback Management

---

## 🏗️ System Architecture

```text
User
 ↓
React Frontend
 ↓
Node.js + Express Backend
 ↓
FastAPI ML Service
 ↓
Random Forest Model
 ↓
MongoDB Database
```

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Deployment
8. Real-Time Prediction

### Models Evaluated

* Logistic Regression
* Decision Tree
* Random Forest ✅

### Final Model Accuracy

```text
Random Forest Accuracy: 86.89%
```

---

## 📋 Input Features

| Feature  | Description                 |
| -------- | --------------------------- |
| age      | Age of patient              |
| sex      | Gender                      |
| cp       | Chest pain type             |
| trestbps | Resting blood pressure      |
| chol     | Cholesterol level           |
| fbs      | Fasting blood sugar         |
| restecg  | Resting ECG results         |
| thalach  | Maximum heart rate achieved |
| exang    | Exercise-induced angina     |
| oldpeak  | ST depression               |
| slope    | Slope of ST segment         |
| ca       | Number of major vessels     |
| thal     | Thalassemia                 |

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Tailwind CSS
* React Router
* Axios
* Framer Motion

### Backend

* Node.js
* Express.js

### Database

* MongoDB Atlas
* Mongoose

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Pickle

### API

* FastAPI

### Authentication

* JWT
* bcryptjs

---

## 📂 Project Structure

```text
HeartCare-AI/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   └── server.js
│
├── ml-service/
│   ├── app.py
│   ├── heart_model.pkl
│   └── scaler.pkl
│
├── dataset/
│   └── heart.csv
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/HeartCare-AI.git
cd HeartCare-AI
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
npm install
npm start
```

### FastAPI Setup

```bash
cd ml-service

pip install -r requirements.txt

uvicorn app:app --reload
```

---

## 🔑 Environment Variables

### Backend (.env)

```env
PORT=5000

MONGO_URI=your_mongodb_connection_string

JWT_SECRET=your_secret_key

FASTAPI_URL=http://localhost:8000
```

---

## 📡 API Endpoints

### Authentication

```http
POST /api/auth/register

POST /api/auth/login

GET /api/auth/profile
```

### Prediction

```http
POST /api/predictions

GET /api/predictions/history

DELETE /api/predictions/:id
```

### Contact

```http
POST /api/contact

GET /api/contact
```

---

## 🎯 Key Highlights

* Real-time AI prediction
* Random Forest ML model
* FastAPI integration
* JWT authentication
* MongoDB database
* Responsive UI
* User prediction history
* Production-ready architecture
* No dummy data
* Fully dynamic dashboard

---

## 🔮 Future Enhancements

* Doctor Recommendation System
* PDF Medical Reports
* Email Notifications
* Risk Probability Score
* Multi-Disease Prediction
* Health Monitoring Dashboard
* Cloud Deployment

---

## 👨‍💻 Author

**Shubham Dalvi**

Data Science & Full Stack Development Project

Built with ❤️ using Machine Learning, FastAPI, React.js, Node.js, Express.js, and MongoDB.
