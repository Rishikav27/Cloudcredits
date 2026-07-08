# Rapid Document Conversion using AWS

## Project Overview

This project automates document processing using AWS services. When a text file is uploaded to the `input` folder in Amazon S3, an AWS Lambda function is automatically triggered. The Lambda function converts the text to uppercase and stores the processed file in the `output` folder.

## AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch

## Architecture

```
Upload File
     │
     ▼
Amazon S3 (input)
     │
     ▼
S3 Event Trigger
     │
     ▼
AWS Lambda (Python)
     │
     ▼
Convert Text to UPPERCASE
     │
     ▼
Amazon S3 (output)
```

## Features

- Automatic file processing
- Event-driven architecture
- Serverless execution
- Secure IAM role-based access
- CloudWatch logging

## Project Structure

```
Rapid-Document-Conversion/
│
├── lambda_function.py
├── README.md
├── architecture.png
└── screenshots/
```

## How It Works

1. Upload a `.txt` file to the `input` folder in Amazon S3.
2. Amazon S3 triggers the Lambda function.
3. The Lambda function reads the uploaded file.
4. The text is converted to uppercase.
5. The processed file is saved in the `output` folder.
6. CloudWatch logs the execution details.

## Technologies Used

- Python
- AWS Lambda
- Amazon S3
- IAM
- CloudWatch

## Future Improvements

- Support PDF documents.
- Add OCR using Amazon Textract.
- Convert documents into multiple formats.
- Process multiple files simultaneously.

## Author

Rishika Verma
