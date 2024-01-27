import boto3

region = "us-west-2"
instances = ['i-009ada209b43ae9f9','i-09c079adedcda7d67','i-0818c7818f67330c6']

ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
  ec2.start_instances(InstanceIds=instances)
  print("Started Your instances: '+ str")
