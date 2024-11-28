import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Replace with your region
table = dynamodb.Table('users')  # Replace with your table name

# Add an item to the table
response = table.put_item(
    Item={
        'kanti': 'unique_partition_value',  # Partition Key
        'chaudhary': 'unique_sort_value',  # Sort Key
        'username': 'janedoe',  # Additional attributes
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)

print("Item added successfully:", response)

