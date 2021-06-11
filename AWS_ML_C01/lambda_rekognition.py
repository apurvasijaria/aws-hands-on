import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    rekog = boto3.client('rekognition')
    response = rekog.detect_text(Image = {"S3Object": {"Bucket": "rekog-demo-apurva", "Name": "Add-text-to-image-to-grab-attention.jpg"}})
    
    text = ''
    for detection in response['TextDetections']:
        if detection['Type'] == 'WORD':
            text = text + ' ' + detection['DetectedText'] 
    print(text)
    return {
        'statusCode': 200,
        'body': text
        
    }