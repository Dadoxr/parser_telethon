#содержит инструкции по созданию образа. Этот файл должен находиться в корневой директории вашего приложения
FROM python:3.11.4

WORKDIR /usr/src/app2
EXPOSE 8003

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENTRYPOINT [ "python" ]
CMD ["./main.py" ]