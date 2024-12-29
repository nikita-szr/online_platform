## Проект онлайн платформы для обучения

## Документация 

* http://localhost:8000/swagger/
---

### Для настроек проекта нужно использовать переменные окружения

###### пример файла .env

```
.env.sample
.env.prod.sample # для docker
```

### Установить все зависимости

```python
pip install - r requirements.txt
```

### Применить все миграции

```python
python manage.py migrate 
```

### Создать админа

```python
python manage.py create superuser
```


---
### Запуск сервера

```python
python manage.py runserver 
```


## Запуск Celery worker
````
celery -A config worker --loglevel=info
````

## Запуск Celery Beat
```
celery -A config beat --loglevel=info
```
---
### Запуск проекта через docker
```
В корневой директории создайте файл .env.prod и добавьте следующие переменные:
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
    REDIS_URL=redis://redis:6379/0
    
Соберите и запустите контейнеры:
    docker-compose up --build

После запуска контейнеров, выполните миграции:
    docker exec -it django_web python manage.py migrate
    
Откройте проект в браузере: Перейдите по адресу http://localhost:8000
```
