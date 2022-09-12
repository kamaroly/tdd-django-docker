# Pull official base image
FROM python:3.10.1-slim-buster

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR '/usr/src/app'

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTONUNBUFFERED 1
ENV COMPOSE_CONVERT_WINDOWS_PATHS 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the entrypoint.sh and run it
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Add app
COPY . .

# Run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]