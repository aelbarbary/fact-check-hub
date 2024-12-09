import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class S3Service:
    def __init__(self, region_name='us-east-1'):
        try:
            self.s3_client = boto3.client(
                's3',
                region_name=region_name,
            )
        except:
            print(f"Error initializing S3 client: {e}")
            raise

    def get_file_content(self, bucket_name, s3_key):
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=s3_key)
            content = response['Body'].read().decode('utf-8')
            return content
        except NoCredentialsError:
            raise Exception("Credentials not available")
        except ClientError as e:
            raise Exception(f"Error getting file content: {e}")

# Example usage:
s3_service = S3Service()
files = s3_service.get_file_content('fact-check-hub', 'sample-political-facts.txt')
print(files)