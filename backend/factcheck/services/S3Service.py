import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class S3Service:
    def __init__(self, region_name='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            region_name=region_name
        )

    def list_files(self, bucket_name):
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in response:
                return [item['Key'] for item in response['Contents']]
            else:
                return []
        except ClientError as e:
            print(f"Error listing files: {e}")
            return []

    def download_file(self, bucket_name, s3_key, local_path):
        try:
            self.s3_client.download_file(bucket_name, s3_key, local_path)
            print(f"File {s3_key} downloaded to {local_path}")
        except NoCredentialsError:
            print("Credentials not available")
        except ClientError as e:
            print(f"Error downloading file: {e}")

# Example usage:
s3_service = S3Service()
files = s3_service.list_files('ragithm')
print(files)
s3_service.download_file('ragithm', 'index.html', '/tmp/index.html')