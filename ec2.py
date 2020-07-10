import boto3
from pprint import pprint
#create management console session
aws_mag_con = boto3.session.Session (profile_name = "chedev")

#create ec2 console session
ec2_con_cli = aws_mag_con.client(service_name='ec2', region_name='us-east-1')

response = ec2_con_cli.describe_instances()['Reservations']
for eachItem in response:
    for each in eachItem['Instances']:
        print('\nThe Images ID is: {}\nThe Instance ID is: {}\nThe Launch Time is: {}' .format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))


