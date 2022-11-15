# Module to Help provision an EKS Cluster and other requried resources
# Including 
# -Auto Scaling Groups
# -Security Groups
# -IAM Roles
# -IAM Policies
module "eks" {
  # Source Code for the Module
  source  = "terraform-aws-modules/eks/aws"
  version = "17.24.0"

  # Name of the EKS cluster.
  cluster_name = local.cluster_name
  # Kubernetes Version
  cluster_version = "1.20"
  # Specify Subnets in which nodes will be created
  # ----- Creating nodes in Private Network
  subnets = module.vpc.private_subnets
  # VPC where the cluster and workers would be deployed
  vpc_id = module.vpc.vpc_id


  workers_group_defaults = {
    root_volume_type = "gp2"
  }

  # Creation of 3 Nodes across 2 Node Groups
  worker_groups = [
    #Private Network
    {
      name                          = "worker-group-1"
      instance_type                 = "t2.small"
      additional_userdata           = "echo nothing"
      additional_security_group_ids = [aws_security_group.worker_group_mgmt_one.id]
      asg_desired_capacity          = 2
    },
    # Public Network 
    {
      name                          = "worker-group-2"
      instance_type                 = "t2.medium"
      additional_userdata           = "echo nothing"
      additional_security_group_ids = [aws_security_group.worker_group_mgmt_two.id]
      asg_desired_capacity          = 1
    },
  ]
}

data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}
