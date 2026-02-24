FROM python:3.10

WORKDIR /app

COPY . .

# Install ffmpeg + curl first
RUN apt update && apt install -y ffmpeg curl

# Install Node 20 (Proper Way)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt install -y nodejs

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade yt-dlp

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
