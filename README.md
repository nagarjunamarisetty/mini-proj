
## Project:

This repository is a code base for a HTTP API called FizzBuzz. The API expects a number to be supplied and in response send the respective value if it is Fizz or Buzz or FizzBuzz based on if it is divisible by 3 or 5 or 3 and 5 respectively. There are three different APIs implemented for this purpose as listed below. 

The FizzBuzz API is implemented in Python 2.7, the code is in the file fbaas.py.j2 ansible template file. The type of python web framework used here is flask and is front ended by gunicorn a python web server gateway interface used to run multiple instances of the web app.

The supported APIs are

### APIs

1. **/fizz/<number>**
2. **/buzz/<number>**
3. **/fizzbuzz/<number>**

### Return codes:

* 200 will return a successful value FIZZ/BUZZ/FIZZBUZZ accordingly
* 400 Not divisible 
* 401 Out of bounds error.


## Deployment:

To deploy it edit the ansible_inventory file with the following required details. 
  Replace the HOST with either the IP or the DNS of the host where you would like to deploy the FBaaS API.
  Similarly replace the USERNAME and PASSWORD also with the respective username and password used to connect to the host via ssh.
  It is also assumed you are defaulting the ssh port to 22.
  
Disbale the strict host key checking via exporting the following variable 
  `export ANSIBLE_HOST_KEY_CHECKING=False`

Command to run the ansible playbook is 
  `ansible-playbook -i ansible_inventory site.yml`


## Testing:


If you have to conduct any load tests using loader.io, there is an ansible variable called `loader_io_key`, which can be used to define the loader.io key. Either it can be replaced in the roles/fbaas/defaults/main.yml file before executing the ansible playbook or can be passed inline with a -e option in the ansible playbook command.




