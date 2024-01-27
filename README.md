# Cost Optimization

# **Problem Statement**

## You work for xyz Company. Your company wanted to reduce the bill on unused EC2-Instances during office off hours.

## You are asked to perform the following tasks:

### 1. Stop the EC2-Instances ( Test, Dev & QA ) after 7PM

### 2. Start the EC2-Instances ( Test, Dev & QA ) after 8AM before 9AM

Create Policy with following permissions for EC2 Instances 

```jsx
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"ec2:RebootInstances",
				"ec2:StartInstances",
				"ec2:StopInstances"
			],
			"Resource": "arn:aws:ec2:*:106298549500:instance/*"
		},
		{
			"Sid": "VisualEditor1",
			"Effect": "Allow",
			"Action": "ec2:DescribeInstances",
			"Resource": "*"
		}
	]
}
```

Verify permissions 

![lambda3.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cd45c56f-cde0-4b31-a477-4ec3fa5f480b/0af63769-8c4d-4c6e-80e3-7291ab5bae5f/lambda3.png)

Review and Create, Policy name Stop-Start-Instance-lambda 

![lambda2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cd45c56f-cde0-4b31-a477-4ec3fa5f480b/cccb83b5-65a5-4bb3-b4b5-d7263b015a65/lambda2.png)

Create Lambda function
