# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    
# # CMD ["fastapi", "run", "main.py", "--port", "8000"]

FROM python:3.9

RUN apt-get update && apt-get install -y coreutils gcc libc-dev libffi-dev libssl-dev
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["fastapi", "run", "main.py", "--port", "8000"]

