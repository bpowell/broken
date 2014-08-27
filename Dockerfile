############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Brandon Powell

# Copy the application folder inside the container
ADD brokenapp/ /my_application

RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git vim sqlite3

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip python-pylons

# Expose ports
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /my_application

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
CMD paster serve --reload development.ini
