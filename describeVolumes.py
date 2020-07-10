import boto3
aws_mag_con = boto3.session.Session (profile_name= "chedev")
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

response = ec2_con_cli.describe_volumes()['Volumes']
for eachItem in response:
    print("The Volume ID is: {}\nThe Availability Zone is: {}\nThe Volume Type is: {}" .format(eachItem['VolumeId'], eachItem['AvailabilityZone'], eachItem['VolumeType']))