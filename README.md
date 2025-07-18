# Assignment 4 – Database Automation with Ansible and Flyway

## 📌 Overview

This project demonstrates automated database deployment and schema management using **Ansible**, **Flyway**, and **MySQL**. It also includes validation scripts and CI/CD integration concepts. The repository is part of a coursework assignment from *Conestoga College*.

---

## 📁 Repository Structure

```
Assignment 4/
├── README.md
├── venv/                       # Python virtual environment
├── scripts/
│   ├── up.yaml                # Ansible playbook to start DB and apply Flyway migrations
│   ├── down.yaml              # Ansible playbook to stop DB and generate migration
│   ├── dbtests.py             # Python script to validate database schema
│   └── sql/
│       └── V1__initial.sql    # Flyway migration script(s)
├── flyway.conf                # Flyway configuration
├── screenshots/               # Screenshots of validation & pipeline (for submission)
└── Answer_Question1.pdf       # Written answers for Question 1 (tool comparison)
```

---

## ⚙️ Requirements

- Python 3.12+
- MySQL Server (running locally in WSL or Linux)
- Ansible
- Flyway CLI
- Virtual environment activated with:
  ```bash
  source venv/bin/activate
  ```

---

## 🚀 Setup & Usage

### Step 1: Create and Activate Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python
```

### Step 2: Start MySQL

```bash
sudo service mysql start
```

Ensure MySQL user `root` has password `durlabh123` and `subscribers` DB exists:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'durlabh123';
CREATE DATABASE IF NOT EXISTS subscribers;
```

### Step 3: Run `up.yaml` Ansible Playbook

```bash
ansible-playbook scripts/up.yaml
```

This will:
- Start the MySQL server (if required)
- Initialize the DB (if not already created)
- Apply Flyway migrations

### Step 4: Validate Schema

```bash
python3 scripts/dbtests.py
```

Expected output:

```
Schema validation passed.
```

### Step 5: Shutdown and Generate Migration

```bash
ansible-playbook scripts/down.yaml
```

This will:
- Dump inserted data
- Stop or clean the database for next run

---

## 🧪 Tests

All schema validation is handled via `dbtests.py`, and must pass before committing changes.

---

## 🖼️ Screenshots (for Submission)

Add the following screenshots to the `/screenshots` folder:
- Terminal showing successful `dbtests.py` run
- Output of `ansible-playbook up.yaml`
- Output of `ansible-playbook down.yaml`
- CI/CD workflow run (optional, for extra credit)

---

## 🧾 Answer to Question 1

See `Answer_Question1.pdf` or `Answer_Question1.docx` included in the submission ZIP.

---

## 📜 Notes

- This project is idempotent — rerunning `up.yaml` won’t break anything.
- All configurations and credentials are for educational purposes only.

---

## 👨‍💻 Author

**Durlabh Tilavat**  
-Email: Dtilavat8972@conestogac.on.ca 
-Course: Database Automation (Conestoga College)
