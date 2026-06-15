# 🧠 AI App Risk Prediction

An AI-powered web application that analyzes applications and predicts their security risk using Machine Learning. The system provides a risk score, identifies potential security issues, visualizes risk through charts, stores scan history, and generates downloadable PDF reports.

---

## 📌 Features

* 🔐 Secure Login Authentication
* 🤖 AI-Based Application Risk Prediction
* 📊 Risk Score Generation (0–100)
* ⚠️ Detection of Potential Security Issues
* 📈 Interactive Pie Chart and Bar Chart Visualization
* 🗄️ SQLite Database for Scan History
* 📄 PDF Report Generation
* 📱 User-Friendly Dashboard using Streamlit
* 🚀 REST API Integration using Flask
* 🧹 RAM Monitoring and Memory Cleanup Module

---

## 🛠️ Technologies Used

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python       | Programming Language   |
| Streamlit    | Frontend Dashboard     |
| Flask        | Backend API            |
| Scikit-learn | Machine Learning Model |
| SQLite       | Database               |
| Pandas       | Data Processing        |
| Matplotlib   | Data Visualization     |
| FPDF         | PDF Report Generation  |
| Requests     | API Communication      |
| Joblib       | Model Serialization    |
| Psutil       | RAM Monitoring         |

---

## 🏗️ Project Architecture

```
User
   │
   ▼
Streamlit Frontend
   │
   ▼
Flask Backend API
   │
   ├──────────────► Machine Learning Model
   │                     │
   │                     ▼
   │              Risk Prediction
   │
   └──────────────► SQLite Database
                         │
                         ▼
                  Scan History Storage
                         │
                         ▼
                 PDF Report Generation
```

---

## 📂 Project Structure

```
AI-App-Risk-Prediction/
│
├── app.py
├── backend.py
├── model.py
├── risk_data.csv
├── risk_model.pkl
├── scans.db
├── requirements.txt
├── README.md
├── reports/
├── screenshots/
└── diagrams/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-App-Risk-Prediction.git
cd AI-App-Risk-Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Flask Backend

```bash
python backend.py
```

### 4. Launch the Streamlit Frontend

```bash
streamlit run app.py
```

---

## 🚀 How It Works

1. User logs into the application.
2. Enter the application name.
3. Click **Run AI Risk Scan**.
4. The frontend sends the request to the Flask backend.
5. The Machine Learning model analyzes the data.
6. A risk score and detected issues are generated.
7. Results are displayed with charts.
8. Scan history is saved in SQLite.
9. Users can download a PDF security report.

---

## 📊 Risk Categories

| Risk Score | Category       |
| ---------- | -------------- |
| 0 – 40     | 🟢 Low Risk    |
| 41 – 70    | 🟡 Medium Risk |
| 71 – 100   | 🔴 High Risk   |

---

## 📸 Screenshots

Add screenshots of:

* Login Page
* Dashboard
* Risk Analysis
* Pie Chart
* Bar Chart
* Scan History
* PDF Report

Example:

```
screenshots/
├── login.png
├── dashboard.png
├── risk_chart.png
└── history.png
```

---

## 🔮 Future Enhancements

* Deep Learning-based Risk Prediction
* Real-Time Threat Intelligence Integration
* Cloud Deployment (AWS/Azure/GCP)
* JWT Authentication
* Role-Based Access Control
* Mobile Application Support
* Email Report Automation
* Comparative Risk Analysis Dashboard

---

## 👩‍💻 Author

**Disha Manje**

Bachelor of Science in Computer Science

AI App Risk Prediction Project (2025–2026)

---

## 📚 References

* Python
* Streamlit
* Flask
* Scikit-learn
* SQLite
* Matplotlib
* FPDF

---

## 📄 License

This project is developed for educational and academic purposes. You are free to use and modify it for learning and research.
