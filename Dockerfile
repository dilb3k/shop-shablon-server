# Python bazaviy image
FROM python:3.10-slim

# Ishchi papkani o'rnatamiz
WORKDIR /app

# Talablar faylini nusxalaymiz va install qilamiz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini yuklaymiz
COPY . .

# Statik fayllarni collect qilamiz
RUN python manage.py collectstatic --noinput

# Tashqi portni ochamiz
EXPOSE 8000

# Daphne bilan ishga tushiramiz (ASGI uchun)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "Config.asgi:application"]

web: gunicorn yourprojectname.wsgi:application

