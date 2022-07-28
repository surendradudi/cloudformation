import boto3
import re
from pprint import pprint
client = boto3.client('ec2',region_name='us-east-1')
bang = boto3.client('iam')
regions = client.describe_regions()
vpcs = client.describe_vpcs()
roles = bang.list_roles()
print(regions)
print(1200*'_')
print(roles)
print(1200*'_')
print(vpcs)
print(1200*'_')




