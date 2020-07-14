#list snapshots

import boto3
aws_mag_con = boto3.session.Session (profile_name= 'chedev')
ec2_con_re = aws_mag_con.resource(service_name= 'ec2', region_name='us-east-1')

sts_con_cli = aws_mag_con.client(service_name='sts', region_name='us-east-1')
response = sts_con_cli.get_caller_identity()
myAccountID = response.get('Account')
'''
for each_snapshot in ec2_con_re.snapshots.filter (OwnerIds = [myAccountID]):
    print(each_snapshot)
'''

#using client operation

ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

print(ec2_con_cl.describe_snapshots(OwnerIds=[myAccountID]))

