

##  Working Process

1. The frontend application is deployed using Amazon S3 static website hosting.

2. Users interact with the web interface to perform task operations.

3. Requests are sent from JavaScript frontend to Amazon API Gateway.

4. API Gateway invokes AWS Lambda functions.

5. Lambda processes CRUD operations.

6. DynamoDB stores and manages application data.


##  AWS Services Implementation

### Amazon S3
Used for hosting the static frontend application.

### API Gateway
Created REST endpoints for communication between frontend and backend.

### AWS Lambda
Implemented serverless backend logic using Python.

### DynamoDB
Used as a NoSQL database for storing task information.

### IAM
Configured permissions for secure service communication.


##  Key Learnings

- Designed a serverless cloud architecture
- Created and deployed AWS Lambda functions
- Integrated API Gateway with Lambda
- Connected Lambda with DynamoDB
- Hosted frontend application on AWS S3
- Implemented end-to-end cloud application deployment


##  Developed By

Rishika Verma
