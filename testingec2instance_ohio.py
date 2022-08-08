import os
import boto3

AMI = 'ami-051dfed8f67f095f5'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'boto3'
SUBNET_ID = 'subnet-02e53fe325cba963f'
REGION = 'us-east-2'
checking = 'i_have_my_bad_luck'

ec2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    init_script = """#!/bin/bash
                yum update -y
                yum install -y httpd24
                service httpd start
                chkconfig httpd on
                echo """ + checking + """ > /var/www/html/index.html
                shutdown -h +5"""

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        InstanceInitiatedShutdownBehavior='terminate', 
        UserData=init_script
    )

    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)

    return instance_id