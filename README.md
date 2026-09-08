# 📝 Django To-Do List

A simple and functional **To-Do List web application** built using **Python and Django**.

This application allows users to add, edit, complete, undo, and delete their daily tasks.

## 🚀 Features

* ➕ Add new tasks
* ✏️ Edit existing tasks
* ✅ Mark tasks as completed
* 🔄 Mark completed tasks as undone
* 🗑️ Delete tasks
* 🕒 Automatically stores task creation and update time
* 💾 SQLite database
* 🎯 Simple and easy-to-use interface

## 🛠️ Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite
* Git & GitHub

## 📂 Project Structure

```text
ToDo/
│
├── db.sqlite3
├── manage.py
├── env/
│
├── todo/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── todo_main/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── templates/
```

## 📌 Task Model

The application uses a `Task` model with the following fields:

| Field          | Description                          |
| -------------- | ------------------------------------ |
| `task`         | Stores the task description          |
| `is_completed` | Stores whether the task is completed |
| `created_at`   | Stores the task creation time        |
| `updated_at`   | Stores the last update time          |

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sarwangoutam2004-dev/todo.git
cd todo
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the virtual environment

**Windows / Git Bash:**

```bash
source env/Scripts/activate
```

### 4. Install Django

```bash
pip install django
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔄 Task Operations

### Add Task

Create and save a new task.

### Edit Task

Update the description of an existing task.

### Mark as Done

Mark a task as completed.

### Mark as Undone

Change a completed task back to an incomplete state.

### Delete Task

Permanently remove a task from the database.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Django project and app structure
* Django Models
* Django Views
* URL routing
* CRUD operations
* Django ORM
* SQLite database integration
* Django Templates
* Git and GitHub

## 🔮 Future Improvements

* 🔐 User authentication
* 👤 User-specific task lists
* 📅 Task deadlines
* 🔔 Task reminders
* 🔍 Search and filtering
* 🎨 Improved UI/UX
* 🌙 Dark mode

## 👨‍💻 Author

**Goutam Kumar Sarwan**

Built with **Python & Django** ❤️
