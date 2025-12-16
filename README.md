# 📞 Contact Book Application

Simple contact management system built with Streamlit and Oracle Database to learn database operations (INSERT, SELECT).

## 🎯 Project Goal
Learn Oracle database connectivity and basic CRUD operations from Python backend to Oracle DB.

---

## 📋 Features
- ✅ Add contacts (Name + Phone)
- ✅ Search contacts by name
- ✅ Real-time database connection
- ✅ Simple and clean UI

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: Oracle Database 23ai Free
- **DB Driver**: python-oracledb

---

## 📁 Project Structure
```
ContactBook/
├── app.py                 # Main Streamlit application
├── db_connection.py       # Database connection & queries
├── create_table.sql       # Table creation script
├── test_connection.py     # DB connection test script
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Oracle Database 23ai Free Edition installed locally
- Oracle SQL Developer (optional)

### Installation Steps

1. **Clone the repository**
```bash
git clone "https://github.com/AI-Solutions-KK/Contact-Book-Application.git"
cd ContactBook
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create database table**
   - Open Oracle SQL Developer
   - Connect to your database (SYSTEM user)
   - Run `create_table.sql`

4. **Configure database connection**
   - Edit `db_connection.py`
   - Replace `your_password_here` with your Oracle SYSTEM password

5. **Test connection**
```bash
python test_connection.py
```

6. **Run the application**
```bash
streamlit run app.py
```

---

## 📊 Database Schema

**Table: CONTACTS**
| Column | Type | Description |
|--------|------|-------------|
| id | NUMBER | Auto-increment primary key |
| full_name | VARCHAR2(100) | Contact name |
| phone_number | VARCHAR2(15) | Phone number |
| created_date | DATE | Auto-generated timestamp |

---

## 🔄 Development Phases

### ✅ Phase 1 - Local Development (COMPLETED)
- Local Oracle DB setup
- Basic CRUD operations
- Streamlit UI
- Works on localhost only

### 🔜 Phase 2 - Cloud Migration (PLANNED)
- Migrate to Oracle Cloud Free Tier
- Configure cloud database connection
- Deploy on Streamlit Cloud
- Make app publicly accessible

---

## 🧪 Testing

1. **Add Contact**: Enter name and phone → Click "Add Contact"
2. **Search**: Type name in search box → Click "Search"
3. **Verify in DB**: Check Oracle SQL Developer

---

## ⚠️ Important Notes

- **Current Status**: Works locally only (localhost)
- **Password**: Never commit database password to Git
- **Cloud Deployment**: Requires Oracle Cloud setup (Phase 2)

---

## 📝 What You can Learn

1. ✅ Oracle DB connection from Python
2. ✅ Using `oracledb` driver
3. ✅ SQL parameterized queries (prevent SQL injection)
4. ✅ Streamlit form handling
5. ✅ Database INSERT and SELECT operations

---

## 🔮 Future Enhancements (Phase 2+)

- [ ] Edit/Delete contacts
- [ ] Email field
- [ ] Export to CSV
- [ ] User authentication
- [ ] Deploy to cloud

---

## 📧 Contact
**Developer**: [Karan-kk]  
**Project**: Learning Oracle + Python Integration

---

## 📜 License
This is a learning project for educational purposes.