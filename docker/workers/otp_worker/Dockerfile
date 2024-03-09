FROM python:3.11.4-slim

# set the working directory
WORKDIR /app

# python unbuffered mode
ENV PYTHONUNBUFFERED 1
# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt also upgrade pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
