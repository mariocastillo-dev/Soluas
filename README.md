# Soluas

Soluas_back/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── base.py
│   │   ├── role.py
│   │   ├── kpi.py
│   │   └── facts.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── kpi_schema.py
│   │   └── role_schema.py
│   │
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user_crud.py
│   │   ├── kpi_crud.py
│   │   └── role_crud.py
│   │
│   └── route/
│       ├── __init__.py
│       ├── data_routes.py
│       ├── role_routes.py
│       ├── kpi_routes.py
│       └── user_routes.py
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── setup.sh