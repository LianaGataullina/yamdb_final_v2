### Автор проекта:

Студент Яндекс.Практикума 29 когорты - Гатауллина Л.Г. 

### Описание проекта api_final_yatube:

api_yamdb - групповой учебный проект 10-го спринта курса backend-разработки
Яндекс.Практикума

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/LianaGataullina/infra_sp2.git
```

```
cd infra_sp2/infra
```

Запустить сборку образа

```
docker-compose up -d --build 
```

Заполнить базу данных

```
docker-compose exec web python manage.py loaddata fixtures.json 

```

### Документация:

Примеры обращений к эндпоинтам находятся по адресу:

```
http://localhost/redoc/
```

### Шаблон наполнения env-файла
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```

#testtetst