terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "1.25.0"
    }
  }
}

provider "databricks" {
  host  = var.databricks_host
  token = var.databricks_token
}

resource "databricks_catalog" "main" {
  name         = "main"
  comment      = "Primary catalog for Customer360"
  force_destroy = true
}

resource "databricks_schema" "customer360" {
  name     = "customer360_schema"
  catalog_name = databricks_catalog.main.name
  comment  = "Schema for customer and transaction tables"
}

resource "databricks_pipeline" "customer360" {
  name       = "customer360_pipeline"
  target     = "dev"
  catalog    = databricks_catalog.main.name
  schema     = databricks_schema.customer360.name
  cluster {
    label = "default"
  }
  libraries {
    notebook {
      path = "pipelines/dlt_pipeline.py"
    }
  }
}
