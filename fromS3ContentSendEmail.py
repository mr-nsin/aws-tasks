import json
import boto3

from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
#SENDER = "singhal.nitin94@gmail.com"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
#RECIPIENT = "singhal.nitin94@gmail.com"

CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "ap-south-1"

# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
            
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
            """            

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # get sender and to email address from json file from s3
    # get a handle on the object you want (i.e. your file)
    obj = s3.Object('send-email-s3-json', key='emails.json')

    # get the object
    response = obj.get()
    
    # read the contents of the file
    file_content = response['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    sender = json_content['emailAddress'][0]['from']
    to = json_content['emailAddress'][0]['to']
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    to,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=sender,
            # If you are not using a configuration set, comment or delete the
            # following line
            ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        return {
            'statusCode' : 200,
            'headers': {
                'Access-Control-Allow-Origin' : '*', 
                'Access-Control-Allow-Credentials' : True
            },
            'body' : json.dumps(e.response['Error']['Message'])
        }
    else:
        return {
            'statusCode' : 200,
            'headers': {
                'Access-Control-Allow-Origin' : '*', 
                'Access-Control-Allow-Credentials' : True
            },
            'body' : json.dumps(response['MessageId'])
        }