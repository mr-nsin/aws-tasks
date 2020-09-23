import boto3

ses = boto3.client('ses')

body = """
    Hello Hari, Hope you are doing great,

    Thanks
    Nitin Singhal

"""

ses.send_email(
    Source = "singhal.nitin94@gmail.com",
    Destination = {
        'ToAddresses' : [
            'singhal.nitin108@gmail.com',
        ]
    },
    Message = {
        'Subject' : {
            'Data' : 'SES Demo',
            'Charset': 'UTF-8'
        },
        'Body' : {
            'Text' : {
                'Data' : body,
                'Charset': 'UTF-8'
            }
        }
    }
)