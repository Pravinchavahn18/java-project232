import boto3

# creat an IAM client
iam = boto3.client ('iam') 

# List all IAM users
responce= iam.list_users()

#print the name of all IAM users
for users in response['Users'];
Print users (users['Username'])