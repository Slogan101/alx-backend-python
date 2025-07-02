# ALX_prodev Database Seeder

This Python project sets up a MySQL database called `ALX_prodev`, creates a `user_data` table with predefined fields, and populates it using data from a CSV file (`user_data.csv`).

---

## 🛠 Features

- Connects to MySQL server
- Creates the database `ALX_prodev` if it doesn't exist
- Creates the `user_data` table with the following schema:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Reads and inserts data from a CSV file, skipping duplicates based on email

---

## 📦 Prerequisites

- Python 3.6+
- MySQL Server (running locally or remotely)
- `mysql-connector-python` package

Install required package:

```bash
pip install mysql-connector-python
