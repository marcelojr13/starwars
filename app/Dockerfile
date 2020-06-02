# Use an official Python runtime as a parent image
FROM python:3.8.3-slim
MAINTAINER Marcelo Leal Junior <marceloleal.junior@gmail.com>

#To build it, type (example):
#>sudo docker build -t msleal/asciivmssdashboard:test .
WORKDIR /app
RUN apt-get update
RUN apt-get install -y git 
#RUN adduser --disabled-password --gecos "" architect
RUN git clone https://github.com/marcelojr13/starwars.git

# Install any needed packages specified in requirements.txt
#RUN cd starwars/app
RUN cd starwars/app && pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
WORKDIR starwars/app
CMD ["./start.sh"]
