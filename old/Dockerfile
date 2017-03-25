FROM tiangolo/uwsgi-nginx:python3.5

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY ./app /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt