# ChefclientDeleteAWS
Delete chef-client from dead instances AWS (Autoscaling)

Create simple notification service (SNS) topic 
Send a notification to:TOPIC tick only terminate  
create simple queue service (SQS) endpoint

Create Subscription to the topic with protocol Amazon SQS
enter Topic ARN  and  sqs Endpoint 

create conjob and run script every min bam !!
Done




