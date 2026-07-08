import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and file name from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read the uploaded file
    response = s3.get_object(Bucket=bucket, Key=key)
    text = response['Body'].read().decode('utf-8')

    # Convert text to uppercase
    converted_text = text.upper()

    # Save the converted file in the output folder
    output_key = key.replace("input/", "output/")

    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=converted_text.encode("utf-8")
    )

    return {
        "statusCode": 200,
        "body": "File converted successfully!"
    }