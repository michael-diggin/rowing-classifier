FROM python:3.6

EXPOSE 5000
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN export FLASK_APP=app.py
CMD ["flask", "run"]
