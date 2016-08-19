import json
from boto3.session import Session
import os
session = Session(
    aws_access_key_id='xxxxxxxxxxxxxxxxxx',
    aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    region_name='ap-southeast-1',
)

client = session.client('sqs')

response = client.get_queue_url(
    QueueName='ASG1' # Or the name of your SQS queue
)
url="https://us-east.queue.amazonaws.com/xxxxxxxxxxxx/SQS"

def instance_id(a):
      b = a['Messages'][0]['Body']
      c=  json.loads(b)
      d = json.loads (c['Message'])
      id ='i-' +str(d['Description'].split('-')[1])
      return id

messages = client.receive_message(
    QueueUrl=url,
    AttributeNames=['All'],
    MaxNumberOfMessages=10,
    VisibilityTimeout=120,
    WaitTimeSeconds=10
)

try:
   id = instance_id(messages)
except KeyError:
      print "Oops!  That was no valid data..."


if type(id) == type(str()):
	ClientDel = "knife client delete -y {}".format(id)
	os.system(ClientDel)
	NodeDel = "knife node delete -y {}".format(id)
	os.system(NodeDel)
else:
	print "nothing to do"
