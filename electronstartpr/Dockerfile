
FROM python:3.11-slim

RUN useradd -s /bin/sh -u 1234 nonroot

WORKDIR /usr/src/electronstartpr

RUN apt-get update && apt-get install -y netcat-openbsd

RUN mkdir media

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' /usr/src/electronstartpr/entrypoint.sh
RUN chmod +x /usr/src/electronstartpr/entrypoint.sh

RUN chown -R nonroot:nonroot /usr/src/electronstartpr
USER nonroot

ENTRYPOINT [ "./entrypoint.sh" ]