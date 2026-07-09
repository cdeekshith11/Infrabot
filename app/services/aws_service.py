import os
import boto3
from dotenv import load_dotenv

load_dotenv()


class AWSService:

    def __init__(self):

        region = os.getenv(
            "AWS_DEFAULT_REGION",
            "us-east-1"
        )

        self.ec2 = boto3.client(
            "ec2",
            region_name=region
        )

        self.s3 = boto3.client(
            "s3",
            region_name=region
        )

        self.iam = boto3.client(
            "iam",
            region_name=region
        )

        self.cloudwatch = boto3.client(
            "cloudwatch",
            region_name=region
        )

        self.ce = boto3.client(
            "ce",
            region_name=region
        )

        self.bedrock = boto3.client(
            "bedrock-runtime",
            region_name=region
        )

        


aws_service = AWSService()