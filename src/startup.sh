#!/bin/bash

# TODO ENVS

# Путь к файлу с версией
#VERSION_FILE="version.txt"

# Проверка наличия файла версии
#if [ ! -f "$VERSION_FILE" ]; then
#    echo "Version file $VERSION_FILE does not exist. Assuming initial setup."
#    FILE_VERSION="initial"
#else
#    FILE_VERSION=$(cat "$VERSION_FILE")
#fi

# Получение версии из базы данных
#DB_VERSION=$(python manage.py shell -c "from myapp.models import Service; print(Service.get_current_version())" 2>/dev/null)

# Проверка, необходимо ли запускать миграции
#if [ -z "$DB_VERSION" ] || [ "$DB_VERSION" != "$FILE_VERSION" ]; then
    echo "Running migrations..."
    python manage.py migrate --noinput

#    # Если миграции были выполнены, обновляем версию в базе данных
#    if [ "$FILE_VERSION" != "initial" ]; then
#        python manage.py shell -c "from myapp.models import Service; Service.objects.all().delete(); Service.objects.create(model_version='$FILE_VERSION')"
#        echo "Migrations finished. Model version updated to $FILE_VERSION."
#    else
#        # Если это инициализация, нам нужно установить версию после миграции
#        FILE_VERSION=$(python manage.py shell -c "import myapp; print(myapp.VERSION)")
#        python manage.py shell -c "from myapp.models import Service; Service.objects.all().delete(); Service.objects.create(model_version='$FILE_VERSION')"
#        echo "Initial setup completed. Model version set to $FILE_VERSION."
#    fi
#else
#    echo "Model version is up-to-date. Skipping migrations."
#fi

# Создание суперпользователя Django, если он не создан
# Замените переменные окружения на те, что вы используете
if [ -z "$(python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists())")" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput
else
    echo "Superuser already exists."
fi

# Запуск сервера Django
# echo "Starting Django server..."
# python manage.py runserver 127.0.0.1:8000

# Запуск api
python main.py
