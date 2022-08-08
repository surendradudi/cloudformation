import os
import boto3

AMI = os.environ['ami-0cff7528ff583bf9a']
INSTANCE_TYPE = os.environ['t2.micro']
KEY_NAME = os.environ['boto3']
SUBNET_ID = os.environ['subnet-0c48f9b67bda8e411']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)