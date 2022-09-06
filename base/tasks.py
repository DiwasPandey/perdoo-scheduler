from time import sleep
from datetime import datetime
from dateutil import parser
from celery import shared_task
import requests


@shared_task()
def send_request(event):
    run_at = parser.parse(event['datetime'])
    delay = int((run_at - datetime.now()).total_seconds())
    if delay > 0:
        sleep(delay)
        if event['method'] == "POST":
            response = requests.post(event['requestURI'])
        elif event['method'] == 'GET':
            response = requests.get(event['requestURI'])
        elif event['method'] == 'PUT':
            response = requests.put(event['requestURI'])
        elif event['method'] == 'DELETE':
            response = requests.delete(event['requestURI'])
            
        return response.text
    else:
        return 'Time already passed!'