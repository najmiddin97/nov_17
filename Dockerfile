# Base image sifatida Python 3.14-slim
FROM python:3.14-slim

# Ishchi papka
WORKDIR /app

# Git o‘rnatish (clone qilish uchun)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# GitHub’dan project’ni klonlash
RUN git clone https://github.com/najmiddin97/nov_17.git .

# Python paketlarini o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Container ishga tushganda testlarni bajarish
CMD ["pytest", "tests"]


