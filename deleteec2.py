import boto3

# Initialize a session using your AWS credentials
session = boto3.Session(
   aws_access_key_id='',
   aws_secret_access_key='',
   #region_name='us-east-1'
)


# Initialize the EC2 client
ec2 = session.client('ec2')

# Define the instance ID of the EC2 instance you want to stop, disable termination protection, and terminate
#instance_id = 'i-0415c4cff81c7d586'
instance_id = input("Enter the EC2 instance ID to delete:")
region=input("EEnter the AWS Region:")

try:
    # Stop the EC2 instance
    response_stop = ec2.stop_instances(
        InstanceIds=[instance_id],
        Force=True  # This forces the instance to stop, even if it's not responding
    )

    print(f"Instance stop response: {response_stop}")

    # Disable termination protection for the EC2 instance
    response_disable_protect = ec2.modify_instance_attribute(
        InstanceId=instance_id,
        DisableApiTermination={'Value': False}  # Set to False to disable termination protection
    )

    print(f"Disable termination protection response: {response_disable_protect}")

    # Terminate the EC2 instance
    response_terminate = ec2.terminate_instances(
        InstanceIds=[instance_id]
    )

    print(f"Instance terminate response: {response_terminate}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
