# Запуск в docker
Использовать ubuntu 20.04 или выше.

Скачать этот репозиторий.
```bash
git clone ...
```

Запустить с помощью docker-compose файла (запустит все необходимое для работы)
```bash
docker compose up -d
```

Доступ к сервису:
- API расположен по адресу http://127.0.0.0:8000
- Документация к API (swagger) по адресу http://127.0.0.0:8000/docs

Другие настройки (пароли к БД) можно редактировать в docker-compose файле.

# Запуск для разработки
Создадать виртуальное окружение.
```bash
python -m venv env
```

Включить виртуальное окружение.
```bash
source env/bin/activate
```

Установить зависимости
```bash
pip install -r requirements.txt
```

Запустить API
```bash
uvicorn app.main:app
```

Миграции
```bash
yoyo init --database postgresql://lvinka:lvinka-db-password@localhost/lvinka
```