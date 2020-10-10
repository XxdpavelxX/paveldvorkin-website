FROM python:3.7.7-slim

# Setup Nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Copy the application
COPY locallibrary locallibrary
COPY requirements.txt requirements.txt
RUN pip -r install requirements.txt
EXPOSE 80
EXPOSE 8000
CMD ["uwsgi", "--http", ":8000", "--module", "locallibrary.wsgi"]

