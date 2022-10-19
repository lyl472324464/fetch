# Install the base requirements for the app.
# This stage is to support development.
FROM ubuntu
WORKDIR /app
RUN apt update && apt install -y python3-pip
COPY requirements.txt .
COPY fetch.py .
RUN pip3 install -r requirements.txt
RUN pyinstaller -F fetch.py
RUN cp ./dist/fetch .