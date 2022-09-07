### Getting Started

#### Create a python virtual environment
`python3 -m venv .env`

#### Activate virtual environment
`source .env/bin/activate`

#### Install Requirements from requirements.txt
`pip install -r requirements.txt`


### Starting redis server
`redis-server --port:<port_number>`
Currently the port I'm using in the settings.is port:9001.  
Please change the port number if you are using default redis-server port which is port:6379.


### Starting Celery Worker
On a separate bash instance, run :
`celery -A scheduler worker -l INFO`
This will start the celery worker and give information on all taks that celery gets


### Starting the Django server
While virtual environment is active, run (on separate bash instance)  

`python manage.py runserver`

This will start the server at default url <htttps://127.0.0.1:8000/> . 

If the port of occupied, the server won't start and you will have to provide the port manually :  
`python manage.py runserver <port_number>`