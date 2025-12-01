# client_queries
Query Management System

A simple Streamlit + MySQL application that allows Clients to submit queries and Support Team members to view & close them.

The system supports:

✅ User Registration (Client / Support)

✅ Secure Login (SHA-256 password hashing)

✅ Client Query Submission

✅ Support Team Dashboard

✅ MySQL Database Storage

🚀 Features
👤 User Accounts

Register as Client or Support

Passwords are securely hashed (SHA-256)

Login session persists using Streamlit Session Sta₹te

📝 Client Portal

## Submit new queries with:

    *Email
  
    *Mobile
  
    *Query Heading
  
    *Description

*Query automatically saved with timestamps

🛠 Support Dashboard

    *View all queries
    
    *Filter by OPEN or CLOSED
    
    *Close queries and update timestamps

🗄 Database (MySQL)

Two tables are created:

| Column          | Type         | Notes            |
| --------------- | ------------ | ---------------- |
| USER_NAME       | VARCHAR(100) | Primary Key      |
| HASHED_PASSWORD | VARCHAR(255) | SHA-256 hash     |
| ROLE            | VARCHAR(20)  | CLIENT / SUPPORT |


| Column       | Type               |
| ------------ | ------------------ |
| ID           | INT AUTO_INCREMENT |
| EMAIL        | VARCHAR(255)       |
| MOBILE       | VARCHAR(20)        |
| HEADING      | TEXT               |
| DESCRIPTION  | TEXT               |
| STATUS       | VARCHAR(20)        |
| CREATED_TIME | DATETIME           |
| CLOSED_TIME  | DATETIME           |


🧰 Installation

1️⃣ Install Dependencies
      
    pip install streamlit pymysql pandas

2️⃣ Start MySQL Server

   Make sure your MySQL root credentials match the ones in:

    db.py

    host='127.0.0.1'
    user='root'
    passwd='YOUR_PASSWORD'

3️⃣ Initialize the Database

Run this once:

    from db import initialize_database
    initialize_database()


Or run:

    python -c "from db import initialize_database; initialize_database()"

▶️ Running the Application

    streamlit run app.py


The app will open in your browser at:

    http://localhost:8501
