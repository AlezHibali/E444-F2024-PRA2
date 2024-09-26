FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy all codes into the dir
COPY templates ./templates
COPY hello.py ./
COPY deploy.sh ./

# Define listening port
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd hello_user
USER hello_user

# add "--host", "0.0.0.0" to ensure it listens on all network interfaces
# run with docker run -p 8080:5000 hello_flask    
# CMD ["flask", "--app", "hello", "run", "--host", "0.0.0.0"]

# run with docker run -p 8080:8080 hello_flask 
CMD ["flask", "--app", "hello", "run", "--host", "0.0.0.0", "--port", "8080"]

# # Approach of using venv
# RUN python -m venv venv
# RUN venv/bin/pip install -r requirements/docker.txt
# ENTRYPOINT ["./deploy.sh"]