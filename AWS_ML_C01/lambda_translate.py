import json
import boto3


def lambda_handler(event, context):
    trans = boto3.client('translate')
    response = trans.translate_text(
        Text='I am positive of passing this exam, i am liking AWS very much',
        SourceLanguageCode='en',
        TargetLanguageCode='hi'
        )
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': response['TranslatedText']}