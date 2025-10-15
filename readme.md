# About project

API test task.

# How to run

* ## Windows
```
git clone https://github.com/pazyn404/cafe-api.git
cd cafe-api
docker compose --env-file .\dev\.env up
```

* ## Linux, MacOS
```
git clone https://github.com/pazyn404/cafe-api.git
cd cafe-api
docker compose --env-file ./dev/.env up
```

# How to create superuser
```
docker exec -it api python manage.py createsuperuser
```
