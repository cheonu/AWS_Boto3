import boto3
aws_mag_con = boto3.session.Session (profile_name= 'chedev')
ec2_con_re = aws_mag_con.resource(service_name= 'ec2', region_name='us-east-1')
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
'''
#get instance ID's using an appended list
listOfInstanceIDS=[]
for each in ec2_con_re.instances.all():
    listOfInstanceIDS.append(each.id)
#using collections concept to start all ec2 instances
#print(dir(ec2_con_re.instances))

'''
'''
ec2_con_cl.start_instances(InstanceIds = listOfInstanceIDS)
waiter = ec2_con_cl.get_waiter('instance_running')
print("starting EC2 instances......")
waiter.wait(InstanceIds = listOfInstanceIDS)
print("Now EC2 instances are up and running")
'''

'''
#using collections concept to stop all ec2 instances
print("Stopping all EC2 Instances......")
ec2_con_cl.stop_instances(InstanceIds = listOfInstanceIDS)
waiter = ec2_con_cl.get_waiter('instance_stopped')
waiter.wait(InstanceIds = listOfInstanceIDS)
print("Now EC2 instances have been stopped")

#using collections concept to terminate all ec2 instances
#print("Terminating all EC2 Instances......")
#ec2_con_re.instances.terminate()
'''

#using tags to filter instances

nonProdInstances = []
TagFilter={"Name": "tag:Name", "Values": ["Non_Prod"]}
for each in ec2_con_re.instances.filter(Filters = [TagFilter]):
    nonProdInstances.append(each.id)
ec2_con_cl.start_instances(InstanceIds = nonProdInstances)
waiter = ec2_con_cl.get_waiter('instance_running')
print("starting EC2 instances......")
waiter.wait(InstanceIds = nonProdInstances)
print("Now EC2 instances are up and running")