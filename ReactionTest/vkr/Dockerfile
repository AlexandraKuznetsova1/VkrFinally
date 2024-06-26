# Использование базового образа Python
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Установка необходимых системных библиотек
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов проекта в контейнер
COPY . .

# Установка зависимостей Python
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Открытие порта 8501 (стандартный порт)
EXPOSE 8501

# Настройка проверки работоспособности
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Определение команды для запуска Django проекта
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]