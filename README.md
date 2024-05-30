# Library Management System

This project is a Library Management System built with Django Rest Framework (DRF) for the backend and React for the frontend. The application allows users to manage library operations including adding, borrowing, and returning books.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Backend](#backend)
- [Frontend](#frontend)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Node.js 14+
- npm 6+
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/PlushaQ/library_management_system.git
cd library_management_system
```

2. Set up backend (Django):
```bash
cd backend-django
python -m venv env
rce env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

3. Set up frontend (React):
```bash
cd ../frontend-react/library-management-system
npm install
```
### Project structure
Project structure is as follows:
```bash
library_management_system/
│
├── LICENSE
├── README.md
├── backend-django/           # Django project for backend
│   ├── accounts/             # Django app for accounts
│   ├── authors/              # Django app for authors
│   ├── books/                # Django app for books
│   ├── library_management_system/  # Main Django project directory
│   ├── manage.py             # Django project management script
│   ├── requirements.txt      # Python dependencies
│   ├── templates/            # Template files
│   └── utils/                # Utility scripts
│
└── frontend-react/           # React project for frontend
    └── library-management-system/
        ├── README.md         # Detailed instructions for the frontend setup and usage
        ├── package.json      # Node.js dependencies and scripts
        ├── public/           # Public files
        └── src/              # Source files
```
### Backend
The backend of this application is powered by Django Rest Framework. For detailed setup instructions and API documentation, refer to the Backend README.

### Frontend
The frontend of this application is built with React. For detailed setup instructions and component documentation, refer to the Frontend README.

## Running the Application
### Using Docker
In making

### Running Locally
#### Backend
Start the Django development server:
```
cd backend-django
source env/bin/activate
python manage.py runserver
```

The backend server will be running at http://localhost:8000.

#### Frontend
Start the React development server:
```
cd frontend-react/library-management-system
npm start
```
The frontend server will be running at http://localhost:3000.

### Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

```
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
```

### License
Distributed under the MIT License. See LICENSE for more information.

For detailed information on how to set up and use the backend and frontend individually, please refer to their respective README files located in the backend-django and frontend-react/library-management-system directories.