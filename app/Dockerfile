# Use an official Python runtime as a parent image
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
MAINTAINER Marcelo Leal Junior <marceloleal.junior@gmail.com>

#To build it, type (example):
#>sudo docker build -t msleal/asciivmssdashboard:test .
WORKDIR /app
RUN apk --update add bash git
RUN git clone https://github.com/marcelojr13/starwars.git

# Install any needed packages specified in requirements.txt
RUN cd starwars/app && pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV STATIC_URL /static
ENV STATIC_PATH /app/starwars/app/static
ENV NAME World

# Run app.py when the container launches
WORKDIR starwars/app
CMD ["flask", "run"]

