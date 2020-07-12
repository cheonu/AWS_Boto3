import boto3


aws_mag_con = boto3.session.Session (profile_name= 'chedev')
ec2_con_re = aws_mag_con.resource(service_name= 'ec2', region_name='us-east-1')

'''
#using all() collector to list all ec2 instance within a specified region
for each in ec2_con_re.instances.all():
    print(each)
'''

#using filters to sort instances based on criteria
Filter1 = {'Name': 'instance-state-name','Values': ['running', 'stopped']}
Filter2 = {'Name': 'instance-type','Values': ['t2.small']}
for each in ec2_con_re.instances.filter(Filters= [Filter1,Filter2]):
    print(each)






