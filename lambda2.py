import json
import boto3
import base64

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2025-10-04-04-48-48-785'

sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])
    
    # Make a prediction:
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image
    )

    inferences = json.loads(response['Body'].read().decode('utf-8'))
    event["inferences"] = inferences

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }