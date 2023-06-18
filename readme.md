# Image Processing Lambda Function

This is a Lambda function written in Python for image processing using Hugging Face API and AWS S3.

## Prerequisites

Before running the Lambda function, make sure you have the following:

- AWS account with appropriate permissions to create and execute Lambda functions.
- Hugging Face API token. Replace `API_TOKEN` variable in the code with your API token.

## Functionality

The Lambda function performs the following steps:

1. Retrieves images uploaded to an S3 bucket.
2. Downloads the images from the S3 bucket.
3. Sends the images to the Hugging Face API for processing.
4. Receives the processed results from the API.
5. Uploads the results as JSON files back to the S3 bucket.

## Setup

1. Create an AWS Lambda function.
2. Configure the function with the appropriate permissions to access S3 and execute other necessary operations.
3. Copy the code into the Lambda function.
4. Replace the `API_TOKEN` variable with your Hugging Face API token.
5. Save and deploy the Lambda function.

## Usage

1. Upload images to the configured S3 bucket.
2. The Lambda function will automatically process the uploaded images using the Hugging Face API.
3. The processed results will be stored as JSON files in the same S3 bucket.

## Important Note

- Make sure to configure the necessary AWS credentials and permissions to access S3 and execute Lambda functions.

