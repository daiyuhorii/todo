# Python image
FROM python:3.7.3

RUN mkdir /var/www
# workdir
WORKDIR /var/www

# Copy required libraries from local
COPY requirements.txt ./

# install them
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src

# activate server
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
