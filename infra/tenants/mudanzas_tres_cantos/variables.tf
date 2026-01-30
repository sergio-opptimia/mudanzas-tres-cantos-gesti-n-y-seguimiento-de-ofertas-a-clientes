variable "project_name" {
  description = "Nombre del proyecto"
  type        = string
  default     = "mudanzas-tres-cantos"
}

variable "environment" {
  description = "Entorno de despliegue (dev, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "El entorno debe ser 'dev' o 'prod'."
  }
}

variable "region" {
  description = "Región de GCP donde se desplegarán los recursos."
  type        = string
  default     = "europe-west1"
}

variable "vpc_cidr_block" {
  description = "Bloque CIDR para la red VPC principal."
  type        = string
  default     = "10.0.0.0/16"
}

variable "gcs_data_bucket_name" {
  description = "Nombre del bucket de GCS para almacenar datos de la aplicación."
  type        = string
  default     = "mudanzas-tres-cantos-data"
}

variable "gcs_config_bucket_name" {
  description = "Nombre del bucket de GCS para almacenar configuraciones de la aplicación."
  type        = string
  default     = "mudanzas-tres-cantos-config"
}

variable "cloud_run_service_name" {
  description = "Nombre del servicio Cloud Run principal."
  type        = string
  default     = "mudanzas-tres-cantos-agent"
}

variable "cloud_run_location" {
  description = "Ubicación de Cloud Run (debe coincidir con la región o ser una región cercana)."
  type        = string
  default     = "europe-west1"
}

variable "service_account_name" {
  description = "Nombre de la cuenta de servicio a crear para el agente."
  type        = string
  default     = "mudanzas-tres-cantos-sa"
}