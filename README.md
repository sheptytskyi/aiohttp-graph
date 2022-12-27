# AioHTTP GraphQL Interview Task
<hr>

## Tech. Stack:
- Python
- AioHTTP
- SqlAlchemy
- Graphene
- PostgreSQL

## Usage:
1. Create venv
```python
python3 -m venv venv
```

2. Activate it
```python
source venv/bin/activate
```
3. Install requirements
```python
pip install -r requirements.txt
```
4. In .env file set your db properties
```python
DB_USER=<your_db_user>
DB_PASS=<your_db_user_pass>
DB_HOST=<your_db_host>
DB_NAME=<your_db_name>
```
5. Apply migrations
```python
alembic upgrade head
```
6. Startup server
```python
python app.py
```
7. Go to endpoint
```python
http://localhost:8080/graphql
```
<hr>

###### The task was completed by Dmytro Sheptytskyi