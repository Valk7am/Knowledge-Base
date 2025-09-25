# Knowledge Base

A simple, clean, and modern web application for creating, viewing, editing, and organizing Knowledge Base articles.  
Built with **Flask**, **SQLite**, and **Bootstrap**, with support for nested categories, tags, full CRUD (Create, Read, Update, Delete), and search.

---

## 🚀 Features

- Create, read, update, and delete articles  
- Nested categories (tree structure: projects → sections → articles)  
- Tags for flexible labeling of content  
- Search by keywords (title, description, content)  
- Filter by categories and tags  
- Clean, responsive UI using Bootstrap  
- Confirmation modal before deleting articles  
- Simple, well-structured backend with input validation  

---

## 🧱 Project Structure
```
knowledge_base/
│
├── app.py # Main Flask app
├── models.py # Database models
├── routes.py # Flask routes/views for CRUD, filtering, etc.
├── forms.py # Forms and validation
├── config.py # Configuration
│
├── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ ├── create_article.html
│ ├── edit_article.html
│ ├── article_detail.html
│ └── manage_categories.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
│
└── knowledge_base.db # SQLite database file
```
yaml
Copy code

---

## 🛠️ Tech Stack
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100"><img src="https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/29fd6286-4e7b-4d6c-818f-c4765d5e39a9" width="100"><img src="https://user-images.githubusercontent.com/74038190/212280805-9bcb336b-8c55-46a8-abf8-ff286ab55472.gif" width="100">

- **Backend**: Python, Flask 
- **Database**: SQLite  
- **Frontend**: HTML, Bootstrap  
- **Forms & Validation**: Flask-WTForms  

---

## ⚙️ Installation & Running Locally

1. Clone the repository:

```bash
 git clone https://github.com/your-username/knowledge-base.git
 cd knowledge-base
```
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Initialize the database:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

Or, if not using migrations, just run db.create_all() inside a Flask shell.

Run the application:

```bash
flask run
```

Open http://127.0.0.1:5000 in your browser.

## 🔧 Usage

- Home Page: view all articles with filters and search
- Create Article: add title, content, tags, and category
- Edit Article: update article fields
- Delete Article: delete via button, with confirmation popup
- Manage Categories: build nested categories (e.g., Project → Calendar → Article)

## 📋 Roadmap
- Authentication & permissions
- WYSIWYG / Markdown editor
- File and image attachments
- Article version history
- Drag & drop category management
- REST API endpoints -> GraphQL

## 🤝 Contributing

- Contributions are welcome!
- Fork the project
- Create a feature branch: git checkout -b feature/YourFeature
- Commit changes: git commit -m "Add some feature"
- Push to your branch: git push origin feature/YourFeature
- Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🧠 Author

Valk7am

