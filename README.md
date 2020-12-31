# Manage Interviews
This project use python with django and psql as local database.

### Installation

postgrest docker server, you can use this:
```
docker pull postgres
```
Then please use this command to run it:
```
docker run --name postgres -e POSTGRES_PASSWORD=psqlpass -d -p 5432:5432 postgres
```
Install project requirements and create database:
```
pip install -r requirements.txt
./manage.py migrate
```
### Running the project
```
./manage.py runserver <port>
```
by default the port is 8000

The site address:
```
http://127.0.0.1:<port>
```
