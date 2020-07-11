#menu driven scripts to perform different status actions on ec2 instances

import boto3
import sys
aws_mag_con = boto3.session.Session (profile_name="chedev")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")

'''
while True:
    print("This script performs to the following actions on EC2 instances")
    print("""
    1. Start
    2. Stop
    3. Terminate
    4. Exit
    """)
    opt = int(input("Enter your option: "))
    if opt == 1:
        instance_id = input("Enter is your EC2 instance ID: ")
        ec2InstanceObj = ec2_con_re.Instance(instance_id)
        ec2InstanceObj.start()
        print("Starting ec2 instance ........")
    elif opt == 2:
        instance_id = input("Enter is your EC2 instance ID: ")
        ec2InstanceObj = ec2_con_re.Instance(instance_id)
        ec2InstanceObj.stop()
        print("Stopping ec2 instance..........")
    elif opt == 3:
        instance_id = input("Enter is your EC2 instance ID: ")
        ec2InstanceObj = ec2_con_re.Instance(instance_id)
        ec2InstanceObj.terminate()
        print("Terminating ec2 instance.........")
    elif opt == 4:
        instance_id = input("Enter is your EC2 instance ID: ")
        sys.exit()
    else:
        print("Your option is invalid, please try again")
'''

#using client option
#if you have multiple instances, enter the instances as a list [instance1, instance2]

ec2ClientObj = ec2_con_cl.start_instances(
    InstanceIds=["i-038d68c1e2bebf0f2"],)
print("Starting EC2 instances ......")

ec2ClientObj = ec2_con_cl.stop_instances(
    InstanceIds=["i-038d68c1e2bebf0f2"],)
print("Stopping EC2 instances ......")

ec2ClientObj = ec2_con_cl.terminate_instances(
    InstanceIds=["i-038d68c1e2bebf0f2"],)
print("Terminating EC2 instances ......")



