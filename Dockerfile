FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy all codes into the dir
COPY templates ./templates
COPY hello.py ./
COPY deploy.sh ./

# Define port
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd hello_user
USER hello_user

CMD ["flask", "--app", "hello", "run"]
# ENTRYPOINT ["./deploy.sh"]