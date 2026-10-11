# Django Blog Application

## Project Overview

A basic blog application developed using Django.  
The application allows users to view blog posts, create new posts, and add comments.

## Technologies Used

- Python
- Django 6.0.8
- HTML
- CSS
- SQLite Database

## Features

- User-friendly blog homepage
- Display all blog posts
- Create new blog posts
- View individual post details
- Add comments to posts
- Django admin panel for managing posts and comments
- Responsive CSS styling

## Project Structure
blog_project/
│
├── blog/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── templates/
│ │ └── blog/
│ │ ├── home.html
│ │ ├── post_detail.html
│ │ └── create_post.html
│ │
│ └── static/
│ └── blog/
│ └── style.css
│
├── blog_project/
│ ├── settings.py
│ └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md


## How to Run the Project

1. Activate virtual environment:


.venv\Scripts\activate


2. Install Django:


pip install django


3. Apply migrations:


python manage.py migrate


4. Run the development server:


python manage.py runserver


5. Open in browser:


http://127.0.0.1:8000/


## Admin Panel

Admin URL:


http://127.0.0.1:8000/admin/


Admin features:
- Add/Edit/Delete blog posts
- Manage comments
- Manage users

## Design Decisions

- Used Django MVT architecture for clean separation of logic.
- SQLite database used for simple development and testing.
- Django templates used for dynamic HTML rendering.
- CSS added for better user experience.

## Challenges Faced

- Configuring Django project structure
- Connecting URLs with views
- Creating models and migrations
- Integrating templates and static files

## Conclusion

This project demonstrates the basic functionality of a Django blog application  with posts, comments, database integration, and frontend styling. .. up to here i have to cpy nd paste