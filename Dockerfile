FROM python:3.11.4-slim

# set the working directory
WORKDIR /app

# python unbuffered mode
ENV PYTHONUNBUFFERED 1
# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# copy the current directory contents into the container at /app
COPY ./src /app

# copy the docker directory into the container at /app/docker because need the code inside workers/*/tasks.py
COPY ./docker /app/docker

# copy the entrypoint.sh file to root because for some reason it refuses to be copied to /app
COPY ./entrypoint.sh /
RUN sed -i 's/\r$//g' /entrypoint.sh
# change the permissions of the entrypoint.sh file
RUN chmod +x /entrypoint.sh

# install any needed packages specified in requirements.txt also upgrade pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
