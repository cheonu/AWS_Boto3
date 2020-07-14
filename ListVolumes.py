import boto3
aws_mag_con = boto3.session.Session (profile_name= 'chedev')
ec2_con_re = aws_mag_con.resource(service_name= 'ec2', region_name='us-east-1')
'''
#print each volume ID and state
for each_volume in ec2_con_re.volumes.all():
    print(each_volume.id, each_volume.state)
'''

'''
# use filter to sort only Volumes in use 
ebs_inUse = {"Name": "status", "Values":["in-use"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[ebs_inUse]):
    print(each_volume.id, each_volume.state)
'''
'''
# use filter to sort and delete only untagged Volumes
ebs_available = {"Name": "status", "Values":["available"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[ebs_available]):
    if not each_volume.tags:
        print(each_volume.id, each_volume.state, each_volume.tags)
        print("Deleting all unused and untagged Volumes......")
        each_volume.delete()
        print("Volume have been deleted")
'''
#using client operations to manage volumes

ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
for eachVol in ec2_con_cl.describe_volumes()['Volumes']:
    if not "Tags" in eachVol and eachVol['State'] == 'available':
        print("Deleting", eachVol['VolumeId'])
        ec2_con_cl.delete_volume(VolumeId= eachVol['VolumeId'])
print("Deleting all unused and untagged volumes")