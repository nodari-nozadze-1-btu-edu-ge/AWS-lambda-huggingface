import io
import json
from pprint import pprint
from urllib.request import urlopen, Request
import boto3

API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URLS = [
    "https://api-inference.huggingface.co/models/google/mobilenet_v1_0.75_192",
    "https://api-inference.huggingface.co/models/facebook/detr-resnet-50",
    "https://api-inference.huggingface.co/models/hustvl/yolos-tiny",
    "https://api-inference.huggingface.co/models/nvidia/mit-b0"
]
s3_client = boto3.client("s3")


def query_image(file_obj, URL):
    file_obj.seek(0) 
    http_request = Request(URL, data=file_obj.read(), headers=headers)
    with urlopen(http_request) as response:
        result = response.read().decode()
        print(result)
    return result


def lambda_handler(event, _):
    pprint(event)
    for record in event.get("Records"):
        bucket = record.get("s3").get("bucket").get("name")
        key = record.get("s3").get("object").get("key")

        print("Bucket", bucket)
        print("Key", key)

        # Download file from bucket
        file = io.BytesIO()
        s3_client.download_fileobj(Bucket=bucket, Key=key, Fileobj=file)
        file.seek(0)

        # Send file to Huggingface API
        for URL in API_URLS:
            result = query_image(io.BytesIO(file.getvalue()), URL)
            print("result", result)

            # Upload result to bucket as JSON
            result_key = URL.split("/")[-1] + key.split(".")[0] + ".json"
            result_file = io.BytesIO()
            result_file.write(result.encode("utf-8"))
            result_file.seek(0)

            s3_client.upload_fileobj(result_file, bucket, result_key)

    return {"statusCode": 200, "body": json.dumps("Done!")}