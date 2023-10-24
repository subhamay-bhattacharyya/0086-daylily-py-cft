# # -*- coding: utf-8 -*-
# """
# Created on Tue Oct 24 13:05:48 2023

# @author: Subhamay Bhattacharyya
# """

import json
import logging
import boto3
import os


# # Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

sns_client = boto3.client(
    'sns', region_name=os.environ.get("AWS_REGION"))
sns_topic_arn = os.getenv("SNS_TOPIC_ARN")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    try:
        logger.info(f"event : {json.dumps(event)}")
        message = "Hello World !"
        response = sns_client.publish(
                                TargetArn=sns_topic_arn,
                                Message=json.dumps({'default': json.dumps(message)}),
                                MessageStructure='json'
        )
        logger.info(f"response : {json.dumps(response)}")
    # An error occurred
    except ParamValidationError as e:
        logger.error(f"Parameter validation error: {e}")
        return dict(
            statusCode=401, message=f"Parameter validation error: {e}")
    except ClientError as e:
        logger.error(f"Client error: {e}")
        return dict(
            statusCode=402, message=f"Parameter validation error: {e}")

