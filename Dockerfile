FROM ubuntu

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y python3-dev python3-pip

WORKDIR /to-do-list

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENV PORT=8000
# CMD gunicorn todolist.wsgi:application --bind 0.0.0.0:$PORT
# CMD python3 manage.py runserver

CMD [ "python3", "manage.py", "runserver", "127.0.0.1:8000" ]