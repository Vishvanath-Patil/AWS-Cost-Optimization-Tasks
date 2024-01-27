
# Problem Statement

### You work for xyz Company. Your company wanted to reduce the bill on unused EC2-Instances during office off hours.

## You are asked to perform the following tasks:

### 1. Stop the EC2-Instances ( Test, Dev & QA ) after 7PM

### 2. Start the EC2-Instances ( Test, Dev & QA ) after 8AM before 9AM

## Create Policy

Create Policy with following permissions for EC2 Instances

```bash
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
![lambda3](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/2151130d-3b2f-45eb-a94c-92b75d22cf80)

![lambda2](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/402de95a-38bd-4ea7-9256-ca476fe5af1d)


![lambda1](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/853cbbc6-5eac-4d91-bb1a-3e489c79a1ec)

![l4](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/1bff33d4-a538-4f4e-89ff-7453ea552104)

![l5](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/5546d925-1c99-47cc-80cd-78e9b7840ae0)

![l6](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/c969a474-78c3-4517-849b-e7e0d7f573b8)

![l7](https://github.com/Vishvanath-Patil/AWS-Cost-Optimization-Tasks/assets/130968991/8b69784f-2218-45ae-8530-a40c0d39c31b)

