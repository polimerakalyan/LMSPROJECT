variable "aws_region" {
  description = "AWS region to deploy EKS"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS Cluster name"
  type        = string
  default     = "lms-eks-cluster"
}

variable "desired_capacity" {
  description = "Number of worker nodes"
  type        = number
  default     = 2
}

variable "instance_type" {
  description = "EC2 instance type for workers"
  type        = string
  default     = "t3.medium"
}
