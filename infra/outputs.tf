output "cluster_endpoint" {
  description = "EKS Cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "cluster_name" {
  description = "EKS Cluster name"
  value       = module.eks.cluster_name
}

output "cluster_certificate_authority_data" {
  description = "Certificate authority data"
  value       = module.eks.cluster_certificate_authority_data
}
