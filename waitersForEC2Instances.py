import boto3
aws_mag_con = boto3.session.Session (profile_name="chedev")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
'''
ec2ReObj = ec2_con_re.Instance("i-053de1e3a581fc87a")
ec2ReObj.start()
print("EC2 instance is starting.....")
ec2ReObj.wait_until_running()
print("Now EC2 instance is running")


ec2ReObj = ec2_con_re.Instance("i-053de1e3a581fc87a")
ec2ReObj.stop()
print("EC2 instance is stopping.....")
ec2ReObj.wait_until_stopped()
print("Now EC2 instance is stopping")


ec2ReObj = ec2_con_re.Instance("i-053de1e3a581fc87a")
ec2ReObj.stop()
print("EC2 instance is being terminated.....")
ec2ReObj.wait_until_terminated()
print("Now EC2 instance is terminating")
'''
#resource waiter waits for 200 seconds
#print(dir(ec2ReObj))
'''
#waiter using client method
print("starting EC2 instance.........")
ec2_con_cl.start_instances(InstanceIds = ["i-053de1e3a581fc87a"])
waiter = ec2_con_cl.get_waiter('instance_running')
waiter.wait(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
print("Now EC2 instance is up and running")
'''

'''
#use EC2 resource and client waiter becuase client waiters take shorter time to initialize
ec2ReObj = ec2_con_re.Instance("i-053de1e3a581fc87a")
print("starting EC2 instance.........")
ec2ReObj.start()
waiter = ec2_con_cl.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-053de1e3a581fc87a',])
print("Now EC2 instance is up and running")
'''

ec2ReObj = ec2_con_re.Instance("i-053de1e3a581fc87a")
print("stopping EC2 instance.........")
ec2ReObj.stop()
waiter = ec2_con_cl.get_waiter('instance_stopped')
waiter.wait(InstanceIds=['i-053de1e3a581fc87a',])
print("Now EC2 instance is stopping")

