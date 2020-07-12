import boto3

aws_mag_con = boto3.session.Session (profile_name= 'chedev')
ec2_con_re = aws_mag_con.resource(service_name= 'ec2')

#use meta to switch between resource and client objects. For instance the resource object does not have the describe_regions object hence the use of meta
for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
    print(each_item['RegionName'])