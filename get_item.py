

import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Replace with your region
table = dynamodb.Table('users')  # Replace with your table name

# Add an item to the table
response = table.put_item(
    Item={
        'kanti': 'python_user',  # Partition Key
        'chaudhary': 'basic_user',  # Sort Key
        'username': 'akhilgeorge',  # Additional attributes
        'first_name': 'akhil',
        'last_name': 'george',
        'age': 30,
        'account_type': 'basic_user',
    }
)

print("Item added successfully:", response)

