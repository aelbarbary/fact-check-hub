from django.shortcuts import render
import csv
from typing import List, Dict
from io import StringIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import boto3
from factcheck.services import S3Service, FactCheckService

# Create your views here.
class FactCheckAPI(APIView):
    def post(self, request):
        try:
            bucket_name = request.data.get("bucket_name")
            s3_key = request.data.get("s3_key")
            statement = request.data.get("statement")
            openai_api_key = request.data.get("openai_api_key")

            if not all([bucket_name, s3_key, statement, openai_api_key]):
                return Response({"error": "All fields (bucket_name, s3_key, statement, openai_api_key) are required."}, status=status.HTTP_400_BAD_REQUEST)

            s3_service = S3Service()             
            csv_content = s3_service.get_file_content(bucket_name, s3_key)

            fact_check_service = FactCheckService(csv_content, openai_api_key)
            validation_result = fact_check_service.validate_answer(statement)

            return Response({"validation_result": validation_result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
