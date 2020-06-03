# Starwars Application

 About the project, I pick up the data with the module Requests in this url: 'https://swapi.dev/'.
 To process the json, I use Pandas, and turn the json it a dictionary type, that is more easy to manipulate to create a table.

 After that and complete the logical part, I commit this project on GitHub. With this, I get the code and other files of my project
 for git and transform it a DockerFile, better, I clone de project and create a DockerFile with that.


## Modules That I Used:

Python Pandas (PypI):
- To install Pandas:
  pip install pandas
- To see the documentation:
https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

Python Flask (PypI):
- To install Pandas:
  pip install flask
- To see the documentation:
https://flask.palletsprojects.com/en/1.1.x/installation/

Docker (Linux):
- To install Docker:
  sudo apt-get install -y docker.io
- To see the documentation:
https://docs.docker.com/

## To See The Project Running:

- To see the project running, I have a page on Instagram with I will put the application execute in a short video.

- My page on Instagram is:
https://www.instagram.com/pandoraprogramming/

## DOCKER INSTRUCTIONS
### Start the Ubuntu/Linux VM to create the docker image
az vm start --name starwars2020 --resource-group starwars

### Make sure the local files are updated
cd starwars/

git pull

### Build the docker image
docker build -t marcelojr13/starwarsjr13:latest .

### Tag the new image ID
docker tag <insert-new-image-id-here> marcelojr13/starwarsjr13:latest

docker push marcelojr13/starwarsjr13:latest

### Deploy docker on Azure Container Instance
az container create --image marcelojr13/starwarsjr13:latest --location southcentralus --ip-address Public --resource-group starwars --name starwarsjr13

### Get the Public IP Address of the ACI created
az container list

### Deallocate the Ubuntu/Linux VM to stop charges
az vm deallocate --name starwars2020 --resource-group starwars
