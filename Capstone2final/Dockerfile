FROM python:3.7.9
RUN apt-get update -y
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN chmod +x /app/mudit.sh
CMD ["/app/mudit.sh"]