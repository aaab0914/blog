# 📝 Django Blog

A modern, feature-rich blogging platform built with Django. Create, read, update, and delete blog posts with an intuitive user interface.

## ✨ Features

- **Create Posts** - Write and publish new blog posts
- **Read Posts** - Browse all published blog posts
- **Update Posts** - Edit existing blog posts
- **Delete Posts** - Remove posts you no longer need
- **Author Attribution** - Track who wrote each post
- **Post Details** - View full post content with metadata
- **Responsive Design** - Works on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Django 6.0.3
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Python**: 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aaab0914/blog.git
   cd blog
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Blog: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## 📖 Usage

### Viewing Posts
- Visit the home page to see all published blog posts
- Click on any post to view its full content

### Creating a Post
1. Navigate to the "New Post" page
2. Enter the post title
3. Select the author
4. Write your post content
5. Click "Save" to publish

### Editing a Post
1. Click on the post you want to edit
2. Click the "Edit" button
3. Modify the title and/or content
4. Click "Save" to update

### Deleting a Post
1. Click on the post you want to delete
2. Click the "Delete" button
3. Confirm the deletion

## 📁 Project Structure

```
blog/
├── django_project/           # Main Django project
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── asgi.py              # ASGI config
│   └── wsgi.py              # WSGI config
├── blog/                     # Blog app
│   ├── models.py            # Post model
│   ├── views.py             # Blog views (CRUD operations)
│   ├── urls.py              # Blog URL patterns
│   ├── admin.py             # Django admin configuration
│   ├── migrations/          # Database migrations
│   └── templates/           # HTML templates
├── accounts/                # User accounts app
│   ├── views.py             # Account views
│   ├── urls.py              # Account URL patterns
│   └── templates/           # Auth templates
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🗄️ Database Models

### Post Model
```python
- title (CharField): Post title (max 200 characters)
- author (ForeignKey): Reference to Django User model
- body (TextField): Post content
```

## 🔧 Available Views

- **BlogListView** - Display all blog posts (home page)
- **BlogDetailView** - Display a single post with full content
- **BlogCreateView** - Form to create a new post
- **BlogUpdateView** - Form to edit an existing post
- **BlogDeleteView** - Confirmation page to delete a post

## 🔐 Security Features

- Django's built-in CSRF protection
- Secure password handling
- User authentication for admin access
- SQL injection prevention through ORM

## 📦 Dependencies

- **Django 6.0.3** - Web framework
- **asgiref 3.11.1** - ASGI utilities
- **sqlparse 0.5.5** - SQL parsing
- **tzdata 2025.3** - Timezone data

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a Django learning project to demonstrate web development concepts.

## 🎓 Learning Outcomes

This project demonstrates:
- Django Class-Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
- Django ORM and database models
- URL routing and reverse URLs
- Template rendering
- Django admin interface
- CRUD operations
- Foreign key relationships

## 🐛 Troubleshooting

### Port already in use
```bash
python manage.py runserver 8001
```

### Database errors
```bash
python manage.py migrate
```

### Static files not loading
```bash
python manage.py collectstatic
```

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Start blogging today!** ✍️
