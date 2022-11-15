# meme-generator

Setting up a Kubernetes Cluster to host a Meme-generator Webservice

# About
This terraform aims to implement the follow infrastructure

![Alt text](/Image/Infrastructure.png)

The terraform would contain VPC with 2 Subnets(Public and Private) in AWS Cloud.
Kubernetes would reside in the Private Subnet.
Traffic from the Private Subnet will route through the NAT Gateway in the Public Subnet.


# Start Up

## Prerequisites 

1. AWS CLI, installed and configured
2. kubectl is installed
3. Terraform

## Start Up

1. Clone the Repository
```bash
git clone https://github.com/hngsiongh/meme-generator.git
```
2. Change into the Terraform directory
```bash
cd meme-generator/terraform-eks-cluster
```
3. Implementing the Infrastructure on AWS
```bash
terraform init
terraform plan
terraform apply --auto-approve
```
4. Extracting the Host Address of the Meme-Generator API
Retrieve access credentials for your cluster and configure kubectl
```bash
aws eks --region $(terraform output -raw region) update-kubeconfig \
    --name $(terraform output -raw cluster_name)
```
Getting the Service Public Address
```bash
kubectl get services -A
```
Expected Output:
![Alt text](/Image/Screenshot.jpeg)
This is the API Host Address!

# API Endpoints

## Health Check

```bash
curl --request GET '<<API Host Address>>/healthcheck'
```

Returns a 200 HTTP Status with Response Body Ok!

## Generate Meme

```bash
curl --request POST '<<API HOST ADDRESS>>/generateMeme' \
--form 'memeImage=@<<Image File>>' \
--form 'topText=<< Example Top Text>>' \
--form 'btmText=<< Example Bottom Text>>"'
```

Returns a Image File

# Example Output

![Alt text](/Image/Sample.jpg)
