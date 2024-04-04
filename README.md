# Запуск
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